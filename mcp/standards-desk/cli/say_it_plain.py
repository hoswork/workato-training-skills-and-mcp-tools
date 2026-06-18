"""
say-it-plain — snippet 1 (rules + rubric).
Audience variants: training keeps "Workato magic" exempt; workato strips internal carve-outs.
"""

RUBRIC = ""
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

JARGON = [
    "leverage", "utilize", "synergy", "paradigm", "best-in-class", "circle back",
    "deep dive", "game-changer", "game changer", "disruptive", "revolutionary",
    "10x", "crush it", "killing it", "rockstar", "ninja", "guru", "hack",
    "unlock", "supercharge", "turbocharge", "skyrocket", "empower", "democratize",
    "seamless", "frictionless", "robust", "scalable", "world-class", "cutting-edge",
    "next-gen", "enterprise-grade",
]

FILLERS = ["very", "really", "just", "basically", "actually", "simply", "obviously", "clearly"]

SUPERLATIVES = [
    "best", "fastest", "easiest", "most powerful", "incredible", "amazing",
    "awesome", "insane", "unbelievable", "mind-blowing", "stunning", "killer",
    "epic", "legendary", "ultimate", "perfect", "unmatched", "unparalleled",
    "unprecedented",
]

URGENCY = [
    "act now", "don't miss", "limited time", "before it's too late",
    "you can't afford", "what are you waiting for",
]

SECOND_PERSON_HYPE = [
    "you need this", "you won't believe", "you'll love", "you deserve",
    "imagine if you",
]

SINCERITY_TELLS = ["honestly", "to be honest", "frankly"]

AGENTIC_OVERREACH = [
    "act autonomously", "reason over", "reason about",
    "understands", "learns on its own", "thinks for itself",
    "decides for itself",
]

REGEX_PATTERNS = [
    {
        "pattern": r"\b(the only|the first|the fastest|the most|no one else|nothing else|unlike anything)\b",
        "message": "Unsubstantiated absolute — remove or add evidence",
        "ignore_case": True,
    },
    {
        "pattern": r"\b(was|were|is|are|been)\s+\w+ed\b",
        "message": "Passive voice — consider active construction (soft check)",
        "ignore_case": True,
    },
]


def _rules(audience):
    banned = JARGON + FILLERS + URGENCY + SECOND_PERSON_HYPE + SINCERITY_TELLS + AGENTIC_OVERREACH
    # Superlatives are included but context-sensitive — include as soft signal
    banned += SUPERLATIVES

    if audience == "training":
        # Training team motto: "Workato magic" stays in-bounds
        banned = [p for p in banned if p.lower() not in ("magic",)]
    elif audience == "education":
        # ETT shares the training carve-out
        banned = [p for p in banned if p.lower() not in ("magic",)]
    # workato audience: full banned list, no carve-outs

    return {
        "applicable": True,
        "banned_phrases": banned,
        "regex_patterns": REGEX_PATTERNS,
        "exclamation_max": 1,
    }


def main(input):
    audience = input.get("audience", "workato")
    return {
        "rubric": RUBRIC,
        "rules": _rules(audience),
    }
