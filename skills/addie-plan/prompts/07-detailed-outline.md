---
title: Detailed Outline
addie_phase: Design
prompt_order: 7
confluence_page_id: 2466218767
confluence_version: 2
confluence_version_date: 2026-05-06
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2466218767
---

**ADDIE Phase:** Design

**Position:** Runs after Learning Objectives are approved. Consumes the LO set, Needs Analysis Module Scope Map, Audience Profile, Content Audit, and Usage Data to produce a lesson-by-lesson blueprint. Its output feeds Script Drafting, Knowledge Checks, Storyboarding, and the reviewing-outlines skill.

### **When to use**

After LOs are approved by stakeholders and you have completed upstream deliverables. Use this prompt to generate a first-draft lesson-by-lesson structure for a single module before building your storyboard. Run once per module — don't try to outline an entire course in one prompt.

Note: The prompt is set up to generate an outline at the module level. Run multiple times for each course module or adjust the language for your needs.

### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Learning Objectives** — the full LO set for this module, including the traceability matrix (LO-to-gap and LO-to-misconception mappings). Both course-level and module-level LOs are needed.
* **Needs Analysis (Course Strategy Document)** — specifically:

    * Section 4 (Module Scope Map) — this module's learning goal, content status, stability rating, build complexity, and scope boundaries
    * Section 5 (Sequencing Rationale) — prerequisite logic affecting this module's internal lesson order

* **Audience Profile** — specifically:

    * Section 2C (Misconceptions) — the instructional implications for each misconception, including where in the sequence it should be addressed
    * Section 5 (Prerequisites) — mitigation strategies (bridge content, assume-and-reference, prerequisite course, etc.)
    * Section 6 (Design Implications) — the top 3 design implications for this persona


### Optional upstream artifacts (use if available)

* **Content Audit Section D** (Reuse Opportunities) — assets tagged for reuse in this module
* **Content Audit Section E2** (Per-Topic Stability Ratings) — stability flags for topics covered in this module (also available via Needs Analysis Section 4, but E2 has more detail)
* **Usage Data Section A** (Priority Workflow Ranking) — workflows this module covers, ranked by teaching priority
* **Usage Data Section B** (Struggle Points) — points where users struggle with this module's topics, with scaffolding recommendations

````
You are an instructional designer working on Workato Academy — a technical e-learning curriculum for a SaaS automation platform. You are creating a detailed lesson-by-lesson outline for a single module.

**Module title:** [e.g., Module 2: How Enterprise MCP Works]
**Course this belongs to:** [e.g., Intro to Enterprise MCP]

### Step 0: Retrieve Upstream Artifacts

Before building the outline, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Learning Objectives** for this module. Extract and hold:
   - The module-level LOs (both standard and corrective)
   - The traceability matrix — which gaps and misconceptions each LO addresses
   - The Bloom's level and assessment evidence for each LO
   - The course-level LOs this module's LOs ladder to

2. **Needs Analysis (Course Strategy Document)** for this course. Extract and hold:
   - Section 4 — this module's entry in the Module Scope Map: learning goal, content status, stability rating, build complexity, known risks
   - Section 5 — sequencing rationale: any prerequisite dependencies affecting this module's internal lesson order (e.g., "Lesson on configuring policies must come after lesson explaining the policy model")
   - Section 7 — SME requirements: which SMEs are assigned to this module and what subject areas they cover (use this to populate the "SME input needed" field per lesson)

3. **Audience Profile** for the target persona. Extract and hold:
   - Section 2C — misconceptions relevant to this module, with instructional implications (where and how to address each)
   - Section 5 — prerequisite mitigation strategies relevant to this module (does the outline need bridge content? An assume-and-reference note? A self-assessment?)
   - Section 6 — top 3 design implications (e.g., "Lead with governance scenarios, not builder workflows")

**Optional — read if the user provides a location:**

4. **Content Audit Section D** — reuse opportunities for this module: assets to reuse as-is (D1), adapt (D2), or repurpose elements from (D3)

5. **Content Audit Section E2** — per-topic stability ratings for topics in this module (more detailed than the module-level rating in the Needs Analysis)

6. **Usage Data Section A** — priority ranking for workflows this module covers (higher-priority workflows get deeper treatment and earlier placement)

7. **Usage Data Section B** — struggle points for this module's topics, with scaffolding recommendations (e.g., "add a guided walkthrough before the lab")

**After retrieval, confirm to the user:** List which artifacts you found, which sections you extracted, and any you couldn't locate.

---

### Step 1: Build the Lesson-by-Lesson Outline

Draft a detailed outline for this module. For each lesson:

```
Lesson [#]: [Title]

Learning objective(s): [LO numbers from the LO set — e.g., "LO 2.1, LO 2.2c"]
Content summary: [3–5 sentences describing what is covered. Be specific — not "covers governance policies"
  but "explains the three-tier policy model (workspace, project, recipe), walks through how policies
  inherit and override, and presents a scenario where a misconfigured policy causes an unintended
  automation to run."]
Modality: [e.g., Narrated concept explanation, Scenario-based walkthrough, Interactive lab,
  Knowledge check, Video demo — choose based on what the content requires and the design
  implications from Audience Profile Section 6]
Approximate time: [minutes]

Misconception addressed: [If this lesson addresses a corrective LO, reference the misconception:
  "Addresses misconception D2 (users confuse MCP with standard API access) — lesson uses a
  side-by-side comparison to surface the distinction before teaching MCP-specific configuration."
  If no misconception is addressed in this lesson, write "None."]

Stability flag: [If this lesson covers a topic rated Moderately Stable or High Maintenance
  in Content Audit E2 or Needs Analysis Section 4:
  "⚠️ Stability: [Moderately Stable / High Maintenance] — [topic]. Last verified: [date].
  Script should prefer concepts over specific UI steps. Screenshots will need version check
  before production."
  If the topic is Evergreen, write "Evergreen — no stability concerns."]

Reusable assets: [Reference specific assets from Content Audit Section D:
  "Reuse as-is: [Asset A3 — OAuth configuration diagram from Foundations course]"
  "Adapt: [Asset A7 — API overview doc, needs MCP-specific framing]"
  "Repurpose element: [Extract the 3-step flow diagram from Asset A12]"
  If no reusable assets apply, write "None — net-new content."]

Scaffolding: [If Usage Data Section B identifies a struggle point at this stage:
  "Scaffolding needed: Usage Data B2 shows 60% of users abandon during initial configuration.
  Add guided walkthrough with checkpoint moments before the lab activity."
  If no scaffolding is flagged, write "Standard — no additional scaffolding needed."]

SME input needed: [If this lesson requires SME validation before scripting, note what specifically
  and reference the assigned SME from Needs Analysis Section 7:
  "SME needed: [Name from Section 7, subject area] — Confirm whether the 3-tier policy model is
  still accurate post-Q2 release (stability flag)."
  If no SME input is needed, write "None — content is validated."]
```

---

### Step 2: Place Misconceptions in the Sequence

After drafting the lesson list, review the misconception inventory from Audience Profile Section 2C. For each misconception relevant to this module:

- Confirm it's placed in the right lesson (per the instructional implication from Section 2C)
- Confirm the placement makes pedagogical sense — the misconception should be addressed *after* the correct concept is introduced but *before* the learner needs to apply the correct understanding
- If a misconception from the Audience Profile says "address in Module X" but this outline is for Module Y, note that the misconception is deferred — don't force it into the wrong module

**Misconception Placement Summary:**

| Misconception | Severity | Placed in Lesson | Corrective LO | Approach |
|---|---|---|---|---|
| D[#]: [label] | [H/M/L] | Lesson [#] | LO [#]c | [Brief — e.g., "Side-by-side comparison before config lesson"] |
| D[#]: [label] | [H/M/L] | Deferred to Module [X] | — | [Why — e.g., "Requires understanding of [concept] taught in Module 3"] |

---

### Step 3: Validate and Summarize

**Sequencing rationale:** [2–3 sentences explaining why lessons are ordered this way. Reference:
- Prerequisite logic from Needs Analysis Section 5
- Misconception placement logic (corrective content comes after the concept it corrects)
- Usage Data priority ranking (higher-priority workflows appear earlier)
- Scaffolding placement (struggle points get support before the challenging content)]

**Validation checks:**

- [ ] Every module-level LO is addressed by at least one lesson
- [ ] Every lesson maps to at least one LO — no decorative lessons without a learning purpose
- [ ] Every Medium/High severity misconception relevant to this module is placed in a lesson or explicitly deferred with rationale
- [ ] Stability flags are applied to every lesson covering a Moderately Stable or High Maintenance topic
- [ ] Reusable assets from Content Audit are referenced where applicable — no redundant creation
- [ ] Scaffolding from Usage Data struggle points is placed at the right point in the sequence
- [ ] Prerequisite mitigation strategy from Audience Profile Section 5 is reflected (bridge content, assume-and-reference, etc.) — typically in Lesson 1 or as a pre-module note
- [ ] Design implications from Audience Profile Section 6 are reflected in modality and content choices
- [ ] Total estimated time aligns with the module's time allocation in the Module Scope Map

**LO Coverage Matrix:**

| LO # | Objective (short) | Covered in Lesson(s) | Assessment in |
|---|---|---|---|
| LO [#] | [abbreviated] | Lesson [#] | [Knowledge check / Scenario in Lesson X / End-of-module quiz] |
| LO [#]c | [abbreviated] | Lesson [#] | [Distractor-based question targeting misconception D#] |

**Module summary:**
- Total lessons: [N]
- Estimated total time: [X] minutes
- Net-new content: [N] lessons
- Adapted/reused content: [N] lessons
- Stability-flagged lessons: [N] — [list which ones]
- Misconceptions addressed: [N] — [list which ones]
- Misconceptions deferred: [N] — [list with target modules]

**🔵 Confidence:** [High / Medium / Low] — [Basis: Are lessons grounded in upstream data (LOs, gaps, misconceptions, usage data) or inferred from topic scope alone? Which lessons have thin upstream backing? What would increase confidence — e.g., "Lessons 3–4 cover topics where Usage Data had no struggle point data. SME review would confirm whether scaffolding is needed."]

---

Write in clear, professional prose. Use the lesson format exactly as specified — downstream prompts (Script Drafting, Storyboarding) reference lessons by number and expect these fields. Flag any lesson where scope is uncertain with **[SCOPE TBD — SME INPUT NEEDED]**.
````
