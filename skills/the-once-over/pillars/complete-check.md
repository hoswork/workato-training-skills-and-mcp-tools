---
name: complete-check
description: Use when shipping or reviewing a training artifact — lab guide, slide deck, course bundle, course plan, Knowledge Check, course abstract — to verify every required element is present and in the right place. Mechanical presence checks; per-artifact checklists. Frame the pillar of Completeness under The Standards Desk.
---

# Complete Check

A pass that runs the **mechanical presence-check** on a training artifact. Every required element accounted for; every required element in the right slot. Yes/no checks, no judgment calls.

Source: the per-artifact required-element rules from `Lab Guide Standards §5.5` and `Presentation Content Standards §3`. This skill is the human-facing version; a companion `html-lab-rules.yaml` is the machine-facing version. They are kept in sync.

## When to invoke

Invoke as the **last pass before publishing** any training artifact:

- Lab guide ready to ship to Gutenberg or to a customer.
- Slide deck ready to deliver.
- Course bundle ready to load into Docebo / WoW.
- Course plan ready to hand to a deck author or another planner.
- Knowledge Check assembled and ready to drop into a Kahoot or LMS.
- Course abstract ready to publish to a course catalog.

Run *after* the judgment-pillar passes (calibrate-challenge, stick-check, say-it-plain) — completeness is mechanical, so it's the final gate. Running it first wastes time on artifacts that fail upstream pillars anyway.

## Posture

Three rules of taste behind the checks:

1. **Mechanical, not judgment.** If a check requires a human to decide "is this good enough?", it doesn't belong here — that's a different pillar. Completeness asks only *is the element present, in the right slot, of the right shape?*
2. **Per-artifact.** A lab guide's required elements differ from a slide deck's; a course plan's differ from a Knowledge Check's. Each artifact type gets its own checklist. Don't apply lab-guide rules to slides.
3. **Reject on first missing element.** A lab guide with no Scenario section isn't *almost done* — it's not done. The completeness check is a binary gate, not a quality scale.

## Check classification

**Static checks** — the vast majority of this pillar. Every §1.x checklist item is binary: the element is present or it isn't. Run the entire §1 against the artifact mechanically:
- §1.1 Lab guide: all 9 top-level section checks, all per-Task subsection checks, the `stats[]` ban, the one-attention-grabber budget, all mechanical structural rules
- §1.2 Slide deck: all required slide checks, engagement cadence count, deck length, per-slide density limits, speaker notes format presence, all mechanical structural rules
- §1.3 Course plan: all frontmatter field presence checks, abstract word count (≤150), outline structural elements presence
- §1.4 Knowledge Check: question count (3–6), format check, distractor count and structural rules (no "all of the above", no negative phrasing)
- §1.5 Course bundle: all artifact presence checks
- §1.6 Bug report: all four subsection presence checks (IMPACT, DIAGNOSED CAUSE, ERROR, SCOPE), Steps to Reproduce structure, Severity presence

**Reasoning checks** — a small set that can't be determined by presence alone:
- Knowledge Check quality: is the question retrieval practice (analyze/evaluate/create) or just recall? A question can be present and correctly formatted but still be a softball recap. This requires reading the question and judging its Bloom's level.
- Distractor plausibility: are distractors real misconceptions or fabricated filler? Requires knowing the domain.
- Course plan abstract quality: "names 2–4 concrete outcomes" requires judging whether the outcomes are genuinely concrete (specific, actionable) or vague ("understand agentic patterns").
- Bug report speculation check: does DIAGNOSED CAUSE stay within confirmed observations? Requires reading for hedged language and inference.

## How to apply

1. **Identify the artifact type.** (Lab guide, slide deck, course plan, Knowledge Check, course abstract, course bundle.)
2. **Load the artifact's checklist** from §1 below.
3. **Walk every item.** Yes/no. No partial credit.
4. **Report failures by name.** Don't paraphrase — name the missing element so the author can find it quickly.
5. **If everything passes, ship.** Completeness is a gate, not a score; passing is the goal, not optimizing it.

## §1. Per-artifact checklists

### 1.1 Lab guide

Source: `Lab Guide Standards §5.5` (v2).

**Top-level sections (7, in order):**

- [ ] `## Exercise Goals` — learning objectives + business context
- [ ] `## Prerequisites` — accounts, prior labs, prior knowledge
- [ ] `## Time estimate` — single integer minutes, real-run-validated
- [ ] `## Scenario` — adult-relevant context (company, persona, system, success criterion)
- [ ] `## Exercise Steps` — contains the Tasks
- [ ] `## Reflect` — at least one retrieval-practice question (v2 rename from `Knowledge Check`; v1 labs may still use the old heading)
- [ ] `## Wrap-up` — 2–4 named transferable patterns in bold

**Per-Task subsections (v2 task body shape):**

- [ ] `#### Hook` — 2–3 sentences, 30–50 words, business-grounded
- [ ] `#### Walkthrough` — outcome-oriented prose, ≤60 words, names ≥1 specific artifact or configuration value
- [ ] `#### Aside` (optional, max 1/Task) — first non-blank line is `Type · Title`; types are Pattern / Watch out / Compare / Background / No dumb questions
- [ ] `#### Intent` — 2–4 sentences inside the Detailed steps disclosure
- [ ] `#### Config` (when applicable) — key/value table visible by default
- [ ] `#### Diagram` (when applicable) — placeholder + caption
- [ ] `#### Steps` — N.M.S numbered, inside Detailed steps disclosure
- [ ] `#### Verifier` — opens with "You'll know this worked when…"; one observable success condition
- [ ] `#### Takeaway` — one sentence; the transfer pattern from this Task

**Banned frontmatter:**

- [ ] `stats[]` is **not present** (schema-level enforcement of `say-it-plain` §1.1 pitch-deck stat-grid ban; `Lab Guide Standards §0 OVR-LG-008`)

**One-attention-grabber budget:**

- [ ] Each Task carries at most one of {Heads-up callout (`▲`), `#### Aside`} — never both

**Mechanical structural rules:**

- [ ] Step list inside Detailed steps disclosure is `<ul class="steps">`, never `<ol>`
- [ ] Each step's `N.M.S` number written into `<li>` text (e.g., `2.3.1`)
- [ ] Every step ends with `.`, `?`, `!`, `:`, `;`, or `…`
- [ ] Headings (h1, h2, h3) never end in terminal punctuation
- [ ] Headings deeper than h3 are not used
- [ ] All images have alt text
- [ ] Callouts use one of five operational classes: `note`, `tip`, `warning`, `pitfall`, `key-insight`
- [ ] Code blocks declare their language

### 1.2 Slide deck

Source: `Presentation Content Standards §3` (required slides), §5 (content density), §11 (style).

**Required slides:**

- [ ] **Title slide** — deck title, subtitle, presenter
- [ ] **Learning objectives slide** — early in the deck, what the audience will be able to do
- [ ] **Summary slide** — at the end, reinforces key takeaways

**Engagement cadence:**

- [ ] Question or activity slide at least every 10 slides

**Deck length:**

- [ ] ≤40 slides per deck (soft ceiling — longer decks split into modules)

**Per-slide density (every slide):**

- [ ] ≤120 words per slide (50 on split-layout slides)
- [ ] ≤6 bullets per slide
- [ ] ≤25 words per bullet
- [ ] ≤2 levels of nested bullets
- [ ] No blank slides
- [ ] No dangling single-word widows

**Speaker notes:**

- [ ] Every content slide has speaker notes in `KEY POINT + TALK TRACK` format

**Mechanical structural rules:**

- [ ] Every slide uses a named layout (no ad-hoc layouts)
- [ ] All images have alt text
- [ ] Slide numbers present on all non-title slides
- [ ] Workato logo on all non-title slides (bottom-left)
- [ ] No `stats[]`-style stat-grid components (form-level hype ban; see `Presentation Content Standards §13.0.1`)

**Per-slide content shape:**

- [ ] **Each slide has a clear headline** — a title that names the takeaway, not a topic label. *"Genies fail silently in async sync"* beats *"Async Sync Failure Modes."*
- [ ] **One concept per slide** — heuristic: if the slide has ≥2 distinct headings (h2 + h3) introducing separate concepts, it's two slides hiding as one.
- [ ] **No redundant slide title** — title doesn't restate verbatim what the body already says. Title and body do different jobs.
- [ ] **Speaker notes don't duplicate body** — notes carry the *talk track* (what the presenter says aloud that isn't on the slide), not a restatement of the bullets.
- [ ] **No solo-bullet lists** — a "list" of one bullet is not a list; rewrite as a sentence.

### 1.3 Course plan

Source: `wow-plan` skill output requirements.

A course plan is a markdown document that an author or planner produces *before* lab and deck authoring begins. Two consumer artifacts: the **Abstract** (short marketing blurb) and the **Detailed outline** (modules → labs/sessions → objectives → time allocations).

**Course plan frontmatter (YAML):**

- [ ] `title` — course title (sentence case for the markdown form)
- [ ] `audience` — object with `role`, `level` (beginner/intermediate/advanced), `size`, `context`
- [ ] `duration` — total minutes (e.g., 480 for a 1-day course)
- [ ] `delivery_mode` — in-person / virtual / async
- [ ] `tier` — Foundational / Intermediate / Advanced (Workato calibration; see `Lab Guide Standards §3` and `calibrate-challenge` Principle 8)
- [ ] `learning_objectives` — 3–6 verb-led, measurable
- [ ] `prerequisites` — concrete, gating not teaching
- [ ] `delivery_date` — target (or `TBD` with rationale)

**Course Abstract (the marketing blurb):**

- [ ] Names a target audience (specific role + level, not "anyone")
- [ ] Names the duration (e.g., "1-day", "half-day")
- [ ] Names 2–4 concrete outcomes the learner walks away with
- [ ] States the prerequisite expectation (e.g., "Assumes 101-level fluency")
- [ ] ≤150 words
- [ ] Passes `say-it-plain` (form + word levels)

**Course Detailed outline (the structured plan):**

- [ ] **Overarching scenario or narrative arc** — names the persona/world/problem the course unfolds in (per `stick-check` Concrete + Stories)
- [ ] **Modules** — each with a name, time allocation (minutes), learning objectives (verb-led), and 1–N lab/session sketches
- [ ] **Lab/session sketches** — each follows the `Agent Studio 201 for WoW` candidate-activity shape: **Premise** · **Lab shape (sketch)** · **Why this works** · **Open questions**
- [ ] **Total time allocation** — sums of module times match the course duration (±10%)
- [ ] **Scaffolding fade across modules** — early modules click-by-click, later modules outcome-driven (per `calibrate-challenge` Principle 8)
- [ ] **Knowledge Check anchors** — at least one Knowledge Check per module; total Knowledge Checks ≥3 per 1-day course
- [ ] **Open questions** section — what's unresolved; what needs research before lab authoring starts

### 1.4 Knowledge Check

A Knowledge Check is a retrieval-practice artifact: a small set of open-ended or multi-select questions, typically delivered through Kahoot or an LMS quiz feature. (Always written full as "Knowledge Check" — never "KC" — per [[feedback_knowledge_checks_naming]].)

- [ ] **3–6 questions** total (more becomes a test, not a Knowledge Check)
- [ ] **Open-ended or multi-select format** — avoid binary yes/no
- [ ] **Bloom's analyze / evaluate / create** — *why*, *when*, *what goes wrong if* — not *what is*
- [ ] **Each question has a correct-answer rationale** — for the author / LMS configuration, not learner-visible
- [ ] **No softball recap questions** — questions that just restate something the lab said
- [ ] **No trick questions** — ambiguity hurts retention measurement
- [ ] **Each question references its source lab/module** — for spaced retrieval design

#### Distractor quality (for multiple-choice or multi-select formats)

When the Knowledge Check uses multiple-choice or multi-select questions, every distractor must hold up to these checks. Source: ADDIE pipeline distractor rubric (Workato Academy ETT, May 2026).

- [ ] **Each distractor reflects a real wrong answer** — a documented misconception, an observed failure mode, or a plausible mistake a learner who hasn't mastered the LO would make. Fabricated distractors fail. ("Delete all data and start over" is not a distractor; it's filler.)
- [ ] **Distractors don't reinforce a different misconception on the way to being wrong.** A distractor using inaccurate framing (wrong product term, wrong mechanism) teaches the wrong model even when the learner picks a different answer. Every option must be accurate on its own terms.
- [ ] **Option text doesn't telegraph the answer.** Don't drop product definitions next to product names when the stem already implies the answer. Keep options terse; teach in the feedback.
- [ ] **Distractors are similar in length and detail to the correct answer.** Length asymmetry signals the right answer to test-takers (not to learners).
- [ ] **No "all of the above" or "none of the above" options.** They reward test-savvy over content mastery.
- [ ] **No negative-phrasing stems** (*"Which of the following is NOT..."*) — reads differently under time pressure than the rest of the question set.
- [ ] **Calibrated to ≥80% first-attempt correct on gated Knowledge Checks.** Distractors should be plausible to someone who hasn't mastered the LO; the correct answer should be clearly right to someone who has. Trick questions, ambiguous-correct answers, and technically-defensible alternatives to the right answer all fail this check.

### 1.5 Course bundle (Docebo / WoW package)

A course bundle is the deployable artifact — what gets uploaded to Docebo or staged in a WoW workspace.

- [ ] **All labs from the course plan are present** — each as bundled HTML or Workato-package fixture
- [ ] **All slide decks from the course plan are present** — each as `.pptx` or rendered format
- [ ] **All Knowledge Checks staged** — Kahoot URL or LMS quiz ID per Knowledge Check in the plan
- [ ] **All seed Workato assets** — recipes, connections, Genies, knowledge bases (RLCM packages where applicable)
- [ ] **Trainer notes / facilitator guide** present per module
- [ ] **Time-budget reconciliation** — actual bundle time-of-delivery within ±10% of course plan duration
- [ ] **Verified-on date** — bundle verified against current Workato product surface (see `fact-check`)

### 1.6 Bug report (generic)

A bug report submitted to any bug-tracking system (Jira, GitHub Issues, Linear, internal incident docs). For Workato CCE filings specifically, the workflow skill `file-workato-product-bug` composes this checklist with Workato-specific form-field rules. The register rules (matter-of-fact posture, no speculation, no teaching) live in `say-it-plain` §3.

**Bug Description has four labeled subsections, in order:**

- [ ] **IMPACT** — present and named first
- [ ] **DIAGNOSED CAUSE** — present, ≤3 sentences total (cause + mechanism)
- [ ] **ERROR** — present
- [ ] **SCOPE** — present

**IMPACT content:**

- [ ] Names the affected component **by name** (tool name, endpoint, recipe ID) — no *"a tool"* / *"the system"* generics
- [ ] Uses first person for reporter observations (*"in my logs"*) — not *"one user's"*
- [ ] Makes involuntariness explicit if the user is affected without taking action
- [ ] Includes a one-line in-the-wild impact observation if available (session counts, customer counts, etc.)

**DIAGNOSED CAUSE content:**

- [ ] States the cause in 1 sentence
- [ ] States the mechanism by which the cause produces the observed impact in 1–2 sentences (no more)
- [ ] Reuses the load-bearing word from IMPACT (e.g., *"poisons"* / *"poisoned"*) consistently
- [ ] Contains no speculation beyond what was diagnosed (no *"probable,"* *"likely,"* *"common causes include"*)

**ERROR content:**

- [ ] Quotes the *literal* error string from the API/runtime/system
- [ ] Does not paraphrase

**SCOPE content:**

- [ ] States a numeric ratio of affected surface (e.g., *"1 of 214 tools"*, *"3 of 50 customers"*)

**Steps to Reproduce:**

- [ ] Two paths present, in order: (A) observable from a user-facing client (for triage / first-line investigation), (B) direct at the layer engineering fixes (for product engineering)
- [ ] Each step is copy-pasteable and unambiguous
- [ ] Each path names its audience explicitly (*"For CCE..."* / *"For engineering..."* or equivalent)

**Severity:**

- [ ] Calibrated by blast radius (session-wide, single-call, customer-blocking), not by frequency
- [ ] Not left at the form's default unless the default genuinely matches the bug

**Speculation / teaching ban (cross-check with `say-it-plain` §3):**

- [ ] No *"probable backing endpoint"* / *"likely cause"* in fact-claiming positions
- [ ] No *"where to look"* / *"common causes include"* / *"things to check"* guesses anywhere in the report
- [ ] No mechanism-walk paragraphs beyond the 1–2-sentence DIAGNOSED CAUSE mechanism
- [ ] No platform-overview / *"how it normally works"* preambles

## §2. Pre-flight failures (common patterns)

Before walking the per-artifact checklist, these patterns are usually present and worth surfacing first:

- **Missing Hook on a Task** (lab guide v2) — the Hook is the load-bearing addition in v2; missing it is the most common v1→v2 migration miss.
- **Missing Walkthrough on a Task** (lab guide v2) — same as Hook; load-bearing v2 addition.
- **Verifier doesn't open with "You'll know this worked when…"** — most common single failure across all task bodies.
- **`stats[]` in frontmatter** — schema-level ban; reject the bundle.
- **Knowledge Check is recall, not retrieval** — *"What is a Monitor block?"* fails the check; *"A teammate suggests catching the error silently — what goes wrong?"* passes.
- **Course plan abstract has no concrete outcomes** — *"You'll learn agentic patterns"* fails; *"You'll build a working Genie, wire it to Slack, and run an eval dataset against it"* passes.

## Integration with other pillars

- **All other pillars run first.** Completeness is the mechanical end-gate. If an artifact fails calibrate-challenge or stick-check or say-it-plain, fix those first; complete-check after.
- **Style — surface (`team-style-guide`).** Some completeness items (alt text, callout class names, frontmatter shape) overlap with surface-style rules. The two skills are siblings; either can run them, but complete-check is canonical for "is it present?" while team-style-guide is canonical for "is it the right format?".
- **Operationalization in `html-lab-rules.yaml`.** The lab guide checklist (§1.1) is mirrored as machine-readable rules in a companion `html-lab-rules.yaml` file. The two are kept in sync; the YAML is what Lab Buddy / DoubleChecker / Ghost (Bakery profile) reads at runtime.

## What this skill is NOT

- Not a quality assessor — completeness is binary, not graded. Quality lives in calibrate-challenge / stick-check / say-it-plain.
- Not a substitute for the judgment pillars — running complete-check on an artifact that fails the judgment pillars produces a "complete bad artifact."
- Not authoritative on per-artifact format details — those live in surface compositions (`Lab Guide Standards`, `Presentation Content Standards`) and in `team-style-guide`.
- Not a Workato-fact-checker — that's `fact-check`. Complete-check verifies *presence*; fact-check verifies *correctness against the product surface*.
