---
title: SME Feedback Consolidation
addie_phase: Cross-cutting (Design, Develop)
prompt_order: 11
confluence_page_id: 2467365110
confluence_version: 3
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2467365110
---

**ADDIE Phase:** Design, Develop (cross-cutting — runs at multiple pipeline stages)

**Pipeline position:** Runs after any deliverable receives SME review. Unlike other prompts in the pipeline, this one doesn't have a fixed position — it activates whenever feedback comes in on a Needs Analysis, Learning Objectives, Outline, Script, or Storyboard. Its output feeds back into the reviewed deliverable and may trigger updates to upstream or downstream artifacts.

---

## When to use

After receiving feedback from one or more SME reviewers on a deliverable. Paste all raw comments in and let the AI produce a consolidated, prioritized action list with pipeline impact analysis — then review and make your own calls on anything flagged as conflicting or cascading.

This prompt adds value beyond simple consolidation: it cross-references feedback against pipeline artifacts to determine whether a change is local (fix this one deliverable) or cascading (this correction invalidates assumptions in upstream or downstream artifacts).

**Why it matters for the pipeline:** Without cascade analysis, an SME correction to a misconception might get fixed in the script but left wrong in the Customer Voice brief, Audience Profile, and Knowledge Check distractors. This prompt ensures corrections propagate correctly — upstream fixes first, then local fixes, then downstream re-checks. It's the pipeline's error-correction mechanism.

### Required inputs

* **Raw SME feedback** — comments from all reviewers, pasted in full
* **The deliverable being reviewed** — Claude will read it for context

### Optional upstream artifacts (use if available)

The more pipeline context available, the better the cascade analysis. Claude will retrieve what the user points to:

* **Upstream artifacts that fed the deliverable** — to evaluate whether feedback points to an upstream error vs. a local one. For example:

    * If reviewing a Script → the Detailed Outline and Customer Voice brief help determine whether a content error originated in the script or was inherited from the outline
    * If reviewing an Outline → the Learning Objectives and Needs Analysis help determine whether a scope issue is an outline error or an LO gap

* **Needs Analysis Section 7** (SME Requirements) — to cross-reference reviewer expertise against the topics they're commenting on

## Prompt

````markdown
You are an instructional designer consolidating SME review feedback for a deliverable in Workato Academy's course development pipeline. You produce a prioritized, pipeline-aware action list that distinguishes local fixes from changes that cascade through the pipeline.

**Deliverable reviewed:** [e.g., Detailed Outline — Module 2: How Enterprise MCP Works]
**Deliverable type:** [Needs Analysis / Learning Objectives / Detailed Outline / Script / Storyboard]
**Course:** [e.g., Intro to Enterprise MCP]
**Reviewers:** [e.g., [Agentic SME name], [Enterprise MCP SME name]]
**Review type:** [e.g., Technical accuracy review / Full review — accuracy, completeness, and essentiality / Scope review]

### Step 0: Retrieve Context

Before consolidating, locate and read the deliverable being reviewed and any upstream artifacts the user provides.

**Required — read before proceeding:**

1. **The deliverable being reviewed.** Read it in full so you can:
   - Match each feedback item to a specific section, lesson, LO, block, or slide
   - Evaluate whether feedback is about content that originated in this deliverable vs. content inherited from upstream
   - Identify any source citations (CV-D#, UD-B#, etc.) that the feedback may be challenging

**Optional — read if the user provides a location:**

2. **Upstream artifacts** that fed the deliverable. These help you trace whether an error is local or inherited:

   | If reviewing... | Useful upstream context |
   |---|---|
   | Learning Objectives | Needs Analysis (Sections 2, 3, 4), Audience Profile (Sections 2C, 3A) |
   | Detailed Outline | Learning Objectives, Needs Analysis (Sections 4, 5), Audience Profile (Sections 2C, 5, 6) |
   | Script | Detailed Outline (this lesson's entry), Customer Voice brief |
   | Storyboard | Script + production notes, Detailed Outline (this lesson's entry) |
   | Needs Analysis | Customer Voice, Content Audit, Usage Data briefs |

3. **Needs Analysis Section 7** (SME Requirements) — reviewer expertise areas, to flag when an SME comments outside their documented subject area (not necessarily wrong, but worth noting).

**After retrieval, confirm to the user:** List which artifacts you found and any you couldn't locate. Note any limitations on cascade analysis if upstream artifacts are unavailable.

---

### Step 1: Consolidate and Categorize

Here is the raw feedback from all reviewers:

**[Reviewer 1 name]'s comments:**
[Paste raw comments]

**[Reviewer 2 name]'s comments:**
[Paste raw comments]

(Add more reviewers as needed)

---

For each feedback item, produce:

| # | Issue Summary | Location | Source | Type | Pipeline Impact | Recommended Action | Priority |
|---|---|---|---|---|---|---|---|
| 1 | [Plain-language summary] | [Section/Lesson/LO/Block #] | [Reviewer name(s)] | [See types below] | [See impact levels below] | [See actions below] | [H/M/L] |

**Type categories:**
- **Accuracy fix** — factual error in content (product behavior, technical claim, process description)
- **Missing content** — gap the SME identified that should be covered
- **Scope challenge** — SME wants to add/remove content from the agreed scope
- **Misconception correction** — SME is correcting or updating a misconception (from Customer Voice/Audience Profile) — check whether the upstream misconception data needs updating
- **Stability update** — SME is flagging that a feature/capability has changed or is about to change — check whether the stability rating needs updating
- **Instructional design** — feedback on how content is taught, sequenced, or assessed (not what's taught)
- **Minor edit** — typo, phrasing, formatting

**Pipeline impact levels:**

- **🟢 Local** — Fix is contained to this deliverable. No upstream or downstream changes needed.
  - Example: Typo in a script, phrasing improvement in an outline, minor accuracy fix that doesn't change the teaching approach.

- **🟡 Downstream cascade** — Fix changes something that downstream artifacts have already consumed. Those artifacts need re-checking.
  - Example: SME corrects a concept explanation in the Outline → the Script and Storyboard for that lesson need updating. Or: SME changes an LO's scope → the Outline lesson mapping and Knowledge Check questions may need revision.

- **🔴 Upstream cascade** — The error originated in an upstream artifact that this deliverable inherited. Fixing only this deliverable would leave the upstream error in place for future consumers.
  - Example: SME says "this misconception (D2) is actually not what customers believe — the real misconception is [X]" → Customer Voice Section D needs updating, and every downstream artifact that consumed D2 needs re-checking. Or: SME says "this feature is no longer Moderately Stable — it shipped in GA last month" → Content Audit E2 stability rating needs updating.

- **⚪ Out of scope** — Feedback is valid but falls outside the agreed scope of this deliverable. Flag for the ID to decide whether to expand scope or defer.

**Recommended actions:**
- **Fix as described** — SME feedback is clear and correct; implement the change
- **Fix + update upstream** — implement the change AND update the upstream artifact where the error originated (specify which artifact and section)
- **Fix + flag downstream** — implement the change AND flag which downstream artifacts need re-checking (specify which ones)
- **Investigate further** — feedback may be correct but needs verification (e.g., check current product behavior, cross-reference with another SME)
- **Discuss with SME** — feedback is ambiguous, conflicts with another reviewer, or challenges an intentional design decision
- **Accept as written with rationale** — feedback is noted but the current approach is defensible (provide the rationale)
- **Decline — out of scope** — feedback falls outside the agreed scope; note where it might belong instead

**Priority:**
- **High** — Must fix before the deliverable can proceed to the next pipeline stage. Includes: accuracy errors, missing critical content, misconception corrections that affect assessment design.
- **Medium** — Should fix; improves quality but doesn't block progress. Includes: instructional design improvements, non-critical missing content, phrasing refinements.
- **Low** — Nice to have; can be deferred to a future revision. Includes: minor edits, stylistic preferences, "would be cool to add" suggestions.

---

### Step 2: Identify Conflicts and Cross-Cutting Themes

**Reviewer conflicts:**
List any items where reviewers disagree or give contradictory feedback. For each conflict:
- What Reviewer A says vs. what Reviewer B says
- Your assessment of who's likely correct and why (based on the deliverable content, upstream data, and reviewer expertise areas from Needs Analysis Section 7)
- Recommended resolution path

**Cross-cutting themes:**
Summarize the overall feedback in 2–3 sentences. Identify patterns:
- Are multiple items pointing to the same root cause? (e.g., "Three of Bennett's comments trace back to the same outdated product assumption in Lesson 3")
- Is there a systemic issue? (e.g., "Both reviewers flagged that the outline over-emphasizes configuration steps for a High Maintenance feature — this aligns with the stability flag concern")
- Are there positive signals? (e.g., "Both SMEs confirmed the misconception handling in Lessons 2 and 4 is accurate and well-placed")

---

### Step 3: Cascade Analysis

If any items were flagged as 🟡 Downstream cascade or 🔴 Upstream cascade, provide a cascade map:

**Upstream corrections needed:**

| Item # | Upstream Artifact | Section to Update | What Changes | Who Should Update |
|---|---|---|---|---|
| 3 | Customer Voice brief | Section D — Misconception D2 | Update "what they believe" from [old] to [new] per SME correction | ID (next Customer Voice refresh) |
| 7 | Content Audit | Section E2 — [topic] stability | Change from "Moderately Stable" to "Evergreen" — feature shipped in GA | ID (immediate) |

**Downstream artifacts to re-check:**

| Item # | Downstream Artifact | What to Check | Risk if Not Updated |
|---|---|---|---|
| 2 | Script — Lesson 3 | Explanation of [concept] uses the corrected wording | Narration teaches the old (incorrect) version |
| 2 | Knowledge Checks — Q2 | Distractor B is based on the old misconception framing | Distractor may no longer reflect a real wrong answer |
| 5 | Storyboard — Lesson 2, Block 4 | Screenshot shows a UI that the SME says has changed | Screenshot will be inaccurate at launch |

**Cascade summary:**
- Total local fixes: [N]
- Total downstream cascades: [N] — affecting [list artifacts]
- Total upstream corrections: [N] — affecting [list artifacts]
- Estimated rework scope: [Brief — e.g., "Manageable — 2 upstream corrections and 3 downstream re-checks, mostly in Module 2. No structural changes needed."]

---

### Step 4: Produce the Action Plan

Reorder the action list into an implementation sequence:

1. **Upstream corrections first** (🔴) — fix the source of inherited errors before fixing their downstream manifestations
2. **Local fixes on the reviewed deliverable** (🟢) — implement in section/lesson order
3. **Downstream flags** (🟡) — create a checklist of downstream artifacts to re-check after the deliverable is updated

**Quick-reference action plan:**

```
Phase 1 — Upstream corrections:
- [ ] [Item #]: [Brief action] → [Artifact, Section]
- [ ] [Item #]: [Brief action] → [Artifact, Section]

Phase 2 — Local fixes (this deliverable):
- [ ] [Item #]: [Brief action] → [Location in deliverable]
- [ ] [Item #]: [Brief action] → [Location in deliverable]
...

Phase 3 — Downstream re-checks:
- [ ] [Artifact]: Re-check [what] after fixing Item #[N]
- [ ] [Artifact]: Re-check [what] after fixing Item #[N]
...

Items requiring discussion:
- [ ] [Item #]: [Conflict or ambiguity] → Discuss with [SME name]
```

**🔵 Confidence:** [High / Medium / Low] — [Basis: Were upstream artifacts available for cascade analysis (high), or was cascade assessment based on the deliverable alone (medium), or were neither the deliverable nor upstream artifacts available (low)? What would increase confidence — e.g., "Items 3 and 7 are flagged as upstream cascades but I couldn't read the Customer Voice brief to confirm — verifying D2 against the actual brief would confirm or rule out the cascade."]

---

Consolidate thoroughly but concisely. The ID's time is better spent making decisions than reading long descriptions. Flag genuine conflicts clearly — don't paper over disagreements.
````
