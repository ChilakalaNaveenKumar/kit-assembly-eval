"""Write a readable transcript for every finished trial: transcripts/<condition>/<kit>/<model>__t<k>.md."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def fenced(text: str) -> list[str]:
    """The text in a code fence longer than any backtick run inside it, so the fence cannot close early."""
    fence = "`" * max(4, max((len(m) for m in re.findall(r"`+", text)), default=0) + 1)
    return [fence + "text", text, fence]


def transcript(r: dict) -> str:
    """One trial as Markdown: settings, provider receipts, prompt, thinking summary, answer and grade."""
    g = r["grade"]
    failed = [c for c in g["checks"] if not c["ok"]]
    lines = [f"# {r['condition']} · {r['kit']} · {r['model']} · trial {r['trial']}", "",
             f"- Result: **{'PASS' if g['pass'] else 'FAIL'}**, score {g['score']:.2f}, tags: {', '.join(r.get('tags') or [])}",
             f"- Model version: `{r.get('model_version')}`, response id: `{r.get('response_id')}`",
             f"- Started {r.get('started')}, finished {r.get('finished')}, {r['seconds']} s, attempts {r['attempts']}",
             f"- Tokens: input {r['input_tokens']:,}, output {r['output_tokens']:,}"
             + (f" (thinking {r['thinking_tokens']:,})" if r.get("thinking_tokens") is not None else " (thinking not reported separately by this provider)"),
             f"- Settings: `{json.dumps(r['settings'])}`, prompt sha256 `{r['prompt_sha256']}`", "",
             "## Failed checks", ""]
    lines += [f"- {c['text']}: error {c['err']} (tolerance {c['tol']})" for c in failed] or ["- none"]
    lines += [f"- issue: {i}" for i in g["issues"]]
    lines += ["", "## Thinking summary (as returned by the provider)", "", *fenced(r.get("thinking") or "(empty)"),
              "", "## Answer", "", *fenced(r["output"]), "", "## Prompt", "", *fenced(r.get("prompt", "")), ""]
    return "\n".join(lines)


def main() -> None:
    """Write or refresh transcripts for every finished trial."""
    n = 0
    for path in sorted((ROOT / "results").glob("*/*/*.json")):
        r = json.loads(path.read_text())
        if r.get("status") != "ok":
            continue
        out = ROOT / "transcripts" / path.relative_to(ROOT / "results").with_suffix(".md")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(transcript(r))
        n += 1
    print(f"wrote {n} transcripts")


if __name__ == "__main__":
    main()
