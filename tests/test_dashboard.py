"""Dashboard tests: endpoints over a local server, path safety, and a live run with a fake model. No network."""
import http.client
import json
import sys
import threading
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import dashboard  # noqa: E402
import run_eval  # noqa: E402
import kitbench.kit  # noqa: E402
import kitbench.models  # noqa: E402
from kitbench.kit import kit_names, reference_svg  # noqa: E402
from kitbench.templates import part_ids  # noqa: E402

FAKE_KEY = "dummy-key-0123456789abcdef"


@pytest.fixture()
def server(tmp_path):
    srv = dashboard.make_server(0, tmp_path / "results_live")
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield srv, tmp_path
    srv.shutdown()
    srv.server_close()


def request(srv, method: str, path: str, body: dict | None = None) -> tuple[int, str, bytes]:
    conn = http.client.HTTPConnection("127.0.0.1", srv.server_address[1], timeout=30)
    data = json.dumps(body) if body is not None else None
    conn.request(method, path, body=data, headers={"Content-Type": "application/json"})
    r = conn.getresponse()
    out = (r.status, r.getheader("Content-Type"), r.read())
    conn.close()
    return out


def test_bound_to_loopback(server):
    assert server[0].server_address[0] == "127.0.0.1"


def test_results_lists_conditions_present(server):
    code, _, body = request(server[0], "GET", "/api/results")
    on_disk = {p.name for p in run_eval.RESULTS.iterdir() if p.is_dir()}
    got = {c["condition"] for c in json.loads(body)["conditions"]}
    assert code == 200 and got == on_disk & set(dashboard.CONDITION_ORDER)


def test_svg_for_existing_trial_and_reference(server):
    cond = json.loads(request(server[0], "GET", "/api/results")[2])["conditions"][0]
    kit = next(iter(cond["grid"]))
    model, cell = next(iter(cond["grid"][kit].items()))
    q = f"src=results&cond={cond['condition']}&kit={kit}&model={model}&trial={cell['list'][0]['trial']}"
    code, ctype, body = request(server[0], "GET", "/svg/trial?" + q)
    assert code == 200 and ctype == "image/svg+xml" and body.startswith(b"<svg")
    code, ctype, body = request(server[0], "GET", f"/svg/reference?kit={kit}&cond=A")
    assert code == 200 and ctype == "image/svg+xml" and b"<use" in body


def test_kit_file_blocks_traversal(server):
    kit = kit_names()[0]
    assert request(server[0], "GET", f"/kitfile/{kit}/reference.png")[0] == 200
    for bad in (f"/kitfile/{kit}/../task.py", f"/kitfile/{kit}/%2e%2e/task.py", "/kitfile/../run_eval.py",
                "/kitfile/%2e%2e%2frun_eval.py", f"/kitfile/{kit}/..%2ftask.py"):
        assert request(server[0], "GET", bad)[0] in (400, 404)


def test_unknown_trial_params_rejected(server):
    assert request(server[0], "GET", "/api/trial?src=results&cond=A&kit=../x&model=m&trial=1")[0] == 404


def test_raw_and_transcript_endpoints(server, monkeypatch):
    srv, tmp = server
    monkeypatch.setattr(run_eval, "RAW", tmp / "raw")
    monkeypatch.setattr(dashboard, "TRANSCRIPTS", tmp / "tr")
    kit, model = kit_names()[0], next(iter(kitbench.models.MODELS))
    (tmp / "raw" / "A" / kit).mkdir(parents=True)
    (tmp / "tr" / "A" / kit).mkdir(parents=True)
    (tmp / "raw" / "A" / kit / f"{model}__t1.json").write_text('{"id": 1}')
    (tmp / "tr" / "A" / kit / f"{model}__t1.md").write_text("# hi")
    q = f"cond=A&kit={kit}&model={model}&trial="
    code, ctype, body = request(srv, "GET", "/raw?" + q + "1")
    assert (code, ctype, json.loads(body)) == (200, "application/json", {"id": 1})
    code, ctype, body = request(srv, "GET", "/transcript?" + q + "1")
    assert (code, ctype, body) == (200, "text/plain; charset=utf-8", b"# hi")
    for path in ("/raw", "/transcript"):
        assert request(srv, "GET", path + "?" + q + "2")[0] == 404
        for bad in (f"cond=Z&kit={kit}&model={model}&trial=1", f"cond=A&kit=../x&model={model}&trial=1", f"cond=A&kit={kit}&model=m&trial=1",
                    f"cond=A&kit={kit}&model={model}&trial=0", f"cond=A&kit={kit}&model={model}&trial=100", f"cond=A&kit={kit}&model={model}&trial=x",
                    f"cond=A&kit={kit}&model={model}&trial=-1", f"cond=A&kit={kit}&model={model}"):
            assert request(srv, "GET", path + "?" + bad)[0] == 400, bad


def test_live_run_writes_pass_and_hides_keys(server, monkeypatch):
    srv, tmp_path = server
    kit, cond, model = "bike", "A", "claude-haiku-5-5"

    def fake_call(m: str, prompt: str) -> dict:
        return {"text": reference_svg(kit, ids=part_ids(kit, cond)), "stop_reason": "end_turn", "input_tokens": 1,
                "output_tokens": 2, "seconds": 0.1, "attempts": 1, "thinking": "fake reasoning", "thinking_tokens": 1,
                "response_id": "resp_test", "model_version": m, "usage": {}, "started": "t0", "finished": "t1",
                "raw": {"id": "resp_test"}}

    monkeypatch.setattr(kitbench.models, "call", fake_call)
    monkeypatch.setattr(run_eval, "call", fake_call)
    monkeypatch.setattr(run_eval, "RAW", tmp_path / "real_raw_guard")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("CLAUDE_ROUTE", raising=False)
    body = {"condition": cond, "kits": [kit], "models": [model], "trials": 1, "workers": 1, "anthropic_key": FAKE_KEY}
    code, _, plan = request(srv, "POST", "/api/plan", body)
    assert code == 200 and json.loads(plan)["trials"] == 1
    code, _, out = request(srv, "POST", "/api/run", body)
    assert code == 200 and FAKE_KEY.encode() not in out
    for _ in range(100):
        status = json.loads(request(srv, "GET", "/api/status")[2])
        if status["state"] != "running":
            break
        time.sleep(0.1)
    assert status["state"] == "done" and status["trials"][0]["pass"] is True
    assert FAKE_KEY not in json.dumps(status) and "ANTHROPIC_API_KEY" not in __import__("os").environ
    files = [f for f in (tmp_path / "results_live").rglob(f"{cond}/{kit}/{model}__t1.json") if "_raw" not in str(f)]
    assert len(files) == 1 and json.loads(files[0].read_text())["grade"]["pass"] is True
    raws = list((tmp_path / "results_live").rglob(f"{status['run']}_raw/{cond}/{kit}/{model}__t1.json"))
    assert len(raws) == 1 and not (tmp_path / "real_raw_guard").exists()
    assert not any(FAKE_KEY in p.read_text(errors="ignore") for p in tmp_path.rglob("*") if p.is_file())
    live = json.loads(request(srv, "GET", "/api/results")[2])["live"]
    assert live and live[0]["conditions"][0]["models"][0]["passes"] == 1
    q = f"src=live&run={status['run']}&cond={cond}&kit={kit}&model={model}&trial=1"
    assert request(srv, "GET", "/svg/trial?" + q)[0] == 200


def test_overview_matches_stats(server):
    from kitbench import stats

    code, ctype, body = request(server[0], "GET", "/api/overview")
    d = json.loads(body)
    rows = dashboard.submitted_rows()
    assert code == 200 and ctype == "application/json"
    assert d["ladder"] == stats.ladder(rows) and d["ladder_order"] == stats.LADDER == ["B", "A", "C"]
    assert d["failure_types"] == stats.FAILURE_TYPES and set(d["failures"]) == {"all", "B", "A", "C", "A_alt"}
    assert d["failures"]["all"] == stats.failure_breakdown([r for r in rows if r["condition"] in stats.LADDER])
    assert d["summary"]["C"] == stats.condition_summary(rows, "C")
    assert [c["id"] for c in d["conditions"]] == [c for c in dashboard.CONDITION_ORDER if c in {r["condition"] for r in rows}]


def test_failures_lists_every_failed_trial_newest_first(server):
    d = json.loads(request(server[0], "GET", "/api/failures")[2])
    rows = dashboard.submitted_rows()
    assert len(d["failures"]) == sum(1 for r in rows if r.get("status") == "ok" and not r["grade"]["pass"])
    dates = [f["date"] for f in d["failures"]]
    assert dates == sorted(dates, reverse=True)
    assert all(f["failure_type"] in d["failure_types"] for f in d["failures"])


def test_method_payload_and_page_is_offline(server):
    d = json.loads(request(server[0], "GET", "/api/method")[2])
    assert set(d["tolerances"]) == set(kit_names()) and d["orient_tol"] > 0
    assert [m["model"] for m in d["models"]] == dashboard.result_models()
    for path in ("/", "/app.js", "/app.css"):
        page = request(server[0], "GET", path)[2].decode()
        assert "http://" not in page.replace("http://www.w3.org/2000/svg", "") and "https://" not in page
        assert "innerHTML" not in page and "eval(" not in page


def test_results_models_come_from_stats(server):
    cond = json.loads(request(server[0], "GET", "/api/results")[2])["conditions"][0]
    assert {"pass_rate", "passk", "mean_output_tokens"} <= set(cond["models"][0])


def failed_trial(model_rows=None):
    rows = [r for r in dashboard.submitted_rows() if r.get("status") == "ok" and not r["grade"]["pass"]
            and any(not c["ok"] and c["kind"] == "joint" for c in r["grade"]["checks"])]
    r = rows[0]
    return r, f"cond={r['condition']}&kit={r['kit']}&model={r['model']}&trial={r['trial']}"


def test_static_files_served_with_types_and_whitelist(server):
    srv = server[0]
    for path, ctype in (("/", "text/html"), ("/index.html", "text/html"), ("/app.css", "text/css"), ("/app.js", "text/javascript"),
                        ("/vendor/echarts.min.js", "text/javascript")):
        code, got, body = request(srv, "GET", path)
        assert code == 200 and got.startswith(ctype) and body
    for bad in ("/vendor/", "/vendor", "/web/app.js", "/vendor/../app.js", "/%2e%2e/dashboard.py", "/dashboard.py", "/app.js/"):
        assert request(srv, "GET", bad)[0] == 404


def test_annotated_svg_marks_and_validation(server):
    r, q = failed_trial()
    idx = next(i for i, c in enumerate(r["grade"]["checks"]) if not c["ok"] and c["kind"] == "joint")
    code, ctype, body = request(server[0], "GET", f"/svg/annotated?{q}&i={idx}")
    text = body.decode()
    assert code == 200 and ctype == "image/svg+xml" and text.startswith("<svg") and "#d03b3b" in text and "#0ca30c" in text and " pixels off</text>" in text
    whole = request(server[0], "GET", f"/svg/annotated?{q}&i={idx}&zoom=0")[2].decode()
    assert 'viewBox="0 0 ' in whole and " pixels off</text>" in whole and whole != text
    assert request(server[0], "GET", f"/svg/annotated?{q}&ref=1&i={idx}")[0] == 200
    assert request(server[0], "GET", f"/svg/annotated?{q}")[0] == 200
    for bad in (f"{q}&i=999", f"{q}&i=x", f"{q}&i=-1", "cond=A&kit=../x&model=m&trial=1"):
        assert request(server[0], "GET", "/svg/annotated?" + bad)[0] == 404
    assert "<script" not in text and "onload" not in text


def test_replay_and_annotations_endpoints(server):
    r, q = failed_trial()
    code, ctype, body = request(server[0], "GET", "/api/replay?" + q)
    d = json.loads(body)
    assert code == 200 and ctype == "application/json" and d["kit"] == r["kit"] and d["failed_points"] and d["failed_parts"]
    assert len(d["parts"]) == len(kitbench.kit.load_kit(r["kit"])) and all(len(p["start"]) == 6 and len(p["ref"]) == 6 for p in d["parts"])
    assert any(p["end"] for p in d["parts"])
    pts = json.loads(request(server[0], "GET", "/api/annotations?" + q)[2])["points"]
    assert pts == d["failed_points"] and {"index", "landed", "expected", "err", "tol"} <= set(pts[0])
    assert request(server[0], "GET", "/api/replay?cond=A&kit=bike&model=nope&trial=1")[0] == 404
    assert request(server[0], "GET", "/api/annotations?cond=A&kit=bike&model=claude-opus-5-5&trial=99")[0] == 404


def test_overview_mistakes_carry_check_index(server):
    d = json.loads(request(server[0], "GET", "/api/overview")[2])
    assert d["top_mistakes"] and all("index" in m["example"] for m in d["top_mistakes"])
    assert json.loads(request(server[0], "GET", "/api/options")[2])["model_names"]["claude-opus-5-5"] == "Claude Opus 5.5"


def shifted_reply(kit: str, cond: str, dx: float, dy: float) -> str:
    """The reference solution with every part moved by (dx, dy), as a model that put the whole object elsewhere would answer."""
    import numpy as np

    def move(part, m):
        t = np.eye(3)
        t[0, 2], t[1, 2] = dx, dy
        return t @ m

    return reference_svg(kit, ids=part_ids(kit, cond), modify=move)


def test_replay_ghosts_sit_exactly_on_a_translated_solution():
    import numpy as np
    from kitbench.grader import grade
    from kitbench.overlay import replay_payload

    kit, cond = "bike", "A"
    reply = shifted_reply(kit, cond, 200, 50)
    payload = replay_payload(kit, reply, cond, grade(kit, reply, cond))
    assert all(p["end"] is not None for p in payload["parts"])
    for p in payload["parts"]:
        assert np.allclose(p["end"], p["ref"], atol=1e-3), p["part"]


def test_alignment_uses_only_the_base_part_so_a_misplaced_part_stays_visible():
    import numpy as np
    from kitbench.overlay import aligned_reference, sanitised_placements
    from kitbench.kit import load_task

    kit, cond = "bike", "A"
    base = load_task(kit).UPRIGHT[0]
    other = next(p for p in load_task(kit).PARTS if p != base)

    def move(part, m):
        t = np.eye(3)
        t[0, 2] = 300 if part == other else 40
        return t @ m

    reply = reference_svg(kit, ids=part_ids(kit, cond), modify=move)
    placed = sanitised_placements(kit, reply, cond)
    aligned = aligned_reference(kit, placed)
    assert np.allclose(aligned[base], placed[base], atol=1e-3)
    assert abs(aligned[other][0, 2] - placed[other][0, 2]) > 200


def test_trial_reference_and_model_svg_share_one_window(server):
    r, q = failed_trial()
    code, ctype, ref = request(server[0], "GET", f"/svg/reference?{q}&plain=1&fit=1")
    model = request(server[0], "GET", f"/svg/trial?src=results&{q}&plain=1&fit=1")[2]
    assert code == 200 and ctype == "image/svg+xml" and b"<use" in ref

    def window(body: bytes) -> str:
        text = body.decode()
        return text[text.index('viewBox="') + 9:text.index('"', text.index('viewBox="') + 9)]

    assert window(ref) == window(model)
    assert request(server[0], "GET", "/svg/reference?cond=A&kit=bike&model=nope&trial=1")[0] == 404


def test_kit_sheet_has_no_attach_points_and_captions_follow_the_condition(server):
    kit = "wheelbarrow"
    code, ctype, body = request(server[0], "GET", f"/svg/kit?kit={kit}&cond=A")
    text = body.decode()
    assert code == 200 and ctype == "image/svg+xml" and 'fill="red"' not in text and "<circle" not in text
    assert ">Wheel fork<" in text and "wheel_fork" not in text.replace("kit-wheel_fork", "")
    anon = request(server[0], "GET", f"/svg/kit?kit={kit}&cond=B")[2].decode()
    assert ">p01<" in anon and ">Boom<" not in anon
    for bad in ("kit=nope&cond=A", f"kit={kit}&cond=Z", "kit=../x"):
        assert request(server[0], "GET", "/svg/kit?" + bad)[0] == 404


def test_annotated_every_mark_and_fitted_window(server):
    r, q = failed_trial()
    text = request(server[0], "GET", f"/svg/annotated?src=results&{q}&all=1&fit=1&zoom=0")[2].decode()
    assert text.startswith("<svg") and "#d03b3b" in text and "#0ca30c" in text and text.count(" pixels off</text>") >= 1


def test_angle_check_closeup_shows_both_orientations_and_degrees(server):
    rows = [r for r in dashboard.submitted_rows() if r.get("status") == "ok"
            and any(not c["ok"] and c["kind"] == "orient" for c in r["grade"]["checks"])]
    r = rows[0]
    i = next(i for i, c in enumerate(r["grade"]["checks"]) if not c["ok"] and c["kind"] == "orient")
    q = f"cond={r['condition']}&kit={r['kit']}&model={r['model']}&trial={r['trial']}&i={i}"
    text = request(server[0], "GET", f"/svg/annotated?{q}")[2].decode()
    assert "°</text>" in text and "#0ca30c" in text and "#d03b3b" in text and "<path d=\"M" in text


def test_closeup_window_can_extend_past_the_canvas_edge():
    from kitbench.overlay import _view

    x, y, w, h = _view([[100.0, -90.0], [110.0, -70.0]])
    assert y < 0 and abs(w / h - 1.5) < 1e-6 and w >= 110


def test_overview_has_story_as_of_and_display_letters(server):
    d = json.loads(request(server[0], "GET", "/api/overview")[2])
    assert d["as_of"].endswith("+00:00") and d["story"]["failed"] >= 1 and d["story"]["noun"]
    letters = {c["id"]: c["letter"] for c in d["conditions"]}
    assert letters == {c: {"B": "B", "A": "A", "C": "C", "A_alt": "A′"}[c] for c in letters} and {"B", "A", "C"} <= set(letters)
    assert "A_alt" not in [c["letter"] for c in d["conditions"]]


def test_mistakes_do_not_repeat_one_displaced_part():
    from kitbench import stats

    top = stats.top_mistakes(dashboard.submitted_rows(), 12)
    keys = [(m["kit"], m["trials"], m["median_err"]) for m in top]
    assert len(keys) == len(set(keys))


def test_method_lists_check_names_and_kits_run(server):
    d = json.loads(request(server[0], "GET", "/api/method")[2])
    assert {k["name"] for k in d["check_kinds"]} >= {"Joint", "On guide line", "Orientation"} and d["kits_run"]


def test_home_fonts_served_with_types(server):
    code, ctype, body = request(server[0], "GET", "/vendor/fonts/fonts.css")
    assert code == 200 and ctype.startswith("text/css") and b"font-face" in body
    for name in ("RobotoCondensed", "SourceSerif4"):
        code, ctype, body = request(server[0], "GET", f"/vendor/fonts/{name}.woff2")
        assert code == 200 and ctype == "font/woff2" and len(body) > 1000


def test_plain_kit_sheet_has_no_captions_or_paper(server):
    kit = kit_names()[0]
    code, ctype, body = request(server[0], "GET", f"/svg/kit?kit={kit}&cond=A&plain=1")
    assert code == 200 and ctype == "image/svg+xml" and b"<use" in body and b"<text" not in body and b"<rect" not in body


def test_kit_svg_endpoints_serve_xml_and_validate(server):
    import xml.etree.ElementTree as ET
    from kitbench.templates import fill
    kit = kit_names()[0]
    for cond in ("A", "B", "C"):
        q = f"kit={kit}&cond={cond}"
        code, ctype, parts = request(server[0], "GET", "/svg/kitparts?" + q)
        assert code == 200 and ctype == "image/svg+xml"
        assert parts.decode() in fill(kit, cond) and b"<use" not in parts
        ET.fromstring(parts)
        code, ctype, sol = request(server[0], "GET", "/svg/solution?" + q)
        assert code == 200 and ctype == "image/svg+xml" and b"<defs>" in sol and b"<use" in sol
        ET.fromstring(sol)
        code, ctype, body = request(server[0], "GET", "/api/kitsvg?" + q)
        data = json.loads(body)
        assert code == 200 and ctype == "application/json" and data["parts_svg"] == parts.decode() and data["solution_svg"] == sol.decode()
    assert ">p01<" not in parts.decode() and "kit-p01" in request(server[0], "GET", f"/svg/kitparts?kit={kit}&cond=B")[2].decode()


@pytest.mark.parametrize("path", ["/svg/kitparts", "/svg/solution", "/api/kitsvg"])
def test_kit_svg_endpoints_reject_bad_input(server, path):
    kit = kit_names()[0]
    for bad in ("kit=nope&cond=A", f"kit={kit}&cond=Z", "kit=../x&cond=A", f"kit={kit}&cond=A%00"):
        assert request(server[0], "GET", f"{path}?{bad}")[0] == 404
    for bad in ("", f"kit={kit}", f"cond=A", f"kit={kit}&cond=A&x=1", f"kit={kit}&kit={kit}&cond=A"):
        assert request(server[0], "GET", f"{path}?{bad}")[0] == 400


def test_overview_home_fields(server):
    code, _, body = request(server[0], "GET", "/api/overview")
    data = json.loads(body)
    assert code == 200 and {"models", "kits", "trials", "kit_names"} <= set(data["totals"])
    assert all(m["short"] and "max_err" in m for m in data["top_mistakes"])
    hero = data["hero"]
    if hero is None:
        return
    assert len(hero["view"]) == 4 and hero["short"]
    q = f"src=results&cond={hero['cond']}&kit={hero['kit']}&model={hero['model']}&trial={hero['trial']}&plain=1&paper=0"
    for path in (f"/svg/trial?{q}&fit=1", f"/svg/reference?{q}"):
        code, ctype, svg = request(server[0], "GET", path)
        assert code == 200 and ctype == "image/svg+xml" and b"<rect" not in svg


def test_post_rejects_foreign_origin_and_wrong_content_type(server):
    srv = server[0]
    port = srv.server_address[1]

    def post(headers: dict, body: bytes = b"{}") -> int:
        conn = http.client.HTTPConnection("127.0.0.1", port, timeout=30)
        conn.request("POST", "/api/plan", body=body, headers=headers)
        code = conn.getresponse().status
        conn.close()
        return code

    assert post({"Content-Type": "text/plain"}) == 415
    assert post({"Content-Type": "application/json", "Origin": "http://evil.example"}) == 403
    assert post({"Content-Type": "application/json", "Host": "evil.example"}) == 403
    assert post({"Content-Type": "application/json", "Origin": f"http://localhost:{port}"}) == 400


def test_vertex_route_needs_no_claude_key(server, monkeypatch):
    srv = server[0]
    monkeypatch.setenv("CLAUDE_ROUTE", "vertex")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_CLOUD_PROJECT", raising=False)
    body = {"condition": "A", "kits": ["bike"], "models": ["claude-haiku-5-5"], "trials": 1, "workers": 1}
    code, _, out = request(srv, "POST", "/api/run", body)
    assert code == 400 and b"GOOGLE_CLOUD_PROJECT" in out and b"ANTHROPIC_API_KEY" not in out


def test_method_shows_settings_stored_in_results(server):
    d = json.loads(request(server[0], "GET", "/api/method")[2])
    for m in d["models"]:
        assert m["settings"]["max_tokens"] == 128000 and m["settings"]["route"] == "vertex"


def test_options_list_only_models_with_results(server):
    o = json.loads(request(server[0], "GET", "/api/options")[2])
    assert o["models"] == dashboard.result_models() and not any(m.startswith("gemini") for m in o["models"])


def test_estimate_cost_uses_each_models_output_cap():
    low = run_eval.estimate_cost([("A", "bike", "claude-haiku-5-5", 1)])
    expected = (len(run_eval.fill("bike", "A")) / 4 * 0.10 + 128000 * 0.50) / 1e6
    assert f"${expected:,.2f}" in low


def test_all_models_means_the_three_claude_models():
    assert kitbench.models.RUN_MODELS == ["claude-opus-5-5", "claude-sonnet-5-5", "claude-haiku-5-5"]
    assert set(kitbench.models.RUN_MODELS) < set(kitbench.models.MODELS)
