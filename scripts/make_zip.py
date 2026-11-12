"""Build dist/kit-assembly-eval.zip from an explicit include list and fail if it is over the size limit."""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIP_PATH = ROOT / "dist" / "kit-assembly-eval.zip"
LIMIT_MB = 50
INCLUDE = ["README.md", "RULES.md", "STORY.md", "CHECK_REPORT.md", "docs", "requirements.txt", ".env.example",
           "run_eval.py", "dashboard.py", "kitbench", "scripts", "tests", "tasks", "results", "results_raw", "transcripts",
           "review", "kitmaking", "web"]
SKIP_DIRS = {"__pycache__", ".pytest_cache", "logs", "dist", "qa", "scratch"}
SKIP_FILES = {".env", ".DS_Store", "UI_FIXES.md", "UI_SPEC.md", "DESIGN_HOME.md", "COPY_HOME.md"}
SKIP_SUFFIXES = {".pyc", ".tmp", ".log"}
HOME_PATH = re.compile(rb"/Users/|/home/[a-z]|C:\\\\Users")
TEXT_SUFFIXES = {".py", ".md", ".txt", ".json", ".svg", ".js", ".css", ".html", ".csv", ".example"}


def package_files() -> list[Path]:
    """Every file on the include list, minus excluded folders, names and suffixes."""
    out = []
    for name in INCLUDE:
        top = ROOT / name
        for p in ([top] if top.is_file() else sorted(top.rglob("*")) if top.is_dir() else []):
            rel = p.relative_to(ROOT)
            if p.is_file() and not (set(rel.parts) & SKIP_DIRS) and p.name not in SKIP_FILES and p.suffix not in SKIP_SUFFIXES:
                out.append(p)
    return out


def has_home_path(p: Path) -> bool:
    """True when a text file mentions a home-directory path."""
    return p.suffix in TEXT_SUFFIXES and bool(HOME_PATH.search(p.read_bytes()))


def build(dest: Path = ZIP_PATH) -> tuple[Path, list[Path]]:
    """Write the ZIP; returns it and the files left out because they mention a home path."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    left_out = []
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for p in package_files():
            if p.name == "make_zip.py" or p.name == "check_package.py" or not has_home_path(p):
                z.write(p, Path("kit-assembly-eval") / p.relative_to(ROOT))
            else:
                left_out.append(p)
    return dest, left_out


def main() -> None:
    if "VIDEO_LINK_HERE" in (ROOT / "README.md").read_text():
        print("README still has VIDEO_LINK_HERE: add the video link before building the ZIP")
        sys.exit(1)
    """Build the ZIP, print its size and exit non-zero when it is over the limit."""
    dest, left_out = build()
    for p in left_out:
        print(f"left out (home path): {p.relative_to(ROOT)}")
    mb = dest.stat().st_size / 1e6
    print(f"{dest.relative_to(ROOT)}: {mb:.1f} MB")
    if mb > LIMIT_MB:
        print(f"over the {LIMIT_MB} MB limit")
        sys.exit(1)


if __name__ == "__main__":
    main()
