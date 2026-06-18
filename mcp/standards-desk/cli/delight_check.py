"""
delight-check — snippet 1 (rules + rubric).
Universal — applies to all audiences.
No static checks — all 7 delight principles require LLM reasoning.
The rubric is returned for client-side reasoning only.
"""

RUBRIC = ""
---
name: delight-check
description: Use when designing or reviewing training/enablement content (labs, decks, courses, exercises, games) to check that it's delightful — fun and personality designed into the core experience, not bolted on; play that makes exploration safe for skeptical experts; the one felt win that turns a skeptic curious. Frame the pillar of Delight under The Standards Desk. Delight is the amplifier on top of the useful floor that `calibrate-challenge` owns.
---

# Delight Check

A pass that checks whether enablement is *lovable*, not just *usable* — whether fun and personality are designed into the core experience, and whether the activity makes a skeptical expert feel safe enough to explore. Minimum *lovable*, not minimum viable.

> **Delight is the amplifier, not the floor.** `calibrate-challenge` owns the floor — accurate, scaffolded, transfer-ready learning. Delight is what sends a learner out *confident and curious* instead of merely correct. An amplifier with no floor is a gimmick a skilled audience sees through. Run `calibrate-challenge` first; this pillar assumes the floor holds.

## When to invoke

Invoke during:

- **Lab / exercise design** — when shaping the activity, before it hardens into a chore with steps.
- **Course / module design** — when deciding the scenario, the framing, the recurring motif, the closing moment.
- **Game or interactive design** — when the artifact is built around play (an LLM-as-judge game, a build-day challenge, a sandbox).
- **Review** — when an artifact is correct and effective but flat, and you want to know what would make a learner *enjoy* it.

Skip on: reference docs, bug reports, status updates — content that should be plain and quick, not delightful. Forcing delight onto these is the failure mode this pillar warns against (Principle 7).

## Posture

Three rules of taste behind the checks:

1. **Floor before amplifier.** Never decorate a lab that doesn't teach. If `calibrate-challenge` hasn't passed, fixing delight is premature — a fun chore is still a chore.
2. **Genuine play, not gamification.** Points, badges, and leaderboards bolted onto a task are exactly what experts see through. Real play makes the *doing itself* safe and enjoyable; it doesn't reward the doing with stickers.
3. **Measured by removal.** The test for whether delight is load-bearing: take it out. If the artifact still teaches but loses its pull, the delight was real — you just found what it was doing. If nothing changes, it was decoration; fold it into the doing or cut it.

## Check classification

**Static checks** — none meaningful. Delight is entirely a judgment call about whether fun is designed into the core experience, whether play is safe, and whether a felt-win moment exists. No count or pattern match determines this. The linter has nothing to run here.

**Reasoning checks** — everything: all seven principles below, applied holistically by reading the artifact as a whole and evaluating design intent, audience fit, and whether delight is load-bearing or bolted on.

## How to apply

Walk the principles below. For each, check the artifact and note where delight is missing, bolted-on, or forced. The recommendation is usually one of three: *make it load-bearing* (move the fun into the core activity), *cut the decoration* (a touch that isn't doing work), or *find the genuine version* (replace forced whimsy with something true to the material).

## The principles

### 1. Designed in, not bolted on

Delight lives in the core experience — the scenario, the build, the interaction — not in a decoration layer added at the end.

**Heuristic (the removal test):** strip out the "fun" — the mascot, the jokes, the theme. Does the artifact still teach but now feel like a chore? Then the delight was sitting *on top* of the work, not *in* it. The fix is to make the activity itself the delightful part: a build worth finishing, a scenario worth caring about, an interaction with a small surprise in it.

> Bolted-on: a dry click-through lab with a cartoon mascot in the corner cracking jokes between steps.
> Designed-in: the lab *is* the hunt — the learner's agent is hanging, one malformed tool among hundreds is poisoning the session on *search* not *use* (or one broken S3 read is silently corrupting downstream results), and they dispatch subagents to corner it. The stakes and the small wins are the activity, not a layer over it.

### 2. Doing and fun — the floor and the amplifier

Hands-on, useful, safe learning is the floor. Delight is the amplifier on top of it. Both are required: useful-but-joyless is incomplete; fun-but-hollow is worse than dry.

**Heuristic:** if the artifact is engaging but a learner couldn't *do* anything new afterward, the floor is missing (back to `calibrate-challenge`). If the artifact is correct and complete but a learner finishes relieved rather than energized, the amplifier is missing — that's this pillar's job.

**Why both:** the doing is what transfers; the delight is what makes them come back, recommend it, and arrive at the next thing curious instead of braced.

### 3. Play makes exploration safe

The barrier to adoption is rarely the technology. A skilled person risks their expert standing by fumbling a new tool in front of peers. Genuine play lowers that guard: it makes a wrong move cheap, reversible, and a little funny — not graded. Under that cover, the expert drops their defenses long enough to actually try.

**Heuristic:** ask *"what does a learner risk by getting this wrong?"* If the honest answer is "looking incompetent," the activity isn't safe enough to explore in. Re-cast so mistakes are expected, recoverable, and part of the fun — a sandbox they can break, a challenge where the first attempt is *supposed* to fail.

**This is the adoption-resistance move.** Skeptical experts don't get argued into a new tool; they get one safe, playful experience of it and recalibrate on their own. (See `stick-check` §2 Unexpected — the open gap that play protects.)

### 4. One genuine experience beats many told facts

Design for the learner to *feel* the win once, in a receptive state — the moment the tool solves a problem that's actually theirs. Belief follows experience, not the reverse. A single honest "oh — that just worked" outlasts a module of claims about how good the tool is.

**Heuristic:** find the artifact's *felt-win moment* — the single point where the learner experiences the payoff themselves. If you can't point to one, the artifact is telling, not showing. Build toward that moment and protect it; everything before it is setup, everything after is transfer.

**Anti-pattern:** burying the win. If the payoff arrives in the wrap-up paragraph instead of in the learner's own hands mid-lab, move it earlier and make it theirs.

### 5. Personality and thoughtful touches

Small signs that a human cared, and that this was made for *this* learner rather than mass-produced: a celebration when the steps are all checked off, copy with a voice, a recurring character or motif, a loading phrase with a wink, an Easter egg for the learner who pokes around.

**Heuristic:** these are texture, and texture is cheap to overdo. **One or two deliberate touches per artifact** — like `stick-check`'s memorability elements, delight piles up badly. Three mascots and a pun and a confetti animation compete instead of compound. Pick the touch that fits the material and let it recur.

**The discriminator vs. Principle 1:** a touch is fine *as texture* even if it's not load-bearing — a completion celebration doesn't teach, and that's okay. The line is forced vs. fitting (Principle 7), and pile-up vs. restraint. A touch that's true to the material and used sparingly earns its place; the same touch tripled does not.

### 6. Imperfection as a feature (AI in the loop)

When the activity uses AI, design *with* the AI's real characteristics — including its limits — not around them. The most delightful AI activities turn a quirk into the lesson.

**The pattern:** an AI that plays a slightly-wrong, confused learner is a *better* sparring partner than a perfect one — spotting and correcting its mistake is the same skill as correcting a real learner, and the human sharpens while the model does. The human-as-grader / LLM-as-judge loop is delightful precisely because both sides improve in front of you.

> Concrete: a trainer-onboarding game where the AI plays the student — tuned to ask the askew, half-formed questions a real learner asks, not clean textbook ones. The trainer has to spot the misconception underneath and correct it live. Correcting the AI's confusion is the same muscle as correcting a student's, so the rep transfers directly — and leaning *into* the model's imperfection makes a better sparring partner than a flawless one would. The play and the learning are the same move.

**Heuristic:** if the activity treats the AI as an oracle that must be perfect, you've designed *around* its nature and you'll fight its failures. Ask instead: *where does the AI's real behavior — its confident-but-wrong moments, its need for context, its variability — become the point of the exercise?* That's where the delight and the learning are the same thing.

### 7. Authenticity gate

Delight only works if it's genuine to the content and the audience. A mascot unrelated to the material, a joke that doesn't land, a theme stapled on for energy — these read as pandering and cost trust faster than dry content does.

**Heuristic:** for each delight touch, ask *"is this true to the material and would this specific audience enjoy it?"* If either answer is no, cut it. Forced whimsy is worse than none. The bar isn't "is it fun in the abstract" — it's "is it fun *here, for them.*"

**Why this gate exists:** technical audiences detect manufactured enthusiasm instantly (same reflex `say-it-plain` §2.6 and `stick-check` §5 warn about). Delight that isn't earned reads as a sales move, and the rest of the artifact loses credibility with it.

## Integration with other pillars

- **Learning Effectiveness (`calibrate-challenge`)** — owns the floor; delight is the amplifier on top. Calibrate first. A delightful artifact at the wrong difficulty, or one that doesn't transfer, fails — fun doesn't rescue a broken learning design. The two are complementary, not competing: `calibrate-challenge` makes it *work*; `delight-check` makes it *loved*.
- **Stickiness (`stick-check`)** — closest neighbor, and they overlap. `stick-check` is about *memory* (does the idea survive the trip to recall); `delight-check` is about *experience* (does the learner enjoy the trip and feel safe taking it). A `stick-check` memorability element (themed humor, recurring motif) is often also a delight touch — but the question differs: stick asks *"will they remember it,"* delight asks *"did a human care, and did the skeptic drop their guard."* When they overlap, run both; the framings catch different misses.
- **Style (`say-it-plain`)** — the authenticity gate (Principle 7) is the same instinct as `say-it-plain`'s war on hype: forced enthusiasm and manufactured fun are hype in playful clothing. Playful copy is fine; pep-rally copy ("you're going to LOVE this!") is not. Delight is shown, not announced.

## What this skill is NOT

- **Not a substitute for the floor.** Delight on top of a lab that doesn't teach is decoration. `calibrate-challenge` first, always.
- **Not gamification.** Points, badges, and leaderboards are not what this pillar means by play. Genuine play makes the doing safe and enjoyable; it doesn't bolt rewards onto a chore.
- **Not "add jokes."** Humor is one texture among several, and the weakest if it isn't true to the material. The load-bearing principles are 1–4 (designed-in, doing-and-fun, safe play, the felt win); the touches (5) are garnish.
- **Not for every artifact.** Reference docs, bug reports, and status updates should be plain and quick. Forcing delight onto content that wants to be brief is the Principle 7 failure mode.
\
"""


def main(input):
    audience = input.get("audience", "workato")
    return {
        "rubric": RUBRIC,
        "rules": {
            "applicable": True,
            "banned_phrases": [],
            "regex_patterns": [],
            "presence_checks": [],
            "note": "delight-check has no mechanical static checks — all principles require LLM reasoning. Use the rubric for client-side evaluation.",
        },
    }
