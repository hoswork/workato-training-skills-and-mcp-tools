---
name: generate-kahoot
description: Use when generating a Kahoot quiz from a learning artifact — course slides, lab guides, outlines, or any training material. Kahoot-importable CSV output. No dependencies.
metadata:
  version: "1.0"
---

# generate-kahoot

Generates a Kahoot-importable CSV quiz from any learning artifact — slide decks, lab guides, course outlines, PDFs, or any training material Claude Desktop can read. Orchestrates content analysis, web research, learning objective formulation, quiz generation, and validated CSV output in one pass. No tools or dependencies required.

## When to invoke

Invoke when:

- Generating a Kahoot quiz from any training material (pre-session review game, end-of-module knowledge check, live event quiz).
- Producing a Kahoot-importable spreadsheet without manually writing quiz questions.

Skip when:

- You need only True/False or open-ended questions — Kahoot's import format supports quiz-type (single-correct-answer) only.

## Workflow

### Step 1 — Analyze the learning artifact

From the provided content, identify:
- Main topic and subject
- Key concepts and learning points
- Speaker notes or annotations with additional context
- Any sections focused on learning objectives, summaries, or key takeaways

### Step 2 — Research the topics

Use WebSearch to research the key topics. Focus on:
- Verifying factual accuracy of the slide content
- **Identifying known misconceptions** about the topic — common wrong mental models, observed failure modes, plausible mistakes a learner who hasn't mastered the material would make. These must become distractors.
- For Workato topics, check Workato documentation for accurate details

Search 2–3 targeted queries based on the core topics identified. Keep a running list of misconceptions found — you'll need them in Step 4.

### Step 3 — Formulate learning objectives

Before writing questions, state 3–5 clear learning objectives based on the presentation content. Use Bloom's taxonomy verbs (identify, explain, apply, analyze, evaluate, create).

These guide question design — each question should map to at least one objective.

### Step 4 — Generate quiz questions

Generate 10–15 questions. Follow these rules:

**Content rules:**
- Cover the learning objectives from Step 3
- Test understanding, not just recall — include application and analysis questions
- Verify factual accuracy against Step 2 research
- Exactly ONE correct answer per question

**Format constraints (Kahoot limits):**
- Questions: max 120 characters
- Answers: max 75 characters each
- 4 answer choices (2–3 for true/false style)
- Time limit: 20s for recall, 30s for standard, 60s for application/analysis

**Distractor rules:**
- Each distractor must reflect a real wrong answer — a misconception from Step 2, an observed failure mode, or a plausible mistake a learner who hasn't mastered the material would make. Fabricated fillers ("delete everything and start over") fail.
- Distractors must not reinforce a different misconception on the way to being wrong — every option must be accurate on its own terms, just not the right answer to this question.
- When a question tests a known misconception, the misconception itself must appear as a distractor and be plausible enough that a learner still holding it would pick it.
- Calibrate difficulty: distractors should be clearly wrong to someone who has mastered the material, plausible to someone who hasn't. Trick questions and technically-defensible alternatives to the correct answer both fail.

**Answer-length balancing — see Quiz design rules below. Run the audit before Step 5.**

### Step 5 — Validate and output CSV

**Validation (required before writing the CSV):**

1. **Character counts** — for every question and answer, count characters. Flag and fix any that exceed the limits:
   - Question over 120 chars: trim or rephrase
   - Any answer over 75 chars: trim or rephrase

2. **Answer-length audit** — check the 40% rule at both extremes (see Quiz design rules). Revise distractors if the correct answer is the longest or shortest in more than 40% of questions.

3. **Distractor quality check** — verify every distractor traces to a real misconception or failure mode from Step 2, not a fabricated filler. Verify no distractor accidentally teaches a wrong model by using inaccurate framing.

4. **Set-level review** — check the full question set for the patterns in Quiz design rules: topic coverage, correct-position distribution, difficulty spread, distractor reuse, question type variety. Fix any pattern violations before writing.

Then output the quiz as a CSV code block using the column order below. Include the header row. The user opens this in Excel or Google Sheets, verifies, and saves as `.xlsx` for Kahoot import.

```
Question,Answer 1,Answer 2,Answer 3,Answer 4,Time limit,Correct answer(s)
```

### Step 6 — Summary

Return a clean summary:

1. **Learning objectives** — the 3–5 objectives from Step 3
2. **Quiz summary** — question count, topic distribution, difficulty spread
3. **Key takeaways** — 5–7 bullets capturing the most important concepts the quiz reinforces

## Kahoot CSV format spec

| Column | Content | Constraint |
|---|---|---|
| Question | Question text | Max 120 chars |
| Answer 1–4 | Answer choices | Max 75 chars each |
| Time limit | Seconds | 5, 10, 20, 30, 60, or 120 |
| Correct answer(s) | 1-based answer index | e.g. `1` or `2,3` for multi-correct |

- Only **quiz** question type supported for import
- 2–4 answers per question; max 200 questions per spreadsheet
- File must be saved as `.xlsx` (Excel 2007+) before uploading to Kahoot

## Quiz design rules

### Answer-length balancing

Correct answers tend to be longer (precision requires words); wrong answers tend to be short (thrown in quickly). Test-takers learn to pick the longest — or shortest — option without knowing the material.

Enforce the 40% rule at both extremes:

- The correct answer should be the longest option in no more than 40% of questions
- The correct answer should be the shortest option in no more than 40% of questions
- Make distractors detailed and plausible — add qualifiers, specifics, or extra words to wrong answers
- Vary correct-answer position (1–4) — distribute roughly evenly across the set
- Never use "all of the above" or "none of the above" — they reward test-savvy over content mastery (per `complete-check §1.4`)

### Set-level review

After generating the full question set, check these patterns across all questions — individual questions can pass and the set can still be exploitable:

- **Topic coverage** — every learning objective from Step 3 is covered by at least one question; no objective dominates more than 40% of questions
- **Correct position distribution** — correct answer positions (1, 2, 3, 4) are spread roughly evenly; no position holds more than 40% of correct answers
- **Difficulty spread** — the set includes a mix of recall (20s), standard (30s), and application/analysis (60s) questions; not all questions at the same time limit
- **Distractor reuse** — the same wrong answer does not appear across multiple questions (tells test-takers which answers are safe to ignore)
- **Question type variety** — not all questions use the same sentence structure (e.g., all "What is X?" or all "Which of the following...")

## What this skill is NOT

- **Not a live presentation tool.** Produces a CSV for Kahoot import — the quiz runs in Kahoot's platform, not here.
- **Not a general quiz generator.** Format and constraints are specific to Kahoot's import template.
- **Not a quality reviewer.** For a Standards Desk review of quiz questions, run `the-once-over` (specifically the `calibrate-challenge` routing for Principles 4 and 6 — observable success criteria and retrieval practice).

## Logging

At completion, invoke: `skill-logger generate-kahoot` (if `skill-logger` is available in the current environment; skip silently if not). This collects org-wide usage telemetry for Workato training-team skills.

## Tape

At the end of a session where this skill produced a meaningful output, offer to run `the-tape` if any decisions were made that overrode, extended, or notably validated these standards:

> "Want to capture any decisions to the tape? It helps the team evolve these standards over time."

Only proceed if they say yes. Skip silently if `the-tape` is not installed.
