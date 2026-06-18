"""
calibrate-challenge — snippet 1 (rules + rubric).
Applies to training and education audiences. Not applicable to workato general audience.
Static checks are presence-only; adult-learning principles require LLM reasoning.
"""

RUBRIC = ""
---
name: calibrate-challenge
description: Use when designing or reviewing training content (labs, slide decks, exercises, knowledge checks, walkthroughs) to check that the cognitive load is calibrated for adult professional learners — productive struggle with appropriate scaffolding, no avoidable friction, transfer-ready by design. Frame the pillar of Learning Effectiveness under The Standards Desk; never call this 'pedagogy'.
---

# Calibrate Challenge

A pass that checks training content against adult-learning theory. Produces calibrated cognitive demand: hard enough to be productive, scaffolded enough to be completable, structured enough to transfer.

> **Never write "pedagogy."** The word means "leading children" and is off-register for adult enterprise learners. Use *adult learning*, *andragogy*, *instructional approach*, or *learning effectiveness*. (Banned in all artifacts AND conversation.)

## When to invoke

Invoke during:

- Lab design — when shaping a new lab, before drafting steps.
- Module / course design — when ordering labs, sequencing difficulty.
- Deck design — when an instructional deck has tasks, knowledge checks, or scaffolded build-up.
- Review — when checking a draft against the rubric for Learning Effectiveness.

Skip on: marketing content, customer-facing decks (a separate concern), and reference docs not meant to teach.

## Posture

Three rules of taste behind the checks:

1. **Productive struggle, not avoidable friction.** Effort that builds schema is the goal; effort spent fighting the tool, the doc, or the format is not.
2. **The learner is competent and time-constrained.** Adult professional learners have shipped software. They have not shipped *this* software. Calibrate to that.
3. **Reveal the seams.** Where the underlying product has friction — async sync, hidden defaults, order-sensitive operations — name it. Hiding friction is patronizing and produces brittle learners.

## Check classification

**Static checks** — a small set of presence checks that are binary and don't require interpretation:
- Verifier sentence: does each task contain "You'll know this worked when…" (or equivalent observable success condition)?
- Wrap-up transfer patterns: does the Wrap-up section contain named patterns in bold (not just a recap of steps)?
- Scenario/persona presence: does the artifact open with a named persona, system, and desired outcome rather than a concept definition?
- Time estimate presence: is there a numeric time estimate, and is it marked as validated vs. provisional?
- Knowledge Check question format: do questions use open-ended or multi-select format? (binary check; question *quality* is reasoning)

**Reasoning checks** — all eleven principles. Learning effectiveness is fundamentally a judgment: whether cognitive load is calibrated for this audience at this tier, whether scaffolding fades appropriately, whether reflection questions require analysis/evaluation/creation rather than recall, whether transfer patterns are genuinely transferable. The surface-specific operational thresholds (max words/slide, max steps/task) live in the surface compositions and `complete-check`, not here — this pillar carries the judgment layer.

## How to apply

Walk the principles below in order. For each, check the artifact against the principle and the heuristic. Note misses; suggest the move.

## The principles

### 1. Problem-first, not topic-first

Open with a scenario, not a concept overview. The scenario is the answer to the unspoken *"why am I doing this?"*. Tasks then serve the scenario.

**Heuristic:** if the first section is a concept definition, you've topic-led. If the first section names a company, a persona, a system, and a desired outcome, you've problem-led.

**Tactical move — Working Backwards.** Amazon's Working Backwards technique applied to training content: write what the audience will say about the artifact *after* delivery (a press release with 2–4 named-persona quotes naming concrete outcomes), then build the artifact to deliver those quotes. The Working Backwards press release is the strongest *problem-first* device available — it forces outcome thinking before topic thinking. Used in `wow-plan` Phase 2 and `stick-check` §7.1.

**Source:** Knowles' andragogy — adults need to know *why* before *how*.

### 2. Just-in-time concept introduction

Introduce a new concept in the task that needs it, not in a preamble. The learner gets the definition right when they have a use for it.

**Heuristic:** if a concept appears in an overview and isn't referenced again for ten minutes, move it to the task that uses it. The overview gets shorter; the task gets one earned sentence of intent.

**Source:** Cognitive Load Theory (Sweller) — extraneous load is highest when working memory has to hold a concept with no live use for it.

### 3. Respect prior knowledge

Use prerequisites to gate, not to re-teach. State the assumption and move on.

**Heuristic:** if prerequisites name "Familiarity with X" and the document then re-explains X in the body, one of the two is wrong. Pick: tighten the prerequisite, or drop the re-explanation.

**Source:** Knowles' andragogy — adult learners draw on prior experience.

### 4. Tasks have observable success criteria

Every task ends with a verifier — a single observable signal that says "this task is complete." The learner self-checks; never trust-me-I-did-it-right.

**Heuristic:** if a task ends without a verifier, or with a verifier that requires the author to check the learner's work, the task is incomplete. State observable behavior the learner can see: "the recipe saves with no validation errors", "a new row appears in the destination table".

**Single condition.** If a verifier needs "and" to join two conditions, the task probably wants to split.

### 5. Reveal the seams

Name friction up front when relevant. Async sync, hidden defaults, order-sensitive operations, gotchas the product introduces. Don't hide them.

**Heuristic:** if a step says "wait a moment" with no explanation, you've hidden a seam. State the actual reason (async, eventually-consistent, rate-limit, cache TTL) and the actual wait shape (seconds, minutes, until-event).

**Why:** hiding friction produces learners who panic when the same friction shows up in production.

### 6. Reflection before transfer

Place reflection between the work and the wrap-up. Reflection questions are open-ended — *why*, *when*, *what goes wrong if* — not factual recall. Bloom: analyze / evaluate / create, not remember / understand.

**Heuristic:** if a knowledge check is multiple-choice with one correct answer the document just stated, you've written a recall question. Re-cast as: *"A teammate suggests X instead — what goes wrong in production?"* or *"Why is this verifier observable rather than internal-state?"*

**Source:** Desirable Difficulties (Bjork) — retrieval practice + spaced retrieval improve transfer.

### 7. Transfer patterns in the wrap-up

The closing names 2–4 named transferable patterns, not a recap of what was done. The patterns are what should survive into later work. Name each pattern in bold; one short paragraph of explanation each.

**Heuristic:** if the wrap-up reads as "you did X, then Y, then Z," it's a recap and the learner will forget it. Re-cast as: *"You wrapped a flaky action in a Monitor block, routed errors with context, and proved the error path runs. Three patterns to carry forward: **Catch then decide.** ... **Errors need addressable context.** ... **Run the failure path on purpose.** ..."*

### 8. Scaffolding then independence

Difficulty scaffolding fades as competence grows.

| Tier | Shape |
|---|---|
| Foundational | Heavy intent, full config table, click-by-click steps, screenshot per UI action, verifier |
| Intermediate | Same structure, denser steps, fewer screenshots, more inference required |
| Advanced | Outcome description and verifier only; the learner builds the steps from the description |

**Heuristic:** if a foundational lab has steps without screenshots, scaffolding is too light. If an advanced lab has click-by-click for routine actions, scaffolding is too heavy.

**Source:** Vygotsky's Zone of Proximal Development — challenge slightly above current ability, with scaffolding that fades.

### 9. Realistic timing

Time estimates reflect what a competent learner actually takes, not the theoretical minimum. Over-estimate by 10 minutes rather than under-estimate by 30.

**Heuristic:** if a time estimate has never been validated against a real run-through, mark it provisional. Trial-run-derived estimates always beat author guesses.

**Why:** under-estimated time produces rushed learners and false confidence; over-estimated time is forgiven the first time a learner finishes early.

### 10. One artifact per task

Each task produces one observable thing — a renamed object, a connected resource, a configured branch, a knowledge base. Don't bundle two artifacts into one task.

**Heuristic:** if a verifier needs to name two observable end states, you have two tasks. Split.

**Source:** Cognitive Load Theory (Sweller) + Miller's Rule (7±2) — one outcome at a time keeps working memory free for the *why*.

### 11. Misconception handling has its own assessment shape

When content is designed to replace a known misconception — the learner arrives with a wrong mental model — the assessment for that content must test whether the model changed, not just whether the correct version can be stated.

**Heuristic:** if the only check for "did the misconception get corrected" is the learner reading the correct version in the content, you haven't assessed the change. The misconception must appear in the assessment — as a plausible wrong answer in a multiple-choice question, as a scenario where it would lead the learner astray, or as a discrimination task asking the learner to distinguish the right model from the wrong one.

**Why:** stating the correct understanding is recognition; selecting the correct understanding over a plausible wrong one is retrieval. Retrieval-with-distractor is what consolidates the model change. Without it, the learner may pass the lesson and still hold the misconception.

**Practical handle:** when a piece of content addresses a misconception, name the misconception explicitly in the content's design notes, place it as a distractor in the matching Knowledge Check (per `complete-check §1.4` distractor quality), and verify the distractor is plausible enough that a learner still holding the misconception would pick it.

**Source:** Bjork's Desirable Difficulties — retrieval practice consolidates more than recognition; the most desirable difficulty is one where the wrong answer is psychologically available at retrieval time.

## The theory base (when you need to cite the rubric)

| Principle | Frame | Source |
|---|---|---|
| Andragogy | Adult learners are self-directed, problem-centered, draw on prior experience, need to know *why* before *how* | Knowles |
| Cognitive Load Theory | Working memory is finite; preserve intrinsic load, remove extraneous load, maximize germane load | Sweller |
| Zone of Proximal Development | Challenge slightly above current ability, with scaffolding that fades as competence grows | Vygotsky |
| Desirable Difficulties | Productive struggle improves retention; retrieval practice + spaced retrieval improve transfer | Bjork |
| Miller's Rule (7±2) | Working memory holds roughly 7 chunks; group, chunk, cap | Miller |
| Multimedia Learning | Paired words + visuals beat words alone for procedural content | Mayer |

Use the names when stating design rationale; never call this "pedagogy."

## Surface-specific operational thresholds

Lab guides, slide decks, and exercises each carry **surface-specific** operational thresholds derived from these principles (max steps per task, max words per slide, max questions per knowledge check, etc.). Those live in the surface composition (`Lab Guide Standards.md`, `Presentation Content Standards.md`), not here. This skill carries the pillar-level principles that apply across surfaces.

## What this skill is NOT

- Not a content reviewer — leave editorial accuracy to `fact-check`.
- Not a sticky-prose check — that's `stick-check`.
- Not a style pass — that's `say-it-plain` (prose) + `team-style-guide` (surface formatting).
- Not a completeness check — that's `complete-check` (family).
- Not authoritative on Workato product behavior — those rules live in `fact-check` and the team-curated Workato sources of truth.
\
"""

PRESENCE_CHECKS_TRAINING = [
    {
        "pattern": r"\d+\s*minutes?\s*\((validated|provisional)\)",
        "message": "Missing time estimate — add '<N> minutes (validated)' or '<N> minutes (provisional)'",
    },
    {
        "pattern": r"you.ll know this worked when|you will know this worked when",
        "message": "Missing verifier: 'You'll know this worked when…' — add observable success condition per task",
    },
]

PRESENCE_CHECKS_EDUCATION = [
    {
        "pattern": r"\d+\s*minutes?\s*\((validated|provisional)\)",
        "message": "Missing time estimate — add '<N> minutes (validated)' or '<N> minutes (provisional)'",
    },
]


def _rules(audience):
    if audience == "workato":
        return {
            "applicable": False,
            "note": "calibrate-challenge applies to training and education content only",
            "banned_phrases": [],
            "regex_patterns": [],
        }

    presence = (
        PRESENCE_CHECKS_TRAINING if audience == "training"
        else PRESENCE_CHECKS_EDUCATION
    )

    return {
        "applicable": True,
        "banned_phrases": [],
        "regex_patterns": [],
        "presence_checks": presence,
    }


def main(input):
    audience = input.get("audience", "workato")
    return {
        "rubric": RUBRIC,
        "rules": _rules(audience),
    }
