"""Pre-submission checks on the files that go into the ZIP: required items, secrets, personal paths, tool signatures, ZIP size."""
import json
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_zip  # noqa: E402

ROOT = make_zip.ROOT
REQUIRED = ["README.md", "tasks", "results", "results_raw", "transcripts", "requirements.txt", ".env.example", "CHECK_REPORT.md"]
BANNED = {
    "api key": re.compile(r"sk-ant-[A-Za-z0-9_-]{10,}|AIza[0-9A-Za-z_-]{20,}|AQ\.[A-Za-z0-9_-]{20,}"),
    "home path": re.compile(r"/Users/|/home/[a-z]|C:\\\\Users"),
    "tool signature": re.compile(r"(?i)generated (with|by) (claude|chatgpt|copilot)|co-authored-by|claude code|anthropic\.com/claude-code"),
}


def without_signatures(node):
    """The JSON value with every 'signature' field removed: those are opaque base64 blobs, not secrets."""
    if isinstance(node, dict):
        return {k: without_signatures(v) for k, v in node.items() if k != "signature"}
    if isinstance(node, list):
        return [without_signatures(v) for v in node]
    return node


def scan_text(p: Path) -> str:
    """The text of a file as it should be scanned."""
    text = p.read_text(errors="ignore")
    if p.suffix == ".json":
        try:
            return json.dumps(without_signatures(json.loads(text)))
        except ValueError:
            pass
    return text


def missing_items() -> list[str]:
    """Required top-level items that do not exist."""
    return [f"missing: {name}" for name in REQUIRED if not (ROOT / name).exists()]


def unmatched_results() -> list[str]:
    """Finished results without a raw response or a transcript."""
    out = []
    for path in sorted((ROOT / "results").glob("*/*/*.json")):
        rel = path.relative_to(ROOT / "results")
        try:
            ok = json.loads(path.read_text()).get("status") == "ok"
        except ValueError:
            out.append(f"unreadable result: {rel}")
            continue
        if ok and not (ROOT / "results_raw" / rel).is_file():
            out.append(f"no raw response for {rel}")
        if ok and not (ROOT / "transcripts" / rel.with_suffix(".md")).is_file():
            out.append(f"no transcript for {rel}")
    return out


def main() -> None:
    """Run the pre-submission checks and exit non-zero on any problem."""
    problems = missing_items() + unmatched_results()
    files = make_zip.package_files()
    for p in files:
        if p.suffix in {".png", ".jpg", ".mp4", ".mov", ".zip", ".woff2"}:
            if p.suffix in {".mp4", ".mov"}:
                problems.append(f"video in package: {p.relative_to(ROOT)}")
            continue
        if p.name in ("check_package.py", "make_zip.py"):
            continue
        text = scan_text(p)
        for label, rx in BANNED.items():
            m = rx.search(text)
            if m:
                problems.append(f"{label} in {p.relative_to(ROOT)}: {m.group(0)[:12]}...")
    with tempfile.TemporaryDirectory() as tmp:
        dest, _ = make_zip.build(Path(tmp) / "kit-assembly-eval.zip")
        mb = dest.stat().st_size / 1e6
    print(f"{len(files)} files, ZIP {mb:.1f} MB (limit {make_zip.LIMIT_MB} MB)")
    if mb > make_zip.LIMIT_MB:
        problems.append(f"ZIP is {mb:.1f} MB, over the {make_zip.LIMIT_MB} MB limit")
    print("\n".join(problems) if problems else "no problems found")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
