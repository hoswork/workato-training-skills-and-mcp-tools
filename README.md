# workato-training-mcp

Workato training team MCP servers — a collection of AI tools built on the Workato platform and exposed via the Model Context Protocol.

## Projects

| Project | What it does |
|---|---|
| [qr-code](qr-code/) | Generates Workato-branded QR codes as base64 PNG |
| [kahoot-generator](kahoot-generator/) | Generates Kahoot-importable CSV quizzes from learning artifacts |

## Architecture

Each project is a Workato Agentic Skill backed by a Python snippet recipe, exposed as an MCP server via Workato's APIM. The MCP servers are BT-managed and available to all Workato employees via Claude Code or Claude Desktop.

Internal MCP registry: https://workato.atlassian.net/wiki/spaces/extbt/pages/2510848002/Internal+MCPs+BT+Managed
