"""Re-grade every saved model output with the current grader. Needs no API keys."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from kitbench.grader import grade  # noqa: E402
from run_eval import tags  # noqa: E402


def main() -> None:
    """Re-grade saved results and report any that differ."""
    changed = total = 0
    for path in sorted((ROOT / "results").glob("*/*/*.json")):
        r = json.loads(path.read_text())
        if r.get("status") != "ok":
            continue
        total += 1
        new = grade(r["kit"], r["output"], r["condition"])
        if new != r["grade"]:
            changed += 1
            print(f"changed: {path.relative_to(ROOT)}  {r['grade']['score']} -> {new['score']}")
            if "--write" in sys.argv:
                r["grade"], r["tags"] = new, tags(new, r.get("stop_reason", ""))
                path.write_text(json.dumps(r, indent=1))
    print(f"re-graded {total} results, {changed} differ from the stored grade")
    sys.exit(1 if changed and "--write" not in sys.argv else 0)


if __name__ == "__main__":
    main()
