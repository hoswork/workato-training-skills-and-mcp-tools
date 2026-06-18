import json
# say-it-plain
RUBRIC_SAY_IT_PLAIN = """\
---
name: say-it-plain
description: Use when writing or editing prose for external/professional consumption — slide decks, findings docs, customer emails, blog posts, READMEs, internal memos that may travel. Two passes, in order — form-level hype shapes (stat grids, drama-framed labels, telegraphic fragments, feature-name constructions, manufactured urgency, misstated hierarchy, aphoristic contrast) and word-level hype (corporate jargon, filler, superlatives, urgency/pressure, second-person hype, AI-slop sincerity tells).
---

# Say It Plain

Plain, direct, honest professional prose. The skill catches hype at **two levels** — and the order matters:

1. **Form-level hype** — the *shape* of the writing reads as marketing (the layout, the sentence rhythm, the section labels). Words can pass the word-level check and still smell like a landing page.
2. **Word-level hype** — corporate jargon, filler, superlatives, urgency language, second-person hype, AI-slop sincerity tells. The classic lexical pass.

**Form-level is the foundation.** Most professional writers have already learned to avoid "leverage" and "world-class" — they default instead to drama-framed labels, aphoristic contrast, and feature-name constructions without noticing. The form-level pass is where this skill earns its keep.

Source: Heiwad's slides-harness validation rules + the 2026-05-27 GUTENBERG/Ghost cascade that promoted form-level hype to a peer of the lexical pass. Renamed from `de-hype` on 2026-05-19, then from `say-it-straight` on 2026-06-03 — the rules are unchanged across renames.

## When to invoke

Invoke before sending or publishing any of:

- Customer-facing decks, docs, emails
- Retro findings, post-mortems, status reports
- Blog posts, READMEs, release notes
- Internal memos that may get forwarded outside the team
- Product marketing copy and landing-page drafts
- AI-generated drafts you're about to ship as your own writing — these need the heaviest pass

Skip on: code comments, private notes, chat messages.

## Posture

Four rules of taste behind every check below:

1. **Inform, don't sell.** Your reader is a technical builder or peer. They can evaluate substance. Pressure and superlatives signal weakness in the underlying claim.
2. **Show, don't tell.** "World-class" and "best-in-class" are claims without evidence. Either cite the evidence or remove the adjective.
3. **Cite or soften.** Absolute claims ("the only", "the first", "no one else") need a source or a hedge. No source = no absolute.
4. **Watch the shape, not just the words.** A passage can pass every word-level check and still read as sales — through the layout, the sentence rhythm, the section labels. The form carries the posture as much as the lexicon does.

## Check classification

**Static checks** — all of §2 (word-level lists). These are pattern matches and counts; no interpretation needed:
- §2.1 Banned jargon: word/phrase list match (leverage, utilize, synergy, etc.)
- §2.2 Filler words: word list match (very, really, just, basically, etc.)
- §2.3 Superlatives: word list match + count per paragraph (max 1)
- §2.4 Unsubstantiated absolutes: phrase patterns ("the only", "the first", "no one else")
- §2.5 Urgency/pressure: phrase list match ("act now", "don't miss", etc.)
- §2.6 Second-person hype: phrase patterns ("you need this", "you won't believe")
- §2.7 AI-slop sincerity tells: word/phrase match ("honestly", "to be honest", "frankly")
- §2.8 Exclamation marks: count (flag if >1 per document)
- §2.9 Passive voice: regex ("was/were/is/are/been + past participle") — soft check
- §2.10 Agentic overreach: phrase list match ("act autonomously", "reason over", "understand", "learns", etc.)

**Reasoning checks** — all of §1 (form-level shapes) and §3 (bug-report register). These require reading the passage and evaluating intent, shape, and posture:
- §1 Form-level: stat grids, drama-framed labels, telegraphic fragments, feature-name constructions, manufactured urgency, misstated hierarchy, aphoristic contrast, testimonial framing — none of these are catchable by word match. A passage can use zero banned words and still read as a landing page.
- §3 Bug-report register: speculation vs. confirmed claim, teaching content vs. mechanism explanation, involuntariness framing — these require understanding what the reporter observed vs. inferred.

The form-level pass is where this skill earns its keep. The static pass catches lexical hype; the reasoning pass catches structural hype.

## How to apply

Three passes, in this order:

**Pass 1 — The aloud test.** Read the draft aloud (or sub-vocalize) as if briefing a colleague over coffee. If any line could lift verbatim into a landing page, a tradeshow banner, or a SaaS value-prop slide — flag it. Don't edit yet, just mark.

**Pass 2 — Form-level shapes.** Walk §1 below (the seven form-level hype tells). These catch hype that the word-level pass misses. Higher leverage; do them first.

**Pass 3 — Word-level lists.** Walk §2 below (the nine lexical lists). Apply the suggested swap, remove the word, or rewrite the sentence so the substance does the work.

Skip a pass if you're confident — they're a safety net, not a ritual.

---

## §1. Form-level hype tells

The seven shapes below pass the word-by-word check but still import a marketing posture. Each Bad/Good pair shows the trade.

### 1.1 Pitch-deck stat grids

A row of side-by-side cards, each with an eyebrow label, a big bold value, and a one-line caption. The layout itself reads as a SaaS value-prop slide; the words can't rescue the shape. If the information is real context (the persona, the situation, what the reader will produce), write it as prose. Don't chrome it as a stat card.

If your source has a `stats:` block in YAML, a stat-grid component in HTML, or a "by the numbers" section in Markdown — delete it and put the substance in normal sentences.

### 1.2 Drama-framed section labels

*"What's broken"*, *"Who's hurting"*, *"Who's affected"*, *"The pain"*, *"The cost"*, *"The risk"*. These presuppose crisis or victims before the reader has context.

Use neutral, situational labels: *"Today"*, *"Current state"*, *"People involved"*, *"Outcome"*, *"What you'll produce"*.

**Heuristic:** if a label needs an adjective to feel important, the label is the problem.

### 1.3 Telegraphic noun fragments

Comma-chained noun phrases without verbs — punchy *because* they're incomplete. Punch is sell.

> Bad: *"Drops, duplicates, no audit trail."*
> Good: *"The current process drops cases, creates duplicates when synced twice, and gives the team no way to audit which cases went over."*

### 1.4 Feature-name constructions

*Adjective + compound noun* phrased as if naming a product, when you mean to describe what the reader will produce or experience.

> Bad: *"A self-healing case sync."*
> Good: *"A recipe that retries failed case writes and posts unrecoverable ones to a triage channel."*

### 1.5 Manufactured urgency

Inflating the consequence of skipping a step or ignoring a recommendation, to dramatize it.

> Bad: *"Without a folder, this lab's work is lost in three weeks."* (Folders don't have that consequence — search finds anything.)
> Good: *"A folder keeps recipes, connections, and lookup tables for one lab together — easier to find, easier to demo, easier to delete."*

State the *actual* benefit in the actual register. A reader who notices the inflation later — and they will — loses trust in the rest of the voice.

### 1.6 Misstated hierarchy

Promoting a smaller concept above its position in the underlying system or product, usually for rhetorical weight.

> Bad: *"The first design decision of any recipe is **where it lives**, not **what it does**."* (True only if you accept the framing; the recipe's actual first decisions are the trigger, the actions, and the shape.)
> Good: *"A Workato project is the isolation boundary. Folders organize within a project as assets accumulate."*

Get the hierarchy right, or skip the framing. A reader who knows the domain will mark you down; a reader who doesn't will internalize a wrong model.

### 1.7 Aphoristic contrast

Two short clauses balanced around a contrast, yielding a sentence that *sounds* wise. The form imitates an aphorism (Twain, Knuth, the Pragmatic Programmer) without earning the underlying insight. The reader gets cadence instead of content.

> Bad: *"The model phrases; the knowledge base knows."*
> Good: *"The LLM writes prose; the knowledge base supplies the facts."*

> Bad: *"It's the boring half — but it's the difference between a recipe you babysit and one you can leave alone."*
> Good: *"Operational hardening is what most teams add late, after the integration is proven; it's what makes the recipe leave-alone-able."*

Aphoristic contrast bites conversational sections especially hard — asides, sidebars, postscripts, blog "lessons learned" — because the register authorizes a lighter tone and writers slide from *conversational* into *aphoristic* without noticing.

### 1.8 Customer-testimonial framing in learner-facing content

Dropping a quote with attribution into the middle of learner-facing prose imports a case-study webinar posture. Even when the underlying insight is true and the customer is real, the *shape* — quote + attribution + framing — reads as marketing borrowing authority, not as instruction.

> Bad: *"As one platform admin described it: 'This changed how we think about automation governance. We went from reactive firefighting to proactive policy enforcement.'"*
> Good: *"The shift here is from reactive firefighting — investigating after something goes wrong — to proactive policy enforcement, where guardrails prevent problems before they happen."*

The customer's insight is the same in both versions. The first teaches it; the second sells it.

Common shapes that import the same posture:

- *"Many organizations struggle with..."* — generic, marketing-flavored.
- *"Our customers report a 60% reduction..."* — reads as sales deck.
- *"One enterprise customer told us they were spending 8 hours a week..."* — reads as support ticket.

**Move:** absorb the insight behind the quote and teach it as a principle, a scenario the learner steps into, or a generalized observation. Cite the source in author/review notes, never in learner-facing text. Use *"Imagine you're a platform admin reviewing audit logs every week..."* instead of *"One customer told us..."*

Bites hardest in: product onboarding modules, scenario stems in Knowledge Checks, abstract opening paragraphs.

---

## §2. Word-level lists

The lexical pass. Walk these after the form pass; they catch the rest.

### 2.1 Banned jargon — swap for plain language

| Term | Swap |
|---|---|
| leverage | use |
| utilize | use |
| synergy | collaboration |
| paradigm | approach |
| best-in-class | leading |
| circle back | follow up |
| deep dive | detailed look (unless scuba) |
| game-changer / game changer | improvement |
| disruptive | new approach |
| revolutionary | significant |
| 10x | significant improvement |
| crush it / killing it | (remove) |
| rockstar | expert |
| ninja | specialist |
| guru | expert |
| hack | technique (unless security) |
| unlock | enable (unless literal lock) |
| supercharge | improve |
| turbocharge | accelerate |
| skyrocket | increase |
| empower | enable |
| democratize | make accessible |
| seamless | smooth |
| frictionless | simple |
| robust | reliable |
| scalable | grows with you (in marketing copy; fine in architecture) |
| world-class | (remove — show, don't tell) |
| cutting-edge | modern |
| next-gen | new |
| enterprise-grade | (remove — let the feature speak) |

### 2.2 Filler words — cut for tighter copy

very, really, just, basically, actually, simply, obviously, clearly, every

`every` often hides a false universal — try "common" or "most" instead.

### 2.3 Superlatives — max one per paragraph or section

best, fastest, easiest, most powerful, incredible, amazing, awesome, insane, unbelievable, mind-blowing, stunning, killer, epic, legendary, ultimate, perfect, unmatched, unparalleled, unprecedented

If a paragraph has more than one, the section is doing emotional work that the content can't back up. Cut to one, or remove all and let the content earn the reader's reaction.

### 2.4 Unsubstantiated absolutes — cite or soften

"the only", "the first", "the fastest", "the most", "no one else", "nothing else", "unlike anything"

Either link to the source that proves the claim, or soften: "one of the few", "among the first", "in our experience".

### 2.5 Urgency / pressure — remove entirely

"act now", "don't miss", "limited time", "before it's too late", "you can't afford", "what are you waiting for"

Technical readers tune these out and lose trust in the rest of the document.

### 2.6 Second-person hype — inform, don't sell

"you need this", "you won't believe", "you'll love", "you deserve", "imagine if you"

These imply you know the reader's needs better than they do. Replace with a factual description of what the thing does.

### 2.7 AI-slop sincerity tells

**"honest" / "honestly" / "to be honest" / "frankly"** — usually a tell that AI-generated copy is trying to perform trustworthiness. Cut it. If you genuinely need to mark a candid moment in a long document, fine — but at most once per piece. If your prose needs to announce its own honesty, the surrounding sentence isn't carrying its weight.

This list will grow as more AI-slop patterns surface. Add new entries when you notice a recurring tell.

### 2.8 Exclamation marks

In professional prose, default to zero. They read as shouting or excitement-performance. One per long doc is the ceiling; zero is better.

### 2.9 Passive voice (soft check)

Prefer active voice. "The team shipped X" beats "X was shipped by the team." Passive voice often hides who did what — which is sometimes exactly the right thing to hide, so this is a judgment call, not a hard rule.

### 2.10 Agentic overreach — describe what the product actually does

Words that claim more autonomous capability than the product delivers. Especially relevant in AI / agentic / Genie / Otto content — these phrases inflate what the product is, then collide with what learners and customers observe in practice.

| Flagged phrase | Why it's wrong | Better |
|---|---|---|
| **"act autonomously"** | Overstates Genie's independence — it follows defined skills and prompts | "act on system events without waiting for an employee message" |
| **"reason over" / "reason about"** | Often imprecise — describe what reasoning actually happens | Specify the decision: "classify", "infer the category", "decide whether to escalate" |
| **"understand"** | Anthropomorphizes — LLMs pattern-match, not understand | "parse", "extract", "classify" |
| **"knows"** | Same | "retrieves", "looks up" |
| **"learns"** | Implies fine-tuning / memory — only use if memory or RLHF is actually in scope | "retrieves from KB", "uses conversation history" |
| **"thinks" / "decides for itself"** | Anthropomorphizes; overstates autonomy | "applies the prompt rules", "follows the configured logic" |

**Rule:** Describe the mechanism, not a humanlike-cognition mimic. If a learner could observe the product doing X mechanically, write that. If a learner can't, don't claim it.

This category fires hardest on Agent Studio, Genie, Otto, MCP, and "agentic" content. It's also useful for any product description where capability inflation creeps in.

---

## §3. Bug-report register (matter-of-fact, not teachy)

When the artifact is a bug report (Jira ticket, GitHub issue, internal incident write-up), the standard hype passes (§1 and §2) still apply — but bug reports demand an additional posture check. Triage and engineering audiences need facts, not pedagogy.

This section is the canonical home for the *register* rules. The mechanical *presence* checks live in `complete-check` §1.6. For Workato CCE filings specifically, the workflow skill `file-workato-product-bug` adds the form-specific layer on top.

### 3.1 Speculation ban

Hedge speculation in IMPACT or SCOPE statements only (e.g., "likely surface area," "we estimate"). Never speculate inside DIAGNOSED CAUSE or ERROR. If you didn't confirm it, leave it out — engineering has the code and will diagnose.

Flag and cut:

- *"Probable cause is X"* → unless confirmed, omit
- *"Common causes include..."* → omit
- *"Things to check: A, B, C..."* → omit
- *"Where to look: probably $ref or nullable: true..."* → omit
- *"I suspect..."* / *"I believe..."* / *"Maybe..."* → either confirm and remove the hedge, or omit the sentence

### 3.2 No teaching content

Bug reports are not class lectures. Triage engineers triage; product engineers investigate. Neither audience needs you to teach them what JSON Schema is, how MCP works, or how their own platform behaves at a general level.

Mechanism explanations are load-bearing only when they tie the diagnosed cause to the observed impact. A 1–2-sentence mechanism statement inside DIAGNOSED CAUSE is sufficient. Multi-paragraph mechanism walks are out of bounds.

Flag and cut:

- Background sections that explain how the platform works in general
- *"Here's how X normally behaves..."* paragraphs
- *"To understand this bug, you need to know..."* preambles
- Standalone "Mechanism" or "How it works" subsections beyond the 1–2-sentence DIAGNOSED CAUSE mechanism

### 3.3 First-person attribution for observations

When the reporter has firsthand observations (logs they saw, sessions they ran), use first person:

- ✅ *"In my logs, this surfaced in 9 sessions across 14 days."*
- ✅ *"I observed the failure when..."*
- 🚫 *"In one user's logs, this surfaced..."* (depersonalized; weakens impact)
- 🚫 *"The user reports..."* (when the user is YOU filing the report)

The bug report is a primary-source artifact. Don't translate yourself into a third party.

### 3.4 Reuse the load-bearing word

If the report uses a load-bearing word for the failure mode in IMPACT (e.g., "poisons," "wedges," "corrupts," "drops"), reuse the same word in DIAGNOSED CAUSE. Different words for the same mechanism dilute the report and make engineering hunt for the throughline.

- ✅ IMPACT says *"poisons the session"* → DIAGNOSED CAUSE says *"poisons every subsequent request"*
- 🚫 IMPACT says *"poisons the session"* → DIAGNOSED CAUSE says *"invalidates the request pipeline"* (different framing, same mechanism)

### 3.5 Quote literal error strings

Quote the exact error string returned by the API, runtime, or system. Don't paraphrase. Engineering will grep for the literal text.

- ✅ Quote: `tools.N.custom.input_schema: JSON schema is invalid. It must match JSON Schema draft 2020-12.`
- 🚫 Paraphrase: *"The API returns an error saying the schema is invalid."*

### 3.6 Make involuntary impact explicit

If the failure mode hits the user without action on their part, say so explicitly. The involuntariness is often what calibrates severity.

- ✅ *"The user does not have to call the tool to be affected."*
- ✅ *"Any session that loads the schema (via tool search or discovery) hits the failure."*
- 🚫 Implicit framing that leaves the reader thinking the user must trigger something.

### 3.7 Name the affected component in IMPACT

Lead with the affected component **by name** (tool name, endpoint URL, recipe ID, etc.). Generic phrasings (*"a tool is broken"*, *"the system fails"*) force the reader to scroll for the specifics.

- ✅ *"Loading the input_schema for `mcp__workato-dev-api__post_api_collections_api_endpoints` poisons the Claude Code session..."*
- 🚫 *"A tool in the MCP server is broken and breaks Claude Code sessions..."*

---

## Edit pattern

When you hit a flagged phrase or shape, the move is almost always one of four:

1. **Swap** — replace with the plain-language alternative (jargon, fillers).
2. **Remove** — delete the word and re-read; if the sentence still makes sense, the word was decoration (superlatives, urgency, "honestly").
3. **Substantiate** — add the evidence that earns the claim (absolutes, superlatives that survive a second look).
4. **Rewrite the shape** — restructure the sentence or section. Drama labels become situational labels; telegraphic fragments become sentences; aphoristic contrast becomes direct statement; stat grids become prose. Form-level hits almost always need this fourth move — swap and remove don't fix the shape.

If you find yourself rewriting the whole sentence: the original was doing emotional work, not informational work. The rewrite is the right outcome.

## Allowed exceptions

Some hype-adjacent phrasing is in-bounds because it carries a precise meaning in an industry-standard framework, or it belongs to a specific team's voice. Leave these alone even when the general rules would flag them.

### Industry-standard terminology

#### "Champion" (sales / customer-success / GTM frameworks)

**"Champion"** is a defined role in MEDDIC, MEDDPICC, and Force Management's *Command of the Message* sales-qualification frameworks. It refers to a specific internal advocate at the customer org who actively sells your solution to other stakeholders — has political capital, has access to power, and is incentivized by your success. Different from a casual fan or supporter.

- ✅ **In-bounds** (specific role, framework usage):
  - *"We need to identify our Champion at Acme before this deal can progress."*
  - *"Sarah is our Champion — she's already pre-sold the EBR to the CFO."*
  - *"MEDDIC Champion validation is part of every Q3 forecast call."*
  - *"They're a strong influencer but not yet a Champion — they don't have the political capital."*
- ❌ **Out-of-bounds** (vague / hype usage — `say-it-plain` should still flag these):
  - *"Salesforce is the champion of CRM."* (just superlative; replace with specific claim)
  - *"Our team are champions of integration."* (vague advocate-y; rewrite)
  - *"Be a champion for change!"* (motivational filler; cut)

The discriminator: if the sentence names a specific stakeholder (or asks about a specific stakeholder) at a specific customer org performing the internal-seller role, **Champion** is the right word and `say-it-plain` should not flag it. If the sentence uses Champion as a synonym for "great" / "advocate-y feeling" / "supporter," the form/word rules apply normally.

This exception is **cross-Workato** — relevant to sales, CS, CSM, marketing, product, and any training content about customer-relationship roles. Not team-specific.

### Workato-internal carve-outs

Exceptions below carry meaning inside Workato-proprietary frameworks (e.g., the Workato Selling System). **This subsection is stripped on projection** to the broadly-distributed `say-it-plain.zip` — these terms are not safe to license outside Workato. Internal users running the rubric via `the-once-over` see this section; downstream projections do not.

#### Workato Selling System (WSS) — sales-framework vocabulary

The **Workato Selling System (WSS)** extends MEDDIC/MEDDPICC and Force Management's *Command of the Message* with Workato-specific frameworks: the Value Framework / Mantra, SPEED/POWER/SCALE differentiators, OrCA, CUP of MEDDPICC. Many WSS terms collide with everyday hype words — *elite, power, scale, compelling, champion, magic, mantra, proof* — but carry precise, bounded meanings inside the methodology.

**Scope.** This exception layer applies to *Workato-internal prose* — sales-enablement content, deal reviews, manager-coaching conversations, internal Slack, internal training, AE coaching rubrics. **It does not apply to customer-facing copy.** When writing for customers or the public, the standard form-level and word-level rules fire normally — these terms read as marketing in external contexts.

**General disambiguation rule.** Allow a WSS term when:

1. It's tied to a buyer's situation, a specific deal/opportunity, a qualification field, or the WSS framework structure, **AND**
2. It carries the specific bounded meaning defined in §5.1–§5.6 below.

Flag it when it appears as self-praise, a vague adjective, a marketing booster, or a generic word that happens to coincide with the WSS term without methodology context.

##### §5.1 Value Framework / Mantra components

The structural building blocks of a value-based conversation. Allowable when describing the *customer's* situation or the value narrative — not when used as loose business adjectives.

- **Current State** *(variants: as-is state)* — What's currently happening in the buyer's business and the associated pain Workato can solve. ✅ Buyer-specific pain tied to discovery, paired with Pain Points or Negative Effects. 🚫 *"In the current state of the market, everyone needs automation."*
- **Pain Points** *(pain, the pain)* — Specific undesirable conditions in the Current State that Workato addresses. ✅ Tied to a named process/team/system the buyer owns. 🚫 *"We take the pain out of integration."* (product slogan)
- **Negative Effects** *(NE)* — Quantified consequences of *not* acting on Pain Points; sized in Revenue/Cost/Risk/Compliance terms to create urgency. ✅ Carries numbers/KPIs ("30% higher costs", "4 FTEs reconciling"). 🚫 *"Manual work has negative effects on morale."* (vague, unquantified)
- **Desired State** *(future state, "stand-in-the-future")* — The buyer's vision of how life is better once the Current State is resolved. ✅ Forward-looking vision attributed to the buyer; precedes SBOs. 🚫 *"Workato is the desired state of automation."* (positioning the product)
- **Specific Business Outcomes** *(SBO, SBOs, business outcomes)* — Tangible measurable impacts in Revenue/Cost/Risk/Compliance terms; the basis for ROI. ✅ Measurable and KPI-tied ("cut processing time 75%", "+25% ARPU"). 🚫 *"We drive great business outcomes for everyone."* (unmeasured)
- **Solution Requirements** *(SR, SRs, requirements)* — Minimum capabilities to bridge Current → Desired, in *customer language*, mapped to SBOs. ✅ Stated as customer needs, used to set traps. 🚫 *"Workato meets all your requirements."* (sales assertion, no SR list)
- **Acceptance Criteria** *(AC)* — Measurable KPIs the customer uses to judge whether an SR is met. ✅ Specific benchmarks ("<2s per transaction", ">99.8% uptime"). 🚫 *"Our solution is acceptable for enterprises."*
- **How Workato Does It** *(HWDI)* — How Workato satisfies the SRs and AC, tailored to the buyer's Desired State and SBOs. ✅ Maps named Workato capabilities to the buyer's SRs/AC. 🚫 *"Here's how Workato does it better than anyone."* (no mapping)
- **How Workato Does It Better** *(HWDIB)* — Articulation of the differentiated way Workato delivers SRs vs. alternatives (including "do nothing" / "do it internally"). ✅ Names specific differentiators against named alternatives. 🚫 *"We're simply better than the competition."*
- **Proof / Proof Points** *(Workato 'Proof')* — Tangible evidence Workato delivered SBOs for similar customers — case studies, Work Automation Index data, analyst reports. ✅ Cites a named customer/result or analyst recognition tied to the buyer's situation. 🚫 *"Our customers love us."*
- **The Mantra** *(conversation summary, "what I heard you say...", reciting back)* — The structured recite-back that confirms SBOs → SRs → AC → HWDI → Better → Proof. Used to "pivot/turn the corner" in a call. ✅ Follows the recite-back structure. 🚫 *"Automation is our mantra."* (slogan use)
- **Value-Based Conversation** *(VBC, value-based selling)* — A consultative conversation flowing Current State → NE → Desired → SBOs → SRs → AC before any product talk. ✅ References the WSS flow/sequence. 🚫 *"We deliver tons of value."*
- **Coat of Pain** *("wear the coat of pain")* — WSS coaching idiom for making the buyer feel the pain enough to be compelled to act. ✅ Used in coaching/role-play about creating urgency. 🚫 *(rarely misused)*

##### §5.2 Customer Value Drivers

Top-of-mind business priorities that exist with or without Workato (revenue, cost, risk). Allowable when used as the lens for a customer conversation — not as generic Workato marketing themes.

**The four unified Value Drivers:**

- **Enterprise Agility** — Innovate quickly, reduce time-to-first-value; governed company-wide access (SPEED + POWER lens). ✅ Framed as a customer priority. 🚫 *"Workato makes you agile."*
- **Efficiency & OrCA** *(Operational Cost Architecture, Operational Efficiency)* — Do more with less; automate the mundane; cost-architecture optimization (SCALE lens). ✅ Used as a Value Driver or for cost-structure discovery. 🚫 *"We're super efficient."*
- **Risk Reduction** — Company-wide orchestration without Shadow IT; GRC as a team sport (POWER lens, CISO-targeted). ✅ Tied to governance/compliance/Shadow IT as a buyer priority. 🚫 *"Lower your risk with us."*
- **Revenue Growth** — Seamless end-to-end CX plus AI-enabled growth at scale (SPEED + POWER lens). ✅ Customer Value Driver, especially for Embed accounts. 🚫 *"Grow revenue fast!"*

**Legacy / segment-specific Value Driver labels** (still WSS canon; allowable when used as named Value Drivers for a segment, not as descriptors):

Differentiated Experience *(Direct)* · Operational Efficiency *(Direct)* · Enterprise Agility & Innovation *(Direct)* · Speed to Solutions *(Embed)* · Customer Churn *(Embed)* · Agility & Responsiveness *(IT)* · Modernization / Platform Consolidation *(IT)* · Total Cost of Operations / OrCA *(IT)* · Risk Mitigation *(IT)*

##### §5.3 Defensible Differentiators — SPEED / POWER / SCALE

Workato's defensible advantages. Per WSS Seller Usage Rules, introduced only *after* the buyer articulates the problem. Allowable when named as differentiators or used in trap-setting/positioning — not as generic feature bragging.

**Categories:**

- **SPEED** · **POWER** · **SCALE** — the three differentiator lenses. ✅ Used to categorize a named differentiator. 🚫 *"We have the power and scale you need."*
- **Unique / Comparative / Holistic** — the three classes of differentiator (only Workato has it / others have but ours is better / faith-building attributes). ✅ Used to classify a named differentiator.

**SPEED differentiators:** Cloud Native Autoscaling Platform · Fast Build & Delivery Experience · Extensive Connectivity *(1,200+ connectors / 14,000+ apps, Connector SDK)* · Globally Recognized Customer Success.

**POWER differentiators:** Company Innovation, Vision & Leadership · **Power of 1** *(Power of One, "one platform, one architecture, one code base, one experience", Breadth of Capabilities & Features)* · **Enterprise MCP** *(EMCP, Enterprise Model Context Protocol — MCP Gateway, Skills Builder, MCP Composition, MCP Registry, MCP Proxy)* · **Enterprise Agentic AI** *(agentic AI, AI agents, agentic orchestration, AI orchestration — governed enterprise AI agents)* · Zero Downtime Upgrade · Composable Platform.

**SCALE differentiators:** Flexible CX Models *(esp. Embed)* · Federated Model *(federated build, central governance)* · Operational Cost Architecture (OrCA) · Enterprise-Grade Security & Governance *(RBAC, audit trails, VPW, EKM)*.

**For all differentiators:**

- ✅ Named as a Workato differentiator, mapped to a buyer's SR, or used in a trap-setting question.
- 🚫 *"Our platform is powerful and secure."* (feature adjectives without the named differentiator or buyer linkage)

**Highest collision risk** — *Power of 1*, *Enterprise MCP*, and *Enterprise Agentic AI* are most easily confused with generic hype. Allow only when referring to the *named* differentiator (the unified single-platform claim; the managed MCP infrastructure; governed enterprise agents). Not when "power," "MCP," or "AI agent" appears generically.

##### §5.4 Discovery & Trap-Setting

- **Discovery Questions** *(elite discovery, open-ended questions)* — Consultative open-ended questions that uncover Current State, NE, Desired State, SBOs, SRs, AC. ✅ Open-ended, sequenced along the value framework. 🚫 *"Let me ask a quick discovery question: do you like saving money?"* (closed/leading)
- **Good → Great → Elite question ladder** — Question-depth progression: *go-deep(er) questions* (find pain) → *quantification questions* (size it) → *implication questions* (second-order effects / urgency). ✅ Labeling depth/quality in discovery or coaching. 🚫 *"We're elite at what we do."*
- **Trap-Setting Questions** *(traps, "set a trap", Select Trap / Open Trap / Close Trap)* — Questions designed to influence the buyer's SRs toward criteria where Workato wins. Three-step flow: Select (introduce concept) → Open (tee up/quantify value) → Close (define the SR or metric in customer language). ✅ Tied to a differentiator and a target SR; uses Select/Open/Close. 🚫 *"It's a trap to use legacy tools."* (rhetorical)
- **Multi-threading** *(multi-thread between personas)* — Engaging multiple personas/stakeholders across the buying group rather than a single contact. ✅ Working multiple stakeholders in a deal. 🚫 *(rare; exclude if about software threads)*

##### §5.5 CUP of MEDDPICC — qualification framework

The qualification framework WSS supports. **The highest-value disambiguation cases** — most overlap with everyday English (Champion, Metrics, Competition, Compelling). Allow **only** when used as a qualification element about a specific deal/opportunity.

**CUP extension:**

- **[C] Compelling Event** — Internal/external, time-bound factors driving the buyer to purchase now (efficiency push, cost mandate, policy change, competitive edge, compliance deadline). ✅ Tied to a deadline/driver in a specific deal. 🚫 *"Our launch is a compelling event for the industry."*
- **[U] Use Case for Rapid First Value** *(First Value, First Time-to-Value, land use case)* — The first use case(s) and the path to "First Time-to-Value." ✅ Names the initial implementation that delivers a quick win. 🚫 *"There are many use cases for AI."*
- **[P] Partner Ecosystem in the Opportunity** *(partner ecosystem)* — Partner(s) needed pre- or post-sales in this deal. ✅ A specific partner in the opportunity. 🚫 *"We value our partners."*

**MEDDPICC elements:**

- **[M] Metrics** — Quantifiable business justification (Revenue, Risk, Cost) — the deal's IMPACT. ✅ Deal-specific quantified justification. 🚫 *"We track lots of metrics."* (analytics chatter)
- **[E] Economic Buyer** *(EB)* — The person with authority to say "yes, buy Workato now." ✅ A named/sought decision-maker with budget authority. 🚫 *"Be economical."*
- **[D] Decision Criteria** — The buyer's shopping list: financial, technical, business justifications. ✅ The criteria the buyer will judge vendors on. 🚫 *"Use good judgment in your decisions."*
- **[D] Decision Process** — Specific events, timelines, and people for evaluation/selection. ✅ The buyer's evaluation steps. 🚫 *"Our process is great."*
- **[P] Paper Process** — All details and timelines to signature (legal/procurement/approval). ✅ Procurement/legal/signature steps for the deal. 🚫 *(rarely misused)*
- **[I] Implicate the Pain** *(Identify Pain)* — Identify the pain/problem/initiative — key focus during Discovery. ✅ Surfacing/sizing the buyer's pain in discovery. 🚫 *"That's a painful bug."* (literal)
- **[C] Champion** — A person with power and influence in the account who can get the seller to the Economic Buyer. *(See the Champion subsection above for the canonical detailed entry; the discriminator is the same — named internal advocate at a specific customer org.)* ✅ Named stakeholder being developed. 🚫 *"Workato is a champion of automation."*
- **[C] Competition** — Alternatives to Workato, including "do nothing right now" and "do it ourselves." ✅ Named rival vendors or no-decision/build-internally alternatives in a deal. 🚫 *"It's a competitive market."*

##### §5.6 GTM process & enablement terms

WSS/GTM-specific operational vocabulary. Allow when referring to the WSS program, its artifacts, or sales process.

- **Workato Selling System (WSS)** — the methodology itself. ✅ Named methodology. 🚫 generic *"our selling system."*
- **Value Play / Workato Value Plays** — packaged value narratives tied to a Value Driver (vs. features). ✅ Named WSS asset. 🚫 *"Let's make a play for that account."* (idiom)
- **Value Card / Value Card Exercise** — the worksheet capturing a Value Driver's framework (Current States → Proof Points).
- **Value Framework (WSS VF)** — the overall framework; variants: WSS VF - Direct, WSS VF - Embedded, IT Buyer VF.
- **Persona Guide** — EA Persona Guide, CIO Persona Guide, AI2 | CIO buyer-persona playbooks.
- **Pre-Call Plan / Purpose, Process, Payoff (PPP)** — structured call opening. ✅ Call-prep structure. 🚫 generic *"payoff."*
- **Opportunity Qualification** — qualifying deals in/out using CUP of MEDDPICC. ✅ Deal-qualification context.
- **Rep Genie / Workato Genie / Workato Go and Genies** — named AI sales-assistant products. ✅ The named product. 🚫 generic *"genie."*
- **WSS Coaching Wizard** — the WSS tool for crafting trap-setting questions.
- **Direct vs. Embed (Embedded) accounts** — the two WSS account contexts. ✅ Account-type framing. 🚫 generic *"embedded software."*
- **Sales Productivity / NRR / Win Rate / ACV / Sales Cycle** — GTM outcome metrics WSS aims to move. ✅ Program/business metrics. 🚫 buzzword-only use.

**Manager Coaching Rubric proficiency levels** — the five WSS proficiency ratings, allowable when assessing AE skill against the rubric:

**Poor · Insufficient · Average · Uncommon · Elite.** ✅ Rating WSS proficiency on a dimension ("Elite discovery", "Uncommon pre-call prep"). 🚫 *"We're an elite vendor."*

##### Quick-match index

For fast allow-list lookup — always apply the disambiguation rule above:

`Current State` · `Pain Points` · `Negative Effects` · `Desired State` · `Specific Business Outcomes (SBO)` · `Solution Requirements (SR)` · `Acceptance Criteria (AC)` · `How Workato Does It (HWDI)` · `How Workato Does It Better (HWDIB)` · `Proof Points` · `The Mantra` · `Value-Based Conversation (VBC)` · `Coat of Pain` · `Enterprise Agility` · `Efficiency & OrCA` · `OrCA` · `Risk Reduction` · `Revenue Growth` · `Differentiated Experience` · `Operational Efficiency` · `Speed to Solutions` · `Customer Churn` · `Agility & Responsiveness` · `Modernization / Platform Consolidation` · `Risk Mitigation` · `SPEED` · `POWER` · `SCALE` · `Unique / Comparative / Holistic` · `Cloud Native Autoscaling Platform` · `Fast Build & Delivery` · `Extensive Connectivity` · `Customer Success` · `Company Innovation, Vision & Leadership` · `Power of 1 / Power of One` · `Enterprise MCP (EMCP)` · `Enterprise Agentic AI` · `Zero Downtime Upgrade` · `Composable Platform` · `Flexible CX Models` · `Federated Model` · `Operational Cost Architecture` · `Enterprise-Grade Security & Governance` · `Discovery Questions` · `Go deep / Quantification / Implication questions` · `Trap-Setting Questions` · `Select Trap / Open Trap / Close Trap` · `Multi-threading` · `Compelling Event` · `Use Case for Rapid First Value / First Value / First Time-to-Value` · `Partner Ecosystem` · `Metrics` · `Economic Buyer` · `Decision Criteria` · `Decision Process` · `Paper Process` · `Implicate the Pain` · `Champion` · `Competition` · `Workato Selling System (WSS)` · `Value Play` · `Value Card` · `Value Framework (WSS VF)` · `Persona Guide` · `Purpose Process Payoff (PPP)` · `Opportunity Qualification` · `CUP of MEDDPICC` · `Rep Genie / Workato Genie` · `WSS Coaching Wizard` · `Direct vs. Embed` · `Poor / Insufficient / Average / Uncommon / Elite`

*Source: Workato Selling System reference set — framework (01), value drivers (02), differentiators (07), CUP of MEDDPICC (08), Manager Coaching Rubric. Internal/Proprietary.*

### Team-specific carve-outs

#### Workato training team

The training team motto is **"allow the world to experience the Workato magic."** That means:

- **"Workato magic"** — in-bounds. Don't swap to "Workato's capabilities" or similar.
- **"magic"** — in-bounds when referring to the customer experience of Workato, especially in training-team and retro contexts ("customers experienced the Workato magic hands-on and left with the feeling that 'it just works'").

These phrases would normally trip the superlative / unsubstantiated-claim checks. They're motto-tier and pass.

## What this skill is NOT

- Not a grammar checker — leave that to writing-clearly skills or human review.
- Not a slide formatter — `no_period_on_bullets`, `title_case_titles`, font sizes belong in the slides skill.
- Not an authority on Workato product terms — that's `required_spellings` in the slides-harness terminology rules.
- Not a humor or voice guide — humor's allowed, just earned.
\
"""
# fact-check
RUBRIC_FACT_CHECK = """\
---
name: fact-check
description: Use when shipping or reviewing Workato training content (labs, slide decks, course plans, abstracts, Knowledge Checks, demos) to verify technical claims against the current Workato product surface — feature availability, action/connector names, UI labels, limits, pricing, deprecations. Frame the pillar of Accuracy under The Standards Desk.
---

# Fact Check

A pass that verifies training content against **the current Workato product surface**. Every technical claim, every named feature, every UI label, every limit, every screenshot — checked against what's actually true in the product *today*, not what was true when the content was authored.

The hardest pillar to keep evergreen, because the product moves. The skill encodes verification *protocol* (how to check) and *patterns* (what tends to drift) rather than a fixed list of facts.

## When to invoke

Invoke before:

- **Shipping** any training artifact (lab guide, slide deck, course plan, Knowledge Check, course abstract) to customers or to WoW
- **Republishing** an artifact >90 days after its last verification
- **Citing** a Workato feature, limit, or pricing tier in any external-facing copy
- **Embedding** a screenshot in content that will ship in the next 90 days
- **Designing** a lab around a feature in development (where availability may shift before delivery)

Skip on: internal drafts before content review; experimental material flagged as "not for delivery."

## Posture

Three rules of taste behind the checks:

1. **Verify, don't trust.** Author memory + 6-month-old screenshots are the most reliable source of drift. Re-check against the live product even when "you just checked last week."
2. **Cite or strip.** Every technical claim either has a source you can re-verify (Workato docs URL, Confluence page, run-through date), or it doesn't belong in the content. No claim should live on "I'm pretty sure."
3. **Drift is not a failure — it's a feature of an active product.** When you find drift, the artifact gets a fresh `verified-on:` date, not a blame label. The job is to keep content current, not to keep it pristine.

## Check classification

**Static checks** — a small but high-value set that can run without accessing the live product:
- `feature_ga_dependency` field presence: is the field present on each module? (§1.1)
- GA date vs. delivery date: is every listed feature's GA target ≥2 months before the course delivery date? (§1.1 — date arithmetic, no judgment)
- Screenshot freshness: is the `verified-on` date >90 days old? (§5 — date comparison)
- Required spellings: pattern match against the §7 required-spelling list (Workato, recipe, connector, Datapill, etc.)
- External link resolution: does every URL in the content resolve with a non-error status? (§6)
- `verified-on` field presence: is it present in the artifact's header/frontmatter? (§5)

**Reasoning checks** — everything else. Fact-checking is inherently a live-product verification task:
- Feature availability: is the feature actually GA in the form the content claims? Requires checking release notes, Confluence PRDs, and the live workspace.
- UI label accuracy: do the button names, field labels, and action names in the content match the current live UI? Requires walking the workspace.
- Limits, quotas, and pricing: do the numbers stated in content match current Workato docs? Requires checking docs.workato.com and Confluence.
- Code/API block correctness: does the code actually run and return what the lab claims? Requires execution.
- Screenshot content accuracy: does the screenshot show the correct current UI? Requires visual comparison.
- Customer attribution: is the claim sourced and approved? Requires checking Highspot and sign-off status.
- PM lookup (§1.1.1): requires reading the Confluence PMO page body and querying the Atlassian user lookup API.

## How to apply

Walk the seven check categories in order. Each maps to a common drift pattern.

## §1. Feature availability (does the feature exist in the form claimed?)

Workato ships rapidly. A feature claimed by a lab may be:

- **GA** — broadly available in customer workspaces. Safe to use.
- **In Testing / Private Beta** — available behind a flag or to selected customers. Risky for cross-customer training; lab may fail for some learners.
- **Draft / In Development** — announced but not yet shipping. Cannot be exercised in a lab.
- **Deprecated / Sunset** — was available; removed or replaced. Lab will break.
- **Renamed** — same capability, new name (e.g., *Compose* → *Generate text*). Lab text references the old name.

**Verification protocol:**

1. **Check Workato product release notes** (`docs.workato.com` → release notes) for any feature mentioned in the content.
2. **Check Confluence PRDs / PMO tickets** if available — gives release-state and tier-availability beyond what docs.workato.com surfaces.
3. **Check the WoW workspace** (or whatever training workspace the lab targets) — features may be flagged for some workspaces and not others.
4. **For features in development:** confirm the delivery date is *before* the content's delivery date. If the delivery date moves, the lab needs to move.

**Common feature-availability drift patterns:**

- Lab claims a feature is "new" — feature has shipped to GA and the framing is now stale.
- Lab uses a feature still in private beta — works in author's workspace, fails for half the learners.
- Lab uses *Compose* — feature is now *Generate text*; the UI labels and walkthrough need updating.

### §1.1 Course-module GA dependency tagging (the GA-2-months rule)

For course plans (especially WoW-style instructor-led courses), every module must declare a **`feature_ga_dependency`** field listing which features must be GA before the module can run. This is the Ryan Koh GA-2-months rule, named for the team feedback that established it (WoW 2026 build):

> *"For every module we tag the feature that needs to be GA - 2 months."*

**fact-check verification per module:**

1. The module's `feature_ga_dependency` list is present and accurate (every feature actually needed for the lab/session is listed).
2. **Every listed feature has a confirmed GA date ≥2 months before the course delivery date.** This buffer gives time for: feature stabilization, content updates if the feature ships differently than planned, screenshot refresh, and trainer dry-runs.
3. If any feature is GA-1-month or closer, flag as ⚠️ and note the specific module/lab that breaks if the feature slips.
4. If any feature won't be GA before delivery, flag as 🔴 and require a fallback (different lab, different feature, different module).

**Course-level Roadmap Dependencies table.** Each course's `feature_ga_dependency` entries roll up into a per-course Roadmap Dependencies table at the end of the course plan:

| Feature | PMO | PM | Current status | GA target | WoW-ready? | Impact if delayed |
|---|---|---|---|---|---|---|

WoW-ready values:
- ✅ Yes — GA confirmed with ≥2 months lead time
- ⚠️ Needs confirmation — target date exists but is close or uncertain
- 🔜 Not yet — dependent on other features or no confirmed date

**Impact if delayed** must name the specific module/lab that breaks, not "this course is affected." If the impact note is generic, the entry isn't actionable.

### §1.1.1 PM-lookup protocol (Confluence PMO pages → PM name)

When you need to populate a PM column (or any DRI field) for a feature documented on a Confluence PMO page, walk this protocol in order. **The lookup runs dynamically against whichever PMOs surface during research** — there's no hardcoded list. Phase 0 roadmap research (in workflows like `wow-plan`) produces a set of relevant PMOs based on the course topic; this protocol turns each of those PMOs into a PM attribution.

It works for *any* course topic — Agent Studio, MCP, recipe-building, integration courses, future ADDIE pipelines — because every Workato product feature gets a PMO page with the same authorship metadata.

**Step 1 — Explicit DRI in the page body.** Read the PMO page via `mcp__atlassian__getConfluencePage`. Scan the body for:
- A field labeled `**Author:** <name>` or `**DRI:** <name>` (often in a metadata table near the top, or in a "Document Status" header block)
- A "Revision History" table that names the original author
- A byline below the title

If a DRI is explicitly named, use that name and stop. This is the most-authoritative signal.

**Step 2 — Page metadata `authorId` → user lookup.** If the body has no explicit Author/DRI field, fall back to the page metadata. The `getConfluencePage` response includes `authorId` (the page creator) and `ownerId`. Use the `authorId`:

```
mcp__atlassian__lookupJiraAccountId(
  cloudId: <your workato cloud ID>,
  searchString: "<the full authorId, e.g. 712020:2f7afb5c-4df1-4964-988b-83f48952c340 or 5de63fe422389c0d118c581e>"
)
```

The tool accepts a full Atlassian account ID as the search string (not just a name fragment). It returns `displayName` and email. Record the `displayName` as the PM.

**Step 3 — Fall back to TBD.** If neither the body nor the user lookup yields a name, record `TBD — check with product team` in the PM column.

**Heuristic for default DRI when a page genuinely has no explicit DRI:** If the same person authors multiple adjacent PMO pages in the same product area (e.g., Bennett Goh authors PMO-2078 Guardrails, PMO-2555 Native Channel, PMO-2893 Evals Phase 1 — all under Agent Studio), they're a strong default-DRI signal for related features that don't have their own DRI lines. Note this signal in the table as `<name> (inferred — adjacent-page DRI signal)` so the inference is auditable.

### §1.1.2 PM lookup applied — keep one home, not many

The protocol above lives in `fact-check` so every workflow that needs PM attribution (wow-plan, addie-plan, and any future course-planning skill) calls into the same routine instead of restating it. When the protocol updates (e.g., a new MCP tool replaces `lookupJiraAccountId`), updating fact-check is the only change needed.

---

**PM lookup (one-line summary for workflows that cite this protocol):** The PM column is populated from the Confluence PMO page for each feature via `fact-check §1.1.1` — explicit DRI in body → page-creator account ID → user lookup → TBD if all fail.

### §1.2 Cross-cutting Workato platform changes

Some roadmap items affect every course regardless of topic — they change how the Workato platform works for builders rather than being features being taught. fact-check verifies that these are tracked in a separate **Platform Changes** table that appears once in the course-plan Overview (not per-course):

| Change | Status | Courses affected | Training impact |
|---|---|---|---|

Examples to look for: RBAC 2.0, Decision Models, Workato Expression Language (WEL), Canvas UX redesign. When platform changes land, instructions and screenshots across multiple courses may drift — fact-check catches the drift before delivery.

## §2. UI labels and action/connector names

Workato UI labels drift more often than feature shape. A button renamed, a tab moved, an action reordered.

**Verification protocol:**

1. **Open the Workato workspace** the lab targets.
2. **Walk the lab steps** — every UI label the content mentions, check against the live UI.
3. **Compare against any screenshots** — UI labels visible in the screenshot must match the prose.

**Common UI-label drift:**

- Button or action renamed (*Compose* → *Generate text*).
- Field label renamed (*Source content* → *Inputs*).
- Action reordered within a connector menu (the lab says "third action under Salesforce" — it's now fifth).
- Connector renamed or re-categorized.
- Setting moved between settings panels (e.g., from Account → Workspace).

**The Ghost verification cycle (per `GHOST_CONTRACT §10`)** is the operational form of this check: Ghost runs each task against the live product, captures real screenshots, and files inline `<!-- ghost-note: -->` corrections when reality and the spec disagree. For non-lab artifacts (decks, course plans), the same protocol applies: walk the live product, compare against the content.

## §3. Limits, quotas, and pricing tiers

Workato platform limits change as the product scales. Pricing tiers and feature gating change as packaging evolves. Any number stated in content is a drift candidate.

**Verification protocol:**

1. **Check the current limit/quota** in Workato docs (e.g., 16MB per file, KB ingestion limits, action execution timeouts).
2. **Check pricing tier availability** in the current packaging (e.g., "Agent Studio is available in the Enterprise tier" — was that true 6 months ago? Is it true now?).
3. **For PRD-referenced limits** (not yet in docs), confirm the limit is the current decision, not a draft proposal.

**Common limits/pricing drift:**

- KB file size limit (was X MB; now Y MB).
- Concurrency limits on a Genie's tool calls.
- Feature gating moved between tiers (Genie X is now available in tier Y where it wasn't before).
- Action execution timeouts (e.g., HTTP connector timeout default).

**Anti-pattern:** *quoting a limit from a draft PRD as if it were live policy*. PRDs change; cite a doc, not a draft.

## §4. Code, configuration, and API blocks

Code blocks in labs and decks must compile or execute against the current platform.

**Verification protocol:**

1. **Run every code block** in the target Workato workspace (or sandbox).
2. **For API blocks** (Workato Developer API, third-party APIs): run the actual call, confirm the response shape matches the lab's claim.
3. **For formula-mode expressions:** evaluate against a real datapill or test value.
4. **For deprecated APIs:** check the Workato API changelog / Confluence for any deprecation notes.

**Common code-block drift:**

- Connector action signature changed (input/output field renamed or removed).
- Formula function renamed or signature changed.
- API endpoint deprecated; new endpoint required.
- Third-party connector version updated, breaking field paths.

**For non-Workato code** (Python, Mustache, SQL, JSON examples): drift is rarer but possible. Re-run before publishing.

## §5. Screenshot freshness

Screenshots drift the moment the UI updates. Old screenshots are the #1 trust erosion in training content.

**Rule:** screenshots ≤90 days old. Re-capture against the live workspace if older.

**Verification protocol:**

1. **Check the screenshot file timestamp** or the `verified-on:` date in `decisions.yaml`.
2. **If >90 days:** re-walk the lab against the live UI and capture fresh.
3. **For each screenshot:** verify UI matches the surrounding prose. Caption must match what's actually visible.

**Anti-patterns:**

- Annotating an old screenshot with new labels (the underlying UI is wrong; annotation lies).
- Using a "representative" screenshot from a different feature ("close enough").
- Photoshop / image-edit fixes to UI elements (always lies).

## §6. External links

Every URL in content must resolve. Workato docs URLs drift; third-party URLs go 404; Confluence pages move.

**Verification protocol:**

1. **Curl or browse every URL** in the content.
2. **Check redirect chains:** a 301 to a different topic is broken even if the page loads.
3. **Check Confluence URLs:** they're internal; some learners won't have access.

**Common link drift:**

- Workato docs URL — page moved or renamed.
- Confluence URL — page moved between spaces; access changed.
- Third-party doc URL — vendor restructured (Salesforce, Jira, Slack all do this).
- API reference URLs — versioned URLs may sunset.

## §7. Workato-specific terminology and required spellings

The Workato product surface has specific spellings that drift in author memory.

**Verification protocol:**

Cross-reference content against the **Workato Education and Training wordlist** (Confluence: `ETT/758775978`) and the **Workato product stylization** guide (Confluence: `PPD/347407142`). When in doubt, the docs.workato.com spelling wins.

**Required spellings** (commonly missed):

- `Workato` (never `WorkAto`, `workato`, `Workato.com` mid-sentence)
- `recipe` (lowercase — the product noun)
- `connector` (lowercase)
- `Connection` (capitalized when it is the UI noun for an established auth)
- `Recipe Lifecycle Management` (no abbreviation in content; *RLCM* may be used in dev-facing copy only)
- `Datapill`, `Datapills`, `Datatree` — each one word, no spaces
- `Knowledge Checks` — always full term ([[feedback_knowledge_checks_naming]])

**Never:** abbreviated forms in customer-facing content unless explicitly approved (see [[feedback_omnifocus_naming]] for the same principle applied to OmniFocus).

## §8. Customer attribution and privacy

When training content references customer data — anonymized or named, in narration or scenarios — the same verification discipline applies as for product facts. Attribution and privacy are factual claims about the customer; they need cite-or-strip handling.

**Verification protocol:**

1. **Anonymize by default.** Industry + size + role beats company name. *"A mid-market SaaS customer"* is verifiable from a description; *"Acme Corp"* needs explicit approval.
2. **Cite attribution only with explicit approval.** Named customers, named individuals, named accounts — only with Marketing/Sales sign-off, and ideally cross-referenced against the approved-for-external-use catalog in Highspot.
3. **Verify metrics at source.** Quantified outcomes (*"40% reduction in..."*) need a traceable source (Gong call ID, Salesforce report, Highspot case study). Author memory is not a source.
4. **Don't expose internal customer data.** ARR, pipeline, churn risk, health scores, and similar fields don't appear in customer-facing content even when anonymized.
5. **Document data lineage during authoring.** When a proof point or scenario draws on customer data, track the source in author/review notes (not in learner-facing content) so the claim can be re-verified during the next freshness pass.

**Common attribution drift:**

- Customer name in content that was approved 18 months ago — re-verify; permissions may have lapsed.
- Anonymized scenario that's re-identifiable from the detail combination (industry + region + size + use case can triangulate).
- Quantified outcome cited in narration with no source in author notes — the claim is unverifiable; strip or re-source.
- Internal data field (health score, expansion ARR) used as a proof point — never appropriate in customer-facing content even with consent.

**Source:** ADDIE pipeline Customer Privacy & Ethics guidelines (Workato Academy ETT, 2026). The check is a peer to product fact-checking — customer attribution is a factual claim, and it drifts the same way product references drift.

## Verification cadence

| Artifact type | Default verification interval | Re-verify trigger |
|---|---|---|
| Lab guide (active delivery) | 90 days | Major Workato release; feature deprecation; UI redesign |
| Slide deck (active delivery) | 90 days | Same |
| Course plan / abstract | At authoring + 30 days before delivery | Feature roadmap shift |
| Knowledge Check | Same as parent lab/module | When parent lab is re-verified |
| Course bundle (in WoW workspace) | 30 days before each delivery date | Workspace reset; new tenant config |

After re-verification, update the `verified-on:` field in the artifact's `decisions.yaml` (per `GHOST_CONTRACT §10`) or equivalent header field.

## What this skill is NOT

- **Not authoritative on Workato product behavior** — that's the live product + Workato docs + the product team. This skill is a *protocol* for checking against those sources, not a replacement for them.
- **Not a stylistic editor** — fact-check verifies *correctness*, not *quality*. Style is `say-it-plain` + `team-style-guide`.
- **Not a completeness check** — fact-check verifies *what's there is true*; complete-check verifies *the right things are there*.
- **Not for non-Workato content** — the skill is Workato-product-specific. Other content has its own source-of-truth checking.

## Source priority

When fact-checking, resolve conflicts in this order:

1. **The live Workato product surface** (the running UI in the target workspace)
2. **docs.workato.com** (official product documentation)
3. **Confluence PRDs / PMO tickets** (forward-looking; useful for features pre-GA)
4. **Workato Education and Training wordlist + style guides** (terminology)
5. **Product team / engineering Slack channels** (for behavior the docs haven't caught up to)
6. **Author memory** (only as a starting hypothesis to verify)

When the live product disagrees with the docs, the live product wins — and the docs get a bug report.
\
"""
# stick-check
RUBRIC_STICK_CHECK = """\
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
# calibrate-challenge
RUBRIC_CALIBRATE_CHALLENGE = """\
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
# delight-check
RUBRIC_DELIGHT_CHECK = """\
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
# team-style-guide
RUBRIC_TEAM_STYLE_GUIDE = """\
---
name: team-style-guide
description: Use when authoring or reviewing Workato training content (lab guides, slide decks, course bundles, Knowledge Checks) for surface-level style — typography, color, casing, punctuation conventions, brand, required spellings, banned terms. Peer to say-it-plain under the Style pillar; say-it-plain handles prose, this handles everything else.
---

# Team Style Guide

The Workato training team's surface-style pass. Covers typography, color, casing, punctuation conventions, imagery, layout, brand, required spellings, and banned terms. Peer skill to `say-it-plain` (which handles sentence-level prose) under the Style pillar of The Standards Desk.

## When to invoke

Before publishing any Workato training artifact:

- Lab guides (HTML — Standard or Print)
- Slide decks (training, customer-facing)
- Course bundles, module pages
- Knowledge Check screens
- Internal-team training materials that will travel

Skip on: code, private notes, chat messages, drafts that haven't reached coherent shape yet (run `say-it-plain` first).

## Check classification

**Static checks** — the overwhelming majority of this pillar. Nearly everything is a threshold, a count, a spelling, or a pattern match:
- §1 Typography: font size floors and ceilings, max families per slide, max font sizes per slide, casing rules (Title Case vs. sentence case), ALL CAPS detection, semantic formatting presence
- §2 Color: WCAG contrast ratio (≥4.5:1 normal / ≥3:1 large text), max color count per artifact, palette compliance (approved colors only), color-only meaning detection
- §3 Punctuation: bullet terminal punctuation per surface, heading terminal punctuation ban, step terminal punctuation (`.?!:;…`), exclamation mark count (max 1)
- §4 Imagery: DPI floor (≥150), format check (png/jpg/svg only), max count per slide (3), size percentage check (10–70% of slide area), alt text presence
- §5 Layout: margin floor (0.5"), max text boxes per slide (4), content height ceiling (4.2"), element overlap detection
- §6 Content density: all word/bullet/sentence count limits
- §7 Brand: logo presence on bookend slides, slide numbers on non-title slides
- §8 Required spellings: exact pattern match
- §9 Banned terms: exact pattern match
- §10 Callout vocabulary: valid class name check (note/tip/warning/pitfall/key-insight)

**Reasoning checks** — a small set where judgment is unavoidable:
- §4 Image content relevance: "content-relevant, no stock clichés" — requires evaluating whether the image strengthens the surrounding content. A DPI check doesn't tell you if it's a hand-shake-on-a-laptop stock photo.
- §11 Allowed exceptions: "Workato magic" staying in-bounds, other team-specific carve-outs — requires understanding context and intent, not just pattern matching.
- Surface mismatch evaluation: when a rule conflict exists between surfaces, determining which profile applies requires reading the artifact and understanding its context.

## Source authorities

Order of precedence when this skill doesn't cover a specific case:

1. **AP Stylebook** — general written conventions.
2. **Conscious Language guidelines** — inclusive vocabulary.
3. **Google Developer Documentation Style Guide** — technical-writing conventions.
4. **Microsoft Writing Style Guide** — UI-facing conventions.
5. **This skill** — Workato-specific consolidations and overrides.

For Workato product terminology: the Workato Documentation style guide and Education and Training wordlist (internal Confluence pages) override the external references.

## Surface profile

This skill applies across surfaces, but five rules **diverge by surface** — labs and slides intentionally part ways. The surface itself sets the choice; this skill carries both profiles.

| Rule | Slide deck | Lab guide |
|---|---|---|
| Heading/title case | Title case | Sentence case |
| Bullet terminal punctuation | No period | Period (AP) |
| Emphasis weight | Poppins SemiBold (never bold) | Bold |
| Body font floor | 14pt absolute, 16pt operational | 12pt floor |
| Contrast | Floor only — projection eats softness | Floor + near-black/near-white for long-form |

Outside these five, surfaces align.

When invoked, **determine the surface first** and apply the matching profile.

## 1. Typography

**Font sizes:**

| Element | Slide deck | Lab guide |
|---|---|---|
| Body | 16pt operational, 14pt floor | 12pt floor |
| Bullets | 16pt | 12pt floor |
| Slide / page headers | 24pt | 24–28pt |
| Section headers | 24–28pt | body + 1–2pt, bold |
| Title slide / lab title | 36pt / lab `<h1>` | n/a / `<h1>` |
| Absolute floor | 14pt anywhere | 12pt anywhere |

**Weights:**

- Slides: **Poppins SemiBold** for all emphasis. **Never bold.**
- Lab guides: **bold** for emphasis.

**Font families:**

- Max 2 families per slide or page.
- Max 3 font sizes per slide (title, subtitle/header, body).

**Casing:**

- Slides: **title case** for titles (`Build a Customer Onboarding Recipe`).
- Lab guides: **sentence case** for all headings, including the lab title and Task titles (`Lab 2: Build a customer onboarding recipe`, `2.3 Configure the Salesforce trigger`).
- **No ALL CAPS** in body text on either surface — reduces readability.

**Semantic formatting:**

- Use the template's heading and body styles. Don't manually resize.
- HTML labs: `<h1>`, `<h2>`, `<h3>`, `<strong>`, `<em>`, `<code>` carry structure. No deeper than `<h3>`.
- Slides: use named layouts. No ad-hoc layouts.

**Text formatting conventions (labs):**

- **boldface** — GUI elements associated with action (`Click Save`); terms defined inline.
- *italic* — book titles; emphasis (sparingly); placeholder variables (`<your-account-name>`).
- `monospace` — commands inline; URLs; code blocks; text on screen; text the learner types.

## 2. Color

**Palette:**

- 3–5 brand palette colors per artifact.
- Approved Workato brand colors only.
- **Teal accent (`#108291` dark teal):** bullets, blockquotes, key takeaways. Chosen for WCAG AA compliance.

**Color usage:**

- **One meaning per color.** Don't use red for both errors and emphasis.
- **Never color-only meaning.** Pair color with icons, labels, or patterns.
- Lab guides (long-form): prefer near-black (`#1a1a1a`) on near-white (`#fafafa`) over pure `#000` on `#fff`. Long dwell time benefits from softened contrast.
- Slides: no softness ceiling. Projection eats contrast.

**Floor (both surfaces):** WCAG 2.1 AA — ≥4.5:1 for normal text (<18pt), ≥3:1 for large text (≥18pt, or ≥14pt bold).

## 3. Punctuation

**Bullets:**

- **Slide decks:** no terminal period. Bullets are scannable phrases.
- **Lab guides:** AP-style period. Capitalize the first letter, end every bullet with a period.

**Headings:**

- Never end in terminal punctuation on either surface.

**Lab Steps:**

- Every Step ends with `.`, `?`, `!`, `:`, `;`, or `…`.

**Exclamation marks:**

- Default zero per artifact. Absolute ceiling: one per deck or lab. Excitement-performance erodes trust.

## 4. Imagery

- **Content-relevant.** Image strengthens the text. No stock clichés.
- **Attribution.** Source in the image title field (`![alt](path "Photo by Jane Doe, Unsplash")`) or visible caption when required.
- **Internal-only artifacts:** real Workato team-member photos when a person is depicted.
- **Quality:** ≥150 DPI. Formats: png, jpg, svg.
- **Quantity (slides):** max 3 images per slide.
- **Size (slides):** max 70% slide area, min 10%.

**Lab screenshots:**

- Inline captions state the action (`Setup menu with API highlighted`), not the element identity.
- Tight crop carries the targeting. No bounding boxes, arrows, or overlays unless explicitly requested.
- Alt text equals caption.

**Picture Superiority guard (slides):** no more than 3 consecutive text-only slides. Break up runs with a relevant visual.

## 5. Layout

**Single-column flow:**

- Top-left for the title (eye-entry point).
- Bottom-right for navigation or key takeaway (eye-exit).
- Body text left-aligned (natural reading direction).

**White space:**

- Slide margin: minimum 0.5".
- No overlapping elements.
- Slides: max 4 text boxes per slide. Prefer single-column flow.

**Slide content safety:**

- Usable content height ≤4.2".
- Safe bottom at 5.0". Content below may overlap logo or slide number.
- Vertical flow — elements stack top-to-bottom, no horizontal sprawls.

**Image handling:**

- Aspect ratio preserved. Fit within bounding box; no stretching.

**Slide title position consistent:** top-left, same position across every slide in the deck.

**Lab chunking:**

- ~120 words per visible page-section.
- 1–3 sentence chunks.
- Pages under ~120 words get read at ~50%; pages much longer get read at ~20%. Cut ruthlessly; front-load value.
- Optimize for scanning: headings, lists, breaks, callouts.

## 6. Content density (slides)

Slides are scanned, not read.

- **Max words per slide: 120.** Hard ceiling.
- **Max words per split-layout slide: 50.** Image + text shares space.
- **Max bullets per slide: 6.** Keep lists scannable.
- **Max words per bullet: 25.** Phrases, not sentences.
- **Max nested bullet depth: 2.**
- **Max sentences per paragraph: 3.**
- **Key takeaway supporting text: max 15 words.**
- **No blank slides.**
- **No dangling words.** Single-word widows on the last line trigger a rewrite or size override.

## 7. Brand

**Logo:**

- Workato logo present on bookend slides (title and final).
- Workato logo present bottom-left on all non-title slides.

**Slide numbers:**

- Slide number bottom-right on all non-title slides.

## 8. Required spellings

- `Workato` (never `WorkAto`, `workato`, `Workato.com` mid-sentence)
- `recipe` (lowercase, the product noun)
- `connector` (lowercase)
- `Connection` (capitalized when it is the UI noun for an established auth)
- `Recipe Lifecycle Management`
- `Datapill`, `Datapills`, `Datatree` — each one word, no spaces
- `Knowledge Checks` — always full term

## 9. Banned terms

**Never write "pedagogy"** — including `pedagogical` and `pedagogically`. The word means "leading children" and is off-register for adult enterprise learners. Substitute: `adult learning`, `andragogy`, `instructional approach`, `learning effectiveness`. Banned in both artifacts and conversation.

**Never abbreviate Knowledge Checks** — never `KC` or `KCs` in any context (prose, slides, code symbols, filenames).

**Never abbreviate OmniFocus** (if referenced) — never `OF`.

**Never frame Workato as "hard."** Complexity belongs to the problem domain (enterprise integration) or the depth of the capability ("with great power comes real depth"). Never Workato itself.

**Banned verb "fire" in Tinsel Town copy.** Use `emit` (events), `runs`/`triggers` (animations), `issue`/`send` (HTTP). Especially HR-adjacent contexts.

**Don't use "spine" as a metaphor.** Skip "content spine," "lab spine." Use "match list" or name the fields directly.

**Never name a customer in learner-facing content without explicit approval.** Even anonymized references (industry + role + size) should pass a re-identification check before publishing. Named customers, named individuals, or named accounts require Marketing/Sales sign-off cross-referenced against Highspot's approved-for-external-use catalog. See `fact-check §8` for the verification protocol.

## 10. Callout vocabulary

Authoring vocabulary uses six branded boxes:

- **Notes** — supplementary context.
- **Info** — background information; non-blocking.
- **Success** — confirmation a step worked correctly.
- **Warning** — be careful here; non-blocking.
- **Error** — what to do when something breaks.
- **Tip** — optional efficiency or insight.

Operational HTML rendering compresses these to five classes — `note`, `tip`, `warning`, `pitfall`, `key-insight` — with Success rendered via `note` and Error via `warning`. The six are the authoring vocabulary; the five are the runtime classes.

## 11. Allowed exceptions

**Workato magic.** `Workato magic` and `magic` (when describing the customer experience of Workato) stay in-bounds. Training team motto: "allow the world to experience the Workato magic." Other superlatives still get cut.

**Audit case as data, not opinion.** Run mechanical checks where possible (font size, weight, hex, contrast ratio, terminal punctuation, banned-term substrings). Reserve judgment for cases where the rule has a "prefer" or "default."

## Edit pattern

When a check fires:

1. **Surface mismatch?** Apply the correct surface profile.
2. **Banned term?** Substitute from the list.
3. **Contrast / size below floor?** Raise to the floor; document if exceeding the operational target.
4. **Color carries meaning alone?** Pair with icon, label, or pattern.
5. **Casing inconsistent?** Apply the surface's casing rule across all headings.

If a rule conflicts with a surface-specific decision logged in `Lab Guide Standards.md §0` or `Presentation Content Standards.md §0` override log, the override wins. This skill is upstream; the surface override log carries the locked downstream choice.

## Downstream consumers

- `Lab Guide Standards.md` §6 — composes this skill into the lab surface.
- `Presentation Content Standards.md` §§4, 6, 9, 11 — composes this skill into the slide surface.
- `HTML Lab Style Guide.md` + `html-lab-rules.yaml` — Lab Buddy's operational kit; mirrors the lab-surface rules from this skill.
- DoubleChecker (Bakery), Gatekeeper, Coach — consume directly when reasoning about Style at the surface layer.
\
"""
RUBRICS = {
    "say-it-plain": RUBRIC_SAY_IT_PLAIN,
    "fact-check": RUBRIC_FACT_CHECK,
    "stick-check": RUBRIC_STICK_CHECK,
    "calibrate-challenge": RUBRIC_CALIBRATE_CHALLENGE,
    "delight-check": RUBRIC_DELIGHT_CHECK,
    "team-style-guide": RUBRIC_TEAM_STYLE_GUIDE,
}

PILLAR_AUDIENCES = {
    "say-it-plain":        ["training","education","workato"],
    "fact-check":          ["training","education"],
    "stick-check":         ["training","education","workato"],
    "calibrate-challenge": ["training","education"],
    "delight-check":       ["training","education","workato"],
    "team-style-guide":    ["training","education"],
}

def main(input):
    audience = (input.get("audience") or "workato").strip().lower()
    raw = input.get("pillars_json") or "[]"
    try:
        requested = json.loads(raw)
    except Exception:
        requested = []
    if not requested:
        requested = list(RUBRICS.keys())
    result = {}
    for p in requested:
        if p in RUBRICS and audience in PILLAR_AUDIENCES.get(p, []):
            result[p] = RUBRICS[p]
        elif p in RUBRICS:
            result[p] = ""  # not applicable for this audience
    return {"rubrics_json": json.dumps(result)}
