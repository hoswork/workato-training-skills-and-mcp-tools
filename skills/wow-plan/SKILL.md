---
name: wow-plan
description: Use when planning a 1-day workshop course (especially a World of Workato session) — produces a course abstract (≤150 words, marketing-shaped) and a detailed outline (modules → labs/sessions → learning objectives → time allocations → narrative arc). Uses Amazon-style Working Backwards (press release first). Composes the Standards Desk pillars (`fact-check`, `calibrate-challenge`, `delight-check`, `stick-check`, `say-it-plain`, `team-style-guide`, `complete-check`) and invokes `the-once-over` at Phase 7 for verification. Renamed from `chart-the-course` 2026-06-03. For async self-paced e-learning, use `addie-plan` instead.
metadata:
  version: "1.4"
---

# wow-plan

A workflow that plans a course — abstract and detailed outline — before any lab guide, slide deck, or Knowledge Check is authored. Working Backwards from the audience win to the module structure to the lab sketches.

The skill is built for **1-day workshop courses** (notably World of Workato sessions); the same workflow scales to half-day or multi-day workshop formats. Not for async self-paced e-learning — that's `addie-plan` (Amelia Blevins' ADDIE Prompt Pipeline wrapper).

**Depends on `the-once-over`.** `the-once-over` is the Standards Desk made tangible — it owns all pillar rubrics (`say-it-plain`, `fact-check`, `stick-check`, `calibrate-challenge`, `delight-check`, `team-style-guide`, `complete-check`) and runs them against an artifact. `wow-plan` cites pillars by name at specific phases (e.g., "apply `say-it-plain` §1 to the press release"); the actual rubric content and the verification pass live inside `the-once-over`. Install both as a pair.

Pillar coverage `wow-plan` invokes through `the-once-over`:
- 🎯 **Accuracy** (`fact-check`) — every named feature / limit / capability verified
- 🧠 **Learning Effectiveness** (`calibrate-challenge`) — scaffolding fades, cognitive load calibrated per module, transfer patterns in the wrap-up
- 🧲 **Stickiness** (`stick-check`) — press release as the sticky north star, named transfer patterns, scenario carries Concrete + Stories
- ✨ **Delight** (`delight-check`) — the amplifier on the learning floor: fun designed into the core activity not bolted on, play that makes exploration safe for skeptical experts, a felt-win moment in the learner's hands, AI's nature used as a feature. Picked up in Phase 5 (memorability + the play/game beat) and verified in Phase 7.
- ✍️ **Style** (`say-it-plain` + `team-style-guide`) — abstract and every learner-facing description pass form + word
- ☑️ **Completeness** (`complete-check`) — course-plan checklist (§1.3) gates the output

## Working in a Project (Claude Desktop)

**This skill requires a Claude Desktop Project.** Each course gets its own Project. Do not run phases in a general chat or in the same Project as other courses.

**Why:** Project instructions are cached automatically (~10% of normal cost). Phase 0 research alone justifies the overhead — it's expensive context that every downstream phase reuses.

### Project setup (once per course)

1. Create a new Project named `[Course name]`
2. In Project Instructions, paste:

```
Course: [course-name]
Working files: brief.md · world.md · plan.md · log.md

If I say "resume", "continue", "pick up", or start a message without context:
1. Read @log.md — the CURRENT STATE block at the top tells you the phase, last output, and next action
2. Announce exactly where we are and what you're about to do — do not ask me to explain
3. Begin immediately

Always read @brief.md before any response. Never ask me to re-explain the course.
```

3. Create the course folder with these files — leave them empty until each phase fills them:

```
[course-name]/
  brief.md    ← inputs: topic, audience, duration, tier, output mode, track context (you fill this)
  world.md    ← what is TRUE: feature deps, GA dates, Jira blockers, platform changes, FDE refs
  plan.md     ← the course plan growing through phases: press release → LOs → modules → abstract
  log.md      ← running record: quality gate results, open questions, CURRENT STATE
```

4. Fill `brief.md` now — it's the only file you write manually. Use Phase 1 inputs as the template.

**brief.md must contain:**
- Topic (1 sentence, sentence-case)
- Audience (role · level · size · context)
- Duration (minutes)
- Tier (Foundational / Intermediate / Advanced)
- Delivery mode (in-person / virtual / hybrid)
- Delivery date
- Prerequisites
- Output mode (planning or proposal)
- Track context (if part of a track)
- Course type (standard or experimental)

`log.md` maintains a **CURRENT STATE** block at the very top — Claude rewrites it after every phase:

```markdown
## CURRENT STATE
phase: Phase 3 — Learning objectives
last_completed: Phase 2 (press release)
last_output: plan.md — press release section
next_action: Open new conversation @brief.md @world.md @plan.md → run Phase 3

---
[gate log entries below, newest first]
```

### One conversation per phase group

Phase 0 typically takes a full session on its own (Confluence + Jira research is intensive). Phases 1-2 share a conversation since the brief informs the press release immediately. After Phase 3, modules need world.md for `feature_ga_dependency` — that's a new conversation.

**What each conversation @mentions:**

| Conversation | @mention these files | Writes to |
|---|---|---|
| Phase 0 — Roadmap research | `brief.md` | `world.md` + trainer briefing |
| Phases 1–2 — Brief + press release | `brief.md` + `world.md` | `plan.md` (press release section) |
| Phases 3–5 — LOs + modules + narrative | `brief.md` + `world.md` + `plan.md` | `plan.md` (expands) |
| Phase 6–7 — Abstract + verification | `brief.md` + `plan.md` | `plan.md` (completes) + `log.md` |

`world.md` re-enters at Phases 3-5 because module design requires `feature_ga_dependency` entries from the roadmap research — those facts aren't fully absorbed into plan.md yet at that point.

---

## When to invoke

Invoke when:

- **Drafting a new course** for World of Workato or another delivery venue.
- **Reviewing a course plan** before lab/deck/Knowledge Check authoring begins.
- **Refactoring an existing course** when objectives, audience, or delivery date shifts.
- **Pitching a course** internally — the press release + abstract is exactly what a leadership pitch needs.

Skip on:
- Individual lab authoring — that's the Bakery's Lab track (Lab Buddy / Ghost Bakery profile), not course planning.
- Module deck authoring — that's `slides` (slides-harness) or the Bakery's Presentation track.
- Course-bundle deployment (assembling the Docebo / WoW package) — that's downstream of this skill.

## Posture

Four rules of taste behind the workflow:

1. **Working Backwards.** Write the success outcome first (the press release). Build the plan to deliver it. Everything else — modules, labs, time allocations — is the question *what would make those quotes come true?*
2. **Outcomes, not topics.** The plan's structuring unit is a learning objective (what the learner can do at the end), not a feature/topic (what we want to talk about). Topic-first plans produce courses that feature-tour and feel exhausting.
3. **The audience win is sticky; the modules are scaffolded.** Apply Stickiness to the framing artifacts (press release, abstract, scenario, hooks) — these have to land. Apply Learning Effectiveness to the structural artifacts (objectives, modules, time, scaffolding tier) — these have to work.
4. **Time reconciles.** If module times don't sum to the course duration ±10%, the plan is wrong. Time is the binding constraint; everything else flexes against it.

## How to apply — eight phases

Walk in order. Don't skip phases; the dependencies are real (Phase 0 grounds Phase 1; Phase 2 informs Phase 3 informs Phase 4...).

### Phase 0 — Roadmap Research

**Before drafting any course content, ground the plan in current product roadmap reality.** This phase produces three artifacts that every downstream phase consumes: a feature availability table (course-specific), a cross-cutting platform changes table (track-wide), and — for Agent Studio courses — confirmed reading of the FDE cookbooks.

**Two-source rule.** Confluence PMO pages are the *discovery* surface — they name the features and link the DRI. Jira is the *authoritative status* surface — it carries current sprint state, fix versions, and the blocker graph. Confluence specs are written once and rarely updated; the latest status is always in Jira. **Never assign WoW-ready status from a Confluence page alone.** Always cross-reference the linked Jira issue (Step 1b below) before filling in Current status or WoW-ready.

**Topic-agnostic principle.** The seven-phase workflow is **topic-agnostic**. The dependency table format, the PM lookup protocol (`fact-check §1.1.1`), the wrap structure, the abstract crispness pass, and all five pillar checks apply identically whether the course is on Agent Studio, Enterprise MCP, recipe-building, connectors, integrations, or anything else. **What changes per topic is exclusively scoped to Phase 0** — which Confluence spaces to search, which best-practice references to read, and which cross-cutting platform changes are relevant. Everything else stays the same.

**Step 1 — Search Confluence for course-specific feature dependencies.**

Identify every product feature relevant to the course topic. For each one, capture:

| Field | Notes |
|---|---|
| Feature name | Plain-language label |
| PMO number | If applicable — e.g., PMO-2937 |
| Confluence page | Direct link |
| Current status | In development / In testing / Beta / GA |
| GA target | Specific quarter or month |
| PM | Resolved via the `fact-check §1.1.1` PM-lookup protocol — explicit DRI in the page body → page-creator account ID → `mcp__atlassian__lookupJiraAccountId` → `TBD — check with product team` if all fail. Runs dynamically against whichever PMOs surface during this Phase 0 search. |
| WoW-ready? | ✅ Yes (GA confirmed with enough lead time) / ⚠️ Needs confirmation (target date exists but close or uncertain) / 🔜 Not yet (dependent on other features or no confirmed date) |
| Impact if delayed | Name the specific lab or module that breaks — not "this course is affected" |

**Per-module GA tagging rule (Ryan Koh, 2026-06):** every module in the course plan must declare a `feature_ga_dependency` field listing which features must be GA before the module can run. Each tagged feature must have a confirmed GA date **≥2 months before the course delivery date**. The `fact-check` pillar verifies this at Phase 7.

**Step 1b — Cross-reference Jira for authoritative status and blocker walk.**

For every feature identified in Step 1, run this protocol before assigning WoW-ready status. This is what makes the Roadmap Dependencies table a real risk register rather than a snapshot of whatever was last written in Confluence.

**1. Find the Jira issue key.**

The PMO page usually links a Jira epic or story — look in the page body, the "Jira" panel, or linked issues. Extract the key (e.g., `PLAT-1234`). If no Jira key is present, mark `jira_key: none` — the feature has no live tracking signal and is a risk by definition; flag it in the table.

**2. Query the Jira issue** (`mcp__atlassian__getJiraIssue`).

Pull: status, fix version(s), due date, last-updated date, assignee, and the full `issuelinks` array.

- If Jira status disagrees with the Confluence page status, **Jira wins**. Record both in the table's Current status cell as: `In testing (Jira) / In development (Confluence page)`.

**3. Walk blockers and dependencies.**

From the `issuelinks` array, find every link where type is `is blocked by` or `depends on`. For each linked issue:

- Fetch its status via `mcp__atlassian__getJiraIssue`.
- If the issue is **not** in a terminal state (Done, Released, Closed, Cancelled) → it is an **active blocker**.
- Go one level deeper: check whether each active blocker itself has unresolved `is blocked by` / `depends on` links. Surface those but do not recurse further.

**4. Assign WoW-ready from the combined signal.**

| Signal | WoW-ready |
|---|---|
| Jira status is GA / Released AND no active blockers at any depth | ✅ Yes |
| Jira status is In testing / Beta AND no active blockers AND GA target ≥2 months before delivery | ⚠️ Needs confirmation |
| Any active blocker found at any depth | 🔜 Not yet |
| Jira status is In development or earlier | 🔜 Not yet |
| No Jira key found | 🔜 Not yet (no live signal) |

A feature that looks like ⚠️ on its own ticket but has an unresolved blocker is **🔜**. The blocker's status is the binding constraint.

**5. Apply the same protocol to Step 2 (Platform Changes).** Cross-cutting platform changes tracked as PMO pages have the same stale-Confluence problem. Cross-reference each one with its Jira issue and walk its blockers before assigning status in the Platform Changes table.

**Annotating blockers in the table.** Active blockers appear as a note beneath their parent feature row:

> ↳ Blocked by PLAT-1198 "Auth token redesign" — status: In progress, assignee: [name], depth: 1

In planning mode include the Jira link. In proposal mode, omit the link but keep the blocker note — stakeholders need to see the dependency chain.

**Step 2 — Search Confluence for cross-cutting Workato platform changes.**

Some roadmap items affect every course regardless of topic — they change how the Workato platform works for builders rather than being features being taught. Examples: RBAC 2.0, Decision Models, Workato Expression Language (WEL), Canvas UX redesign.

Search Confluence outside the course's primary feature space (e.g., for an Agent Studio course, check platform/core spaces too). Flag anything that changes: workspace setup, permission model, expression syntax, recipe editor UI, or connector availability.

These go in a separate **Platform Changes** table that appears once in the document Overview, not per-course:

| Change | Status | Courses affected | Training impact |
|---|---|---|---|
| RBAC 2.0 | Available | All | Workspace permission setup instructions may differ from pre-RBAC-2.0 |
| Decision Models | Available | 101, 201, 301 | Available as alternative routing pattern; optional teaching moment |
| Workato Expression Language | New — impact TBD | All | Syntax changes in lab steps if WEL replaces existing expressions |
| Canvas UX (PMO-2887) | Already tracked per-course | Genie-building courses | Tracked in per-course tables as a feature dep; also cross-cutting for any course that teaches Genie building. Lab screenshots and step-by-step procedures change if it ships before WoW. |

**Dual-nature features (per-course AND cross-cutting):** When a feature is tracked as a per-course dependency (e.g., Canvas UX in Agent Studio courses) AND changes how the platform works for builders across the track, list it in **both** tables — per-course for the specific GA-2-months impact on that course's labs, and Platform Changes for the track-wide pattern. Each table answers a different question.

**Step 3 — Read best-practice reference materials (topic-aware).**

- **For Agent Studio / Genie / agentic-patterns courses** (BLOCKING): read the FDE Agentic Design Cookbook V2.0 and Agentic Development Cookbook V2.0 before Phase 4. Cookbook frameworks (four levels of prompting, KB one-call enforcement, agentic vs. Orchestrate criteria) directly shape which modules and labs to include. These cookbooks are Agent Studio-specific and should not be referenced for other topics.

- **For any other topic** (NON-BLOCKING): search Confluence and the FDE space for equivalent best-practice or implementation reference materials (e.g., a recipe design guide for a recipe-building course, a connector guide for an integration course, the Enterprise MCP server PMO page and Workato Dev API docs for an MCP course, etc.). Proceed to Phase 1 if no equivalent is found. Document what was searched and what was found (or not found) in the frontmatter.

**Step 4 — Produce a Trainer Roadmap Briefing** (a per-course companion document — see [The Trainer Roadmap Briefing output](#the-trainer-roadmap-briefing) below).

**Frontmatter additions from Phase 0:**

```yaml
roadmap_research:
  searched_spaces: [list of Confluence spaces searched]
  reference_materials:
    - title: "Agentic Design Cookbook V2.0"
      type: "FDE cookbook"
      read: true
  feature_dependencies:                # per-course-specific features
    - name: "Genie Evaluations Phase 2"
      pmo: "PMO-2937"
      jira_key: "PLAT-1234"           # authoritative status source
      jira_status: "In testing"
      confluence_status: "In development"  # only present when they disagree
      pm: "Bennett Goh"
      ga_target: "Aug–Sep 2026"
      wow_ready: "⚠️"
      impact_if_delayed: "Eval loop lab (Module 5) needs API fallback"
      blockers:                        # active blockers found in Step 1b; empty if none
        - key: "PLAT-1198"
          summary: "Auth token redesign"
          status: "In progress"
          assignee: "…"
          depth: 1                     # 1 = directly blocks parent; 2 = blocks a blocker
  platform_changes:                    # cross-cutting, track-wide
    - change: "RBAC 2.0"
      status: "Available"
      training_impact: "Workspace permission setup instructions differ from pre-2.0"
```

### Phase 1 — Brief

Collect inputs. If any is unknown, mark `TBD` with rationale and continue.

| Input | Notes |
|---|---|
| **Topic** | What the course is about, in 1 sentence. Sentence-case, no marketing register. |
| **Audience** | `role` (e.g., "Solutions engineers") · `level` (beginner / intermediate / advanced) · `size` (approximate, e.g., "20–30") · `context` (e.g., "Customer-facing builders attending WoW Day 2") |
| **Duration** | Total minutes. 1-day = 480 mins, ~360 of which is content (the rest is breaks, intro, wrap, lunch). |
| **Tier** | Workato calibration: Foundational / Intermediate / Advanced. Per `Lab Guide Standards §3` and `calibrate-challenge` Principle 8. |
| **Delivery mode** | in-person / virtual / hybrid / async. Affects engagement cadence and activity types. |
| **Delivery date** | When the course runs. Anchors the verification cycle (`fact-check`). |
| **Prerequisites** | What the learner must have done / know coming in. Concrete; gating not teaching. |
| **Output mode** | **`planning`** (default) or **`proposal`**. See [Output modes](#output-modes) below. |
| **Track context** | If this course is part of a track (e.g., WoW 2026 Agent Studio track), name the track and the course's position in it. Triggers the Phase 5 track continuity check. |
| **Course type** | `standard` (committed offering) or `experimental` (proposal-stage concept). Experimental proposals are held to lower detail density in Phases 4 and 6. |

Save these as frontmatter (see §The course plan frontmatter below).

#### Output modes

Output mode determines what the produced course plan includes:

- **Planning mode** (default): Full output — frontmatter, Open Questions, Structural Gaps, Roadmap Dependencies table with Confluence links, Pillar Verification Log, dependency notes. Used by the author when lab authoring begins.
- **Proposal mode**: Stripped output for stakeholder review — abstract, Simulated Attendee Quotes, learning outcomes, agenda table, total content line, Roadmap Dependencies table (without links). **Omit:** frontmatter, Open Questions, Structural Gaps, Pillar Verification Log, inline PMO references, inline dependency notes.

**One callout per document principle (proposal mode):** Feature dependency callouts in a proposal are consolidated. If the same feature (e.g., EAX, Canvas UI, Headless API) is a dependency across multiple courses, note it once in the Overview or the consolidated callout — not inline at every module where it matters. The document should read as a proposal, not as a risk register.

Internal planning questions go into a separate companion document, not the proposal.

### Phase 2 — Working Backwards press release

**Write what the audience will say about the course *after* it ends.** Amazon-style. 2–4 quotes, each from a named-persona audience member, each naming a concrete outcome and why it mattered.

```yaml
press_release:
  context: |
    A 1-day course delivered to ~25 Solutions Engineers at World of Workato.
    The course is "Agent Studio 201" — assumes 101-level fluency.
  quotes:
    - persona: "Marcus"
      role: "Senior SE, EMEA"
      quote: |
        "I rebuilt our IT helpdesk Genie's prompts in the four-layer model on
        the flight home. By Friday I'd cut the false-positive escalation rate
        from 22% to under 5%."
    - persona: "Priya"
      role: "SE Lead, Americas"
      quote: |
        "The eval framework lab gave me language for what 'good' means in
        production. I built our team's first eval dataset the next sprint."
    - persona: "Jonas"
      role: "Solutions Architect"
      quote: |
        "I came in skeptical of Workato's Agent Studio — left with three
        concrete patterns I'll use in a customer demo next month."
```

**Rules for the press release:**

- **Named persona, named outcome.** *"Marcus, an SE in EMEA, cut his escalation rate from 22% to <5%"* — not *"attendees felt empowered."*
- **Concrete numbers where they exist.** Stickiness Principle 3 (Concrete) — but only real numbers; per `say-it-plain` §1.5, no manufactured urgency or inflated consequence.
- **One outcome per quote.** Don't pack three things into one quote — split into two quotes if the course delivers multiple distinct wins.
- **The outcome must be *takeable*** — *"Marcus rebuilt the prompts on the flight home"* is specific and accessible; *"Marcus mastered agentic design"* is abstract.
- **No marketing language.** Apply `say-it-plain` §1 (form-level: no aphoristic contrast, no drama labels). Quotes should read like real engineers talking.

The press release is the **quality bar** for the rest of the plan. Each module exists to make at least one quote true.

### Phase 3 — Learning objectives + scaffolding

From the press release, distill **3–6 verb-led measurable learning objectives**. Each one is a sentence starting with an action verb (`build`, `configure`, `debug`, `evaluate`, `design`, `wire up`) and naming an observable outcome.

```yaml
learning_objectives:
  - "Refactor a monolithic Genie prompt into the four-layer model (Job Description / Skill Prompt / Field Prompt / App Event Prompt)."
  - "Design and ingest a scoped Knowledge Base, including chunking rules and exclusion filters."
  - "Configure user feedback collection on a Genie and build an evaluation dataset from real failures."
  - "Run an eval dataset with skill-assertion graders; interpret pass/fail and tweak prompts to improve."
  - "Deploy a Genie to a Slack channel in Help Desk mode and observe the persistent tool-call feedback."
```

**Rules:**

- **Verb-led.** Never *"Learn / understand / appreciate / know"* (per `calibrate-challenge` rule from Andragogy + `Lab Guide Standards §5.2`).
- **Measurable.** A reviewer can decide *yes* or *no* — did the learner do this?
- **One per module** (typically). If two objectives map to one module, the module is doing too much (per `calibrate-challenge` Principle 10: One artifact per task; scaled up to one outcome per module).
- **Scaffolding fade across objectives.** Early objectives get heavier scaffolding (foundational tier per Principle 8); later objectives expect more learner inference. Order objectives by complexity.

### Phase 4 — Module breakdown

Decompose into **4–6 modules** (typical for 1-day; adjust for other durations). Each module:

| Field | Notes |
|---|---|
| **Name** | Sentence-case, verb-friendly. Names the *outcome* or the *capability*, not the *feature*. (Good: "Refactor the prompt"; Bad: "Prompt Engineering Concepts".) |
| **Time** | Minutes. Modules in a 1-day usually run 45–90 mins. Account for any module-internal breaks. |
| **Learning objective(s)** | 1 (preferred) or 2 (if tightly paired). |
| **Scaffolding tier** | Foundational / Intermediate / Advanced for the labs in this module. May rise across modules (scaffolding fade). |
| **Lab/session sketches** | The activities the learner does. Each sketch follows the four-part shape below. |
| **Knowledge Check anchor** | One Knowledge Check per module (at least). Anchored on the module's learning objective. |
| **`feature_ga_dependency`** | Features from Phase 0 that must be GA before this module can run. Each entry lists the feature, its current status, and the GA date. The `fact-check` pillar verifies every tagged feature has a confirmed GA date **≥2 months before the course delivery date** (Ryan Koh's GA-2-months rule). |

**Wrap standardization (1-day WoW courses):** Every course ends with a **30-minute wrap** structured as `Quiz · prizes · CTAs`. The wrap is not a summary — it is an active closing sequence with three distinct components: a recap quiz that reinforces transfer patterns, prize / recognition / certificate delivery, and clear calls to action for what learners do next. Don't draft a wrap that deviates from this without explicit rationale.

**Experimental proposals — lower detail density:** If `course_type: experimental` (set in Phase 1), Phase 4 modules carry **less** detail than standard offerings, not more. The signal for an experimental proposal is imagination — stakeholders need enough to say yes or no to the concept, not enough to build the lab. When drafting experimental modules:

- Prefer generalized architecture descriptions over specific product names unless verified (e.g., "PrivateLink" not named gateway products)
- Don't name both AWS and Azure unless the lab explicitly supports both
- Don't include specific PMO numbers or feature names in learner-facing text — those belong in the planning doc, not the proposal
- Trim descriptions until they are the minimum needed to make the concept legible

**Agenda table — the default proposal-mode module format:** In proposal mode, the canonical Phase 4 output is a four-column agenda table:

| | What you do | Detail | Min |
|---|---|---|---|
| Opening | Welcome + scenario premise | One paragraph: company, problem, what they'll build by EOD | 15 |
| Module 1 | (Module title) | One paragraph: the scenario premise, the core build/decision, the verification | 60 |
| Lab 1.1 | (Lab title) | One paragraph: same shape | 30 |
| Break | — | — | 15 |
| ... | ... | ... | ... |
| Wrap | Quiz · prizes · CTAs | Closing recap and what to do next | 30 |

Each row is one of: `Opening`, `Module N`, `Lab N.M`, `Break`, `Lunch`, `Wrap`. Module rows group the Lab rows that belong to them. The Detail column carries **one paragraph** — the scenario premise, the core build or decision, the verification. Not bullet points. The Min column must sum to the course content duration.

In planning mode, modules still carry the agenda-table data, but they also get the four-part Lab/session sketch shape below for deeper authoring detail.

**Lab/session sketch shape** (poached from the user's existing course-planning workflow as captured in `Agent Studio 201 for WoW/experiment-brief.md`):

```markdown
### Lab/session: <Name>

**Premise.** [Why this matters in the persona's terms; what real-world problem
the activity maps to; what concrete artifact the learner will end up with.]

**Lab shape (sketch).**
1. [First step — sets up the scenario or fixtures]
2. [Second step — the core build/decision]
3. [Third step — verification / observation]
4. [Optional fourth step — stretch / connection to next module]

**Why this works as a [tier] activity.**
[2–4 sentences: which `calibrate-challenge` principles it activates, which
`stick-check` framings land, why this beats a feature-tour alternative.]

**Open questions.**
- [Unresolved decisions that need to be settled before lab authoring starts]
- [Dependencies on Workato product timeline (`fact-check`)]
- [Logistics — WoW workspace capabilities, prerequisite labs, etc.]
```

This shape forces the planner to articulate *premise* (the why), *shape* (the how), *why-this-works* (the calibration), and *open questions* (the unresolved). All four are necessary before lab authoring starts.

### Phase 5 — Narrative arc + memorability

**Overarching scenario.** One persona, one company (fictional or real), one ongoing problem the course unfolds. Apply `stick-check` §3 (Concrete) and §6 (Stories) — named persona, named system, narrative thread.

> "Anitech is rolling out an IT helpdesk Genie across three regions. The team has a working prototype but it escalates 22% of conversations to humans — many for reasons that better prompts, better KBs, or better evals would have caught. Over today's course, you'll rebuild the team's Genie module by module."

The scenario links the modules; without it, the course is six unrelated workshops.

**Track continuity check** (when `track_context` is set in Phase 1): if this course is part of a track, the scenario isn't just a narrative device — it's the **prerequisite contract**. Participants who built Casey in 101 are the target for 201, GameDay, and any extension labs. Breaking the scenario thread (e.g., introducing a new company in 301) breaks the on-ramp.

For each course in a track, confirm:

- **Canonical scenario persona and company** — what's the agreed-upon persona/company across the track?
- **Same persona, company, and Genie name** — does this course use them?
- **Entry state of the participant's Genie** — what state does their Genie arrive in at the start of this course?
- **Exit state of the participant's Genie** — what state does it leave in?
- **Prereq and feed chain** — what course does this prerequisite, and what course does it feed?

If any of these conflict with sibling courses in the track, name the conflict in Open Questions (planning mode) and resolve before drafting modules.

**Memorability elements catalog** (poached from slides-harness `014-memorability-elements`):

Mark one or two of these per module — too many and nothing stands out (per `stick-check` Posture rule 2: "One sticky moment per piece, max two").

| Element | When to use | Example shape |
|---|---|---|
| **Mnemonic** | When introducing a 3–5 item framework that learners must recall | *"The 3 R's of Genie debugging: Read the conversation → Reproduce the input → Refactor the prompt"* |
| **Named framework** | When introducing an ordered set of principles | *"The Four Layers of Prompting: Genie Prompt → Skill Prompt → Field Prompt → App Event Prompt"* |
| **Compare aside** | When the lab forces a choice between two approaches | *"LLM drafting vs. Transforms" — when to use which* |
| **Story** | When the abstract concept needs an emotional/practical anchor | Challenge-plot opening for a module on observability |
| **Activity / poll** | When attention is flagging mid-module | "Show of hands: who's seen a Genie hallucinate in production?" |
| **Themed break** | When a long module needs a deliberate interlude | A 5-minute Workato magician interlude (per `project_tinsel_town_theatre_register`) |

**Delight pass (apply `delight-check`).** Memorability is about what the learner *remembers*; delight is about whether they *enjoy the trip and feel safe taking it*. After picking memorability elements, run the course design against `delight-check`:

- **Felt win** — name the single moment in each module where the learner *feels* the tool solve a problem that's actually theirs (`delight-check` Principle 4). Put it in their hands mid-module, not in the wrap-up. If you can't name it, the module is telling, not showing.
- **Safe play** — for the audience's skepticism level, is a wrong move cheap, reversible, and a little funny rather than graded (`delight-check` Principle 3)? Skilled experts explore once it's safe to fumble. Design the first attempt to be *supposed* to fail.
- **Designed-in, not bolted-on** — is the fun in the activity itself (a build worth finishing, a scenario worth caring about), or stapled on as a mascot over a chore (`delight-check` Principle 1)? Removal test: take the fun out — does it still teach but feel like a chore?
- **The game beat (optional, high-value).** A module built as a *game* is the strongest delight + safe-play device available. Two patterns that fit agentic content well: an **LLM-as-judge game** (the learner builds, an AI grades against a rubric, they iterate — the human-as-grader / symmetric loop, where correcting the AI sharpens the human) and a **subagent game** (the learner directs subagents to solve or debug something — e.g. isolating a poisoned tool, or cornering the one broken S3 read silently corrupting downstream results). Use the imperfection-as-feature move (`delight-check` Principle 6): an AI that asks slightly-wrong questions is a better sparring partner than a perfect one — e.g. a trainer-onboarding game where the AI plays an off-angle student and the trainer spots and corrects the misconception live. One game beat per course, max — it's expensive and it has to be authentic to the material (`delight-check` Principle 7).
- **Restraint** — one or two delight touches per module, like memorability elements. Piled up, they compete instead of compound.

### Phase 6 — Abstract

The course abstract goes in the WoW agenda, Docebo catalog, and any proposal doc. It is **structured, not prose** — four labeled sections that scan instantly on a schedule page.

**Shape:**

```
[Course name]

Who this is for
[1-2 sentences. Name the role and imply the level through role language — e.g.,
"built for developers already comfortable with recipe logic" signals intermediate
without saying it. No difficulty labels exposed to learners.]

Prerequisites
• [Specific, honest — 2-4 bullets]
• [Vague prereqs erode trust when learners show up unprepared]

What You'll Be Able to Do
[2-3 sentences, outcomes-first. Anchor to capability, not feature names — this
hedges against features that ship late or change. Use "You'll leave..." as the
closing beat. Name the concrete artifact they'll have at the end.]

[Duration] · [Format]
e.g. Half day · AM · Instructor-led lab
```

**Rules for each section:**

- **Who this is for:** starts with "Built for" or "Designed for" — names the persona, not the difficulty tier. Difficulty is implicit in the role description and prereqs.
- **Prerequisites:** honest and specific. "Some Workato experience" is not a prereq. "Has built and deployed at least one Genie in Agent Studio" is.
- **What You'll Be Able to Do:** capability language, not feature names. "Design multi-step agent workflows" not "use Agent Studio 2.0." The last sentence names a concrete artifact or state the learner will hold at the end.
- **Duration + Format:** one line. Learners need logistics, not positioning.

**Required passes (same as before):**

- `say-it-plain` §1 (form) + §2 (word) — no drama labels, no hype, no agentic overreach phrases
- Crispness: every sentence names who it's for, what they'll do, or what they'll leave with. Cut everything else.

**Experimental proposals:** establish concept + audience + 2-3 concrete outcomes. Nothing else.

**Example (Agent Studio — Spotlight 201):**

```
Agent Studio — Spotlight (201)

Who this is for
Designed for Workato developers with hands-on platform experience who are ready
to move beyond core Genie setup — into production-grade capabilities, delivered
in focused, self-contained modules.

Prerequisites
• Active Workato recipe development experience (triggers, actions, conditionals, data mapping)
• Has built and deployed at least one Genie in Agent Studio
• Familiar with how Genies use knowledge bases and skills to respond and take action

What You'll Be Able to Do
You'll work hands-on with Agent Studio Evaluations and Guardrails — two of the
platform's newest production capabilities. You'll leave knowing how to define
what "good" looks like for your agent, measure whether it's getting there, and
constrain its behavior when it strays. Pick what fits your day — each module is
self-contained.

Half day · AM · Instructor-led lab
```

**Example (Agent Studio — Essentials 101):**

```
Agent Studio — Essentials (101)

Who this is for
Built for technology professionals attending WoW who want to see what enterprise
AI agents can actually do — and leave having built one themselves. No prior
Workato or Agent Studio experience assumed.

Prerequisites
• No prior Workato or Agent Studio experience required
• Comfortable navigating web-based software tools
• Familiar with the idea of business workflows or process automation

What You'll Be Able to Do
You'll leave with a working AI agent you built, configured, and tested yourself —
grounded in company knowledge and connected to real business actions. You'll
understand how agents decide what to retrieve, what actions to take, and how to
verify what ran and why.

Half day · AM · Instructor-led lab
```

### Phase 7 — Verification gates (run `the-once-over`)

Before declaring the course plan ready, invoke **`the-once-over`** (the Standards Desk evaluator). It routes the plan through every pillar and returns a verdict + recommendations. The table below summarizes what each pillar gate checks; pillar skills hold the actual rubrics — `the-once-over` runs them.

| Pillar | Check |
|---|---|
| 🎯 `fact-check` | Every named feature, limit, capability, action name verified against current Workato product surface. **Every module's `feature_ga_dependency` entries have confirmed GA dates ≥2 months before the course delivery date** (Ryan Koh's GA-2-months rule). The Roadmap Dependencies table (below) is populated. Every cited tier (Foundational / Intermediate / Advanced) maps to a `calibrate-challenge` Principle 8 scaffolding shape. |
| 🧠 `calibrate-challenge` | Module times sum to ±10% of duration. Scaffolding fades across modules (early heavy, late light). Each module has 1 clear learning objective (Principle 10: one outcome per artifact). Knowledge Checks present (≥1 per module; ≥3 total per 1-day). Problem-first (Principle 1) — scenario opens; concepts introduced just-in-time (Principle 2). |
| 🧲 `stick-check` | Press release has 2–4 quotes, each named-persona + concrete outcome. Scenario is Concrete + Stories. Each module has at least one Memorability Element. The wrap-up names 2–4 transferable patterns (per `calibrate-challenge` Principle 7). |
| ✨ `delight-check` | Each course names its **felt-win moment** in the learner's hands, not the wrap-up (Principle 4). Exploration is **safe** for the audience's skepticism level — wrong moves cheap, reversible, expected (Principle 3). Fun is **designed into the activity**, not bolted on (Principle 1). If a game beat is used, it's authentic to the material and uses imperfection-as-feature (Principles 6/7). Touches are restrained — 1–2 per module. |
| ✍️ `say-it-plain` | Abstract passes both form (§1) and word (§2) passes including the agentic overreach phrase category. Press release / Simulated Attendee Quotes read like real engineers (no marketing register). Module names are outcome-shaped, not feature-shaped. Crispness pass run on abstract. |
| ☑️ `complete-check` | Course plan §1.3 checklist passes. Knowledge Check plan §1.4 has ≥3 questions per Knowledge Check, Bloom analyze/evaluate/create level. Wrap is 30 minutes with `Quiz · prizes · CTAs` structure. |

A course plan that doesn't pass all pillars goes back to the failing pillar's phase. Don't ship a plan with known failures; the failures compound into the labs and decks.

#### The Roadmap Dependencies table (per-course, end of document)

Each course proposal carries a dedicated **Roadmap Dependencies** section at its end — a table of every feature the course depends on that is not GA today. This keeps the proposal body clean (no inline PMO references, no per-module dependency notes) while making the risk register visible in one place.

**Rules:**

- Only include features that are **not GA today**. GA features don't need a row.
- The "Impact if delayed" column must name the specific lab or module that breaks, not just "this course is affected."
- WoW-ready status uses three values: ✅ Yes (GA confirmed with enough lead time), ⚠️ Needs confirmation (target date exists but close or uncertain), 🔜 Not yet (dependent on other features or no confirmed date).
- This section appears at the end of each individual course section — not once globally for the whole track. Each course owns its own dependency table.
- Features that affect multiple courses appear in each course's table independently. The per-course table is the reference for whoever owns that course's lab authoring.
- In **planning mode**, the table includes Confluence PMO page links and Jira issue keys. In **proposal mode**, links are omitted but the table (including blocker notes) is still present.
- The cross-cutting **Platform Changes** table (from Phase 0 Step 2) appears once in the document Overview, not per-course.
- **Current status is always the Jira status**, not the Confluence page status. If they disagree, record both (see Step 1b).
- **Blocker notes appear as indented rows beneath the parent feature** — one note per active blocker. Do not collapse multiple blockers into a single cell.

**Table format:**

| Feature | PMO | Jira | PM | Current status | GA target | WoW-ready? | Impact if delayed |
|---|---|---|---|---|---|---|---|
| (Feature name) | PMO-#### | PLAT-#### | (DRI name) | In testing (Jira) / In development (Confluence) | Q3 2026 | ⚠️ | Module 3 lab setup |
| ↳ Blocked by PLAT-1198 | — | PLAT-1198 | (assignee) | In progress | — | 🔜 | Escalates parent to 🔜 if unresolved |

`fact-check` populates or verifies this table at Phase 7. If a feature has no confirmed GA date, that's ⚠️ in WoW-ready and a note in Impact if delayed. If a feature has no Jira key, that's 🔜 — no live signal.

## The course plan frontmatter

```yaml
---
title: "Agent Studio 201"
slug: "agent-studio-201"
audience:
  role: "Solutions Engineers"
  level: "intermediate"
  size: "20-30"
  context: "World of Workato Day 2; customer-facing builders"
duration: 480              # minutes; 1-day
content_duration: 360      # excludes breaks, intro, wrap
delivery_mode: "in-person"
tier: "Intermediate"
delivery_date: "2026-09-15"
prerequisites:
  - "Completed Agent Studio 101 or equivalent fluency"
  - "Active Workato workspace with Agent Studio enabled"
  - "Slack workspace for the Genie deployment lab"
learning_objectives:
  - "Refactor a flat Genie prompt into the four-layer model"
  - "Design and ingest a scoped Knowledge Base with chunking and exclusion rules"
  - "Configure user feedback collection on a Genie and build an evaluation dataset"
  - "Run an eval dataset with skill-assertion graders and tweak prompts to improve"
  - "Deploy a Genie to a Slack channel in Help Desk mode"
press_release:
  context: |
    1-day course at World of Workato, Day 2, for ~25 Solutions Engineers
    with Agent Studio 101 fluency.
  quotes:
    - persona: "Marcus"
      role: "Senior SE, EMEA"
      quote: |
        I rebuilt our IT helpdesk Genie's prompts in the four-layer model
        on the flight home...
    # ... 2-4 quotes total
modules:
  - name: "Refactor the prompt"
    time: 75
    tier: "Foundational"
    learning_objective: "Refactor a flat Genie prompt into the four-layer model"
    labs: [...]
    knowledge_check_anchor: "Identify which layer a piece of prompt instruction belongs in"
  # ... 4-6 modules
verified_on:                  # filled after Phase 7 pillar passes
  fact-check: TBD
  calibrate-challenge: TBD
  stick-check: TBD
  say-it-plain: TBD
  complete-check: TBD
---
```

## The output shape

The skill produces a **course plan** as the primary output, plus a **Trainer Roadmap Briefing** as a companion document.

### The course plan

A single markdown document with the frontmatter above plus a body. Sections vary by output mode (set in Phase 1).

**Planning mode (default) — full output:**

1. **Scenario** — the overarching narrative arc (1–3 paragraphs).
2. **Press Release** — formatted version of the frontmatter quotes (markdown blockquote per quote).
3. **Learning Objectives** — bulleted, verb-led.
4. **Platform Changes** (track-wide, one-only) — cross-cutting Workato platform changes that affect every course in the track.
5. **Module Breakdown** — one `## Module N` section per module, containing the lab/session sketches and `feature_ga_dependency` per module.
6. **Knowledge Check Plan** — one Knowledge Check per module, each with 3–6 retrieval-practice questions per `complete-check §1.4`.
7. **Wrap** — 30 minutes, `Quiz · prizes · CTAs` structure.
8. **Abstract** — the ≤150-word marketing-shaped blurb.
9. **Roadmap Dependencies** — per-course table (with Confluence links).
10. **Open Questions** — what's unresolved, what needs research, what depends on Workato product timeline.
11. **Structural Gaps** — known holes the planner is aware of.
12. **Pillar verification log** — short table summarizing which pillar passes have run and when.

**Proposal mode — stripped output for stakeholder review:**

1. **Overview** — single paragraph + the one consolidated feature-dependency callout (per the one-callout principle).
2. **Platform Changes** (track-wide, one-only) — same table as planning mode, but link-free.
3. **Per-course sections** — for each course, in this order:
   - **Abstract** (≤150 words, post-crispness pass)
   - **Simulated Attendee Quotes** (the press-release content, renamed)
   - **Learning outcomes** (bulleted, verb-led)
   - **Agenda table** (four-column: type, what you do, detail, min) — the canonical module format in proposal mode
   - **Total content line** (sums the agenda's Min column)
   - **Roadmap Dependencies** — per-course table (without Confluence links)

**Omit in proposal mode:** frontmatter, Open Questions, Structural Gaps, Pillar Verification Log, inline PMO references, inline per-module dependency notes. Internal planning questions go into a separate companion document.

### The Trainer Roadmap Briefing

A standalone markdown document saved alongside the course plan, named `<course-slug>-trainer-briefing.md`. This is a **trainer reference document** — distinct from the Roadmap Dependencies table (which is a risk register for the proposal). The briefing is what a trainer or course author who didn't draft the course needs to come up to speed before designing or delivering.

**For each feature relevant to the course:**

- **Feature name and PMO number**
- **What it does** — 2–3 sentences, plain language, no PMO jargon
- **Why it matters for this course** — specifically how it changes what the trainer teaches or what the learner experiences. Not a general product description — a course-design-specific callout.
- **Direct Confluence link** — so the trainer can go deeper if needed
- **Current status and GA target** — so the trainer knows what's live vs. coming

**Organization:** by reading priority (read first / read second / etc.), not alphabetically. Features with the highest course design impact come first.

**Scope:** Only features that are (a) relevant to this specific course and (b) either already GA or expected GA before delivery. Features that are too early-stage to teach are noted briefly at the bottom under "On the horizon — not yet teachable" without full detail.

**Per-course, not per-track.** In a multi-course track, produce one briefing per course — trainers shouldn't have to filter a track-level list for the one course they're delivering.

**Default save location:** `~/brain/10 Initiatives/Courses/50 Experiments/<slug>/course-plan.md` and `<slug>-trainer-briefing.md` alongside it. For non-Heiwad users: save to the working directory or wherever specified.

## Working interactively in Claude Desktop

Walk this sequence. Each phase group is a separate conversation in the Project.

---

**CONVERSATION 1 — Phase 0: Roadmap research** (@mention `brief.md` only)

Before touching course structure, search Confluence for every relevant product feature. Build the per-course feature dependency table and the cross-cutting Platform Changes table. Read FDE cookbooks (Agent Studio courses) or equivalent references (other topics). Produce the Trainer Roadmap Briefing as a side artifact.

> **→ Phase gate.** Write research outputs to `world.md`. Save the trainer briefing as `[slug]-trainer-briefing.md`. Update CURRENT STATE in `log.md`. Then: **close this conversation and open a new one.**

---

**CONVERSATION 2 — Phases 1–2: Brief + press release** (@mention `brief.md` + `world.md`)

1. Confirm the Phase 1 brief inputs from `brief.md`. Ask only for gaps — don't re-collect what's already there.
2. **Establish the scenario thread** (overlaps Phases 1 + 5) — name the company, the Genie, the problem, and the arc now, before modules. If this is a track, confirm the thread works across sibling courses.
3. **Working Backwards (Phase 2)** — walk the user through the press release / Simulated Attendee Quotes. Surface examples; let them pick personas and outcomes. Don't generate quotes the user hasn't endorsed.
4. Write the press release section to `plan.md`.

> **→ Phase gate.** `plan.md` now contains the press release. Update CURRENT STATE in `log.md`. Then: **close this conversation and open a new one.**

---

**CONVERSATION 3 — Phases 3–5: LOs + modules + narrative** (@mention `brief.md` + `world.md` + `plan.md`)

1. **Draft abstracts before module detail (Phase 6 preview).** Get a draft abstract approved first — the abstract is the quality bar that modules must deliver. Drafting modules before the abstract is locked wastes iteration.
2. **Objectives (Phase 3)** — distill 3–6 verb-led LOs from the press release. Write to `plan.md`.
3. **Modules (Phase 4)** — propose 4–6 modules with `feature_ga_dependency` per module from `world.md`. For experimental modules, lower detail density. Write to `plan.md`.
4. **Narrative + Memorability (Phase 5)** — pick the scenario; pick memorability elements per module; run the delight pass. Run the track continuity check if applicable. Write to `plan.md`.

> **→ Phase gate.** `plan.md` now contains LOs, modules, and narrative arc. Update CURRENT STATE in `log.md`. Then: **close this conversation and open a new one.**

---

**CONVERSATION 4 — Phases 6–7: Abstract + verification** (@mention `brief.md` + `plan.md`)

1. **Abstract (Phase 6)** — write the ≤150-word abstract. Apply `say-it-plain` form + word passes. Run crispness pass: can it be 20% shorter without losing a concrete outcome?
2. **Global continuity pass** — scenario thread, naming consistency, time totals, feature dependency consolidation, one-callout principle (proposal mode). Run BEFORE pillar checks.
3. **Pillar gates (Phase 7)** via `the-once-over` — gates, not commentary. Fix failures before proceeding; don't flag and move on.
4. Write completed `plan.md`. Append gate results to `log.md`, update CURRENT STATE to `phase: Complete`.

> **→ Done.** Surface open questions (planning mode only). The course plan + trainer briefing are ready for lab authoring.

---

### Publishing the finished plan

After Conversation 4 completes and `plan.md` is final, generate an HTML version for Google Docs distribution:

- **Trigger:** "publish" or "generate the HTML"
- **Source:** `plan.md`
- **Output:** `plan.html` in the same folder
- **Format rules:**
  - Replace all markdown tables with **card layout** — each row becomes a `<div>` card with a label and value, not a table cell. Module cards, feature dependency cards, KCs.
  - Use inline styles only (Google Docs strips class-based CSS on paste)
  - Section headings → `<h2>` / `<h3>` (Google Docs preserves these)
  - Blockquotes (press release quotes) → styled `<blockquote>` with left border
  - No `<table>` elements — Google Docs renders them as tables, not cards
  - Target: paste into Google Docs and have it read as a polished document, not raw markdown

**Card template (module):**
```html
<div style="border:1px solid #e0e0e0;border-radius:6px;padding:14px;margin:10px 0;background:#fafafa">
  <div style="font-weight:bold;font-size:14px;color:#108291">Module 1 — Refactor the prompt</div>
  <div style="margin-top:6px;font-size:13px"><strong>Duration:</strong> 75 min · <strong>Tier:</strong> Foundational</div>
  <div style="margin-top:4px;font-size:13px"><strong>Objective:</strong> Refactor a flat Genie prompt into the four-layer model</div>
  <div style="margin-top:4px;font-size:13px"><strong>GA dependency:</strong> Genie Evaluations Phase 2 — ⚠️ Q3 2026</div>
</div>
```

**Don't:** generate the full plan in one shot without the user's input on the press release. The press release is the load-bearing decision; everything downstream is wrong if it's off.

**Don't:** default to verbose. Each draft should be **shorter** than the previous one, not longer. Trim toward minimum-viable detail; expand only when the user asks. Iterative crispness, not iterative expansion.

**Do:** check current Workato product state (per `fact-check`) at Phase 0, Phase 4, and Phase 7. Features in development may slip; verify timing against the GA-2-months rule.

## Integration with other pillars and skills

- `say-it-plain` — applies to every learner-facing string (abstract, scenario, press-release quotes, module names, learning objectives, Knowledge Check questions). Both form (§1) + word (§2). Form-level first.
- `stick-check` — applies to the press release (§3 Concrete + §6 Stories), the scenario (§3 + §6), module hooks (§2 Unexpected), the wrap-up (§5 Emotional + §6 Stories).
- `calibrate-challenge` — applies to objectives (Principle 4: observable success criteria — objectives are verb-led + measurable), module sequencing (Principle 8: scaffolding fade), time allocation (Principle 9: realistic timing), module count (Principle 10: one outcome per artifact), Knowledge Check shape (Principle 6: reflection before transfer), wrap-up structure (Principle 7: transfer patterns in the wrap-up — 2–4 named patterns).
- `fact-check` — applies to every feature reference (§1 feature availability), every UI label or action name (§2), every limit/quota (§3), every external link (§6).
- `complete-check` — gates the output (§1.3 course plan checklist + §1.4 Knowledge Check checklist).
- `team-style-guide` — applies to surface formatting (casing, banned terms, spelling). Especially `Knowledge Checks` (never *KC*), `Workato magic` motto exception.

## What this skill is NOT

- **Not a deck builder.** That's `slides` (slides-harness) downstream of this skill.
- **Not a lab authoring tool.** That's the Bakery's Lab track (Lab Buddy / Ghost Bakery profile, with the HTML Lab Style Guide + html-lab-rules.yaml).
- **Not a Knowledge Check authoring tool.** This skill specifies the *anchors* and *count* per module; the actual question writing is downstream.
- **Not a course-bundle deployer.** Assembling the package for Docebo / WoW is downstream of this skill.
- **Not authoritative on Workato product state.** That's `fact-check` + the live product. This skill provides the *protocol* for verification, not the verified facts themselves.

## Pattern (for future Standards-Desk-applied skills)

`wow-plan` is the first workflow skill (alongside the pillars `say-it-plain`, `fact-check`, `stick-check`, `calibrate-challenge`, `team-style-guide`, `complete-check` and the evaluator `the-once-over`) in the four-package architecture. Its sibling workflow is `addie-plan` (ADDIE wrapper for async self-paced courses). The pattern:

1. **Skill anchors on the pillar set, not on one pillar.** Course planning isn't a single-pillar pass — it's a coordinator that runs each pillar at the right phase.
2. **Working Backwards from the audience win** is the structural device that makes the pillars cohere. Without it, pillars run in parallel and produce a complete-but-incoherent plan.
3. **Each phase produces a frontmatter field, not a free-form decision.** This makes the plan re-usable (other skills can read the frontmatter) and re-runnable (a future Coach iteration can re-walk individual phases).
4. **The output document doubles as the audit trail.** Pillar verification log + open questions section make the plan reviewable and the unresolved decisions visible.

This pattern likely also fits future Standards-Desk skills (e.g., a `design-a-module` skill for deck-level planning; a `design-a-lab` skill for lab-level planning that wraps Lab Buddy).

## Logging

At completion, invoke: `skill-logger wow-plan` (if `skill-logger` is available in the current environment; skip silently if not). This collects org-wide usage telemetry for Workato training-team skills.

## Tape

At the end of a session where this skill produced a meaningful output, offer to run `the-tape` if any decisions were made that overrode, extended, or notably validated these standards:

> "Want to capture any decisions to the tape? It helps the team evolve these standards over time."

Only proceed if they say yes. Skip silently if `the-tape` is not installed.
