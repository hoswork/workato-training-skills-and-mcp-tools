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
