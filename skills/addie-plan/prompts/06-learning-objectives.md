---
title: Learning Objectives
addie_phase: Design
prompt_order: 6
confluence_page_id: 2466251447
confluence_version: 4
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2466251447
---

**ADDIE Phase:** Design

**Position:** Runs after Needs Analysis and Audience Profile are complete. Consumes the performance gaps, learning goal, module scope, persona outcomes, and misconception inventory from upstream. Its output feeds the Detailed Outline, and through the outline, Script Drafting, Knowledge Checks, and Storyboarding.

### When to use

After the Needs Analysis (Course Strategy Document) is complete and scoping is approved, and after the Audience Profile has been generated for the target persona. Use this prompt to generate learning objectives at two levels:

* **Course-level LOs:** Run once to generate the 3–5 top-level objectives for the entire course. These should ladder directly to the course-level learning goal (Needs Analysis Section 3).
* **Module-level LOs:** Run once per module to generate 2–4 objectives per module. These should ladder to the course-level LOs and align with the module learning goal from the Module Scope Map (Needs Analysis Section 4).

LOs drive structure — run this before starting the Detailed Outline.

Note: The prompt references "Course/Module" as the LO level. You should choose one or the other for your prompt and run multiple times as needed.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Needs Analysis (Course Strategy Document)** — specifically:

    * Section 2 (Performance Gap) — the gaps LOs need to close
    * Section 3 (Course-Level Learning Goal) — the outcome LOs must ladder to
    * Section 4 (Module Scope Map) — module goals, stability ratings, and scope
    * Course Strategy (Project Strategy Statement) — the behavior change and business impact LOs serve

* **Audience Profile** — specifically:

    * Section 2C (Misconceptions) — misconceptions that need corrective objectives
    * Section 3A (Bloom's-mapped outcomes) — the target Bloom's levels per persona outcome
    * Section 5 (Prerequisites) — what learners already know (LOs shouldn't re-teach prerequisites)


### Optional upstream artifact

* **Customer Voice Section D** (Misconception Inventory) — if the Audience Profile isn't available yet, the prompt can pull misconceptions directly from Customer Voice. The Audience Profile is preferred because it maps misconceptions to the specific persona.

````
You are an instructional designer working on Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are drafting learning objectives for a course or module.

**LO level:** [Course-level / Module-level]
**Course name:** [e.g., Intro to Enterprise MCP]
**Module title (if module-level):** [e.g., Module 2: How Enterprise MCP Works]

### Step 0: Retrieve Upstream Artifacts

Before writing any objectives, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Needs Analysis (Course Strategy Document)** for this course. Extract and hold:
   - Course Strategy — Project Strategy Statement (the "This program helps [audience] learn how to [competency] so they can [behavior change]..." sentence)
   - Section 2 (Performance Gap) — each gap with its type, evidence sources, and training-closability
   - Section 3 (Course-Level Learning Goal) — the performance outcome statement
   - Section 4 (Module Scope Map) — for the module being scoped: its learning goal, stability rating, and scope boundaries
     - Note the stability rating: if a module covers a **High Maintenance** topic, write objectives around concepts and decision-making rather than specific procedures that may change
     - Note "Concepts explicitly out of scope" from the module's scope boundaries

2. **Audience Profile** for the target persona. Extract and hold:
   - Section 2C (Misconceptions) — the numbered misconception items with severity, persona relevance, and instructional implications
   - Section 3A (Bloom's-mapped outcomes) — the target Bloom's levels for each persona outcome
   - Section 5 (Prerequisites) — what the persona is assumed to already know

**After retrieval, confirm to the user:** List which artifacts you found and any you couldn't locate. If the Audience Profile is not available, ask the user whether to proceed with Needs Analysis data only (lower quality) or wait.

---

### Step 1: Generate Learning Objectives

Using the upstream data, draft learning objectives following these rules:

**For course-level LOs (3–5 objectives):**
- Each objective must ladder to the Course-Level Learning Goal (Needs Analysis Section 3)
- Each objective must address at least one documented performance gap (Needs Analysis Section 2)
- The set of objectives should collectively cover the behavior change stated in the Project Strategy Statement
- Use Bloom's levels from Audience Profile Section 3A — don't default to lower levels unless justified

**For module-level LOs (2–4 objectives per module):**
- Each objective must ladder to one or more course-level LOs
- Each objective must align with the module's learning goal from the Module Scope Map
- Each objective must be achievable within the module's time and format constraints
- If the module's stability rating is **Moderately Stable** or **High Maintenance**, prefer objectives that target understanding, evaluation, or decision-making over objectives that target specific procedural recall

**For all objectives:**
- Begin each objective with a specific, measurable action verb appropriate to the Bloom's level
- Write for the persona described in the Audience Profile — use their frame of reference
- Avoid vague verbs: understand, learn, know, be aware of, appreciate
- Each objective should be testable — if you can't imagine a knowledge check question or activity that proves achievement, the objective is too vague

---

### Step 2: Generate Misconception-Driven Corrective Objectives

Review the misconceptions from Audience Profile Section 2C (or Customer Voice Section D if Audience Profile isn't available). For each misconception rated **Medium or High severity** that is relevant to this course/module:

Generate a **corrective learning objective** — an objective specifically designed to replace the wrong mental model with the correct one.

**Format for corrective objectives:**

```
LO [#]c: [Objective statement]

Type: Corrective — addresses misconception [D# from Audience Profile/Customer Voice]
Misconception: [What they currently believe]
Correct understanding: [What they should believe after this objective is achieved]
Bloom's level: [Typically Analyze or Evaluate — correcting misconceptions requires higher-order thinking than simple recall]
Assessment approach: [How to test — e.g., "Scenario presenting the misconception as a plausible option; learner must identify why it's wrong and select the correct alternative"]
```

**Rules for corrective objectives:**
- Don't just add "distinguish between X and Y" objectives mechanically — only generate a corrective LO if the misconception is genuinely relevant to this module's scope
- If a misconception is better addressed in a different module (based on the sequencing rationale), note that instead of forcing a corrective LO here
- Low-severity misconceptions don't need their own objectives — they can be addressed through narration or knowledge check distractors without a formal LO

---

### Step 3: Compile and Validate

For each objective (standard and corrective), provide:

```
LO [#]: [Objective statement]

Bloom's level: [Remember / Understand / Apply / Analyze / Evaluate / Create]
Addresses gap: [Reference Needs Analysis Section 2 gap — e.g., "Performance Gap #2: Cannot configure governance policies"]
Addresses misconception: [Reference misconception item if corrective, or "N/A"]
Ladders to: [Course-level LO # (for module-level LOs) or Course Learning Goal (for course-level LOs)]
Stability note: [If the topic is Moderately Stable or High Maintenance, note how the objective is written to be durable — e.g., "Written as a decision-making objective rather than procedural recall to accommodate UI changes"]
Assessment evidence: [1 sentence — what activity or question would demonstrate achievement. E.g., "Scenario-based question where learner evaluates a governance policy configuration and identifies the gap"]
```

**Validation checks (run these before presenting the final set):**
- [ ] Every documented performance gap (Needs Analysis Section 2) is addressed by at least one LO
- [ ] Every Medium/High severity misconception relevant to this module has a corrective LO or an explicit note about where it's addressed instead
- [ ] No LO targets a prerequisite (something the Audience Profile Section 5 says they already know)
- [ ] No LO targets content explicitly out of scope for this module
- [ ] The full set of LOs, if achieved, would satisfy the Course-Level Learning Goal
- [ ] Bloom's levels match the Audience Profile Section 3A targets — flag any LO where you deliberately chose a different level and explain why

**🔵 Confidence:** [High / Medium / Low] — [Basis: Are the LOs grounded in documented gaps and misconceptions (high), or inferred from module scope alone (medium), or generated without upstream data (low)? What would change it.]

---

### Output Summary

After the full LO set, provide:

**LO-to-Gap Traceability Matrix:**

| LO # | Objective (short) | Gap Addressed | Misconception Addressed | Bloom's Level | Module |
|---|---|---|---|---|---|
| LO 1 | [abbreviated] | Gap #[X] | — | Apply | Course-level |
| LO 2c | [abbreviated] | Gap #[X] | D[#] | Analyze | Module 2 |

**Coverage check:**
- Gaps with no corresponding LO: [list, or "None — all gaps covered"]
- Misconceptions with no corrective LO: [list with justification — e.g., "D4 (low severity) — addressed through narration in Module 3, not a formal LO"]
- LOs with no gap or misconception backing: [list — these may indicate scope creep or an undocumented gap worth adding to the Needs Analysis]

**Downstream note for Detailed Outline:** When building the outline, each lesson should map to one or more LOs from this set. Corrective LOs (marked with 'c') should be placed at the point in the sequence identified in the misconception's instructional implication (from Audience Profile Section 2C). The traceability matrix above is the input the Outline prompt will consume.

Write in clear, professional prose. Flag any objective where you're uncertain about the right Bloom's level or where the gap evidence is thin — mark with **[NEEDS VALIDATION]**.
````
