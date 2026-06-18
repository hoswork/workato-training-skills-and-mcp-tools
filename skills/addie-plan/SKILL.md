---
name: addie-plan
description: Use when planning a Workato async self-paced e-learning course (Workato Academy Rise 360 format). Wraps the ETT team's ADDIE Prompt Pipeline (Amelia Blevins) — 11 prompts embedded as files in `prompts/`. Tells you which prompt to run at which ADDIE phase (Project Prep → Analyze → Design → Develop → SME Feedback) and invokes `the-once-over` at quality gates between phases. Prompts are snapshotted from Confluence; an opt-in sync path lets users refresh against the canonical Workato ETT space when needed. For instructor-led workshop courses (1-day workshops, World of Workato sessions), use `wow-plan` instead. Locked 2026-06-03; addie-plan pivoted to embed-and-sync 2026-06-04.
metadata:
  version: "1.2"
---

# addie-plan

A workflow wrapper around the **ADDIE Prompt Pipeline** authored by Amelia Blevins and the Workato ETT team. The pipeline's 11 prompts are embedded as `prompts/01-customer-voice.md` … `prompts/11-sme-feedback.md`. This skill tells you which prompt to run at which ADDIE phase and where to invoke `the-once-over` (the Standards Desk evaluator) between phases.

**Why embed instead of point to Confluence?** Anyone installing this skill — including users outside Workato's ETT Confluence space — gets a working, offline-usable pipeline. The trade-off is freshness: the embedded prompts are a snapshot. Each prompt file's frontmatter records its `synced` date and Confluence page version, and an explicit sync path (below) lets users refresh on demand.

## The pipeline at a glance

Five conversations, one file written per conversation. Each conversation runs its prompts in order within a single session.

| Conversation | Prompts | Reads | Writes |
|---|---|---|---|
| **1 — Project Prep** | 01 · 02 · 03 | `brief.md` | `world.md` |
| **2 — Analyze** | 04 · 05 | `brief.md` + `world.md` | `course.md` |
| **3 — Design** | 06 · 07 | `brief.md` + `world.md` + `course.md` | `course.md` (completes) |
| **4 — Develop** | 08 · 09 · 10 | `brief.md` + `course.md` | `build.md` |
| **5 — SME Feedback** | 11 | `brief.md` + `build.md` | `build.md` (revised) |

The 11 prompt files (`prompts/01-customer-voice.md` … `prompts/11-sme-feedback.md`) remain the authoritative source. Each has a Step 0 retrieval pattern, numbered output sections for cross-reference (D1, B2, E2.3, etc.), and a Confidence rating. Run all prompts within a conversation in order — the threading is part of the design.

**Not embedded (snapshot scope):** the Confluence parent page (ID 2432991701) also has *Certification Assessment Exam*, *Storyboard Mockups*, and a *Launch* draft section (Internal Announcement / Customer Email / Community Announcement). These weren't part of the v2.0-finalized 11-prompt core and weren't included in this snapshot. To use them, fetch from Confluence directly (see Sync).

## Working in a Project (Claude Desktop)

**This skill requires a Claude Desktop Project.** Each course gets its own Project. Do not run ADDIE phases in a general chat or in the same Project as other courses.

**Why:** Project instructions are cached automatically (~10% of normal cost). Each phase conversation reloads the system prompt for free. Without a Project, every turn re-pays for the skill context.

### Project setup (once per course)

1. Create a new Project named `[Course name]`
2. In Project Instructions, paste: `You are working on the course defined in @brief.md. Read it before every response.`
3. Create the course folder and these files — leave them empty until each phase fills them:

```
[course-name]/
  brief.md    ← WHO / WHAT / WHEN / CONSTRAINTS (you fill this before starting)
  world.md    ← what is TRUE externally: customer voice, content gaps, usage data,
                 GA deps, roadmap state, platform changes, risks — facts, not decisions
  course.md   ← what WE'VE DECIDED: needs analysis, audience profile, LOs, outline —
                 design decisions derived from world.md, not world.md itself
  build.md    ← what gets BUILT: scripts, KCs, storyboards per module
  log.md      ← running record: quality gate results, SME feedback, decisions made
```

4. Set your **Project Instructions** to exactly this (replace `[course-name]`):

```
Course: [course-name]
Working files: brief.md · world.md · course.md · build.md · log.md

If I say "resume", "continue", "pick up", or start a message without context:
1. Read @log.md — the CURRENT STATE block at the top tells you the phase, last output, and next action
2. Announce exactly where we are and what you're about to do — do not ask me to explain
3. Begin immediately

Always read @brief.md before any response. Never ask me to re-explain the course.
```

5. Fill `brief.md` now — it's the only file you write manually. Everything else Claude writes.

**brief.md must contain:**
- Target audience (role, experience level, prior knowledge)
- Learning goal in one sentence
- Delivery format (Rise 360 async, duration target)
- Delivery date
- Product focus areas (which Workato features/surfaces)
- Known constraints (GA dependencies, team capacity, SME availability)

### One conversation per phase

Each ADDIE phase is a separate conversation in the Project. At the end of each phase, Claude will prompt you to close the conversation and open a new one. This keeps context lean — each conversation loads only what the next phase needs, not the full history of all prior phases.

**What each conversation @mentions:**

| Conversation | @mention these files |
|---|---|
| Project Prep (prompts 01–03) | `brief.md` |
| Analyze (prompts 04–05) | `brief.md` + `world.md` |
| Design (prompts 06–07) | `brief.md` + `world.md` + `course.md` |
| Develop (prompts 08–10) | `brief.md` + `course.md` |
| SME Feedback (prompt 11) | `brief.md` + `build.md` |

Design reads both because the detailed outline (prompt 07) needs the factual world state (GA deps, product scope) AND the prior design decisions (LOs, needs analysis). Develop only needs course.md because world facts were already absorbed into the design decisions.

`log.md` is appended to after each quality gate. It also maintains a **CURRENT STATE** block at the very top that Claude rewrites after every phase — this is what powers the resume pattern. Format:

```markdown
## CURRENT STATE
phase: Design
last_completed: prompts 04–05 (Analyze)
last_output: course.md — needs analysis + audience profile
next_action: Open new conversation @brief.md @world.md @course.md → run prompt 06

---
[gate log entries below, newest first]
```

---

## When to invoke

- **Planning a Workato Academy Rise 360 course** (async self-paced e-learning) from scratch.
- **Picking up an in-flight ADDIE course** at a specific phase and wanting to know what's next.
- **Adding Standards Desk evaluation** to ADDIE outputs — running the pillars on each phase's artifact via `the-once-over`.

Skip when:

- Planning a 1-day instructor-led workshop or WoW session — use `wow-plan` (Working Backwards workflow, different shape).
- Authoring lab guides, slide decks, or Knowledge Checks directly — those are downstream artifacts; the pipeline produces specs for them, not the artifacts themselves.

## How to apply

### Step 1 — Identify the current ADDIE phase

If starting from zero, you're in Project Prep. Otherwise, locate yourself by what already exists:

- Needs analysis exists? → entering Design
- Learning objectives exist? → entering Develop
- Storyboards exist? → entering SME Feedback

### Step 2 — Run the phase's prompts in order

Open the prompt file for the current phase (e.g., `prompts/04-needs-analysis.md`). Each file has the full Confluence prompt as a fenced markdown block. Copy the prompt, fill in the bracketed inputs, and run it against the data sources it specifies (Gong, Salesforce, Highspot, Drive, Slack, data warehouse, prior artifacts).

At each phase gate, write your output to the appropriate file and open a fresh conversation for the next phase. Do not continue in the same conversation across phase boundaries.

---

**CONVERSATION 1 — Project Prep** (@mention `brief.md` only)

1. `01-customer-voice.md` → Customer Voice Research Brief
2. `02-content-audit.md` → Content Audit & Gap Analysis Report
3. `03-usage-data.md` → Usage Data-Informed Design Brief

> **→ Phase gate.** Write all three outputs to `world.md`. Update the CURRENT STATE block in `log.md`. Run `the-once-over` if needed. Then: **close this conversation and open a new one.**

---

**CONVERSATION 2 — Analyze** (@mention `brief.md` + `world.md`)

4. `04-needs-analysis.md` → Course Strategy Document (consumes world.md)
5. `05-audience-profile.md` → Audience Profile (consumes 4 + Customer Voice from world.md)

> **→ Phase gate.** Write needs analysis + audience profile to `course.md`. Invoke `the-once-over` in **gate mode** (pillars: `fact-check`, `say-it-plain`, `complete-check`). Gate mode means: single pillar fail = overall fail, block advance. If it fails, take the Coach recommendations, fix the artifact in this conversation, re-run the gate. Iterate until clean. Append final gate result to `log.md` and update CURRENT STATE. Then: **close this conversation and open a new one.**

---

**CONVERSATION 3 — Design** (@mention `brief.md` + `world.md` + `course.md`)

6. `06-learning-objectives.md` → LO set (consumes course.md)
7. `07-detailed-outline.md` → Module outline (consumes 6 + course.md + world.md GA deps)

> **→ Phase gate.** Append LOs + outline to `course.md` (it now contains the complete course design). Invoke `the-once-over` in **gate mode** (pillars: `calibrate-challenge`, `say-it-plain`). If it fails, fix and re-run in this conversation until clean. Append final gate result to `log.md` and update CURRENT STATE. Then: **close this conversation and open a new one.**

---

**CONVERSATION 4 — Develop** (@mention `brief.md` + `course.md`)

8. `08-script-drafting.md` → Per-lesson narration scripts (consumes course.md)
9. `09-knowledge-checks.md` → Assessment questions (consumes course.md)
10. `10-storyboarding.md` → Rise 360 production blueprint (consumes 8 + course.md)

> **→ Phase gate.** Write all three outputs to `build.md`. Invoke `the-once-over` in **gate mode** on each artifact (see pillar subsets in Step 3). Fix and re-run each failing artifact in this conversation until clean before moving on. Append final gate results to `log.md` and update CURRENT STATE. Then: **close this conversation and open a new one.**

---

**CONVERSATION 5 — SME Feedback** (@mention `brief.md` + `build.md`)

11. `11-sme-feedback.md` → Cross-cutting; runs whenever SME review lands on any deliverable in build.md

> **→ Final gate.** Update `build.md` with SME-revised content. Invoke `the-once-over` in **gate mode** on affected artifacts (full re-run). Fix and re-run until clean. Append to `log.md` and update CURRENT STATE to `phase: Complete`. Then open a final conversation for Rise 360 assembly prep.

---

### Step 3 — Invoke `the-once-over` at phase gates

After each ADDIE phase produces its artifact, invoke `the-once-over` in **gate mode** — this is a workflow gate, not an advisory review. Signal gate mode by telling the-once-over: "this is a phase gate invoked by addie-plan workflow."

**Gate mode behavior:** single pillar fail = overall fail, pipeline blocked. The skill returns a verdict + Coach recommendations. Take the recommendations, fix the artifact in the same conversation, re-run the gate. Iterate until all pillars pass. Only then write the output file and close the conversation.

Pillar subsets per artifact:

| Phase output | Pillars `the-once-over` runs |
|---|---|
| Needs analysis (Analyze) | `fact-check`, `say-it-plain`, `complete-check` |
| Learning objectives (Design) | `calibrate-challenge` (Principle 4), `complete-check` |
| Detailed outline (Design) | `calibrate-challenge` (Principles 8/9/10), `say-it-plain` |
| Narration scripts (Develop) | `say-it-plain` (§1 + §2), `team-style-guide`, `fact-check` |
| Knowledge Check questions (Develop) | `calibrate-challenge` (Principles 4/6), `complete-check` (§1.4), `say-it-plain` |
| Storyboards (Develop) | `complete-check`, `team-style-guide` |
| SME-revised drafts | Full re-run on the affected artifacts |

A fail at any gate sends the artifact back for revision in the same conversation. Don't advance to the next phase, close the conversation, or write to the output file until the gate passes clean.

### Step 4 — End of pipeline

After SME Feedback Consolidation, the course is content-complete and ready for Rise 360 assembly. Before assembly, run `the-once-over` on the **full course bundle** (`complete-check §1.5`) — catches cross-artifact inconsistencies that per-artifact gates miss.

## Publishing the finished artifacts

After Conversation 5 completes and `build.md` is final, generate an HTML version for Google Docs distribution:

- **Trigger:** "publish" or "generate the HTML"
- **Source:** `course.md` + `build.md` (or just the relevant artifact the user specifies)
- **Output:** `[artifact-name].html` in the same folder
- **Format rules:**
  - Replace all markdown tables with **card layout** — each row becomes a `<div>` card with a label and value, not a table cell. Module cards, script sections, Knowledge Check items.
  - Use inline styles only (Google Docs strips class-based CSS on paste)
  - Section headings → `<h2>` / `<h3>` (Google Docs preserves these)
  - No `<table>` elements — Google Docs renders them as tables, not cards
  - Target: paste into Google Docs and have it read as a polished document, not raw markdown

**Card template (module/section):**
```html
<div style="border:1px solid #e0e0e0;border-radius:6px;padding:14px;margin:10px 0;background:#fafafa">
  <div style="font-weight:bold;font-size:14px;color:#108291">Module 2 — Audience Profile</div>
  <div style="margin-top:6px;font-size:13px"><strong>Learning objective:</strong> Identify primary learner needs</div>
  <div style="margin-top:4px;font-size:13px"><strong>Prompt:</strong> 05-audience-profile.md</div>
  <div style="margin-top:4px;font-size:13px"><strong>Status:</strong> ✅ Passed Standards Desk</div>
</div>
```

## Sync — refreshing the embedded prompts from Confluence

The embedded prompts are a snapshot dated in each file's frontmatter (`synced: YYYY-MM-DD`, `confluence_version: N`). To refresh against Amelia's canonical Confluence:

**When to sync:**
- Before starting a new course (catches any major prompt-pipeline revisions)
- When a prompt's behavior surprises you (Amelia may have shipped a fix)
- Quarterly as routine hygiene

**How to sync:**

The Confluence parent page is **ID `2432991701`** in the Workato ETT space (`https://workato.atlassian.net/wiki/spaces/ETT`). Each of the 11 prompts has its own child page. The mapping is in each `prompts/*.md` file's frontmatter under `confluence_page_id` and `source`.

If you have Atlassian MCP access in Claude Code, ask Claude something like:

> "Compare each prompt file in `~/.claude/skills/addie-plan/prompts/` against its Confluence source (parent page ID 2432991701). For each one, report the embedded `confluence_version` vs. the current Confluence version. Show me the diff for any that have drifted, and update the embedded version if I approve."

If you don't have Atlassian MCP access:
- Open each prompt's Confluence page directly using the `source` URL in the frontmatter
- Copy the latest body markdown into the prompt file
- Bump the `confluence_version`, `confluence_version_date`, and `synced` fields in the frontmatter

The sync is intentionally **directions, not tooling** — there's no sync script and isn't planned to be one. Each prompt's frontmatter (`confluence_page_id`, `confluence_version`, `confluence_version_date`, `synced`) carries enough metadata for Claude to do the comparison via the Atlassian MCP without bespoke code. Amelia owns the pipeline; we don't want a background sync that overwrites changes silently. Treat each sync as a deliberate refresh.

## Why embed (not thin-point at Confluence)

- **Offline usable.** Anyone installing the skill — including non-Workato users — gets a working pipeline.
- **Versioned snapshot.** Each prompt's frontmatter records its synced state. Drift is visible, not hidden.
- **Sync stays opt-in.** Users refresh deliberately; nothing changes behind their back.
- **Amelia stays canonical.** The Confluence pages are the source of truth; this skill is a portable snapshot of them. Updates flow Amelia → Confluence → opt-in sync → this skill.

## What this skill is NOT

- **Not a re-implementation of the ADDIE pipeline.** The prompt content is Amelia's; this skill embeds her work with attribution and provides workflow routing + sync mechanics around it.
- **Not for workshop / instructor-led course planning.** That's `wow-plan` — different workflow shape, different output.
- **Not a Rise 360 authoring tool.** The pipeline produces specs and content; Rise 360 assembly is downstream.
- **Not a forked pipeline.** If Amelia ships a v3.0, sync brings it in. We don't fork our own variant.

## Related

- [Amelia Blevins' ADDIE Prompt Pipeline](https://workato.atlassian.net/wiki/spaces/ETT/pages/2432991701) (Confluence, Workato ETT space) — the canonical source
- `wow-plan` — workshop-course sibling workflow
- `the-once-over` — the Standards Desk evaluator invoked at phase gates
- Memory entries: `project_addie_plan`, `project_the_once_over`, `project_skill_packages`, `project_skill_packages_experiment`

## Logging

At completion, invoke: `skill-logger addie-plan` (if `skill-logger` is available in the current environment; skip silently if not). This collects org-wide usage telemetry for Workato training-team skills.

## Tape

At the end of a session where this skill produced a meaningful output, offer to run `the-tape` if any decisions were made that overrode, extended, or notably validated these standards:

> "Want to capture any decisions to the tape? It helps the team evolve these standards over time."

Only proceed if they say yes. Skip silently if `the-tape` is not installed.
