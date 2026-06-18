---
name: the-once-over
description: Use to give a Workato training artifact a comprehensive review against The Standards Desk pillars — lab guide, slide deck, course plan, course abstract, Knowledge Check, course bundle, game/interactive activity, anything readable. **Self-contained** — bundles all pillar rubrics in `pillars/` (`fact-check`, `calibrate-challenge`, `delight-check`, `stick-check`, `say-it-plain`, `team-style-guide`, `complete-check`). Routes the artifact through each, returns a verdict (which pillars passed / failed) plus recommendations (what to change and why). Bundles the Standards Desk's Gatekeeper (verdict) and Coach (iteration) roles into a single pass for solo authors. Locked 2026-06-03.
metadata:
  version: "1.4"
---

# the-once-over

A comprehensive review pass — *"give it the once-over"* — that routes a training artifact through The Standards Desk's pillar rubrics, gathers findings, and returns a single verdict plus prioritized recommendations.

**Self-contained.** The skill bundles all pillar rubrics inside `pillars/` (`say-it-plain.md`, `fact-check.md`, `stick-check.md`, `calibrate-challenge.md`, `delight-check.md`, `team-style-guide.md`, `complete-check.md`). You don't need to install any pillar skills separately — the rubric content is right here. **`pillars/` is the canonical home for pillar rubrics** — the standalone pillar source-skills at `~/.claude/skills/<pillar>/` were retired 2026-06-04 to eliminate two-file sync. Edits land here.

In Standards Desk architecture terms, the-once-over operationalizes **The Gatekeeper** (renders the verdict — pass / conditional / fail per pillar) and **The Coach** (drafts the recommendations — what to change, in what order, and why). Solo authors get both at once; the architecture's role split stays in the docs.

## When to invoke

Invoke when:

- **Before publishing or shipping** any training artifact externally (lab guide, slide deck, course plan, course abstract, Knowledge Check, course bundle).
- **Before filing a bug ticket** — the general bug-report rubric runs via `say-it-plain` §3 (Bug-report register) + `complete-check` §1.6 (Bug report). For Workato CCE filings specifically, use the workflow skill `file-workato-product-bug`, which composes the-once-over at its review step.
- **At quality gates inside a workflow** — `wow-plan` Phase 7 invokes the-once-over; `addie-plan` invokes it between ADDIE phases (e.g., after Design before Develop).
- **After a substantive revision** to verify nothing regressed across pillars.
- **When uncertain whether an artifact is ready** — the-once-over is the routine "second read."

Skip when:

- You only need one pillar's check (run that pillar directly — `say-it-plain` for a prose pass, `fact-check` for a feature claim, etc.).
- The artifact has no reviewable structure yet — wait until there's enough shape to give useful feedback.
- The artifact is a one-off internal note that won't travel.

## Posture

### Two modes: gate vs. advisory

**We gatekeep automation, not humans.**

| | Gate mode | Advisory mode |
|---|---|---|
| **Invoked by** | An LLM workflow at a defined phase boundary (wow-plan Phase 7, addie-plan phase gates) | A person — the author, a peer, anyone running the-once-over directly |
| **Default** | Automatic when called from a workflow | Automatic when called by a human |
| **Role** | Gatekeeper — blocks the pipeline if a pillar fails | Editor / Coach — surfaces findings and suggestions; the author decides what to act on |
| **Verdict scale** | Pass / Conditional pass / Fail | Looks good / A few things to consider / Worth your attention before shipping |
| **Single pillar fail** | Overall fail; pipeline stops | Surfaced prominently, framed as "before you ship" — author retains agency |
| **`complete-check` findings** | Can block | Always "consider" tier — a checklist for finalizing, not a verdict on the current draft |

**Lifecycle calibration in advisory mode.** Ask or infer from context where the artifact is:

- **Exploring / early draft** — structure still settling. Run `fact-check` and `say-it-plain §1` (form-level). Everything else is a brief note for later.
- **Mid-development** (default if not stated) — all pillars run. `complete-check` and `say-it-plain §2` (word-level) are "consider" tier.
- **Near-final** — all pillars run at full depth. Findings are still framed as advisory, but the report explicitly calls out what would block at a gate so the author knows what to address before publishing.

**Artifact-level scope.** Never flag a check that doesn't apply to this artifact type. If the routing table doesn't include `complete-check` for a course abstract, don't flag missing Knowledge Checks — that's not the right level. State the pillar as "not in scope for this artifact" and move on.

### Standing rules (both modes)

1. **The Standards Desk pillars are the rubric.** the-once-over doesn't introduce new criteria — it composes existing pillars. If a finding doesn't trace to a pillar, it doesn't belong in the output.
2. **Findings + suggestions both ship.** The findings tell the author what the pillars surfaced. The suggestions tell the author what to do about it. Returning only one is incomplete.
3. **Surface what's load-bearing.** If 17 things were flagged but only 3 are structural, lead with the 3. Cascade issues (fact-check, calibrate-challenge, say-it-plain §1 form-level) ripple through the artifact — fix the structural issue first; word-level issues often dissolve once form is right.
4. **End with what's working.** Every report closes with what passed or what's strong — so the author knows what not to change.

## How to apply

### Step 1 — Establish mode, lifecycle, and artifact type

**Mode:** Is this invoked by a workflow (gate mode) or by a person (advisory mode)? If invoked by a person and lifecycle stage isn't stated, default to mid-development advisory mode.

**Artifact type:** Different artifacts compose different pillar subsets. Use the routing table:

| Artifact | Pillars run |
|---|---|
| **Lab guide** | `fact-check`, `calibrate-challenge`, `stick-check`, `delight-check`, `say-it-plain`, `team-style-guide`, `complete-check` (§1.1) |
| **Slide deck** | `fact-check`, `calibrate-challenge`, `stick-check`, `delight-check`, `say-it-plain`, `team-style-guide`, `complete-check` (§1.2) + load `presentation-content-standards` as a surface reference (density limits, pacing, speaker notes, voice calibration for the slide medium) |
| **Course plan** | `fact-check`, `calibrate-challenge`, `stick-check`, `delight-check`, `say-it-plain`, `complete-check` (§1.3) |
| **Game / interactive activity** | `calibrate-challenge`, `delight-check` (lead — play, safe exploration, felt win, imperfection-as-feature), `stick-check`, `say-it-plain` |
| **Knowledge Check** | `calibrate-challenge` (Principles 4/6), `say-it-plain`, `complete-check` (§1.4) |
| **Course abstract** | `say-it-plain` (§1 + §2), `stick-check` (§3 Concrete + §5 Emotional) |
| **Course bundle** | `complete-check` (§1.5), `team-style-guide`, plus the pillars for each contained artifact |
| **Findings doc** | `say-it-plain` (§1 + §2), `findings-doc` skill, light `stick-check` |
| **Other professional prose** | `say-it-plain` (§1 + §2), `stick-check` (selective) |
| **Bug report** (any bug-tracking system) | `fact-check`, `say-it-plain` (§1 + §2 + §3 Bug-report register), `complete-check` (§1.6) — for Workato CCE filings specifically, use `file-workato-product-bug` workflow skill which composes this routing |

If the artifact type isn't listed, default to `say-it-plain` + the artifact-fit subset from the routing table above.

### Step 1b — Apply the two-tier execution model

Before running full reasoning, apply the static tier first. Each pillar file contains a `## Check classification` section that lists what's static vs. reasoning — read that section to know what belongs where.

**In Claude Code (Bash available):**

- For **slide decks**: if the `slide-check` plugin is installed, run `npx tsx ${CLAUDE_PLUGIN_ROOT_SLIDE_CHECK}/tools/static-checker.ts input.json` and collect the static findings. Skip re-running those checks in the reasoning pass.
- For **all artifact types**: read the `## Check classification → Static checks` list from each pillar in the routing set. Apply those rules mechanically — count words, match patterns, check presence. No inference needed; this is a checklist.
- **Subagent dispatch (recommended for 3+ pillars):** dispatch each pillar's reasoning pass as a concurrent subagent. Each subagent receives exactly: the artifact text + that pillar's `## Reasoning checks` section. Do not include the static rules or other pillars' content — keep each subagent's context lean. Static findings stay on the main thread; collect only distilled reasoning findings back. This keeps the main thread's context clean for the synthesis pass in Step 3.

**In Claude Desktop (no Bash):**

- Apply the `## Check classification → Static checks` sections as a mechanical checklist (count/match/compare, no interpretation). List findings.
- Then apply reasoning checks sequentially on the main thread.

Running tiers in sequence — not interleaved — keeps context focused and avoids applying LLM inference to checks that are objectively deterministic.

### Step 2 — Run each pillar in sequence

Invoke each pillar in the artifact's pillar set. For each pillar, capture:

- **Verdict** — pass / conditional / fail
- **Findings** — what failed, with line refs or section refs
- **Why** — which pillar rule was tripped

Run pillars in **structural → surface order** (form before word, foundation before polish):

1. `fact-check` — accuracy gates; a beautifully written course plan that names a deprecated feature is broken regardless of how the prose reads
2. `calibrate-challenge` — learning effectiveness; if the cognitive load is wrong, no amount of polish helps
3. `stick-check` — stickiness; the framing + narrative; works on the structural shape
4. `delight-check` — delight (the amplifier on the floor); is the experience lovable, is play safe enough for a skeptic to explore, is there a felt win, does it use the AI's nature as a feature — runs after the `calibrate-challenge` floor holds
5. `say-it-plain` — prose §1 (form-level shapes) → §2 (word-level lists); the form-level pass is the foundation
6. `team-style-guide` — surface-level style; typography, casing, banned terms, brand
7. `complete-check` — mechanical presence checks; "is every required element here?"

### Step 3 — Aggregate the verdict

**Gate mode** (workflow-invoked):

| Combined verdict | Means |
|---|---|
| **Pass** | All pillars pass. Pipeline continues. |
| **Conditional pass** | One or more conditional findings, no fails. Pipeline continues; soft asks tracked. |
| **Fail** | One or more pillars fail. Pipeline stops. Do not advance until the failed pillars pass on re-run. |

A single pillar fail = overall fail. The Gatekeeper doesn't average; it gates.

**Advisory mode** (person-invoked):

| Combined verdict | Means |
|---|---|
| **Looks good** | No findings that would block at a gate. Clean to ship when ready. |
| **A few things to consider** | Conditional findings, style gaps, or completeness items — worth addressing before shipping; author's call on priority. |
| **Worth your attention before shipping** | One or more findings that would block at a gate. Surfaced as information — the author decides what to act on and when. No artifact "fails" in advisory mode. |

In advisory mode, `complete-check` findings are always "consider" regardless of severity. Findings from pillars outside the artifact's routing table (e.g., flagging Knowledge Check presence on a course abstract) are not findings — call them "not in scope at this artifact level" and move on.

### Step 4 — Prioritize the recommendations

Rank the open issues using two filters:

- **Blocker vs. soft** — a blocker fails the verdict; a soft ask is a "would be better" without a pillar fail.
- **Cascade vs. local** — a cascade issue (typically `fact-check`, `calibrate-challenge`, or `say-it-plain` §1 form-level) ripples through the artifact; a local issue is one paragraph, one slide, one term. Cascade issues land first; fixing them often dissolves the local issues.

Surface the recommendations in this order: **blocker-cascade → blocker-local → soft-cascade → soft-local**. Lead with the smallest set that unblocks shipping.

### Step 5 — Return the report

**Gate mode format:**

```markdown
## the-once-over — {artifact name}

**Combined verdict:** Pass / Conditional pass / Fail
**Pillars run:** {list}

### Per-pillar findings

| Pillar | Verdict | Notes |
|---|---|---|
| fact-check | pass | — |
| calibrate-challenge | conditional | Module 3 time allocation runs 15min long; Principle 9 |
| stick-check | pass | — |
| delight-check | conditional | Felt-win moment buried in the wrap-up; move it into the learner's hands mid-lab (Principle 4) |
| say-it-plain | fail | Abstract uses 3 superlatives + manufactured urgency (§1.5, §2.3, §2.7) |
| team-style-guide | pass | — |
| complete-check | pass | All §1.3 frontmatter fields present |

### Recommendations

1. **(Blocker, cascade)** Rewrite course abstract per `say-it-plain` §1 (form-level) — the urgency + superlatives are form-shape problems, not word-swap problems.
2. **(Soft, local)** Trim Module 3 by 15min — drop the second LLM-drafting comparison; keep the Transforms-first walk-through.

### What passed

(Brief note on the strongest aspects so the author knows what NOT to change.)
```

**Advisory mode format:**

```markdown
## the-once-over — {artifact name}

**Overall:** Looks good / A few things to consider / Worth your attention before shipping
**Mode:** Advisory ({lifecycle stage})
**Pillars run:** {list}

### Per-pillar

| Pillar | Signal | Notes |
|---|---|---|
| fact-check | clean | — |
| calibrate-challenge | worth revisiting | Module 3 time allocation runs 15min long (Principle 9) — consider trimming |
| stick-check | clean | — |
| delight-check | worth revisiting | Felt-win moment is in the wrap-up; stronger if it lands in the learner's hands mid-lab (Principle 4) |
| say-it-plain | flag for attention | Abstract has 3 superlatives + manufactured urgency (§1.5, §2.3, §2.7) — this is structural, not just word-choice |
| team-style-guide | clean | — |
| complete-check | (consider when finalizing) | Module frontmatter missing `feature_ga_dependency` on 2 of 4 modules — checklist item when you're ready to finalize |

### Before you ship

These are structural findings that would block a gate. Your call on timing.

- **Abstract prose shape** (`say-it-plain §1`) — the urgency + superlatives are a form-level issue, not word-swap. Cut "transformative," "game-changing," "unlock," then re-read for claims the paragraph can't keep.

### Things to consider

Lower-priority; worth a pass when you have headroom.

- Trim Module 3 by ~15min — the second LLM-drafting comparison is the cut candidate.
- Felt-win moment: move it into the activity, not the wrap.

### What's working

(What's strong — so the author knows what not to change.)
```

Signal labels in advisory mode: **clean** / **worth revisiting** / **flag for attention** / **(not in scope at this artifact level)** / **(consider when finalizing)** for complete-check.

## Execution architecture (intended model)

The-once-over runs three tiers at three intelligence levels. Today it runs sequentially on the main thread; the model below is the target architecture as tooling matures.

**Everything stays inside the Standards Desk umbrella.** Pillars are the single source of truth for both static and reasoning checks. The execution layer reads from the pillar; it doesn't maintain a separate spec. Static checks are extracted and run mechanically by a TypeScript linter; reasoning checks are read by an LLM subagent focused on that pillar's rubric. The pillar file expresses both — the runner decides how to execute each.

### Pillar file convention: static vs. reasoning sections

Every pillar that contains deterministic checks should separate them from reasoning checks so the execution layer can route each correctly. **Two formats supported — use whichever matches the current maturity level:**

**Single-file (current convention):** Organize with labeled sections within the same file. The linter and LLM subagent read the same file; the section header tells each which rules apply to it.

```markdown
### Static checks
(Deterministic — applied mechanically. Run by linter if available; applied as a checklist by the LLM otherwise — no reasoning, just count/match/compare.)
- Max 120 words per slide body
- Max 6 top-level bullets
- Flesch-Kincaid grade level ≤ 10 (body) / ≤ 12 (speaker notes)
- Prohibited terms: leverage, utilize, synergy…

### Reasoning checks
(Require LLM judgment — run by the subagent, or by the main thread in sequential mode.)
- Does the form-level shape of the abstract match what it's trying to claim?
- Is the felt-win moment genuinely in the learner's hands, or just dressed up?
```

**Split-file (context-optimized):** When pillar files grow large enough to meaningfully degrade subagent context, split into two files. The subagent loads only `reasoning.md`; the linter reads only `static.md`. Main thread loads neither.

```
pillars/
  fact-check/
    reasoning.md    ← LLM subagent loads this only
    static.md       ← linter reads this only
  say-it-plain/
    reasoning.md
    static.md
```

The execution layer changes which file it points to; the pillar contract stays the same. Migrate to split-file when a pillar's static section is large enough that the subagent loading the full file is noticeably wasteful.

**Static checks in Claude Desktop:** Claude Desktop cannot run a TypeScript linter directly. Options: (1) expose checks as an MCP server tool — works in both Claude Desktop and Claude Code, single implementation; (2) LLM applies the `### Static checks` section as a mechanical checklist — still useful, lower cost than full reasoning. The `### Static checks` label is meaningful in both cases.

Existing pillars will need a pass to adopt this convention. When writing a new pillar, classify each check before writing it.

### Tier 1 — Static pre-pass (TypeScript linter, zero LLM tokens)

Reads the `### Static checks` sections from each pillar in the artifact's routing set. Runs deterministic checks: word counts, bullet limits, font size floors, prohibited word lists, required element presence, contrast ratios, Flesch-Kincaid grade level. Returns a structured findings list. Cost: negligible. Tooling: TypeScript (`text-readability` for grade level; no Python dependency).

### Tier 2 — Parallel pillar subagents (orthogonal, concurrent)

Pillars are independent — `fact-check` findings don't depend on `calibrate-challenge` findings. Dispatch concurrently. Each subagent receives: the artifact + the `### Reasoning checks` section of its pillar only. Static findings already captured in Tier 1 are not re-run. Distilled findings return to the main thread; full rubric text stays in the subagent's context.

Pillar orthogonality map (safe to run in parallel):
- Group A: `fact-check`, `calibrate-challenge`, `stick-check`
- Group B: `delight-check`, `say-it-plain`, `team-style-guide`
- `complete-check` is mostly static → folds into Tier 1; any remaining judgment calls run as a lightweight subagent

### Tier 3 — Main thread synthesis (reasoning on clean context)

Receives only distilled findings from Tiers 1 and 2 — never the full rubric text, never a re-read of the artifact. Context is clean. This is where judgment happens: cascade identification (a form-level problem that makes word-level findings moot), prioritization, and writing recommendations that lead with the smallest set that unblocks shipping.

The quality of this pass is directly proportional to how uncontaminated the context is when it runs.

**Current state:** Runs sequentially on main thread. The architecture above is the target; apply it when subagent dispatch is available and the linter tooling exists.

## How pillar content lives here

The six pillar rubrics are embedded in this skill's `pillars/` subdirectory. When evaluating an artifact, load the relevant pillar file(s) from `pillars/` and apply their rules. The verdict and recommendations cite pillar rules by section reference (`say-it-plain §1.5`, `calibrate-challenge Principle 9`, `complete-check §1.3`).

**The pillars are canonical here, not a mirror.** As of 2026-06-04, `pillars/` is the single canonical home for pillar rubric content. Standalone pillar source-skills (`~/.claude/skills/say-it-plain/`, `~/.claude/skills/fact-check/`, etc.) were retired to eliminate the two-file sync problem. When a pillar rule changes, edit the corresponding file in `pillars/` — that's the one place to update, and the change propagates via `the-once-over.zip` re-bundle plus the `say-it-plain` projection in the repo README.

## What the workflow skills do with the-once-over

| Workflow | Invocation pattern |
|---|---|
| **`wow-plan`** | Phase 7 invokes the-once-over on the produced course plan. A fail in Phase 7 sends the plan back to the failing pillar's phase (e.g., fail on `say-it-plain` → re-do Phase 6 Abstract). |
| **`addie-plan`** | Invokes the-once-over at gates between ADDIE phases (Analyze → Design; Design → Develop; Develop → SME Feedback). Each gate's pillar subset is per the routing table above, scoped to the artifact the phase produces. |
| **Ad-hoc** | Author or peer runs the-once-over directly. Defaults to advisory mode — Editor/Coach role, not Gatekeeper. No workflow needed. |

## What this skill is NOT

- **Not a new pillar.** the-once-over composes pillars; it doesn't introduce criteria. If a finding doesn't trace to a pillar rule, the-once-over doesn't catch it.
- **Not a one-shot autofix.** It returns findings + recommendations; the author makes the edits. (A future "the-coach-autofix" skill could pair with the-once-over to apply recommendations; not in scope today.)
- **Not for code review or product spec review.** The pillar rubrics are training-content-shaped. For code, use `code-review`. For product specs, use a product review pattern.
- **Not authoritative on Workato product state.** That's `fact-check` + the live product. the-once-over runs the protocol; the facts come from the product surface.

## Pattern

the-once-over is the **only evaluator** in the four-package skill architecture (see [[project_skill_packages]]). Adding a second evaluator would create rubric-aggregation drift — different evaluators producing different verdicts on the same artifact. The architecture stays singular: one evaluator that composes all pillars; workflows that invoke it; pillars that hold the rubrics. The singularity is what makes the-once-over's verdicts canonical.

## Logging

At completion, invoke: `skill-logger the-once-over` (if `skill-logger` is available in the current environment; skip silently if not). This collects org-wide usage telemetry for Workato training-team skills.

## Tape

At the end of a session where this skill produced a meaningful output, offer to run `the-tape` if any decisions were made that overrode, extended, or notably validated these standards:

> "Want to capture any decisions to the tape? It helps the team evolve these standards over time."

Only proceed if they say yes. Skip silently if `the-tape` is not installed.
