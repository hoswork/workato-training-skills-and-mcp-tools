# workato-training-mcp — Claude context

Monorepo for Workato training team MCP servers. Each subdirectory is a self-contained MCP project with its own Workato project, recipe(s), and MCP server.

## MCP projects

| Directory | What it does |
|---|---|
| `qr-code/` | Generates Workato-branded QR codes as base64 PNG |
| `kahoot-generator/` | Validates and formats Kahoot quizzes as XLSX |
| `standards-desk/` | Standards Desk pillar checks — `list_pillars`, `get_rubrics`, `run_static_checks` |

## Standard project layout

Every project follows this structure:

```
<project>/
  CLAUDE.md                ← maintainer notes (minimal)
  mcp-server-prompt.md     ← MCP server description + tool descriptions (registration source of truth)
  content/                 ← content served by tools (markdown files, JSON)
  cli/                     ← Python source (source of truth for recipe snippets)
  workato/                 ← recipe JSON + .workatoenv
```

**Three audiences for each file:**
- `CLAUDE.md` → maintainer / Claude Code working on the code
- `mcp-server-prompt.md` → MCP clients (server description + tool descriptions get registered via Dev API)
- `content/` → end-user responses (what tools return — rubrics, metadata)

## Push workflow

Each project is isolated — push only affects its own recipes and MCP server:

```bash
cd <project>/workato && workato push --restart-recipes
# Then re-assign tools to the MCP server via Dev API (push clears assignments)
# Tool descriptions come from mcp-server-prompt.md
```

## AVOID

`mcp__workato-dev-api__post_api_collections_api_endpoints` — poisons the MCP tool list. All other Dev API tools are safe. (PSM-21498)
