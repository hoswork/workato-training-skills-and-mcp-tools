"""
Build script — embeds pillar rubric markdown into each pillar Python file.
Run from standards-desk/ root before pushing to Workato.

Usage: python3 cli/build.py
Output: updates RUBRIC = "" placeholder in each cli/*.py with current content/pillars/*.md
"""
import os
import re

PILLAR_MAP = {
    "say_it_plain":        "say-it-plain.md",
    "fact_check":          "fact-check.md",
    "stick_check":         "stick-check.md",
    "calibrate_challenge": "calibrate-challenge.md",
    "delight_check":       "delight-check.md",
    "team_style_guide":    "team-style-guide.md",
}

def embed_rubric(pillar_module: str, rubric_filename: str):
    cli_dir = os.path.join(os.path.dirname(__file__))
    content_dir = os.path.join(os.path.dirname(__file__), "..", "content", "pillars")

    py_path = os.path.join(cli_dir, f"{pillar_module}.py")
    md_path = os.path.join(content_dir, rubric_filename)

    with open(md_path, "r") as f:
        rubric = f.read()

    with open(py_path, "r") as f:
        source = f.read()

    # Replace RUBRIC = "" with embedded content (triple-quoted)
    escaped = rubric.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    replacement = f'RUBRIC = """\\\n{escaped}\\\n"""'
    updated = re.sub(r'^RUBRIC = "".*?$', replacement, source, flags=re.MULTILINE)

    with open(py_path, "w") as f:
        f.write(updated)

    size = len(rubric)
    print(f"  {pillar_module}.py ← {rubric_filename} ({size:,} bytes)")

if __name__ == "__main__":
    print("Embedding rubrics into pillar Python files...")
    for module, filename in PILLAR_MAP.items():
        embed_rubric(module, filename)
    print("Done. Review changes before pushing to Workato.")
