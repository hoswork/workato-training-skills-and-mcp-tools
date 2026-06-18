# workato-training-skills-and-mcp-tools

Monorepo for Workato training team Claude skills and MCP servers.

## Structure

```
pillars/        ← canonical Standards Desk pillar rubrics (source of truth)
skills/         ← Claude Code/Desktop skill source files
mcp/            ← Workato MCP server implementations
  standards-desk/
  qr-code/
  kahoot-generator/
pipeline/       ← build + sync tooling
  sync_pipeline.py   (pillar sync: canonical → skills + MCP)
  Makefile           (make build / test / deploy-skills / deploy-mcp)
```

## When a pillar changes

Edit `pillars/<pillar>.md` → pre-commit hook runs tests → commit → run pipeline:

```bash
make sync          # dry run: diff + build + test + changelog
make deploy-skills # Gate 1: skill zips + Confluence
make deploy-mcp    # Gate 2: Workato push + MCP re-assign
```

## MCP servers

Each server in `mcp/` has its own isolated Workato project. Push to one doesn't affect others.

```bash
cd mcp/<server>/workato && workato push --restart-recipes
# Then re-assign tools via Dev API — push clears assignments
```

## AVOID

`mcp__workato-dev-api__post_api_collections_api_endpoints` — poisons the MCP tool list. (PSM-21498)

## Skill vs MCP decision rule

Before building anything new, decide which archetype it is:

| Archetype | Pattern | Example |
|---|---|---|
| **Consumer skill** | Calls many MCPs + reasons over results; runs in the user's Claude session with their credentials | brief-me, addie-plan, wow-plan |
| **Provider MCP** | Exposes a deterministic, credential-free operation to clients; deployed as a Workato recipe | standards-desk, kahoot-generator, qr-code |
| **Static validator** | Runs locally on Claude Code; zero LLM tokens; TypeScript/Python linter against §Static checks | the-once-over (Code path) |

**Should it be an MCP server?** Only if:
1. The operation is deterministic and stateless (same input → same output every time)
2. It does NOT require the calling user's personal credentials (Jira, Gmail, Gong, Slack, Drive are all personal-auth — these can't be shared service accounts without a significant IT decision)
3. Any user, not just the author, would get the same result

**Brief-me is the canonical counter-example.** It consumes 6+ authenticated MCP servers (Jira, Drive, Snowflake, Gong, Gmail, Slack) — all personal-auth. It can never be a provider MCP because there is no shared credential that works for all users. It is a consumer skill.

**Standards-desk is the canonical provider example.** Static checks run against the artifact itself — no user credentials needed. Any user gets the same result from the same input. Deterministic, shareable, appropriate for a backend recipe.
