#!/usr/bin/env python3
"""Read-only project inventory. Does not execute project files."""
import argparse, json
from pathlib import Path

SKIP_DIRS = {".git", ".gradle", ".idea", "node_modules", "build", "dist", ".venv", "__pycache__"}
INTERESTING = {
    "AndroidManifest.xml", "build.gradle", "build.gradle.kts", "settings.gradle",
    "settings.gradle.kts", "package.json", "pubspec.yaml", "Cargo.toml",
    "pyproject.toml", "requirements.txt", "pom.xml", "go.mod", "Dockerfile",
    "docker-compose.yml", "docker-compose.yaml", ".env.example", ".env.sample"
}
SECRET_HINTS = ("secret", "password", "token", "apikey", "api_key", "private_key", "credential")

def main():
    ap = argparse.ArgumentParser(description="Create a read-only inventory of a project directory.")
    ap.add_argument("project", help="Path to authorized project directory")
    ap.add_argument("--out", default="reports/inventory.json", help="Output JSON path")
    args = ap.parse_args()
    base = Path(args.project).expanduser().resolve()
    if not base.is_dir():
        raise SystemExit(f"Not a directory: {base}")
    items, markers, warnings = [], [], []
    for p in base.rglob("*"):
        if any(part in SKIP_DIRS for part in p.relative_to(base).parts):
            continue
        rel = p.relative_to(base).as_posix()
        if p.is_file():
            try:
                size = p.stat().st_size
            except OSError:
                size = None
            items.append({"path": rel, "size_bytes": size, "suffix": p.suffix.lower()})
            if p.name in INTERESTING:
                markers.append(rel)
            low = p.name.lower()
            if any(h in low for h in SECRET_HINTS) or (p.name.startswith(".env") and p.name not in {".env.example", ".env.sample"}):
                warnings.append({"path": rel, "warning": "Potential secret-bearing file; do not print or commit its contents."})
    result = {
        "project_root": str(base),
        "file_count": len(items),
        "files": sorted(items, key=lambda x: x["path"].lower()),
        "project_markers": sorted(markers),
        "security_warnings": warnings,
        "execution_performed": False
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Inventory written to {out} ({len(items)} files). No project code was executed.")
if __name__ == "__main__":
    main()
