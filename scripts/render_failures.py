"""Draw every failed trial (and the matching reference) into figures/failures/<condition>/<kit>/."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from kitbench.render import assembly_svg, to_png  # noqa: E402


def main() -> None:
    """Render every failed trial to PNG."""
    n = 0
    for path in sorted((ROOT / "results").glob("*/*/*.json")):
        r = json.loads(path.read_text())
        if r.get("status") != "ok" or r["grade"]["pass"]:
            continue
        g = r["grade"]
        title = f"{r['model']} t{r['trial']} ({r['condition']}): score {g['score']:.2f}"
        svg = assembly_svg(r["kit"], r["output"], r["condition"], title)
        if svg is None:
            continue
        to_png(svg, ROOT / "figures" / "failures" / r["condition"] / r["kit"] / f"{path.stem}.png")
        n += 1
    print(f"rendered {n} failed assemblies")


if __name__ == "__main__":
    main()
