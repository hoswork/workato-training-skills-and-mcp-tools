"""
stick-check — snippet 1 (rules + rubric).
Universal — applies to all audiences.
Static checks are minimal (presence only); SUCCESs evaluation is LLM reasoning.
"""

RUBRIC = ""
---
name: stick-check
description: Use when designing or reviewing training content, course materials, hooks, takeaways, scenarios, openings/closings — anything that needs to *land and stay landed* in the audience's memory. Applies the Heath brothers' SUCCESs framework (Simple, Unexpected, Concrete, Credible, Emotional, Stories). Frame the pillar of Stickiness under The Standards Desk.
---

# Stick Check

A pass that checks whether content is *memorable by design*, not by accident. Designs hooks, scenarios, takeaways, and key moments to survive the trip from page to long-term recall.

Source: Chip & Dan Heath, *Made to Stick* (2007). The book studied why some ideas survive (urban legends, proverbs, conspiracy theories) and why most well-intentioned communications fade. The pattern reduces to six properties, captured as the **SUCCESs** mnemonic.

## When to invoke

Invoke during:

- **Course / module / lab design** — when shaping hooks, scenarios, opening framing, key takeaways, closing summaries.
- **Slide deck design** — for the slides that have to land: opening, takeaway slides, section dividers, the summary slide.
- **Customer-facing content** — case studies, success stories, launch announcements, demo scripts.
- **Internal communications that must travel** — leadership messages, big-decision recaps, framing for cross-team launches.
- **Marketing-adjacent content** *with caution* — Made to Stick is descriptively powerful but its applied use in marketing slides into manipulation. Apply with the say-it-plain pass (which catches hype) layered on top.

Skip on: reference docs (sticky reference is overrated), procedural step-by-step (Steps need clarity, not stickiness — that's `calibrate-challenge` territory), code comments.

## Posture

Three rules of taste behind the checks:

1. **Memorable, not manipulative.** SUCCESs describes *why* ideas survive. Use it to help the right idea survive. Don't use it to make a bad idea harder to forget.
2. **One sticky moment per piece, max two.** Stickiness is expensive — concentration of cognitive resources. If everything is unexpected, nothing is. Pick the moment that has to land.
3. **The Curse of Knowledge is the enemy.** The author knows the punchline; the audience doesn't. SUCCESs is largely a set of moves to defeat the Curse of Knowledge — to put the audience in a state where the punchline can land.

## Check classification

**Static checks** — minimal:
- Presence of a named memorability element per module/section (is one of the §7.2 element types tagged or identified?)
- Presence of a Working Backwards press release when the artifact is a course plan (§7.1)

Everything else is reasoning. You cannot determine whether an opening creates a genuine curiosity gap, whether an analogy carries information rather than decoration, or whether a story is load-bearing — from a word count or a regex.

**Reasoning checks** — all six SUCCESs dimensions and all §7 tactical moves. Apply by reading the artifact and judging whether each property is present, designed-in, and true to the material and audience.

## How to apply

For each piece of content (hook, takeaway, scenario, opening, closing), walk the six checks in order. They're roughly ordered cheapest-first (Simple is structural; Stories is generative). For most short content (a takeaway, a hook), only 2–3 of the six apply meaningfully.

## The six checks (SUCCESs)

### 1. Simple

**Strip to the core.** What's the single most important thing? If the audience remembers one sentence, what should that sentence be?

**Heuristic:** if you can't say it in one sentence, the audience won't remember it in one sentence either. Most "core ideas" need 2–3 stripping passes before they're actually simple.

**Anti-pattern:** *forcing simplicity by dropping detail*. A simple idea is the *most important* idea, fully articulated. Brevity ≠ simplicity. A short sentence that hides an oversimplification (or a slogan that papers over a real choice) fails the check.

**Apply to:** Course-level promises. Module openings. Slide titles. Key takeaway sentences.

**Quick test:** the audience says back the core idea in their own words. If they can, it's simple. If they say back a longer version with the original's structure, it isn't.

### 2. Unexpected

**Open with a gap.** Curiosity comes from the gap between what someone knows and what they realize they don't know. Open the gap; don't close it for them prematurely.

**Patterns that work:**

- **Counterintuitive opening.** *"Folders aren't the isolation boundary — projects are."* Forces the audience to recalibrate before continuing.
- **Mystery.** *"This Genie returned the right answer 95% of the time in testing and 30% in production. Why?"* Sets up a knowledge gap.
- **Pattern violation.** Three normal examples, then one that doesn't fit. The break holds attention.

**Anti-pattern:** *unexpectedness via novelty*. New ≠ unexpected. A novel feature isn't surprising; what makes it *useful* might be.

**Avoid:** manufactured surprise. The audience knows when a "surprising" stat is staged for effect. See `say-it-plain` §1.5 (manufactured urgency) — same anti-pattern in stickiness clothing.

**Apply to:** Course openings. Module hooks. Scenarios that introduce a problem. The first slide.

### 3. Concrete

**Show, don't abstract.** Abstract concepts are hard to remember; concrete examples are hard to forget. Concrete = specific, sensory, named, dated.

**Concrete moves:**

- **Specific people, not roles.** *"Dana, an IT lead at Anitech, spends two hours a shift watching Salesforce."* Not *"A user spends time monitoring systems."*
- **Specific numbers in context.** *"95% to 30%"* is more concrete than *"a big drop."*
- **Named systems.** *"Salesforce, Jira, Slack"* is more concrete than *"the integration tools."*
- **Sensory anchors.** *"The chip is the data binding; the typed text is just a label."* The visual difference is concrete.

**Anti-pattern:** *concreteness via stats inflation*. See `say-it-plain` §1.1 (pitch-deck stat grids) — the form looks concrete but is shaped to impress, not inform. Real concreteness names specifics; fake concreteness shapes them.

**Apply to:** Every scenario. Every example. Every persona. Every analogy.

### 4. Credible

**Why should the audience believe this?** Credibility can come from authority, statistics-in-context, vivid detail, or *testable claims* (the audience can verify the claim themselves).

**Sources of credibility, ranked by power:**

1. **Testable** — *"You'll know this worked when the verifier fires."* The audience can check.
2. **Vivid detail** — a sufficiently specific anecdote feels true. *"At 3 AM, the on-call engineer's phone buzzed because the recipe failed silently."* Detail = credibility.
3. **Statistics in context** — *"30% production accuracy"* needs the comparison-point (*"versus 95% in testing"*) to land.
4. **Authority** — citing the product team, the docs, the source-of-truth. Use sparingly; over-reliance signals weakness in the substance.
5. **Anti-credibility** — superlatives, urgency, hype shapes. These trigger skepticism in technical audiences. See `say-it-plain`.

**Anti-pattern:** *credibility by stacked logos*. "Used by Fortune 500 companies" is the slide-deck form of borrowing authority. Replace with what's *actually* differentiating.

**Apply to:** Claims in the abstract. Stats anywhere. Promises about what the audience will learn.

### 5. Emotional

**What does the audience care about?** Ideas land when they connect to something the audience already cares about. The technical audience cares about: their own time, their own credibility, problems they've hit personally, work that won't be wasted.

**Emotional anchors that work for technical audiences:**

- **Self-interest.** *"This pattern saves you 2 hours every time a recipe fails silently."*
- **Identity.** *"This is what production-quality recipe authors do."*
- **Mastery.** *"Once you understand the prompting layers, you'll debug Genies in minutes instead of hours."* (Care with multipliers — see `say-it-plain` §2.1; use only when literally true.)
- **Curiosity.** From the Unexpected check — the open gap creates a small emotional pull to close it.

**Avoid:**

- **Manufactured urgency.** *"If you don't learn this, you'll fall behind."* See `say-it-plain` §1.5. Technical audiences detect this instantly.
- **Self-deprecation as connection.** *"I used to make this mistake too."* Sometimes lands; often reads as performative.
- **Pep-rally enthusiasm.** *"You're going to LOVE this."* Cuts trust.

**Apply to:** Course abstracts (why should they sign up?). Module openings (why this module?). Closing summaries (what did they gain?).

### 6. Stories

**Wrap the idea in a story.** Stories are how the human brain stores procedural and emotional information together. A teaching point delivered as a story will outlast the same point delivered as a list.

**The three story types that work for training content:**

- **Challenge plot** — protagonist faces an obstacle, overcomes it via something we're about to teach. *"Dana was paged at 3 AM because the recipe failed silently. By the end of this module, you'll have wired the Monitor block that would have caught that failure."*
- **Connection plot** — bridge between two unrelated-seeming things. *"What does a router recipe and an agentic Genie have in common? Both are decision-making patterns that need observability."*
- **Creativity plot** — protagonist solves a problem in an unexpected way. *"The team tried six retry strategies before they realized the issue wasn't the recipe — it was the source system's eventual consistency."*

**Anti-pattern:** *story as decoration*. A story tacked on at the start of a module that has nothing to do with the content. The audience tunes out.

**Apply to:** Course-level scenarios. Module-level openings. Case studies. Customer success stories. Closing recaps.

## §7. Tactical moves (concrete patterns that activate the framework)

The six checks above are the *framework*. Tactical moves are the *menu* — concrete, named patterns an author can pick up and apply. Each maps to one or more SUCCESs checks. Backpropped from slides-harness 2026-05-27 (`specs/done/014-memorability-elements`, `specs/done/015-fake-press-release`, `specs/done/017-narrative-structure-library`).

### 7.1 Working Backwards (write the outcome first)

The Amazon Working Backwards technique applied to training content: **write what the audience will say about the artifact *after* delivery, before you build the artifact itself.**

- For a course → a press release with 2–4 audience-quote outcomes (named persona + concrete outcome).
- For a lab → the Wrap-up section drafted before the Tasks. *"The learner walked away with a recipe that retries failed case writes and posts unrecoverable ones to triage."*
- For a deck → the Summary slide drafted before the body slides.

**Why it works:** Working Backwards forces *outcome thinking* rather than *topic thinking*. The natural failure mode of training content is *"here's what I want to talk about"*; Working Backwards reframes as *"here's what they'll be able to do"*. The outcome quotes become the quality bar — if any module/section/slide doesn't make a quote come true, cut it.

**Activates:** §1 Simple (the outcome is the core idea), §3 Concrete (named persona + specific outcome), §5 Emotional (the outcome resonates with audience self-interest), §6 Stories (challenge-plot frame implicit).

**Anti-pattern:** *generic audience quotes*. *"Loved the session, very informative!"* fails the test. Real Working Backwards quotes are specific enough that a reader would say *"this could only be from someone who did this course."*

**Used by:** `wow-plan` Phase 2 (the press release IS the deliverable for that phase).

### 7.2 Memorability elements catalog

Six typed element types an author can place in any teaching artifact. **One or two per module/section, not more** (per Posture rule 2 — stickiness is expensive).

| Element | When to use | Example |
|---|---|---|
| **Mnemonic** | When introducing a 3–5 item framework that learners must recall later | *"The 3 R's of recipe debugging: Read the error → Reproduce the trigger → Repair the step"* |
| **Named framework** | When introducing an ordered set of principles or steps | *"The Four Layers of Prompting: Genie Prompt → Skill Prompt → Field Prompt → App Event Prompt"* |
| **Compare aside** | When the audience must choose between two approaches that look similar | *"LLM drafting is for prose a human reads; Transforms are for system-facing fields where format matters"* |
| **Themed humor / dad-joke** | Calibrated humor that anchors a memorable break | A recurring magician-character interlude; one earned pun per module |
| **Activity / poll** | Mid-section when attention is flagging or you want a calibration check | "Show of hands: who's seen a Genie hallucinate in production?" |
| **Themed break / recurring motif** | A long-form artifact (full course, multi-deck module) where a recurring visual or framing motif anchors transfer | A persona character (Dana, the IT lead) reappearing across modules |
| **Working analogy** | When the abstract concept needs an emotional/practical anchor — *as long as the analogy carries information* (not decorative metaphor) | *"A Workato project is the isolation boundary — like a Unix process. Folders organize within it — like the directory tree inside that process's working directory."* |

**Activates:** §1 (mnemonic / named framework forces Simple), §2 (themed humor / activity = Unexpected), §3 (named framework / working analogy = Concrete), §6 (themed break + recurring motif = Stories at the course level).

**Anti-pattern:** *element pile-up*. Two mnemonics and a poll and a dad-joke in one module produces sticky-feeling content that the learner retains nothing from — the moments compete instead of compound. Pick the one that has to land.

**Used by:** `wow-plan` Phase 5 (each module picks 1–2 memorability elements).

### 7.3 Narrative structures library

Seven starter narrative shapes for any teaching artifact. Pick one explicitly per artifact; the structure shapes the entire deliverable.

| Structure | When to use | Shape |
|---|---|---|
| **Product demo** | When introducing a product/feature to a familiar-with-the-domain audience | Hook → context → live build → result → next-steps |
| **Problem → solution** | When the audience already feels the pain (or is about to) | Felt pain → root cause → solution shape → demonstration → adoption path |
| **Quarterly / status review** | When reporting outcomes to stakeholders | Outcomes → key wins → blockers → next quarter |
| **Training intro** | Opening module of any course | Audience win (press release) → scenario → objectives → roadmap |
| **Training closing** | Closing module of any course | Recap of artifacts produced → named transfer patterns → what next |
| **Onboarding** | When the audience is new to the system | World tour → first hands-on success → next steps |
| **Working Backwards** | When the outcome is more important than the path | Outcome (press release) → why it matters → modules that deliver it |

**Activates:** §6 Stories directly; the chosen structure is the story shape.

**Anti-pattern:** *no chosen structure*. An artifact whose narrative defaults to "list of topics in some order" is the unmarked failure mode of training content. Always pick a structure explicitly.

**Used by:** `wow-plan` Phase 5 (the Scenario arc + module sequencing implicitly choose a structure; making it explicit improves transfer).

---

## Integration with other pillars

- **Style (`say-it-plain`)** — stick-check and say-it-plain pull in opposite directions sometimes. Stickiness wants vivid, emotional, story-rich; say-it-plain cuts hype. *The reconciliation:* concreteness, emotional connection, and story all work *without* hype shapes. A specific anecdote (Concrete + Stories) is sticky AND straight. Manufactured urgency (Emotional, badly applied) is sticky-feeling AND hype. When the two pillars conflict, the answer is almost always "rewrite the shape" (say-it-plain Edit move 4) — find the version that's sticky without being hypey.
- **Learning Effectiveness (`calibrate-challenge`)** — stickiness serves Learning Effectiveness. A sticky framing for *the wrong concept at the wrong difficulty level* is worse than no framing. Calibrate first; stick-check second.
- **Accuracy (`fact-check`)** — the most sticky framing must still be true. A vivid anecdote that's wrong undoes trust the moment someone checks.

## Surface-specific notes

**Lab guides (`Lab Guide Standards`):** labs carry Stickiness lightly — labs are doing-heavy, not narrative-heavy. The Scenario carries most of the stickiness load; the Wrap-up's named patterns carry the rest. Per-Task Hooks (`§11`) and Takeaways (`§15.2`) each get one sticky check at most.

**Slide decks (`Presentation Content Standards`):** Stickiness has more surface to work with. Opening slide (Unexpected), Scenario slide (Concrete + Stories), Key takeaway slides (Simple + Emotional), Closing slide (Stories). Each major slide carries one Stickiness check, not all six.

**Course-level planning (`wow-plan`):** course-level Hypothesis and What-good-looks-like sections carry Simple + Unexpected. The course Abstract carries Concrete + Emotional. Module hooks carry Stories.

## What this skill is NOT

- Not a marketing copy generator — stickiness applied without say-it-plain is manipulation.
- Not a substitute for substance — sticky ≠ valuable. A sticky bad idea is worse than a forgettable good one.
- Not for every paragraph — pick the moments that have to land. Most content does not.
- Not authoritative on the underlying framework — for the full SUCCESs reasoning + research backing, read *Made to Stick* directly.
\
"""

PRESENCE_CHECKS = [
    {
        "pattern": r"you.ll know this worked when|you will know this worked when",
        "message": "Missing verifier: 'You'll know this worked when…' — add observable success condition",
    },
]


def _rules(audience):
    # Verifier presence check only applies to lab/course content (training/education)
    # General Workato content doesn't require observable success conditions
    presence = PRESENCE_CHECKS if audience in ("training", "education") else []
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
