# standards-desk MCP — server description and tool descriptions

## Server description (inject at MCP server registration)

> Standards Desk — pillar-based quality checks for Workato training content. Before running any checks: (1) Check memory for a saved `standards_desk_audience` value and use it silently if found. (2) If not found, ask once: "Which role best describes you? Training / Education / Workato (default)." (3) Save the answer to memory as `standards_desk_audience`. (4) Pass it as the `audience` parameter on all tool calls.

## Tool: list_pillars

> Lists the available Standards Desk pillars and what each checks for. Pass audience to filter to applicable pillars. Returns name, description, checks_for, and whether an audience variant exists.

## Tool: get_rubrics

> Returns full rubric markdown for the requested pillars, scoped to the audience variant. The calling agent uses these for LLM reasoning client-side. Omit pillars to get all applicable rubrics for the audience.

## Tool: run_static_checks

> Runs mechanical static checks (banned phrases, regex patterns, structural rules) for the requested pillars using the audience-appropriate rule set. Returns per-pillar findings and a pass/fail flag. Omit pillars to run all applicable checks for the audience.
