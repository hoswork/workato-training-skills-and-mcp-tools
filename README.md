# workato-training-skills-and-mcp-tools

Source repository for the Workato training team's Claude skills and Workato MCP servers.

**What lives here:**
- `pillars/` — canonical Standards Desk pillar rubrics (the source of truth for quality checks)
- `skills/` — Claude Code/Desktop skills distributed to the training and education team
- `mcp/` — Workato-hosted MCP servers accessible from Claude Code and Claude Desktop
- `pipeline/` — sync and build tooling

**Install the skills:** https://workato.atlassian.net/wiki/spaces/ETT/pages/2604859430/AI+Initiatives+Shared+Skills  
**Full BT MCP registry:** https://workato.atlassian.net/wiki/spaces/extbt/pages/2510848002/Internal+MCPs+BT+Managed

---

## The three layers

### Pillar rubrics (`pillars/`)

The Standards Desk quality framework. Each pillar is a markdown file that defines what "good" looks like for a specific dimension of training content:

| Pillar | What it checks |
|---|---|
| `say-it-plain` | Jargon, hype, marketing-speak |
| `fact-check` | Feature GA dates, product claims, PM attribution |
| `stick-check` | Memorability — SUCCESs framework |
| `calibrate-challenge` | Difficulty calibration, adult learning principles |
| `delight-check` | Engagement, game beats, delight design |
| `team-style-guide` | Workato training team style conventions |
| `complete-check` | Structural completeness |

These files are the canonical source. Changes here propagate automatically to the Claude skills and the MCP server via the sync pipeline.

### Claude skills (`skills/`)

Skills are installed into Claude Code or Claude Desktop and give team members AI-assisted workflows:

| Skill | Who uses it | What it does |
|---|---|---|
| `the-once-over` | Trainer + Education | Standards Desk quality evaluation |
| `wow-plan` | Trainer | Plans 1-day WoW workshop courses |
| `addie-plan` | Education | Guides ADDIE e-learning course design |
| `mbo-asset-tracker` | Trainer + Education | Logs AI work to quarterly MBO sheet |
| `the-tape` | Trainer + Education | Records decisions that extend team standards |
| `generate-kahoot` | Trainer | Generates Kahoot quiz from learning artifacts |
| `file-workato-product-bug` | Everyone | Files CCE product bugs |
| `workato-setup` | Trainer + Education | Configures Claude Code with Workato MCPs |

Install: https://workato.atlassian.net/wiki/spaces/ETT/pages/2604859430/AI+Initiatives+Shared+Skills

### MCP servers (`mcp/`)

Workato-hosted tools that any team member can call from Claude, without installing anything:

| Server | Tools | Who can use |
|---|---|---|
| `standards-desk` | `list_pillars` · `get_rubrics` · `run_static_checks` | Trainer + Education |
| `kahoot-generator` | `get_kahoot_constraints` · `format_kahoot` | Trainer |
| `qr-code` | `generate_qr_code` | Trainer |

Each server runs in its own isolated Workato project — deploying one doesn't affect the others.

---

## Getting started (contributors)

### Prerequisites

- Python 3.9+
- `workato-platform-cli` (`pip install workato-platform-cli`)
- Workato trial workspace access (ask Heiwad)
- Dev API token in `~/.mcp.json` (from the trial workspace profile)

### Clone and verify

```bash
git clone https://github.com/hoswork/workato-training-skills-and-mcp-tools.git
cd workato-training-skills-and-mcp-tools
python3 pipeline/sync_pipeline.py --stage test  # should show ✅ for all 8 tests
```

---

## Making changes

### Editing a pillar rubric

1. Edit the file in `pillars/` (e.g. `pillars/say-it-plain.md`)
2. Commit — the pre-commit hook runs regression tests automatically
3. If tests pass, the commit goes through
4. Run the sync pipeline to propagate changes downstream:

```bash
make sync           # see what changed, run tests, generate changelog
make deploy-skills  # Gate 1: rebuild skill zips + push to GitHub + update Confluence
make deploy-mcp     # Gate 2: push to Workato + re-assign MCP tools (run separately)
```

### Editing a skill

1. Edit the skill's `SKILL.md` in `skills/<skill-name>/`
2. Bump `metadata.version` in the frontmatter
3. Update `manifest.json` version for that skill
4. Run `make deploy-skills` to rebuild zips and publish

### Editing an MCP server recipe

1. Edit the Python source in `mcp/<server>/cli/`
2. Embed into recipe JSON (see each server's `CLAUDE.md` for the exact build step)
3. Push: `cd mcp/<server>/workato && workato push --restart-recipes`
4. Re-assign tools via Dev API (push clears assignments — see `CLAUDE.md`)

---

## CI pipeline (what happens on commit)

The pre-commit hook automatically:
1. **Detects** if `pillars/` or MCP recipe files are in the staged changes
2. **Runs** 8 regression tests (hype catches, clean passes, audience scoping, not-applicable behavior)
3. **Blocks** the commit if any test fails
4. **Scans** log and decision files for PII (emails, phone numbers, SSNs) and secrets (tokens, API keys, private keys)

The sync pipeline has two explicit publish gates:
- **Gate 1** (`make deploy-skills`) — skill zips → GitHub → Drive → Confluence
- **Gate 2** (`make deploy-mcp`) — Workato push + MCP tool re-assign (requires local Workato credentials)

---

## Architecture notes

- `pillars/` is the canonical source. `skills/the-once-over/pillars/` and `mcp/standards-desk/content/pillars/` are downstream copies maintained by the pipeline.
- MCP static checks are Python rules extracted from the pillar `§Static checks` sections. LLM reasoning stays client-side.
- Each MCP server is isolated (its own Workato project). Pushing one doesn't restart or affect the others.
- The pre-commit hook prevents secrets and PII from landing in log or decision files. Use `[REDACTED]` for sensitive values.
