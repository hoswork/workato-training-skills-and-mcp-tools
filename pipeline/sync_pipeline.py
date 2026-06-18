"""
Standards Desk sync pipeline.

Triggered by git push when content/pillars/ changes.
Two separate publish gates: skills distro and MCP deploy.

Usage:
  python3 cli/sync_pipeline.py              # full pipeline (interactive)
  python3 cli/sync_pipeline.py --check      # CI mode: stages 1-6 only, no deploy
  python3 cli/sync_pipeline.py --stage test # run tests only
  python3 cli/sync_pipeline.py --deploy mcp # Gate 2: MCP only (requires local creds)

Stages:
  1  DIFF           mechanical  — detect changed canonical pillar files
  2  COPY           mechanical  — copy to skill-packages + content/pillars/
  3  EXTRACT        mechanical  — parse §Static checks → flag rule changes
  4  BUILD          mechanical  — rebuild recipe Python + skill-packages zips (+ projection)
  5  TEST           mechanical  — regression tests against fixtures
  6  CHANGELOG      reasoning   — interpret changes for human review
  ── GATE 1 ────────────────────────────── skill distro publish
  7  SKILLS DEPLOY  mechanical  — push skill-packages to GitHub + Drive + Confluence
  ── GATE 2 ────────────────────────────── MCP deploy (separate, explicit)
  8  MCP DEPLOY     mechanical  — Workato push + MCP re-assign tools
"""

import os, sys, json, re, subprocess, hashlib
from pathlib import Path
import datetime

ROOT = Path(__file__).parent.parent          # repo root
CANONICAL_DIR = ROOT / "pillars"             # canonical pillar source
CONTENT_DIR = ROOT / "mcp/standards-desk/content/pillars"
SKILL_PACKAGES_PILLARS = ROOT / "skills/the-once-over/pillars"
CLI_DIR = ROOT / "mcp/standards-desk/cli"
FIXTURES_DIR = CLI_DIR / "test_fixtures"
SKILL_PACKAGES = Path.home() / "code/skill-packages"  # legacy — remove after migration

PILLARS = [
    "say-it-plain", "fact-check", "stick-check",
    "calibrate-challenge", "delight-check", "team-style-guide"
]

# ── Helpers ───────────────────────────────────────────────────────────────

def banner(stage, name, mode="mechanical"):
    icon = {"mechanical": "🔧", "reasoning": "🧠", "human": "👤", "gate": "🔒"}[mode]
    print(f"\n{icon}  Stage {stage}: {name}")
    print("─" * 55)

def ok(msg): print(f"  ✅ {msg}"); return True
def fail(msg): print(f"  ❌ {msg}"); return False
def warn(msg): print(f"  ⚠️  {msg}")

def file_hash(path):
    return hashlib.md5(Path(path).read_bytes()).hexdigest() if Path(path).exists() else ""

# ── Stage 1: DIFF ─────────────────────────────────────────────────────────

def stage_diff():
    banner(1, "DIFF", "mechanical")
    changes = {}
    for pillar in PILLARS:
        canonical = CANONICAL_DIR / f"{pillar}.md"
        content_copy = CONTENT_DIR / f"{pillar}.md"
        sp_copy = SKILL_PACKAGES / "the-once-over/pillars" / f"{pillar}.md"
        if not canonical.exists():
            warn(f"{pillar}: canonical missing — skip")
            continue
        ch = file_hash(canonical)
        content_stale = ch != file_hash(content_copy)
        sp_stale = ch != file_hash(sp_copy)
        if content_stale or sp_stale:
            changes[pillar] = {"content_stale": content_stale, "sp_stale": sp_stale}
            destinations = []
            if content_stale: destinations.append("content/pillars")
            if sp_stale: destinations.append("skill-packages")
            fail(f"{pillar}: stale in {', '.join(destinations)}")
        else:
            ok(f"{pillar}: in sync")
    if not changes:
        print("\n  ✅ All pillars in sync. Nothing to do.")
        sys.exit(0)
    print(f"\n  {len(changes)} pillar(s) need sync: {list(changes.keys())}")
    return changes

# ── Stage 2: COPY ─────────────────────────────────────────────────────────

def stage_copy(changes):
    banner(2, "COPY", "mechanical")
    for pillar, info in changes.items():
        canonical = CANONICAL_DIR / f"{pillar}.md"
        text = canonical.read_text()
        if info.get("content_stale"):
            (CONTENT_DIR / f"{pillar}.md").write_text(text)
            ok(f"{pillar} → content/pillars/")
        if info.get("sp_stale"):
            sp_dest = SKILL_PACKAGES / "the-once-over/pillars" / f"{pillar}.md"
            sp_dest.write_text(text)
            ok(f"{pillar} → skill-packages/the-once-over/pillars/")

# ── Stage 3: EXTRACT (flag rule changes) ─────────────────────────────────

def extract_static_rules(text):
    """Extract explicitly enumerated static rules from pillar §Static checks."""
    banned, patterns, presence = [], [], []
    in_static = False
    for line in text.splitlines():
        if re.search(r'##\s+Static\s+checks', line, re.I): in_static = True
        elif re.match(r'##\s+', line) and in_static: in_static = False
        if not in_static: continue
        for m in re.findall(r'`([^`]{2,40})`', line):
            if not m.startswith(r'\b') and len(m.split()) <= 5:
                banned.append(m.lower())
        if re.search(r'regex|pattern|\\b', line, re.I):
            patterns.append(line.strip()[:80])
    return {"banned": list(dict.fromkeys(banned)), "patterns": patterns}

def stage_extract(changes):
    banner(3, "EXTRACT", "mechanical")
    extracted = {}
    for pillar in changes:
        canonical = CANONICAL_DIR / f"{pillar}.md"
        rules = extract_static_rules(canonical.read_text())
        extracted[pillar] = rules
        n_banned = len(rules["banned"])
        n_pat = len(rules["patterns"])
        if n_banned == 0 and n_pat == 0:
            warn(f"{pillar}: no extractable rules found — verify §Static checks section exists")
        else:
            ok(f"{pillar}: {n_banned} banned phrases, {n_pat} pattern hints extracted")
    return extracted

# ── Stage 4: BUILD ────────────────────────────────────────────────────────

def stage_build():
    banner(4, "BUILD", "mechanical")
    # Embed rubrics into cli/*.py modules
    r = subprocess.run([sys.executable, str(CLI_DIR / "build.py")],
                       capture_output=True, text=True, cwd=str(ROOT))
    if r.returncode == 0:
        ok("build.py: rubrics embedded into cli/*.py")
    else:
        fail(f"build.py failed: {r.stderr[:200]}")
        return False

    # Run skill-packages build (zips + say-it-plain projection)
    build_cmd = """
mkdir -p dist/skills dist/bundles
for skill in addie-plan file-workato-product-bug generate-kahoot the-once-over the-tape wow-plan; do
  zip -qr "dist/skills/${skill}.zip" "${skill}/" -x "*.DS_Store"
done
mkdir -p say-it-plain
cp the-once-over/pillars/say-it-plain.md say-it-plain/SKILL.md
python3 - <<'PYEOF'
import re
with open('say-it-plain/SKILL.md') as f: c = f.read()
c = re.sub(r'### Workato-internal carve-outs\n.*?(?=### Team-specific carve-outs)', '', c, flags=re.DOTALL)
c = re.sub(r'### Team-specific carve-outs\n.*?(?=## What this skill is NOT)',
    '### Team-specific carve-outs\n\nAdd team-specific phrase exceptions here.\n\n', c, flags=re.DOTALL)
c = c.replace('name: say-it-plain\n', 'name: say-it-plain\nmetadata:\n  version: "1.0"\n')
c = c.rstrip() + '\n\n## Logging\n\nAt completion, invoke: `skill-logger say-it-plain` (if available; skip silently if not).\n'
with open('say-it-plain/SKILL.md', 'w') as f: f.write(c)
PYEOF
zip -qr dist/skills/say-it-plain.zip say-it-plain/ -x "*.DS_Store" && rm -rf say-it-plain
"""
    r2 = subprocess.run(build_cmd, shell=True, capture_output=True, text=True, cwd=str(SKILL_PACKAGES))
    if r2.returncode == 0:
        ok("skill-packages: zips rebuilt (including say-it-plain projection)")
    else:
        fail(f"skill-packages build failed: {r2.stderr[:200]}")
        return False

    warn("recipe_run_static_checks.py rules are inline — review Stage 6 for any rule deltas")
    return True

# ── Stage 5: TEST ─────────────────────────────────────────────────────────

def run_checker(artifact, audience, pillars):
    sys.path.insert(0, str(CLI_DIR))
    import importlib
    for k in list(sys.modules):
        if 'recipe_run_static_checks' in k: del sys.modules[k]
    rsc = importlib.import_module('recipe_run_static_checks')
    out = rsc.main({"artifact": artifact, "audience": audience, "pillars_json": json.dumps(pillars)})
    return json.loads(out["results_json"])

def stage_test():
    banner(5, "TEST", "mechanical")
    passed = True
    hype = (FIXTURES_DIR / "hype.txt").read_text()
    clean = (FIXTURES_DIR / "clean.txt").read_text()
    exp = json.loads((FIXTURES_DIR / "hype_expected.json").read_text())

    # Hype catches
    r = run_checker(hype, "workato", ["say-it-plain"])
    sip = r.get("say-it-plain", {})
    findings = [f["match"] for f in sip.get("findings", [])]
    p = not sip.get("pass") and len(findings) >= exp["say-it-plain"]["min_findings"]
    passed &= ok(f"hype/say-it-plain: {len(findings)} findings") if p else fail(f"hype/say-it-plain: only {len(findings)} findings (need ≥{exp['say-it-plain']['min_findings']})")
    for phrase in exp["say-it-plain"]["must_match"]:
        found = any(phrase.lower() in f.lower() for f in findings)
        passed &= ok(f"  → '{phrase}' caught") if found else fail(f"  → '{phrase}' NOT caught — regression")

    # TSG training catches
    r2 = run_checker(hype, "training", ["team-style-guide"])
    tsg = r2.get("team-style-guide", {})
    tsg_findings = [f["match"] for f in tsg.get("findings", [])]
    p2 = not tsg.get("pass")
    passed &= ok(f"hype/team-style-guide (training): {len(tsg_findings)} findings") if p2 else fail("hype/team-style-guide (training): should fail but passed")

    # TSG workato = not applicable
    r3 = run_checker(hype, "workato", ["team-style-guide"])
    p3 = r3.get("team-style-guide", {}).get("pass") is True
    passed &= ok("team-style-guide (workato): not-applicable → pass") if p3 else fail("team-style-guide (workato): should be not-applicable")

    # Clean passes
    r4 = run_checker(clean, "workato", ["say-it-plain"])
    p4 = r4.get("say-it-plain", {}).get("pass") is True
    passed &= ok("clean/say-it-plain: pass") if p4 else fail("clean/say-it-plain: clean text should pass")

    print(f"\n  {'✅ All tests passed' if passed else '❌ Test failures — fix before proceeding'}")
    return passed

# ── Stage 6: CHANGELOG (reasoning) ───────────────────────────────────────

def stage_changelog(changes, extracted, test_passed):
    banner(6, "CHANGELOG", "reasoning")
    today = datetime.date.today().isoformat()
    lines = [f"## Sync {today}", f"**Changed:** {', '.join(changes.keys())}",
             f"**Tests:** {'✅ passed' if test_passed else '❌ FAILED'}",
             "\n**Rule extraction:**"]
    for pillar, rules in extracted.items():
        n = len(rules["banned"])
        lines.append(f"- {pillar}: {n} banned phrases, {len(rules['patterns'])} pattern hints")
        if rules["banned"]: lines.append(f"  sample: {rules['banned'][:5]}")
    lines += ["\n**Review before Gate 1 (skills distro):**",
              "- [ ] Extracted rules match §Static checks intent",
              "- [ ] No unintentional removals",
              "- [ ] recipe_run_static_checks.py updated if rules changed",
              "\n**Before Gate 2 (MCP deploy):**",
              "- [ ] Workato push ready",
              "- [ ] Tool re-assign ready"]
    changelog = "\n".join(lines)
    print(changelog)
    log_path = ROOT / "CHANGELOG-sync.md"
    with open(log_path, "a") as f: f.write("\n\n" + changelog)
    ok(f"Changelog appended to {log_path.name}")
    return changelog

# ── Gate 1: Skills deploy ─────────────────────────────────────────────────

def gate_skills_deploy(auto=False):
    banner("GATE 1", "SKILLS DISTRO PUBLISH", "gate")
    if not auto:
        answer = input("  Publish skills distro to GitHub + Drive + Confluence? [y/N] ").strip().lower()
        if answer != "y": print("  Skipped."); return False
    r = subprocess.run(["git", "add", "-A"], cwd=SKILL_PACKAGES, capture_output=True)
    r2 = subprocess.run(["git", "commit", "-m", f"sync: pillar update {datetime.date.today()}"],
                        cwd=SKILL_PACKAGES, capture_output=True)
    r3 = subprocess.run(["git", "push", "origin", "main"], cwd=SKILL_PACKAGES, capture_output=True)
    ok("skill-packages pushed to GitHub") if r3.returncode == 0 else fail("skill-packages push failed")
    warn("Upload dist/bundles/skills-distro.zip to Drive manually (no upload MCP available)")
    warn("Update Confluence page versions manually via Atlassian MCP")
    return r3.returncode == 0

# ── Gate 2: MCP deploy ────────────────────────────────────────────────────

def gate_mcp_deploy(auto=False):
    banner("GATE 2", "MCP DEPLOY", "gate")
    warn("This gate requires local Workato credentials and the workato CLI.")
    if not auto:
        answer = input("  Deploy to Workato + re-assign MCP tools? [y/N] ").strip().lower()
        if answer != "y": print("  Skipped."); return False
    workato_dir = ROOT / "workato"
    r = subprocess.run(["workato", "push", "--restart-recipes"],
                       cwd=str(workato_dir), capture_output=True, text=True)
    ok("Workato push complete") if r.returncode == 0 else fail(f"Workato push failed: {r.stderr[:150]}")
    # Commit workato-training-mcp
    repo = ROOT.parent.parent
    subprocess.run(["git", "add", "-A"], cwd=str(repo), capture_output=True)
    subprocess.run(["git", "commit", "-m", f"sync: pillar update {datetime.date.today()}"],
                   cwd=str(repo), capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=str(repo), capture_output=True)
    warn("Re-assign MCP tools via Dev API — push clears tool assignments (see mcp-server-post-push-wiring.md)")
    return r.returncode == 0

# ── Main ──────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    check_only = "--check" in args
    deploy_mcp = "--deploy" in args and "mcp" in args

    if "--stage" in args:
        i = args.index("--stage")
        if args[i+1] == "test":
            sys.exit(0 if stage_test() else 1)

    if deploy_mcp:
        gate_mcp_deploy()
        return

    print("═" * 55)
    print("  STANDARDS DESK SYNC PIPELINE")
    if check_only: print("  CHECK MODE — no deploy")
    print("═" * 55)

    changes = stage_diff()
    extracted = stage_extract(changes)
    stage_copy(changes)
    build_ok = stage_build()
    if not build_ok: print("\n❌ Build failed."); sys.exit(1)
    test_passed = stage_test()
    stage_changelog(changes, extracted, test_passed)

    if check_only:
        print(f"\n{'✅' if test_passed else '❌'} Check complete. {'Tests passed.' if test_passed else 'Fix test failures before deploying.'}")
        sys.exit(0 if test_passed else 1)

    if not test_passed:
        print("\n❌ Tests failed — cannot deploy. Fix and re-run."); sys.exit(1)

    gate_skills_deploy()
    print("\n  Gate 2 (MCP deploy) is separate — run when ready:")
    print("  python3 cli/sync_pipeline.py --deploy mcp")

if __name__ == "__main__":
    main()
