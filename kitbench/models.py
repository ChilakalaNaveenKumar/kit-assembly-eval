"""Model calls with fixed settings. Credentials come only from the environment.

The submitted run used Claude through Google Vertex AI: set CLAUDE_ROUTE=vertex, GOOGLE_CLOUD_PROJECT, optionally
CLAUDE_VERTEX_REGION (default "global") and Google application-default credentials (gcloud auth application-default login).
Without CLAUDE_ROUTE the Claude API is used (ANTHROPIC_API_KEY); Gemini models need GEMINI_API_KEY.
"""
import os
import time

MODELS = ["claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5", "gemini-3.1-pro-preview", "gemini-3.8-flash"]
RUN_MODELS = ["claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5"]  # what "--models all" runs; Gemini stays available by id
MAX_OUTPUT_TOKENS = 64000
CLAUDE_MAX_OUTPUT_TOKENS = 128000  # the most each Claude 5.5 model can output
SETTINGS = {
    "anthropic": {"max_tokens": CLAUDE_MAX_OUTPUT_TOKENS, "thinking": {"type": "adaptive", "display": "summarized"},
                  "output_config": {"effort": "high"}},
    "gemini": {"max_output_tokens": MAX_OUTPUT_TOKENS, "thinking_level": "high", "include_thoughts": True},
}
TIMEOUT_S = 2400
RETRIES = 4


class ApiError(RuntimeError):
    """The provider failed after all retries; the trial is not a model result."""


def provider(model: str) -> str:
    """Which provider serves a model id."""
    return "gemini" if model.startswith("gemini") else "anthropic"


def claude_route() -> str:
    """Claude via the Claude API (default) or Google Vertex AI (CLAUDE_ROUTE=vertex): same model, same settings."""
    return "vertex" if os.environ.get("CLAUDE_ROUTE", "").lower() == "vertex" else "claude-api"


def settings(model: str) -> dict:
    """The exact request settings used for a model, stored with every result."""
    extra = {"route": claude_route()} if provider(model) == "anthropic" else {}
    return {"provider": provider(model), **extra, **SETTINGS[provider(model)]}


def _anthropic(model: str, prompt: str) -> dict:
    import anthropic

    if claude_route() == "vertex":
        client = anthropic.AnthropicVertex(region=os.environ.get("CLAUDE_VERTEX_REGION", "global"),
                                           project_id=os.environ["GOOGLE_CLOUD_PROJECT"], timeout=TIMEOUT_S, max_retries=0)
    else:
        client = anthropic.Anthropic(timeout=TIMEOUT_S, max_retries=0)
    s = SETTINGS["anthropic"]
    # streamed so long thinking runs do not hit HTTP timeouts
    with client.messages.stream(model=model, max_tokens=s["max_tokens"], thinking=s["thinking"],
                                output_config=s["output_config"],
                                messages=[{"role": "user", "content": prompt}]) as stream:
        msg = stream.get_final_message()
    text = "".join(b.text for b in msg.content if b.type == "text")
    thinking = "\n\n".join(b.thinking for b in msg.content if b.type == "thinking" and getattr(b, "thinking", ""))
    return {"text": text, "thinking": thinking, "stop_reason": msg.stop_reason, "input_tokens": msg.usage.input_tokens,
            "output_tokens": msg.usage.output_tokens, "thinking_tokens": None,
            "response_id": msg.id, "model_version": msg.model, "usage": msg.usage.model_dump(mode="json"),
            "raw": msg.model_dump(mode="json")}


def _gemini(model: str, prompt: str) -> dict:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"], http_options=types.HttpOptions(timeout=TIMEOUT_S * 1000))
    s = SETTINGS["gemini"]
    resp = client.models.generate_content(
        model=model, contents=prompt,
        config=types.GenerateContentConfig(max_output_tokens=s["max_output_tokens"],
                                           thinking_config=types.ThinkingConfig(thinking_level=s["thinking_level"],
                                                                                include_thoughts=s["include_thoughts"])))
    cand = resp.candidates[0] if resp.candidates else None
    parts = (cand.content.parts if cand and cand.content and cand.content.parts else [])
    text = "".join(p.text or "" for p in parts if not getattr(p, "thought", False))
    thinking = "\n\n".join(p.text or "" for p in parts if getattr(p, "thought", False))
    u = resp.usage_metadata
    return {"text": text, "thinking": thinking, "stop_reason": str(cand.finish_reason) if cand else "no_candidate",
            "input_tokens": u.prompt_token_count or 0,
            "output_tokens": (u.candidates_token_count or 0) + (u.thoughts_token_count or 0),
            "thinking_tokens": u.thoughts_token_count or 0,
            "response_id": resp.response_id, "model_version": resp.model_version,
            "usage": u.model_dump(mode="json", exclude_none=True), "raw": resp.model_dump(mode="json", exclude_none=True)}


PRICE_PER_MTOK = {  # USD input / output list prices for prompts under 100K tokens; Gemini Flash standard rate unconfirmed
    "claude-opus-5-5": (4.00, 20.00), "claude-sonnet-5-5": (2.00, 10.00), "claude-haiku-5-5": (0.10, 0.50),
    "gemini-3.1-pro-preview": (2.00, 12.00),
}


def _retryable(e: Exception) -> bool:
    status = getattr(e, "status_code", None) or getattr(e, "code", None)
    if isinstance(status, int) and 400 <= status < 500:
        return status in (408, 409, 429)
    # 5xx, mid-stream overload events and connection/timeout errors are transient
    return True


def call(model: str, prompt: str) -> dict:
    """One fresh single-turn call: answer text, thinking summary, token counts, provider ids and timing."""
    fn = _gemini if provider(model) == "gemini" else _anthropic
    last = None
    for attempt in range(1, RETRIES + 1):
        t0 = time.time()
        try:
            started = time.strftime("%Y-%m-%dT%H:%M:%S%z")
            out = fn(model, prompt)
            return {**out, "seconds": round(time.time() - t0, 1), "attempts": attempt,
                    "started": started, "finished": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
        except Exception as e:  # noqa: BLE001 - any provider failure is retried or reported, never graded
            last = e
            if not _retryable(e):
                break
            time.sleep(min(60, 10 * attempt))
    raise ApiError(f"{type(last).__name__}: {str(last)[:300]}")
