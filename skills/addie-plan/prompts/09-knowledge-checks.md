---
title: Knowledge Checks & Quiz Questions
addie_phase: Develop
prompt_order: 9
confluence_page_id: 2467692837
confluence_version: 7
confluence_version_date: 2026-05-27
synced: 2026-06-04
source: https://workato.atlassian.net/wiki/spaces/ETT/pages/2467692837
---

**ADDIE Stage:** Develop

**Position:** Runs after lesson scripts are drafted (or after the Detailed Outline is approved, if writing assessments before scripts). Consumes Learning Objectives (with Bloom's levels), misconception data (threaded from Customer Voice through Audience Profile and Outline), and Usage Data struggle points. Its output feeds Storyboarding (for knowledge check blocks) and the reviewing-scripts/storyboards skills.

### **When to use**

After lesson content is drafted or the Detailed Outline is complete for a module. Use to generate a first-draft question set — always review and edit for accuracy before including in a course. Works best when you have the lesson outline and/or script available so questions are grounded in what was actually taught.

#### Required upstream artifacts

Before running this prompt, the following deliverables must exist. Claude will locate and read them automatically.

* **Learning Objectives** — the module-level LOs with Bloom's levels, traceability matrix, and assessment evidence notes. Bloom's level determines question complexity; corrective LOs (tagged with 'c') generate misconception-based distractors.
* **Detailed Outline** — the module's lesson-by-lesson blueprint, specifically:

    * LO coverage matrix (which LOs are covered in which lessons)
    * Misconception placement summary (which misconceptions were addressed and where)
    * Content summaries per lesson (what was taught — questions should test this, not outside knowledge)


### Optional upstream artifacts (use if available)

* **Customer Voice Section D** (Misconception Inventory) — the full misconception detail: what they believe, why it's wrong, why they hold it. Used to build distractors that reflect real wrong answers, not fabricated ones.
* **Usage Data Section B** (Struggle Points) — where users actually fail, with metrics. Used to build scenario stems grounded in real failure patterns.
* **Usage Data Section C** (Adoption Barriers) — prerequisite gaps that cause real-world mistakes. Used for scenario context.
* **Audience Profile Section 2C** (Misconceptions) — persona-specific misconception mapping with severity ratings. Helps prioritize which misconceptions deserve their own questions vs. appearing as distractors in other questions.
* **Lesson scripts** (if drafted) — paste the narration or on-screen text for the lessons being assessed. Questions should test what was taught, in the way it was taught.
* **Storyboards** (if drafted) — used in optional Step 2.5 to cross-check against in-module KC blocks and avoid duplicate questions.

### Rise 360 Question Types — Reference

The prompt below assumes the assessment will be delivered in Articulate Rise 360. Different Rise question blocks support different feedback patterns, and this directly affects how the question and its feedback should be written.

| Rise block | Best for | Feedback behavior | Constraints |
| --- | --- | --- | --- |
| **Multiple Choice** | Single-correct scenario or recall | Per-option feedback (1 correct + 3 incorrect, one per distractor) OR single binary | 4 options max in practice |
| **Multiple Response** (multiselect) | Testing 2+ related concepts in one question | Binary only — 1 correct (exact match required) + 1 incorrect (any other combo) | No partial credit; no per-option feedback. The incorrect message must teach the principle regardless of which specific mistake the learner made |
| **Matching** | Vocabulary-to-concept, scenario-to-category | Single completion feedback | Best with 3–4 pairs; gets cramped on mobile beyond that |
| **Sorting** | Categorizing 4–6 items across 2–4 buckets | Per-attempt or completion feedback | Confirm mobile layout for ≥6 items |
| **Fill-in-the-Blank** | Terminology or specific phrasing recall | Single correct/incorrect | Brittle — accepts only exact matches by default |

`````markdown

````
You are an instructional designer creating assessment questions for Workato Academy — a technical e-learning curriculum for a SaaS automation platform.

**Module title:** [e.g., Module 2: How Enterprise MCP Works]
**Course:** [e.g., Intro to Enterprise MCP]
**Assessment type:** [e.g., End-of-module knowledge check — 3–5 questions; not a certification exam]
**Question format:** [Specify per question. Rise 360 supports: Multiple Choice (1 correct, 3 distractors) / Multiple Response (multiselect, 2+ correct out of 4) / Matching (pair items across columns) / Sorting (items into categories) / Fill-in-the-Blank. Match the format to the cognitive task; scenario-based where possible.]
**Pass criteria:** [Default: gated, ≥80% first-attempt correct (Workato Academy standard). Override only if the KC is formative / not gated.]

### Step 0: Retrieve Upstream Artifacts

Before writing any questions, locate and read the following upstream deliverables. The user will tell you where each one lives.

**Required — read these before proceeding:**

1. **Learning Objectives** for this module. Extract and hold:
   - Each module-level LO with its Bloom's level
   - Corrective LOs (tagged 'c') — these target specific misconceptions and should generate misconception-based questions
   - Assessment evidence notes — the LO prompt's suggestion for how to test each objective
   - The traceability matrix — which gaps and misconceptions each LO addresses

2. **Detailed Outline** for this module. Extract and hold:
   - LO Coverage Matrix — which LOs are covered in which lessons
   - Misconception Placement Summary — which misconceptions were addressed, in which lessons, using what approach
   - Content summaries per lesson — what was actually taught (questions must stay within this scope)

**Optional — read if the user provides a location:**

3. **Customer Voice Section D** (Misconception Inventory) — the numbered misconceptions with:
   - What customers believe (the wrong answer → distractor)
   - Why they hold it (helps write plausible distractor rationale)
   - Severity rating (High/Medium misconceptions get their own questions; Low misconceptions appear as distractors in other questions)

4. **Usage Data Section B** (Struggle Points) — where users actually struggle, with:
   - What happens (the failure → scenario stem)
   - Hypothesized cause (the knowledge gap → what the question tests)
   - Percentage affected (helps calibrate question difficulty — if 60% of users struggle with this, it's a core question, not an edge case)

5. **Usage Data Section C** (Adoption Barriers) — prerequisite gaps that cause real mistakes. Used for scenario context that feels authentic.

6. **Lesson scripts** (if available) — paste or point to the narration/on-screen text for the lessons this assessment covers. Questions should test what was taught, using similar framing and terminology.

7. **Storyboards** (if available) — used in optional Step 2.5 to check for in-module KCs on the same content.

**Extend with lesson-specific failure modes (if needed):**
After retrieving the upstream artifacts, check whether you have enough real failure scenarios and misconceptions to build all distractors. If the upstream data is thin for specific lessons:
- Search Gong for troubleshooting calls about **[this module's specific topic]** — look for mistakes customers make
- Search Slack (#solutions-engineering, relevant product channels) for repeated questions about this topic
- Tag any new findings as "[New — not in upstream briefs]"

**After retrieval, confirm to the user:** List which artifacts you found and any you couldn't locate.

---

### Step 1: Map Questions to LOs and Bloom's Levels

Before writing questions, create a question plan:

| Question # | LO Assessed | Bloom's Level | Rise Block Type | Misconception Used | Source for Distractors |
|---|---|---|---|---|---|
| Q1 | LO 2.1 | Apply | Multiple Choice | — | Usage Data B2 (config failure) |
| Q2 | LO 2.2c | Analyze | Multiple Response | D2 | Customer Voice D2 |
| Q3 | LO 2.3 | Apply | Multiple Choice | D4 (as distractor) | Usage Data B3 |

**Rules for the question plan:**
- Every module-level LO should be assessed by at least one question
- Corrective LOs (tagged 'c') must generate a question that specifically tests whether the learner has replaced the misconception with the correct understanding
- Bloom's level determines question complexity:
  - Remember/Understand → Direct questions (but avoid pure definition recall — even these should require some application)
  - Apply → Scenario-based: "Given this situation, what should you do?"
  - Analyze → Diagnostic: "This workflow is failing. Based on the symptoms, what is the most likely cause?"
  - Evaluate → Judgment: "Which approach would be most effective for this governance scenario, and why?"
- Rise block type should match the cognitive task — see the Rise 360 Question Types reference. Multiple Response is efficient when testing 2+ related concepts in one question but provides only binary feedback; if per-option teaching is critical, prefer Multiple Choice.
- Higher-priority struggle points (from Usage Data Section B) should appear in earlier questions

---

### Step 2: Write Questions

Generate [number] knowledge check questions. For each question provide the structure below. **Learner-facing content (stem, options, correct answer, feedback) sits at the top of each question; review-only metadata (LO, misconception, Rise block type, LO connection, sources, ID notes) is grouped at the bottom under a clear divider** so the CD can see at a glance what ships in Rise vs. what's internal.

```
Q[#]: [Question stem]

A. [Option text]
B. [Option text]
C. [Option text]
D. [Option text]

Correct answer: [Letter(s)]

Learner-facing feedback (write according to the Rise block type's feedback structure — see Rise 360 Question Types reference):

[For Multiple Choice — per-option feedback:]
- Correct ([Letter]): [Teach the principle the option tests. 1–2 sentences.]
- Incorrect ([Letter]): [Explain why this option is wrong and what concept the learner should re-anchor on. 1–2 sentences.]
- Incorrect ([Letter]): [Same as above for this distractor.]
- Incorrect ([Letter]): [Same as above for this distractor.]

[For Multiple Response — binary feedback only:]
- Correct feedback (triggers only when the learner selects the EXACT correct set — no more, no less): [Affirm the principle being tested, naming the correct options and the key idea each represents.]
- Incorrect feedback (triggers for every other combination — missing one correct, picking a distractor, picking only one of the correct options): [Teach the underlying principle regardless of which specific mistake the learner made. Name both correct answers and the misconception each distractor reflects.]

[For Matching / Sorting — single completion feedback:]
- Correct completion: [Affirm the pattern the learner just demonstrated.]
- Incorrect: [Teach the principle that should guide the matches/sorts.]

— — — Review metadata (not learner-facing) — — —

LO assessed: [LO number and Bloom's level]
Misconception targeted: [D# if this is a corrective question, or "None"]
Rise block type: [Multiple Choice / Multiple Response / Matching / Sorting / Fill-in-the-Blank]
LO connection: [One sentence noting how this question tests the LO. For ID/SME review only — not learner-facing.]

Sources:
- Scenario stem based on: [CV-C2 item #, Usage Data B# or C#, or "Lesson content"]
- Distractor A based on: [CV-D#, Usage Data B#, or "Common misconception from Gong/Slack"]
- (etc.)

ID notes (optional — flags only): [Use only to flag distractor sourcing concerns, feature/positioning verification needs, or other internal review items. Do NOT restate why the answer is correct — that lives in the learner-facing feedback.]
```

---

### Step 2.5 (optional): Cross-check against existing in-module KCs

**Use this step when:** writing an end-of-course or capstone KC, OR when the module's storyboards already include knowledge check blocks on the same lessons.

For each question, check whether an in-module KC in the storyboards already tests the same concept. If so, note how this question differs:
- Different scenario / context?
- Different Bloom's level (e.g., Understand vs. Apply)?
- Different misconception or distractor focus?
- Different cognitive task (matching vs. discrimination)?

If a question is too close to an existing in-module KC, revise it to add new evidence rather than repeat the test. Document the deconfliction logic in a brief note under each affected question so a future reviewer can see the rationale.

---

### Writing guidelines

**Scenario stems — grounded in reality, generalized for instruction:**
- Use real customer scenarios from Customer Voice Section C2 and Usage Data Section B as foundations, but generalize them (same principle as Script Drafting — teach from the scenario, don't cite the customer)
- ✅ "A platform admin has configured an MCP connection for their AI agent, but the agent is returning errors when trying to access recipe data. The audit log shows the connection authenticated successfully."
- ❌ "One of our customers reported that their MCP connection was failing..." (sounds like a support ticket, not an assessment)

**Distractors — based on real mistakes, not random wrong answers:**

Good distractors are based on real mistakes customers make. Every distractor should pass the "would a real learner choose this?" test.

- ✅ "Check the data source permissions at the account level" — This is what many users try first (from Usage Data B2), but the actual issue is at the connection level. The distractor is plausible because the learner hasn't yet internalized the permission hierarchy.
- ✅ "Increase the rate limit threshold" — This seems logical if you misunderstand the error as a rate limit issue (misconception D3), but the root cause is authentication scope.
- ❌ "Delete all data and start over" — No real learner would choose this. It's filler, not a distractor.
- ❌ "Configure the workflow to fail intentionally" — Obviously wrong. Wasting an option slot.

**Distractor quality checklist:**
1. Each distractor should be traceable to a real mistake — from Customer Voice Section D, Usage Data Section B, or lesson-specific Gong/Slack research
2. Each distractor should be plausible to someone who hasn't mastered the learning objective
3. The feedback for why it's wrong should teach something valuable — not just "this is incorrect"
4. Distractors should be similar in length and detail to the correct answer
5. **Distractors must not reinforce a misconception on the way to being wrong.** A distractor that uses inaccurate framing (e.g., "the agent's training data" when the correct mechanism is "context") teaches the wrong mechanism even when learners pick a different answer. Every option should be accurate on its own terms.
6. **Option text should not telegraph the answer.** Don't include product definitions or description glosses next to product names if the stem already implies the answer by describing the function. Keep option text terse; teach in the feedback.

**General rules:**
- Avoid "all of the above" and "none of the above" options
- Do not use negative phrasing in question stems (e.g., "Which of the following is NOT...")
- Questions should test application and judgment, not recall of definitions or trivia
- Write in plain language — the question stem should never be harder to read than the content it's assessing
- Distractors should be similar in length and detail to the correct answer so they don't stand out
- **Calibrate against the ≥80% first-attempt pass criterion.** Distractors must be plausible to someone who hasn't mastered the LO, but the correct answer must be clearly right to a learner who has internalized the lesson content. Avoid trick questions, ambiguous "correct" answers, or distractors that are technically defensible alternatives. First-attempt correct on a gated KC is the design target, not a stretch goal.

---

### Step 3: Validate and Summarize

**Assessment Coverage Matrix:**

| LO # | Objective (short) | Assessed by Q# | Bloom's Level Matched? | Misconception Tested? |
|---|---|---|---|---|
| LO 2.1 | [abbreviated] | Q1 | ✅ Apply → scenario | — |
| LO 2.2c | [abbreviated] | Q2 | ✅ Analyze → diagnostic | D2 ✅ |

**Validation checks:**
- [ ] Every module-level LO is assessed by at least one question
- [ ] Every corrective LO generates a question that specifically targets the misconception
- [ ] Question complexity matches the LO's Bloom's level (no recall questions for Apply-level LOs)
- [ ] Every distractor is traceable to a real mistake (upstream source cited)
- [ ] No question tests content outside what was taught in this module's lessons
- [ ] No question tests prerequisite knowledge (from Audience Profile Section 5) — only what this module taught
- [ ] Scenario stems reflect realistic situations, generalized for instruction (no customer citations in question text)
- [ ] Each question specifies its Rise block type
- [ ] Feedback structure matches the Rise block type's capabilities (per-option for Multiple Choice; binary for Multiple Response; single completion for Matching/Sorting)
- [ ] For Multiple Response questions, the incorrect feedback works for any wrong combination — not just the most likely one
- [ ] No distractor reinforces a misconception, even one outside the question's scope
- [ ] The question set is calibrated for ≥80% first-attempt correct on a gated KC. No trick questions, no ambiguous correct answers, no distractors that are technically defensible alternatives to the right answer.
- [ ] Per-question template structure followed — learner-facing content at top, review metadata grouped below the divider

**Distractor source summary:**

| Source Type | Count | Examples |
|---|---|---|
| Customer Voice misconceptions (D#) | [N] | D2, D4 |
| Usage Data struggle points (B#) | [N] | B2, B3 |
| Usage Data adoption barriers (C#) | [N] | C1 |
| Lesson-specific research (Gong/Slack) | [N] | [New — call IDs] |
| Inferred (no upstream source) | [N] | [Flag these — they should be the minority] |

**🔵 Confidence:** [High / Medium / Low] — [Basis: Are distractors grounded in real misconceptions and failure data (high), or inferred from topic knowledge (medium), or fabricated without upstream data (low)? Which questions have the weakest distractor sourcing? What would increase confidence — e.g., "Q4 distractors are inferred — a quick Slack search in #solutions-engineering for [topic] would validate or replace them."]

---

Write clearly and precisely. Flag any question where the distractor sourcing is weak with **[DISTRACTOR SOURCING — NEEDS DATA]** so the ID knows to strengthen it before publishing.
````
`````
