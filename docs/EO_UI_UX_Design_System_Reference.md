# EO Creative Ops — UI/UX Design System & Competitive Reference Library

> **Verbatim Reference Compilation** from official platform design documents.

---

## 📚 Competitive Case Studies & Industry Benchmarks (`EO_Competitive_References_v1.md`)

# EO Competitive References v1

**Status:** Reference document. Not a spec. Nothing here amends the frozen 1.0.
**Date:** 28 July 2026
**Purpose:** Named, verified competitor evidence for pitch prep and build reference.

---

## 0. How to use this document

Three jobs:

1. **Pitch defence.** When leadership asks "can't we just buy something?", §5 is the answer with named products behind it.
2. **Build reference.** §3 and §4 list specific mechanics worth studying, per open question — not per product quality.
3. **Contamination control.** §2 records four claims that were checked and failed. Do not re-import them into the next research round.

**Verification legend used throughout:**

| Mark | Meaning |
|---|---|
| ✅ | Verified this pass against vendor documentation or support pages |
| ⚠️ | Second-hand from another research pass. Plausible, not verified. Verify before citing to Ramon. |
| ❌ | Checked and false |

No product was trialled. All ✅ claims come from vendor-published documentation, which is marketing-adjacent. Treat capability claims as "the vendor says this exists," not "this works well."

---

## 1. Provenance

Six independent research passes were run. This document reconciles them.

| Pass | Agent / source | Read official docs? | Verdict |
|---|---|---|---|
| 1 | Hermes (tencent/hy3) | No | Good lane coverage. Flagged its own Ziflow risk, then ranked Ziflow #2 anyway. |
| 2 | Gemini (first) | Partial | Grounded on 70+ branches. Introduced Aproove, ReviewStudio, Esko, EFI Pace. |
| 3 | Function Benchmark Report | No | **Strongest prior pass.** Best critical work. ReviewStudio finding originated here. |
| 4 | Multi-Branch Collateral Report | No | Wrong architecture assumption. Four invented EO facts. See §2.5. |
| 5 | Gemini / Antigravity (official docs) | Yes | Correct domain profile. Two false product claims. |
| 6 | Gemini / Antigravity (competitors) | Yes | Introduced RoboHead (holds up) and Rocketlane. |
| 7 | Claude (this pass) | Yes, via project record | Opened three unexamined lanes. Ran the verifications in §2. |

Roughly 40 distinct products were named across all passes. Ten survive as worth studying.

---

## 2. Corrections — do not re-import

### 2.1 Branch count: 400+, not 70+ ❌

Passes 2, 3 and 4 all reason from "70+ branches." Passes 5 and 6, which read the official docs, confirm **400+**. The 70 was contamination propagated between agents.

**Consequence:** Pass 4 built its buy-vs-build verdict on $42k–$168k/yr licensing for 70 locations. At 400 the same per-location rates give roughly $240k–$960k/yr. Its own conclusion inverts. See §5 for why the per-location figure is the wrong argument anyway.

### 2.2 PageProof does not do derived return routing ❌

Passes 5 and 6 both claim PageProof "automatically returns revised proofs to the exact person who requested changes" and maps to INV-18.

It does not. PageProof documentation states that a gatekeeper decides whether the proof continues through the workflow or is returned **to the proof owner** with a to-do list; the final approver likewise either approves or returns a to-do list to the proof owner. The return address is **fixed**, not derived.

**What PageProof is actually a good reference for:** see §4.4. The correction is more useful than the claim was.

**The larger finding:** across all six passes and ~40 products, **no product implements derived return routing.** Everything returns to a fixed address — usually the originator. INV-18 is genuinely novel. That is good for the pitch and it is also the single highest-risk item in the build, because there is no reference implementation to check the logic against.

### 2.3 Artwork Flow is not a placement-library reference ❌

Pass 5 ranks Artwork Flow #2 and asserts it "stores placement specifications and physical dimensions" and "location-based graphic specifications" across retail branches.

Unsupported. Artwork Flow is CPG and label compliance — artwork per SKU, barcode and claim verification, packaging variants. The unit of organisation is a **product**, not a **place**.

Do not build the Branch Placement Library against it. Use SignAgent (§4.1).

### 2.4 "Pending Release" no longer exists ❌

Pass 6 references "the CD Hard Gate (LC-04) where a job cannot proceed to **Pending Release**." That stage was removed. CD sign-off lives inside Internal Review per Spec v3/v4; the Invariants/Workflows contradiction was resolved and Invariants bumped to v2 with INV-17–20.

Pass 6 claims to have read Workflows v3, which contains the corrected state machine. Treat its state-machine reasoning as unreliable, and its product mappings to specific INV numbers as unchecked.

### 2.5 Pass 4 answers a different product ❌

Pass 4 assumes the franchise brand-portal architecture: every branch has an account and files its own requests. MarcomCentral, Xpressdocs, Prindustry, Phase3 and the whole web-to-print storefront lane presume 400 branch logins.

EO does not work that way. Requests are filed by a small number of Requestors **on behalf of** branches. Branch is a target, not a user. This makes most of Pass 4's landscape section structurally irrelevant.

Pass 4 also invents four EO facts that appear nowhere in the spec:

- multi-step optical-pricing validation
- per-branch doctor schedules rendered in artwork
- POS/inventory integration
- offline-capable branch workflows

**None of these may reach the pitch.** If Ramon asks about POS integration because it surfaced in a research doc, you are defending scope you never wrote.

---

## 3. The 10, ranked by open question

Ranked by what is still undecided in the build — not by product quality.

| # | Product | Category | Open question it answers |
|---|---|---|---|
| 1 | **SignAgent** ✅ | Signage/wayfinding lifecycle | Branch Placement Library (D-018/D-019) |
| 2 | **ReviewStudio** ✅ | Creative proofing | Two-channel Activity (INV-12), including version privacy |
| 3 | **shopVOX** ✅ | Sign/print shop MIS | Print tail; memory surviving JO closure |
| 4 | **PageProof** ✅ | Proofing / approval | Revisions as a resolved to-do list; gatekeeper placement; unlock-by-request |
| 5 | **Simple Admation** ✅ | Marketing approval governance | Type-scoped approver chains; brief approved before work starts |
| 6 | **RoboHead** ✅ | In-house creative ops | Conditional intake forms; workload as % allocated |
| 7 | **Enfocus Switch + PitStop** ⚠️ | Preflight / automated routing | Rule-driven routing — nearest analog to INV-18 |
| 8 | **Esko WebCenter** ⚠️ | Packaging artwork mgmt | One parent JO → N branch variants |
| 9 | **Bindy** ✅ | Retail audit / execution | The missing tail: proof of install at branch |
| 10 | **Zipline** ✅ | Retail HQ→store ops | The Viber argument (pitch weapon, not build reference) |

**Baseline — no longer needing study.** Ziflow, Aproove, Lytho, Adobe Workfront, Wrike, Filestage. All competent, all covered by the ten above on every dimension that matters here.

**Design references, not workflow references.** Linear, Monday. Already in use for BIFOCAL. Do not let them into workflow discussions.

**Actively misleading for EO's architecture.** MarcomCentral, Xpressdocs, Prindustry, Marq, Artwork Flow, EFI Pace. Each presumes either branch logins or product-as-primary-object.

---

## 4. Detail — Steal / Skepticize

### 4.1 SignAgent 🥇 ✅

*The located-asset reference.* Wayfinding and signage lifecycle management, three modules (Design, Build, Manage). The only product found across all six passes where **a sign at a place, with a spec and a history, is the primary object.**

**Steal:**

- **Location plans as substrate.** Floor plans are uploaded and sign locations placed directly on top of them. Each placed sign links to a sign type from the library, so data stays connected. Multi-page PDFs auto-split into separate locations.
- **Sign type as standards library.** One sign type carries layouts, rules, fields, materials, specs and artwork templates. Designers reuse types across projects instead of rebuilding. This is your material law, structured — and it is the mechanic that makes Branch → Placement → Sizes coherent rather than three loose tables.
- **Batch propagation.** When something changes, affected signs update individually or in batches, with approvals and comments tracked and schedules exported without manual reconciliation.
- **As-built survey to build inventory.** Most organisations start by surveying existing signage via the mobile app, capturing photos mapped to exact locations. That is your placement historical log, populated once at the start rather than accumulated over years.
- **Scoped permissions.** Teams and vendors see only what they are responsible for — scoped by location, sign type, or project phase.

**Skepticize:**

- Project-shaped, not request-shaped. A wayfinding rollout has a start and an end. It has no intake queue, no Requestor role, no craft review loop.
- It solves Angle 3 and ignores Angles 1–2 entirely.
- Sign templates live in Illustrator, outside the platform.

### 4.2 ReviewStudio 🥈 ✅

*The two-channel reference.* Originated in Pass 3; verified and expanded here. Richer than either pass reported.

**Steal — five mechanics:**

1. **Privacy is declared once, per participant, not per comment.** Each user or guest is marked internal or external. Internal members always see everything. Explicitly designed so internal users never have to remember to mark a comment private.
2. **Default private, explicit reveal.** Every internal comment is private by default. The internal member overrides per comment via an `@mention` of an external member, an `@external` alias that reveals to all externals, or by clicking the privacy icon.
3. **Status icon on every comment.** All comments and replies display an icon showing internal-private or external-visible status. **This is a hard UI requirement for the Activity feed** — the AD needs to know at a glance whether a note is about to be seen by a Requestor.
4. **Version privacy, not just comment privacy.** An internal version invisible to external reviewers can be converted to an external version to become visible to all. This is In Layout drafts hidden from the Requestor, then promoted at the review gate. **This mechanic is not currently specified.**
5. **Lock and record.** A review can be set to Locked, or auto-locked by setting a deadline. Feedback prints to PDF as an offline record. That is the Approval Sheet.

Also: an org-wide setting establishes when a file counts as approved with multiple approvers — "All Approvers" versus a subset.

**Skepticize:**

- Their external party is a paying client with mildly adversarial interests. Your Requestor is a colleague. The trust model differs.
- **Exclusive mode is almost certainly wrong for EO.** In exclusive mode external users see only their own comments. Multi-branch JOs need Requestors seeing a shared thread. Take inclusive.
- Review-scoped, not lifecycle-scoped. A Review is a bundle of files, not a job in custody.

**Decision this forces:** on a multi-branch JO, do all Requestors on that JO see one another's comments? Currently unspecified. ReviewStudio proves this is a real fork, not a detail.

**Pricing reference:** Pro $15/user/month, Advanced $25/user/month.

### 4.3 shopVOX 🥉 ✅

*The custody-through-print reference.* Sign, print and apparel shop management. Chosen over Printavo — which Passes 1 and 2 both picked — for two features Printavo lacks.

**Steal:**

- **Job Notes recalled on reorder.** Notes added to a job are copied to the work order and recalled when the job is reordered. Institutional memory that survives the job closing — exactly what the placement historical log is reaching for, solved at the job level rather than the placement level.
- **Image Notes.** On-site survey photos are annotated to store measurements, install instructions and design ideas. Photo plus spec plus intent, attached to the physical thing.
- **Custom workflow stages.** Stages configured to match the shop's own process, rendered as a job board viewable as kanban, calendar or filterable list.
- **Timestamped proof sign-off** tied to the job rather than living in email, so the approved artwork is unambiguous at print time.

**Skepticize:**

- The requestor is a paying customer. There is no internal advisory stage and no craft review at all — approval is commercial, not editorial.
- Take the memory mechanics. Leave the state machine.

### 4.4 PageProof ✅

*The revision-payload reference.* Repositioned after the §2.2 correction.

**Steal:**

- **Revisions leave review as a resolved action list, not a comment thread.** The approver reads all comments, clarifies instructions where needed, and marks which comments become to-dos. Marked pins change from grey to red. The artist receives decisions, not raw disagreement. **This is the strongest answer found in six passes to the conflicting AD/CD notes problem.**
- **Gatekeeper role placement.** Used sparingly — documented as typically an agency creative director in the first workflow step. Independent confirmation that your CD sits where you put him.
- **Lock plus request-unlock.** A proof locked by gatekeeper, approver or owner can only be unlocked by request. Clean mechanic for the hard gate: locked is a state, unlocking is an event with an author.
- **Step conditions.** Each workflow step can require all mandatory decisions, one, or a set number. Reviewer roles are reviewer / mandatory reviewer / gatekeeper / approver — a four-tier hierarchy where you currently have two.
- Workflow templates are saveable, shareable and favoritable.

**Skepticize:**

- Return address is fixed to the proof owner. See §2.2. Do not model INV-18 on this.
- Proof-centric. The file is the object.

### 4.5 Simple Admation ✅

*The governance-spine reference.* Closer to EO than Lytho on one axis: its primary object is the **brief**, not the proof. Same as yours — a JO in custody.

**Steal:**

- **Approver chain selected by asset type via smart templates.** The requester picks a template; the correct chain follows. Your JO-type-scoped routing.
- **Brief approved before creative work begins.** Multi-user briefing lets nominated stakeholders approve the brief upstream, cutting downstream revisions.
- **Feedback consolidated and deduplicated before it reaches the creative team.** Stated as one of three changes that most reliably reduce revision rounds. Pairs with PageProof's to-do list mechanic.
- Tiered approval levels, mandatory checklist completion as a hard precondition for sign-off, immutable audit trail.

**Skepticize:**

- Built for regulated finance, insurance and health. Heavy. No location concept, no print routing, no in-house/vendor split.
- Its AI compliance checking against uploaded rule sets is a tempting rabbit hole. **Not v1.**

### 4.6 RoboHead ✅

*The intake and workload reference.* Built specifically for in-house marketing and creative teams. Verified after being introduced in Pass 6.

**Steal:**

- **Conditional-logic intake forms.** Questions show or hide based on what the requester selects, so the requester sees only relevant fields rather than a wall of questions. That is RQ-04 type-scoping, shipping.
- **Workload as percentage allocated.** A workforce insights report shows the percentage of each team member's time already allocated to other projects. Views for planned, assigned and actual hours, and capacity by both individual and role.
- **Compare against your own formula.** Your SYS-02 alert fires at median × 1.5. RoboHead expresses the same idea as % of capacity. Worth deciding which reads better to Don and JC before the formula freezes.
- A "My Work" view consolidating tasks and to-dos per person.

**Skepticize:**

- Time tracking is central to their model and absent from yours. Their capacity numbers assume logged hours. Yours will not have them, so the % framing may not port cleanly.
- No location concept, no print routing.

### 4.7 Enfocus Switch + PitStop ⚠️

*The rule-driven routing reference.* **Not verified this pass — described from prior knowledge.** Verify before citing.

Preflight profiles and action lists validate PDFs against rule sets; Switch builds automated flows with conditional routing. Relevant as the nearest analog to two EO ideas: material law as machine-checkable rules, and routing determined by properties of the job rather than by a human choosing a destination.

Given §2.2 — that nothing else does derived routing — this is the closest reference you have. Which means verifying it is worth an hour.

### 4.8 Esko WebCenter ⚠️

*The variant-model reference.* **Second-hand from Passes 2 and 3.** Not verified this pass.

Reported: projects organised parent-child with versions; multi-stage approval cycles where stages inherit or reject comments; forced approval and forced rejection per stage; sequential or parallel reviewers; role-based Approver / Reviewer / Viewer scoping per project.

Relevant to one parent JO with N branch variants. Pass 3's independent conclusion is worth keeping: **no print MIS models EO's multi-branch shape**, and WebCenter's parent-child versioning is the closest available approximation.

### 4.9 Bindy ✅

*The missing-tail reference.* Retail and hospitality audit, task and communication, built for multi-unit networks.

**Steal:**

- **Sign-off locks the record.** Signing a visit provides a record of integrity and locks it from further edits. Immutability enforced by state, not by policy.
- **Region and site-based field hierarchy** with site affiliations controlling who can start an inspection and who can view sensitive information.
- Photo and video verification with timestamps, geotags and geo-fencing. Best-practice reference photos attach at the form level so the person on site can see what "correct" looks like.
- Conditional-logic forms; per-question effective date ranges.

**Why it matters:** your JO ends at Closed with no evidence the signage was actually installed at the branch. Bindy is what the tail looks like if you ever build it. Not v1 — but it is the answer when someone asks "how do we know it went up?"

**Skepticize:**

- No creative side at all. Zero review, zero artwork.
- Notification-heavy by design, which cuts against your passive-flag decision. Take the locking and the hierarchy; leave the alerting model.

### 4.10 Zipline ✅

*Pitch asset, not build reference.* Retail HQ-to-store communications, tasks and execution. Customers include Sephora, 7-Eleven, Bath & Body Works.

**Use it for one thing.** A customer quote states, roughly, that if it is on Zipline it is official and if it is not, it is not — and that it is a solid record of what was done, when, and how it was directed. That is INV-02 in a customer's own words.

Their 2026 report, based on 227 retail leaders across the US and Canada, found HQ leaders rated their own understanding of day-to-day store operations at 9.13 out of 10 while store leaders rated HQ's understanding at 5.67.

They also claim 90%+ execution rates against a 29% average. **Vendor self-reported. Do not put that number in a slide.**

**The argument it supports:** when Ramon asks whether Viber is really the problem, the answer is that an entire venture-funded software category exists because retail HQs coordinating hundreds of stores over chat apps could not prove what was said.

---

## 5. The white-space argument, for the pitch

The honest, verifiable answer to "can't we just buy something?":

| Capability | Who covers it | Who doesn't |
|---|---|---|
| Craft review + CD hard gate | Ziflow, PageProof, Admation, Aproove | SignAgent, shopVOX, Bindy, Zipline |
| Branch / placement memory | SignAgent, partially shopVOX | every proofing and creative-ops tool |
| In-house vs vendor print split | shopVOX, print MIS | every proofing and creative-ops tool |
| Derived return routing | **nobody** | everybody |
| Proof of install at branch | Bindy | everybody else |

Four capabilities. No product covers more than two. **The intersection is not sold.**

### Do not lead with licensing cost

Pass 4's per-location math is the wrong argument in both directions. EO has a handful of Requestors, not 400 seats — so the franchise-portal per-location pricing model never applied. Quoting a corrected $240k–$960k figure would be quoting a cost you would never have incurred, and it invites a correction you cannot win.

**Lead with the intersection.** The argument is not "buying is expensive." It is "the thing we need is not for sale, and here are five named products and what each one is missing."

### Second-order point worth having ready

Every product in §3 that handles approvals well is priced per user per month in USD, in the $15–60 band, for the fraction of the loop it covers. Two or three of them stacked is the realistic buy path, and it still leaves derived routing and branch memory unbuilt. That is a structural gap, not a budget line.

---

## 6. Build implications

Consolidated from all six passes. Recommendations, not amendments.

| # | Implication | Source |
|---|---|---|
| 1 | Model branches as one-to-many location records attached to the JO, not sub-orders. No MIS models this shape natively. | Pass 3 |
| 2 | Tie JO-type restrictions to requestor **groups**, not individual users. Per-user matrices become unmanageable. | Pass 3 |
| 3 | Convert units at render time only. Never store multiple units in the record. | Pass 3 |
| 4 | Internal is the default for comment visibility. Never rely on users remembering to mark a comment private. | ReviewStudio |
| 5 | Extend privacy to file versions, not just comments. Internal draft → promoted to external at the review gate. **Currently unspecified.** | ReviewStudio |
| 6 | Every Activity entry needs a visible internal/external status marker. | ReviewStudio |
| 7 | Revisions should leave review as a resolved to-do list, not a raw comment thread. | PageProof |
| 8 | Sign-off should lock the record by state. Unlocking is an event with an author, not a permission. | Bindy, PageProof |
| 9 | Sign type / placement type should carry materials, specs, sizes and template — one object, not scattered fields. | SignAgent |
| 10 | Job-level notes should be recalled on reorder, not just archived. | shopVOX |

**Open decision surfaced by this research:** on a multi-branch JO, do all Requestors see one another's comments? Inclusive or exclusive. Not currently answered anywhere in the official docs.

---

## 7. Sources

**Verified this pass (vendor documentation and support pages):**

- signagent.com — Design, Manage, Municipal pages; support.signagent.com knowledge base (sign types, location plans, sign IDs)
- support.reviewstudio.com — Internal-External Privacy Workflows, Review Settings and Defaults, Managing Files in a Review, Managing Users; reviewstudio.com/blog product update on privacy mode; Capterra listing for pricing
- shopvox.com — sign shop and print shop software pages, success stories, sign industry guide; softwareconnect.com review
- pageproof.com/learn — Deep Dive Workflows, Control the Flow with Workflows, Gatekeepers and Approvers; help.pageproof.com workflow roles and managing proofs
- simple.io — Simple Admation product page, approval workflow solution page, marketing approval workflow best practices guide, smart templates post
- robohead.net — features, resource planning; softwareadvice.com Aquent RoboHead profile; thecmo.com marketing PM roundup
- bindy.com — retail audit, task management, industries pages; blog.bindy.com workflow and lexicon posts
- getzipline.com — platform, task management, employee communication pages; 2026 State of Retail Communication and Execution press release
- marq.com — franchise page; zendikt.com product assessment
- filestage.io — PageProof alternatives comparison (for Lytho positioning)

**Second-hand, unverified:** Esko WebCenter (docs.esko.com, via Passes 2–3), Enfocus Switch/PitStop (prior knowledge), Aproove, Approval Studio, GoProof, EFI Pace/Radius, Rocketlane, Artwork Flow.

**Prior passes reconciled:** Hermes deep-research pass; Gemini pass 1; Function Benchmark Report; Multi-Branch Retail Collateral Approval Workflows report; Gemini/Antigravity reference apps analysis; Gemini/Antigravity creative ops competitors research.

---

## 8. Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 2026-07-28 | Initial. Six passes reconciled. Four corrections recorded in §2. Ten products retained from ~40 named. Top 3: SignAgent, ReviewStudio, shopVOX — stable across two rounds of new input. |

---

*Reference document. Supersedes no official doc. If anything here conflicts with EO_System_Invariants v2, EO_Workflows_and_Scenarios v3, or EO_Creative_Ops_Platform_Spec v4, the official doc wins.*


---

## 📚 Creative Experience Principles & UI Patterns (`EO_Creative_Experience_Principles_v7.md`)

# EO Creative Experience Principles — v7

**Supersedes v6.** Version bumped July 30, 2026 (Round 17). Adds DL-18 (real-time input guards on structured fields) — formalizes a build decision made and implemented July 29, never previously written down, found during a Requestor JO-form deep-dive scan.

**Supersedes v5.** Version bumped July 30, 2026 (Round 16), resolving D-047/D-048. Adds DL-17 (non-blocking warning stamps require explicit acknowledgment) — generalizes the Layout Approval Sheet's dimension-mismatch treatment into a reusable rule for any future non-blocking validation warning, rather than a one-off pattern that only applies to this one feature.

**Supersedes v4.** Version bumped July 29, 2026, batch pass resolving Ed's review. Adds DL-07b (periodic attention nudge — a real, named exception, not a stretch of DL-07a). Part D reframed — this is the actual platform being built incrementally, not a prototype workaround. Part E retired — the v1 reconciliation checklist added no value at this point and is closed rather than left as a stale open loop.

**Supersedes v3.** Version bumped July 29, 2026, to fold in two design laws resolved in the "Design system compliance" session (Jul 28) that never made it into v3: DL-15 (rail identity — department by default) and DL-16 (universal toast + undo, superseding the release-only scoping).

**Supersedes v2.** Version bumped July 28, 2026, to add two structural patterns for multi-track/multi-branch JOs: DL-13 (drawer row sort) and DL-14 (collapsed-card urgency signal). Both follow directly from INV-01's row-derived lifecycle amendment in System Invariants v3 — once a JO can hold multiple independently-progressing rows, both "how are they ordered when I open it" and "how do I know something needs attention without opening it" needed answers.

**Supersedes v1.** Version bumped July 28, 2026, to fold in the BIFOCAL design system.

**What changed:** v1 described experience principles for the pre-BIFOCAL interface. The BIFOCAL design session (v1–v13+, July 27–28, 2026) established a complete visual and interaction language that existed only in artifact code and session context. This version makes that language official and enforceable.

**Namespace:** Design laws are numbered `DL-01` onward. This is deliberately separate from `INV-xx` (System Invariants — behavioural/data rules) and `D-xxx` (Decision Backlog). A design law constrains how the interface looks and behaves; an invariant constrains what the system may do.

**Status of v1 content:** All v1 principles are retained unless explicitly listed in Part E as superseded. Part E must be reconciled against the actual v1 text before this document is considered closed.

---

## Part A — The material law

BIFOCAL is a matte material system. Its coherence comes from restraint, not decoration. These rules are absolute; a change to any of them is a change to the design system, not a local styling choice.

### DL-01 — One stroke weight

**1.5px. Everywhere.** Borders, dividers, focus rings, icon strokes, table rules.

There is no thin variant and no heavy variant. Hierarchy is expressed through elevation and colour, never through line weight.

### DL-02 — Four elevations, no fifth

The system has exactly four elevation levels. Every surface sits on one of them.

If a new component appears to need a fifth level, the composition is wrong — the correct fix is to re-seat the component on an existing level, not to add one.

### DL-03 — Single accent per screen

One accent-weighted element per screen. Everything else is neutral-weighted.

The accent marks the single highest-value action available in that context. Two accents on one screen means the hierarchy has not been decided.

> **Open item — accent scoping.** The specific contest between *Sign Off* and *New Job Order* button weight is unresolved (carried from the pre-BIFOCAL backlog). It requires a decision, not a default. Until decided, neither is to be assumed dominant.

### DL-04 — Richness lives in containers

Visual interest belongs to surfaces, materials, and containers. Content — text, data, values — stays neutral.

A metric is never styled to be interesting. The card holding it may be.

### DL-05 — Matte, never gloss

No gloss. No gradient used as decoration. No drop shadow used as ornament.

Gradients and shadows are permitted only where they express elevation (DL-02) or material depth. If a gradient is doing aesthetic work rather than structural work, remove it.

### DL-05a — Amendment: material light has to be at real strength

*Added July 28, 2026, after DL-05 as first written produced a visibly flat hero card.*

"Matte" constrains the **kind** of light, not its **intensity**. A radial bloom at 26% accent inside a card is material light; a specular sweep across a button on hover is material light. Neither becomes decoration by being strong enough to see.

The failure mode DL-05 was written against is ornament — gloss for polish's sake, gradient standing in for hierarchy. It was not written against legible depth.

**Practical rule:** if a surface is supposed to read as elevated and does not, the light is too weak, and strengthening it is the correct fix. Chroma does more of that work than luminance — a card that is *hued* against a neutral page separates more clearly than one that is merely lighter.

**Also settled here:** a one-shot, hover-triggered specular sweep is a hover state under DL-07 and is permitted. It is not gloss.

### DL-06 — Dual mode parity

Light and dark are both first-class. Neither is a derived variant of the other.

Any component shipped in one mode without the other is incomplete. Contrast ratios must hold independently in both — a token that passes in dark and fails in light is a failing token.

### DL-07 — Motion is functional only

Motion exists to communicate state, causality, or affordance. Never to decorate.

Sanctioned categories:

- **Hover states** — signalling interactivity
- **Exit animations** — a row leaving a list, showing where it went
- **Toast confirmations** — closing the loop on an action
- **Dwell time on connectors** — expressing duration in the custody rail (see DL-09)
- **Self-retiring invites** — see DL-12

Anything outside these categories requires a new sanctioned category to be added here first.

### DL-07a — Amendment: ambient material motion

*Added July 28, 2026, after DL-07 as first written removed motion that was wanted and that was not the actual problem.*

**Sanctioned category added: ambient material motion.** Slow, looping motion inside a background material layer — line art behind content, at reduced opacity, in `--art` or another non-accent colour.

**The diagnosis DL-07 got wrong.** The hero isometric's pulsing plus badge was stealing focus from the CTA. The cause was not that it moved. The cause was that it was **accent-coloured, inside a bordered panel, in the content flow** — an accent object in a focal position. Motion only decided which of several competing accents won.

Once the same art is de-accented, dropped to ~34% opacity, and moved behind the copy, the motion carries no focal weight. It reads as the surface being alive.

**Conditions — all four required:**

1. Background layer only, behind content
2. No accent colour anywhere in the animated element
3. Reduced opacity, roughly 30–50%
4. Slow enough not to draw the eye — 2.8s or longer per cycle

**Standing lesson:** when something out-competes the focal element, check colour and position before blaming motion. Cutting the motion is the easy fix and usually the wrong one.

### DL-07b — Periodic attention nudge: single-metric only

*Added July 29, 2026 — resolved after checking the actual `attnPeek`/`attnBounce` code against DL-07a's four conditions. Fails 3 of 4 (foreground not background, opacity reaches full strength not 30–50%), but earns its own exception rather than a fix, because it's a different, legitimate category, not a violation of DL-07a's.*

**Sanctioned category added: a periodic nudge on the single actionable metric.** Where exactly one element on a screen is the genuinely actionable one (everything else on that dashboard is inert), that element may pulse/brighten on a repeating timer to signal "this still needs you" — rather than sitting as a permanent, easy-to-tune-out static badge.

**Conditions — all required:**
1. Applies to **at most one element per screen** — the single actionable item, never a general-purpose attention-getter (this keeps it consistent with DL-03's one-focal-element discipline, just applied to a nudge instead of an accent)
2. Pauses immediately on hover — the moment a person's attention is actually on it, the animation stops asking
3. Slow enough to read as a nudge, not a demand — matches DL-07a's 2.8s+ floor

**Why this isn't just DL-07a with looser numbers:** DL-07a's category is ambient material — background art staying "alive" without asking for anything. This is the opposite job — a specific, single, foreground call to action. Both are legitimate; they're not the same rule stretched, they're two different reasons motion is allowed to exist.

---

## Part B — Structural patterns

These are not styling rules. They are decisions about how the product represents its own state, and they carry product meaning.

### DL-08 — Chain of custody, not progress

Job Order state is represented as a **custody rail** — a logistics-style chain showing who holds the work — not as a progress bar.

**Rationale, and this matters:** a progress bar implies monotonic advance toward completion and invites the question "how far along is it?" A custody rail answers a different and more honest question: *who has it right now.* The work genuinely does move backward and sideways; the representation must be able to show that without reading as failure.

The rail's stages follow the corrected `INV-01` lifecycle. It is not free to invent its own stage set.

### DL-09 — Revisions are a detour, not a stage

A revision renders as a **detour off the rail's spine** — visibly departing and returning — never as an additional inline stage.

A revision is not progress and not regression. It is a loop. The geometry says so.

**Duration is expressed on connectors, not nodes.** Time spent between stages lives on the line; the node marks the handoff event itself.

### DL-10 — No ETA, anywhere

The interface never displays an estimated completion date or time remaining.

**Replaced by: next action + owner.**

**Rationale:** the underlying data does not support a credible ETA — measured p90 cycle time is 39 days against a 7-day median, with a recorded maximum of 174. An ETA drawn from that distribution would be fiction, and a fiction the interface would be blamed for. "Next action + owner" is always knowable, always true, and more actionable than a date.

This is a hard prohibition. A future ETA feature requires this law to be repealed explicitly, with the variance problem solved first.

### DL-11 — Drawer for interaction, page for study

From a dashboard or queue, Job Order interactions open in a **drawer** — the user keeps their place in the list.

The **full detail page** is a separate destination, for study rather than action.

The distinction is intent: acting on a JO should not cost you your position in the queue; examining one should give you the whole surface.

### DL-12 — Self-retiring affordances

An invite animation that teaches an interaction **stops permanently once the user has demonstrated the behaviour.**

Reference implementation: the chevron invite on the custody rail.

**Rationale:** a persistent hint is a permanent admission that the affordance failed. Retiring it respects the user's learning and keeps the resting state clean.

### DL-13 — Drawer row sort: breach-first, alphabetical tiebreak

*Added July 28, 2026, for multi-track/multi-branch JOs — INV-01 v3.*

When a JO's drawer shows multiple (branch, track) rows, rows with an active deadline-breach flag or rush override sort to the top. Everything else sorts alphabetically by branch.

**Rationale:** pure urgency-sort re-orders on every glance as rows resolve, which reads as unstable mid-review. Pure alphabetical buries what needs attention. Breach-first with an alphabetical tiebreak only moves a row when its breach state actually changes — a real custody event worth noticing, not visual churn.

### DL-14 — Collapsed-card urgency signal, not row detail

*Added July 28, 2026, for multi-track/multi-branch JOs — INV-01 v3, INV-22.*

A kanban card for a multi-row JO never renders per-row detail. It shows branch/track counts, a compact per-row status-token segment bar, and a done fraction — collapsed, always, regardless of row count.

If **any** row inside has an active breach or rush override, the card additionally shows a single status-token indicator (not per-row, not named which row). This is a status token per DL-04/DL-03's restraint rule, not an accent — it doesn't compete with the screen's one accent element.

**Rationale:** DL-08 exists to answer "who has it right now" — a collapsed card that hides an active rush item contradicts the rail's own purpose. But full row detail on a card defeats the point of collapsing at all. One signal, no detail, click through to the drawer for the rest.

---

### DL-15 — Rail identity: department by default, named person on revision

*Added July 29, 2026 — resolved Jul 28 in the "Design system compliance" session, never folded in until now.*

A custody rail node's "who" label shows the **department/role** by default (e.g. "Purchasing," "Art Director"), not a named individual.

**Exception:** the node shows the **named person** (e.g. "Laarni") only when that specific person triggered a revision at that stage. Custody at rest is institutional; custody at the moment someone acted on it is personal.

**Rationale:** most of the time, who currently holds a JO is a role-level fact — it doesn't matter which Purchasing officer is at their desk. But a revision is a specific person's decision, and INV-17 already requires that decision to record its origin — the rail should surface that, not flatten it back into "Purchasing" once it's the interesting fact.

### DL-16 — Confirm-then-toast is universal, not release-only

*Added July 29, 2026 — resolved Jul 28 in the "Design system compliance" session, never folded in until now. Supersedes the release-only scoping noted in the Round 12 changelog entry.*

Every submit or stage-advancing action — not just Pending Release — gets the same two-part confirmation: a **confirm pop-up before it fires**, with copy contextual to that specific action, then a **toast with an undo window after** it completes.

**Rationale:** the release-vs-reopen friction asymmetry flagged in the Round 12 session (release had none, reopen had a full modal plus a written reason) wasn't really about release specifically — it was that confirmation patterns had been decided ad hoc, per screen, instead of as a rule. Making it universal removes the asymmetry at its source: every stage-advancing action gets the same weight of confirmation, and Reopen's heavier reason-required step (INV-03) sits on top of this as an addition, not as a different pattern entirely.

### DL-17 — Non-blocking warning stamps require explicit acknowledgment

*Added July 30, 2026 (Round 16) — generalized from the Layout Approval Sheet's dimension-mismatch treatment (LC-19, INV-31), so future non-blocking validation warnings follow one rule instead of being designed one-off each time.*

Where the system flags a data-quality concern that should **not** block the user from proceeding (they may know something the system doesn't), the warning is shown as a **visible stamp or badge adjacent to the content it concerns — never covering or obscuring it.** Proceeding past the warning requires an **explicit action** (e.g. an "as-is"/"override" button), never a silent pass-through, and may offer an **optional reason field**. Every override is logged: who, what was overridden, when, and the reason if one was given.

**Rationale:** a silent warning that doesn't require acknowledgment gets ignored; a warning that blocks entirely punishes the user for cases where they're right and the system's check is too rigid. This pattern gives the system's concern real visibility without taking away the user's judgment — and the logged override means a wrong call is traceable later as a knowing decision, not a mystery.

### DL-18 — Real-time input guards on structured fields

*Added July 30, 2026 (Round 17) — formalizes a build decision made and implemented on July 29, but never written down here. Found only because a JO-form deep dive went looking for it.*

Any field with a known valid shape — numeric measurements (width, height, quantity), or a pattern-constrained format (mobile/landline numbers) — rejects invalid input **as it's typed**, not only at submit time. A digit-only field simply doesn't register a letter keystroke; a phone field only accepts digits/parens/dashes while typing, then checks the full pattern on blur (`09XX-XXX-XXXX` for mobile, the applicable landline formats). The person never gets to fill out an entire form only to be told at the end that one field was wrong the whole time.

**Rationale:** submit-time-only validation punishes the person for a mistake they made minutes ago and have long since forgotten about — they have to hunt back through the form to find what's wrong. Catching it at the keystroke is cheaper for everyone and was already how the actual JO form got built; this just makes sure the next screen with a structured field follows the same rule on purpose, instead of by accident.

---

## Part C — Tokens: extraction required

**These values are not authored here. They are to be read out of the shipped BIFOCAL artifact code and transcribed into this section.**

Do not infer, round, or reconstruct these from visual inspection. Read the source, copy the literal values, note the file and line.

| Token group | Source of truth | Status |
|---|---|---|
| Spacing scale | BIFOCAL artifact CSS | **Extract** |
| Type scale — sizes, weights, line-heights | BIFOCAL artifact CSS | **Extract** |
| Corner radii — per elevation level | BIFOCAL artifact CSS | **Extract** |
| Colour — light mode, full set | BIFOCAL artifact CSS | **Extract** |
| Colour — dark mode, full set | BIFOCAL artifact CSS | **Extract** |
| Elevation definitions — the four levels of DL-02, concretely | BIFOCAL artifact CSS | **Extract** |
| Accent colour + its neutral counterparts | BIFOCAL artifact CSS | **Extract** |
| Motion — durations and easing curves per DL-07 category | BIFOCAL artifact CSS/JS | **Extract** |
| Per-type JO tint badges | BIFOCAL artifact CSS | **Extract — verify all six JO types present** |

**Extraction rule:** where the code contains a value that contradicts a law in Part A or B, the contradiction is a **bug report**, not a token. Log it; do not transcribe it as law.

---

## Part D — Not a design principle

Recorded here specifically so it is not mistaken for one.

**Single-file SPA (`EO_requestor_app.html`).** *(Reframed July 29, 2026 — this project is not a prototype. Everything built or modified from here forward is a step toward the actual finished, full-fledged EO Creative Ops platform, not throwaway demo work.)* The consolidation of screens into one file was a workaround for cross-file navigation failing in the design preview environment — a build-environment artifact, not a decision about the real platform's architecture.

It carries **no** authority over production architecture. Do not enshrine it, and do not treat de-consolidation as a violation of anything.

---

## Part E — Retired

*(Retired July 29, 2026 — Ed's call: every round since v1 has been a tracked, deliberate amendment. Closing a checklist against ancient v1 text at this point adds nothing; the current doc set is already miles ahead of v1 by construction, not by comparison. This section stays here as a record that it was considered and closed, not left dangling as a stale open loop.)*

---

## Part F — Enforcement

This document exists to be checked against, not read once.

**Any agent editing frontend code must, before committing:**

1. Confirm no new stroke weight was introduced (DL-01)
2. Confirm no fifth elevation was introduced (DL-02)
3. Confirm accent count per touched screen is exactly one (DL-03)
4. Confirm both light and dark render correctly (DL-06)
5. Confirm any added motion falls in a sanctioned DL-07 category
6. Confirm no ETA, countdown, or estimated date was introduced (DL-10)
7. Confirm any non-blocking warning uses an adjacent stamp, explicit override action, and logs the override (DL-17) — never a silent pass-through
8. Confirm any structured field (numeric or pattern-constrained) rejects bad input as typed, not only on submit (DL-18)

**A change that violates a design law is not shipped and then documented.** The law is amended here first, with a Changelog entry and a version bump — same discipline as the System Invariants.

---

*End of v7.*


---

## 📚 Executive Pitch Framing & Presentation Narrative (`EO_Pitch_Framing.md`)

# EO Creative Ops — Pitch Framing
**Not a deck. The angles, and what actually backs each one, so the pitch is substance-first, not adjective-first.**

The trap to avoid: presenting this as "we digitized the spreadsheet." That invites "why not just fix the spreadsheet" as the obvious counter-question. Every angle below exists because a spreadsheet structurally cannot do it — that's the actual argument, not "it looks nicer."

**The one sentence that ties all seven angles together, worth saying out loud before walking through them:**

> EO Creative Ops isn't replacing spreadsheets because spreadsheets are old. It's replacing them because the department has outgrown what a spreadsheet can represent — approvals, operational knowledge, standardized workflows, accountability, and organizational memory. A spreadsheet was never built to hold any of that; it just happened to be the only tool available.

That gives the audience a mental model before the seven angles arrive individually — otherwise each one lands as a separate feature instead of pieces of the same argument.

---

## Angle 1 — The pain-point angle (table stakes, not the headline)
Four spreadsheets + tribal knowledge + Viber for revisions, replaced by one system.
- **What backs it**: multi-branch JOs, real-time stage tracking, phone/deadline validation catching errors spreadsheets never could.
- **Why it's table stakes, not the pitch**: this alone is "digitized the spreadsheet." Necessary, not sufficient. Don't lead with this.

## Angle 2 — The institutional trust angle
A spreadsheet has no memory of *who* approved *what*, *when*, on *which version*. This system does — and the value isn't the timestamp, it's that nobody has to argue later.
- **What backs it**: the Approval Sheet (stamped, timestamped, reviewer-named — replaces the red-pen sign-off), version-tagged comments, immutable activity log (INV-07, INV-08, INV-10).
- **Why it lands**: instead of "I never approved that," the system says "Version 12, Approved by John, July 18, 2:13 PM." Conversation over. That's not a paper trail — it's the end of a certain kind of argument ever happening again.

## Angle 3 — The operational memory angle (the strongest differentiator)
The knowledge of what's at SM Megamall — every placement, size, material, what's run there before — currently lives in senior artists' heads, not in any system.
- **What backs it**: Branch Placement Library (reframed from the already-built placement/material bank), reuse-from-branch flow for recurring campaigns.
- **Why it lands**: this reframes the pitch from "a tracking tool" to "the department stops depending on any one person's memory." That's a business-continuity argument, not a workflow argument — it survives someone quitting, retiring, or being out sick.

## Angle 4 — The cross-team visibility angle
Right now, status-chasing across 400+ branches means everyone asks everyone else what's happening.
- **What backs it**: role-specific dashboards (not permission-filtered — each role answers *their* actual question), the two-channel Activity system (Requestor gets what they need, AD/CD get craft-review context, nobody gets noise that isn't theirs).
- **Why it lands**: less "where is my JO" back-and-forth is time given back to actual creative work, provably.

## Angle 5 — The proactive-intelligence angle
A spreadsheet only tells you what you go looking for. This system tells you what you need to know before you ask.
- **What backs it**: workload-imbalance alerts, deadline-breach flags, revision soft-cap flags, Pending Release dormancy counters — all already built and computing live.
- **Why it lands**: this isn't "managers become unnecessary" — it's that managers stop spending their attention on repetitive observation (who's overloaded, what's slipping, what's gone quiet) and get that attention back for coaching, prioritization, and actual creative direction. The system does the noticing; the manager does the managing.

## Angle 6 — The operational consistency angle
Today, every senior artist has their own naming conventions, organization, and workflow — knowledge that lives in individual habits, not a shared standard.
- **What backs it**: the same Branch Placement Library and standardized JO structure that back Angle 3, applied here to a different problem — not memory loss, but inconsistency between people who are all still here.
- **Why it lands**: onboarding a new artist stops being "go ask Mhan" and starts being "the platform already shows you how this branch works." That's a faster, lower-risk ramp-up, and it's a concrete, checkable claim rather than a vague culture argument.

## Angle 7 — The roadmap angle (ambition without overpromising)
Everything above is real and built. This angle is the credible next chapter, presented as vision, not as a claim about what's already working.
- **What to show**: the branch-library reuse flow as a working demo (real, in the week), framed as step one of "organizational memory" — with campaign cloning, placement version history, and smart reassignment suggestions named explicitly as what comes next.
- **Why it lands**: decision-makers buy a credible roadmap as readily as a finished feature — and being honest about what's vision vs. built is more persuasive than quietly hoping nobody asks.

---

## Words to avoid in this pitch

Don't call this "AI," "a smart platform," or "digital transformation." None of those are the actual competitive advantage, and all three invite comparison to every other generic tool pitch in the building. The real advantage is much more specific than any of those words: it knows how *this* department works, how campaigns actually evolve, how branches differ from each other, who owns what, and what happened before. That specificity is what makes the pitch believable — buzzwords dilute it.

## Suggested pitch order

1. Open with Angle 3 (operational memory) — it's the hook, not the tracker.
2. Angle 2 (institutional trust) — the risk-reduction case, which usually matters most to whoever's approving budget.
3. Angle 4, 5, and 6 together — the day-to-day proof that this isn't just theory: less status-chasing, proactive flags instead of manual noticing, and consistency that survives any one person leaving.
4. Angle 1 last, briefly — "and yes, obviously, it also replaces the four spreadsheets."
5. Close on Angle 7 — where this goes next, named honestly as roadmap.

This order deliberately buries "JO tracker" as the least interesting fact about the system, because by the time you say it, it'll sound like the smallest part of the pitch — which is exactly the point.

**The internal rule to keep**: the trap to avoid is presenting this as "we digitized the spreadsheet." If anyone preparing this pitch ever hears themselves say "it's basically a better spreadsheet," that's the signal the framing has slipped — go back to Angle 3.

---

## The mantra, for the project, not just the pitch

> EO Creative Ops captures how the Creative Department works — not just what it works on.

That's the line worth keeping in view past the pitch itself, for every future decision about what this system builds next. It's not a prettier Job Order system. It's the department's operational knowledge, encoded into software — a different category of product than "a better spreadsheet," and worth defending as that category stays true through every future scope decision.


---

## 📚 Creative Leadership Operational Intelligence (`EO_Creative_Leadership_Operational_Intelligence_v2.md`)

# EO Creative Ops — Creative Leadership & Operational Intelligence
**v2 — Round 19, July 30 2026. Part 8 renamed from "MVP Aug 7" to "Implementation Phases," with Phase 1's contents made honest against what's actually locked for Aug 7 — pinpoint annotation and decision history marked conditional, not guaranteed. Adds Part 11: one flagship workspace per role, an organizing principle that gives every role's build the same coherent shape. Companion INV-37 (post-submission immutability) formalized in System Invariants v8.**

**v1 — July 30, 2026. The fifth pillar document, alongside System Invariants (behavioral rules), Workflows & Scenarios (process rules), Experience Principles (UX laws), and the Changelog (history/rationale). This one defines the decision-making philosophy: how the platform helps a Creative Director and Art Director run the department, not just how screens behave.**

**Scope note, read this first:** Part 8 (Implementation Phases) is explicit about what Phase 1 actually includes for Aug 7 versus what's conditional. Parts 3–7 and 9–11 are **real product direction, not a build target for Aug 7.** This document is the pitch's roadmap material and the long-term product spec. It is not this week's engineering plan. See the Changelog for the full reasoning.

---

## Part 1 — Philosophy

Not screens. Not widgets. What leadership actually does:

> The Requestor creates work. The Production Coordinator distributes work. The Artist creates work. The Art Director improves work. The Creative Director governs the creative operation.

That distinction changes the product — CD/AD tooling isn't "the same dashboard with an approve button," it's a genuinely different job.

## Part 2 — Daily Operating Model

Instead of "what pages should CD have," ask "what decisions does CD make every morning":

- What needs my approval?
- Which artists are overloaded?
- Which jobs are stuck?
- Which revisions keep looping?
- Which projects are at risk?
- What should I personally intervene in?
- Is the studio healthy today?

Those questions become product features, not the other way around.

## Part 3 — Operational Intelligence

Not AI — operational intelligence. Five categories:

**Workload Intelligence** — overloaded artist, underutilized artist, assignment imbalance, queue distribution, average active workload.

**Flow Intelligence** — bottlenecks, average approval time, revision frequency, stalled approvals, aging jobs.

**Quality Intelligence** — repeat revisions, revision hotspots, recurring design issues, frequently rejected placements.

**Decision Intelligence** — approvals pending, approvals delayed, approvals requiring immediate action.

**Studio Health** — high-level indicators: workload balance, approval health, production health, revision health, delivery health.

## Part 4 — Creative Director Workspace

Not "Dashboard" — **Decision Workspace.**

- **Daily Briefing** — "Good morning. Today: 38 active JOs, 7 awaiting approval, 2 breached SLA, 1 overloaded artist, 3 revision hotspots."
- **Attention Queue** — priority-sorted, not chronological: needs approval, needs escalation, needs intervention, waiting too long, rush, blocked, repeated revisions.
- **Approval Workspace** — the flagship feature (see Part 6).
- **Studio Pulse** — operational health, ICU-monitor framing: workload, revision pressure, approval throughput, department flow, production state.

## Part 5 — Art Director Workspace

Different focus from CD — creative quality, not department governance: Review Queue, Interactive Approval Sheet, Comment Resolution, Revision Tracker, Creative Consistency, Design QA, brand compliance, version comparison, typography/layout/placement issue checks.

## Part 6 — Interactive Approval Sheet

Likely EO Creative Ops' strongest differentiator, long-term.

**Context-aware review** — JO metadata always visible, placement details beside the artwork, revision history without leaving the page.

**Figma-like annotations** — click anywhere on the artwork to comment. Types: Suggestion, Revision Required, Question, Approval Note. Threaded, anchored to exact artwork locations. *(Note: this is the full version of the pinpoint-annotation idea from earlier — the Aug 7 stretch version is a single comment-drop, not this full typed/threaded system.)*

**Resolution workflow** — Open → Addressed → Verified → Closed. Filter to unresolved only. Carry unresolved annotations forward into new versions where relevant.

**Change awareness** — side-by-side version comparison, highlighted changed regions, "since your last review" summary, resolved-vs-newly-introduced comment lists.

**Approval readiness panel** — summarizes before the reviewer has to mentally check it themselves: required assets complete, correct dimensions, placement count, outstanding comments, previous approvals, revision count, production readiness, external dependencies.

## Part 7 — Design Principles

- Don't show data. Show decisions.
- Every widget must answer "what action should I take?"
- Reduce approval anxiety — provide confidence before commitment.
- Surface anomalies, not averages — leadership manages exceptions, not normal operation.
- Prioritize intervention over observation — the workspace exists to help leaders act, not just monitor.

## Part 8 — Implementation Phases *(renamed from "MVP Aug 7" per Round 19 review — this document is architecture, like the other four pillars, not a build spec; phases replace a single MVP label so the document stays visionary without implying Phase 3 belongs in this week's build)*

### Phase 1 — Walking Skeleton (Aug 7)
- Approval Workspace (single-approver Internal Review, not the AD/CD parallel-lane model)
- Basic Approval Sheet — view artwork, approve/reject, comment
- Placement comments — plain per-placement comment thread, not the typed/threaded Figma-style annotation system in Part 6
- **Pinpoint annotation (minimal, single comment-drop) — conditional, not guaranteed.** Sequenced as a Day 4 stretch item behind the 7-role breadth build; cut first if the schedule slips, per the priority order already locked.
- **Decision history — not currently in the locked Aug 7 scope.** Worth a cheap addition if Phase 1 lands early (an append-only log of stage changes costs little once `placement.stage` exists), but not committed here — would need to be explicitly added to the walking-skeleton plan, not assumed from this list.

### Phase 2 — Operational Visibility
- Attention Queue
- Studio Pulse
- Workload insights
- Revision trends

### Phase 3 — Operational Intelligence
- Predictive bottlenecks
- Recommendation engine
- Leadership briefing
- Organizational learning

## Part 9 — Further roadmap (later still)

**Predictive Intelligence** — forecast workload bottlenecks, predict SLA breaches, identify likely revision loops.

**Continuous Improvement Engine** — recommend artist reassignments, suggest workload redistribution, highlight recurring approval delays.

**Organizational Learning** — monthly studio health summaries, approval trend analysis, revision pattern reports, team performance insights.

## Part 10 — Competitive positioning

Compare against Adobe Workfront, Monday.com, Jira, Asana, ClickUp, Figma (annotation model), Linear (attention-first UX), Notion (information architecture) — not to copy, but to identify where EO Creative Ops offers a more specialized experience for creative operations specifically. *(Same caution as the earlier Competitive References doc — verify before citing any of these by name in the actual pitch.)*

## Part 11 — One flagship workspace per role *(added Round 19 — the organizing principle the earlier drafts were missing)*

> Every role in EO Creative Ops has exactly one flagship workspace — not a dashboard. A dashboard is something you look at. A workspace is where you do your job.

| Role | Flagship workspace |
|---|---|
| Requestor | Job Order Builder |
| Production Coordinator | Assignment Workspace |
| Artist | Production Workspace |
| Art Director | Review Workspace |
| Creative Director | Decision Workspace |
| Purchasing | Procurement Workspace |
| Admin | Governance Workspace |

This is naming and framing, not new engineering scope — the Requestor's workspace already exists as the JO Builder (Round 17). It matters because it gives every future role-specific build the same coherent shape: not seven variations of one generic screen, but seven environments each built around that role's actual highest-value decision. This is also the direct answer to "the dashboards need to be fully built" — a workspace built around the role's real job is what "fully built" should mean, not a feature-complete generic table view.

---

## How this document is meant to be used

For the Aug 7 pitch: this is roadmap material, presented as vision, not demoed as working software. The walking skeleton proves the architecture; this document proves the ambition. Together they're a stronger pitch than either alone.

For engineering, post-Aug-7: this becomes the actual spec once the walking skeleton is real and the pitch outcome (or portfolio decision) is known.


---

## 📚 EO Workflows & End-to-End Scenarios (`EO_Workflows_and_Scenarios_v8.md`)

# EO Creative Ops — Workflows & Scenarios (Master Tracker) — v8
**Living document. Add new scenarios as they come up — keep the ID scheme so anything can be cross-referenced later.**

**What changed from v7**: Round 17 — a Requestor JO-form deep dive surfaced one real doc-vs-code bug and one real doc gap. **Bug**: AR-03 had been marked ✅ built (Artist-side ft→in size conversion) for at least two rounds; a direct code check found no conversion logic anywhere in that view. Corrected to ❌, logged as **D-056**, genuinely outstanding. **Gap**: a July 29 build decision — remarks live per-placement, never as one global JO-level box, plus real-time reject-on-type input guards on W/H/Qty/CP#/Landline — was implemented in code that same session but never written into this doc. Formalized as **INV-36** (remarks) and **DL-18** (input guards), new scenarios **RQ-26/RQ-27**, RQ-13/RQ-14 updated to reference them correctly.

**What changed from v6**: Round 16 — resolves D-047/D-048. New Part 1.5 added: the Layout Approval Sheet (LC-19 through LC-21) — dimension-proportion check against the JO's own declared size, partial/staggered sheet submission with independent per-sheet release, and the auto-compiled final sheet with mixed AD/CD stamp attribution. New scenarios: RQ-24 (Requestor flags a single placement for revision), AR-12 (Artist self-raises a placement revision), PC-11 (PC notified on placement-level revisions under both paths), PU-06 (Purchasing receives a partial approval sheet with a pending-count indicator), RQ-25 (Requestor JO view shows per-placement status breakdown, not one aggregate label). PU-05 updated from open to resolved. *(Also fixed this round: this header had been showing a stale "v4" for several rounds — a leftover that was never updated when the doc actually reached v5/v6. No content was affected, just the version number in this title line.)*

**What changed from v5**: Batch pass resolving Ed's review of the whole doc set (July 29). LC-17 (PC-assignment) resolved — no longer open, now a real visible stage in Part 0's state table. ADM-05 through ADM-11 un-deferred — reframed as scoped-not-yet-built, not intentionally postponed, since this is being built as the actual platform, not a demo. New scenarios: RQ-22 (My JO Requests / All JO Requests tabs), RQ-23 (Placement Bank browse-and-use modal), RX-13 (comment editing with notification fan-out). AR-01's removal note, self-claim, and the JO-type list are all confirmed against the corrected 10-category model (INV-30) — Spec v4's old 6-type list is superseded everywhere it's referenced.

**What changed from v3**: Combo JOs (independent digital + printed tracks per branch) and Mall Admin Approval are now formalized — see System Invariants v3 (INV-01 amendment, INV-21, INV-22). New scenarios added: LC-15 (Mall Admin Approval), LC-16 (combo JO — independent tracks), RQ-19 (branch/track-level deadline override). Part 0's flags list updated to include Mall Admin Approval alongside External Review.

**What changed from v2**: Part 0's state table was corrected — it previously showed CD sign-off happening at Pending Release, which contradicted `EO_Creative_Ops_Platform_Spec_v3.docx` (CD signs off inside Internal Review; Pending Release is post-approval routing only). See `EO_System_Invariants.md` v2 for the invariant-level fix and D-020 in the Changelog for the resolution record. New scenarios added: LC-13/LC-14 (print-route ownership), RQ-18 (Requestor-raised post-approval revision), AD-07/CD-06 (the optional second-review pattern).

See also: `EO_System_Invariants_v7.md` (rules every scenario below must satisfy) and `EO_Changelog_v8.md` (why decisions were made).

ID prefixes: `LC` lifecycle · `RQ` Requestor · `AR` Artist · `PC` Project Coordinator · `AD` Art Director · `CD` Creative Director · `PU` Purchasing · `ADM` Admin · `RX` cross-role interaction · `SYS` system-triggered event · `FL` failure/exception scenario

Status tags: ✅ built & verified · 🔧 spec'd, not yet built · 🆕 add here as new ones come up

---

## Part 0 — State Transition Table

**Corrected against `EO_Creative_Ops_Platform_Spec_v3.docx` §6.** The previous version of this table put CD sign-off at Pending Release. That was wrong. CD signs off inside Internal Review — AD review is optional, CD is always required, and CD can approve without AD ever seeing it. Pending Release is what happens *after* approval: the Requestor's go-signal plus a print-route choice. This version also makes print routing an explicit branch (In-House Printing vs. Sent to Purchasing), since they have different owners and different exits, and adds Cancelled as a terminal state available from any stage.

| Current state | Allowed next states | Trigger |
|---|---|---|
| Submitted | PC Assignment | JO lands in PC's queue |
| PC Assignment | In Layout | PC assigns an artist (INV-06/INV-26 — the only path in, no self-claim; resolved D-036, no longer a sub-state timestamp) |
| In Layout | Internal Review, Revision | Artist marks layout ready / AD or CD sends back |
| Internal Review | Pending Release *(Internal Approved)*, Revision | CD signs off (AD review optional, may precede or be requested mid-review — see AD-07/CD-06) |
| Revision | In Layout | Artist resubmits — always loops to Internal Review next, regardless of who raised it |
| *(flag)* External Review | *(no stage change)* | Requestor sends an Internally Approved layout externally — only if `requires_external_approval` is set; External Approved/rejected is logged by the Requestor, not a system state |
| Pending Release | In-House Printing, Sent to Purchasing | Requestor gives the explicit go-signal and chooses the print route; RFQ/RS# optionally logged while waiting (RS# never applies to in-house or digital — see INV-20) |
| In-House Printing | Closed | Artist completes the print run (INV-19 — routes to Artist, not Purchasing) |
| Sent to Purchasing | Closed, Revision | Purchasing completes the order, **or** flags a supplier issue and routes to Revision (PU-04/D-009) — re-clears Internal Review, then returns directly to Purchasing, not back through the Requestor (INV-18) |
| Closed | *(re-enters at whichever stage LC-10 determines)* | Requestor reopens with reason |
| Cancelled | — *(terminal)* | Requestor or CD cancels, from any stage |

**Not a valid transition from anywhere**: direct jump to Closed without passing a print-route stage. Direct jump to Pending Release without CD sign-off in Internal Review — there is no skip path, spec'd or otherwise.

External Review is not in this table as a state, on purpose — per INV-04, it's a flag, not a stage, so it never appears as a "current state" or "next state." It can be raised at any point before Pending Release and doesn't interrupt whatever stage the JO is actually in.

> **Source of truth**: The YAML transition model below is the canonical representation, intended for future implementation. The prose table above exists for human readability. If they ever diverge, update the prose to match the YAML and treat the discrepancy as a documentation bug — not the other way around.

**Machine-readable version** (same rules, meant to become actual validation config later rather than staying prose-only):

```yaml
states:
  Submitted:
    next: [PC Assignment]
  PC Assignment:
    next: [In Layout]
    owner: pc   # INV-06/INV-26 — only path to an artist, resolved D-036
  In Layout:
    next: [Internal Review, Revision]
  Internal Review:
    next: [Pending Release, Revision]   # CD sign-off happens here — INV-02
  Revision:
    next: [In Layout]
    origin: [internal, requestor, purchasing]   # INV-17 — immutable once set
  Pending Release:
    next: [In-House Printing, Sent to Purchasing]   # no approval gate here — INV-02
  In-House Printing:
    next: [Closed]
    owner: artist   # INV-19
  Sent to Purchasing:
    next: [Closed, Revision]
    owner: purchasing
  Closed:
    next: []  # re-entry only via Reopen (LC-10), target stage determined by D-002, not a normal transition
  Cancelled:
    next: []  # terminal, reachable from any non-terminal stage

revision_return:   # INV-18 — derived, never manually chosen
  internal:   Internal Review        # never left the building, loop is unconditional
  requestor:  Requestor               # re-clears Internal Review, then returns to whoever raised it
  purchasing: Sent to Purchasing      # re-clears Internal Review, then returns directly — not via Requestor

flags:  # attributes on a row, never states themselves — see INV-01, INV-04, INV-21
  - External Review
  - Mall Admin Approval   # optional, Requestor-triggered, sits after Internal Review — INV-21
  - Deadline-breach
  - Workload-imbalance
  - Revision soft-cap
  - Pending Release dormancy
```

**Note on rows (INV-01 v3):** the state table above describes one row's lifecycle. A JO with multiple branches and/or independent digital/printed tracks decomposes into multiple (branch, track) rows, each progressing through this same table independently — see LC-16.

---

## Part 1 — JO Lifecycle, start to finish

### LC-01 — Filing
Requestor selects identity, picks JO type (restricted if scoped), fills branch(es) with floor/contact pairs, item description + size/orientation/unit, optional suggested artist, uploads reference/mockup, optionally curates from placement/material bank. Deadline auto-computed at +3 days. ✅

**Resolved (D-016, D-017, D-019)**: Branch is a first-class object — hierarchy is **Branch → Placement → Sizes/measurements**. Placements append permanently to their originating branch, not just to one Requestor's personal bank. All Requestors can browse the full branch-scoped bank. Reuse is never automatic (D-017) — Requestor manually pulls up the branch and selects which known placements to append. New placements can also be added directly to a branch's library from within the form. Phone number stays one input box (existing validation already covers mobile + landline formats, per D-019).

### LC-02 — Submitted
Unclaimed unless a suggested artist was named. Visible to PC for assignment. Next real stage is PC Assignment (LC-17), not directly In Layout. ✅

### LC-17 — PC Assignment *(resolved — Ed's review, July 29; supersedes the "still open" framing)*
The moment between Submitted and In Layout where the PC actually assigns an artist. Previously invisible, folded silently into "Submitted." **Now a real, visible SPINE stage** — resolves D-036 in favor of the structurally-accurate option, not the quiet-timestamp one. It has an actor (the PC), a timestamp, and — since self-claim is removed (INV-06/INV-26) — it is the **only** path a JO takes to get an artist. Being visible means anyone can see how long a JO sat waiting for assignment, and when it was assigned or reassigned, the same way any other custody stage is visible.

### LC-03 — In Layout
Artist assigned by the PC (LC-17 — no self-claim, per INV-06/INV-26) builds first layout. Requestor-facing Activity channel open throughout. ✅ *(corrected — previously said "claims or is assigned"; self-claim was removed in Round 13)*

### LC-04 — Internal Review (the CD hard gate; AD optional)
Artist marks the layout ready. AD review is optional and may happen before or be requested during CD's look (see AD-07/CD-06 for the second-review pattern). **CD sign-off is always required — no JO reaches Internal Approved without it, and CD can approve without AD ever seeing it.** Approve → Pending Release. Return → Revision. Rail copy never says "optional" on-screen — the step still functions as optional, it just doesn't announce it. ✅ *(corrected — this was previously documented as an AD-only gate; see D-020)*

### LC-05 — Revision
Revision count increments; 3+ triggers the soft-cap flag. Every revision now records its **origin** — internal (AD/CD, during the original Internal Review loop), requestor, or purchasing (D-022) — immutable once set. Origin determines the return address once the revision re-clears Internal Review (D-023, INV-18); it is never a manual choice for whoever completes the rework. 🔧 *(confirm live backend computation, not a demo counter — same treatment as the workload alert)*

### LC-06 — External Review (flag, not a stage)
Requestor can raise any time before Pending Release, naming the reviewer. Visible to Artist/PC/AD/CD as an active flag. ✅

### LC-07 — Pending Release (Requestor go-signal + print-route choice — no approval gate)
Surfaced on Requestor dashboard with blocker-note field. Dormancy counter visible to CD. **No CD sign-off happens here** — the JO already carries its CD stamp from Internal Review. This stage is the Requestor's explicit go-signal plus the in-house-vs-Purchasing routing decision; RFQ/RS# optionally logged while waiting. ✅ *(corrected — this was previously documented as the CD hard gate; see D-020)*

### LC-13 — In-House Printing *(new, D-024)*
Requestor's print-route choice at Pending Release. Routes to the **Artist**, not Purchasing, as a go-ahead to print — the Artist owns execution. AD, CD, and PC are notified for visibility but aren't owners of the action (INV-19). Exits to Closed.

### LC-14 — Free printing / Digital Placements — link presence gates the send, RS# never applies *(new, D-025)*
For these two routes specifically, there is no RS# concept at all (INV-20). The only gating condition is whether the Artist has produced the final file link:
- **Link already exists** (e.g. a durable Drive link) → either the Artist or the Requestor can send it onward — Requestor typically does, since no further artist action is needed.
- **No link yet** → nothing is actionable until the Artist provides one. A future nudge system (not yet built) will ping the Artist if this sits too long; until then it's a visibility-only wait state, not a Requestor action item.

### LC-15 — Mall Admin Approval, and the full sequence after Internal Review *(extended, Jul 28 session — supersedes the one-line version)*
Optional, Requestor-triggered flag on a row — raised only if that row's placement needs mall/landlord sign-off, sitting after Internal Review and before the print/release branch (INV-21). Same non-stage treatment as External Review (INV-04): raising or clearing it never changes the row's actual stage.

**The full sequence this sits inside (INV-28), previously undocumented:** Internal Review clears → Mall Admin Approval clears if raised, otherwise skipped → Requestor nudges the Artist for the final file, skipped if the Artist already provided it → the row's media type decides what happens next, independently per row:
- **Digital**: Requestor sends the final link directly to whoever needs it. Done. Purchasing never involved.
- **Printed**: Requestor sends the final link plus RS# (if required) to Purchasing → LC-18.

### LC-18 — Purchasing as parent stage, Printing as sub-status *(new, Jul 28 session — corrects the flat "Sent to Purchasing" framing)*
A row that needs Purchasing custody (INV-20) enters **Purchasing** as its stage. "Printing" — sent to supplier — is a **sub-status inside Purchasing**, not a stage of its own. Purchasing marks the row **Done** once the print comes back. This is the same branch point as LC-13's in-house exception, just stated from the other side: does this row need Purchasing custody at all? No → LC-13, straight back to the Artist. Yes → this scenario.

### LC-08 — Sent to Purchasing
The outside-print route only (see LC-13 for In-House). Requestor sees "Sent to Purchasing" only, no granular print detail — Purchasing sees the Printing sub-status per LC-18. Purchasing pings Requestor on change. **Supplier rejection: full chain is Purchasing → PC → Artist → Internal Review → Purchasing** (PU-04/D-009, INV-18) — *(corrected, Jul 28 session: this previously said the revision "returns directly to Purchasing," which described the endpoint but skipped the PC hop — Purchasing notifies the PC, who triggers the artist, same as any other Purchasing-raised revision; the destination was always right)*. ✅

### LC-16 — Combo JO: independent digital + printed tracks *(new, D-027/D-028)*
One JO, one branch, can carry both a digital placement track and a printed track simultaneously — each with its own final-file nudge, its own send/route action, and its own lifecycle stage (INV-01 v3). They complete independently: the digital track can reach Closed while the printed track is still waiting on RS# or sitting In-House Printing. The JO's own status is an aggregate of its rows, never a single borrowed stage. Same principle scales to multi-branch JOs — one row per (branch, track) pair, per row sorted per DL-13, summarized on the collapsed card per DL-14. 🔧

### RQ-19 — Branch/track-level deadline override *(new, D-029)*
A Requestor can mark a specific branch, or a specific track within a branch, as rush — overriding the JO's default +3-day deadline for that row only (INV-22). Falls through to the next level up when no override is set: track → branch → JO default. Triggers DL-14's card-level urgency signal and DL-13's drawer sort-to-top for that row once active. 🔧

### LC-09 — Closed
Counted in Closed stats. Clickable from Requestor dashboard. ✅

### LC-10 — Reopen (branches off Closed)
Requestor **or PC**-triggered, reason required (INV-03), notifies Artist/PC/AD/CD. **Corrected (Jul 28 session, INV-25) — supersedes D-002's "manually chosen by the Requestor":** re-entry is not a manual stage choice by whoever reopens it. Reopen sends the JO to the **PC**, who reassigns it (same or new artist) using normal assignment authority (INV-06) — the same custody handoff as any other assignment, not a special reopen-specific choice.

### LC-11 — Final deliverable link
Artist populates (pasted link, not upload). Read-only/empty on Requestor's view until populated. ✅

### LC-12 — Deadline passes while awaiting External Review
Resolved (D-011): the deadline-breach flag stays visible but is **annotated** to note External Review is active (e.g. "Deadline passed — awaiting external review by [name]") rather than hidden or left unexplained. ✅

---

## Part 1.5 — Layout Approval Sheet *(new — Round 16, resolves D-047/D-048)*

**Confirmed as a build-it MVP feature (D-047)** — the drag-and-drop label & compile tool, fully specified in Spec v4 but never given a scenario ID or built. Research into comparable proofing/signage platform patterns informed the mechanics below (see project reference material for the full findings). This section covers the tool end to end: dimension checking on upload, partial/staggered sheet submission, and the auto-compiled final sheet.

### LC-19 — Proxy upload dimension check
For each placement, the Artist drops in the for-approval proxy (small JPG/PNG/MP4/PDF — never the final deliverable file, see INV-32). The system checks the proxy's aspect ratio against **that JO row's own declared W×H** — not a separate Material library lookup (INV-31). Within ~2–3% tolerance, no signal shown. Outside tolerance, or any orientation mismatch (hard flag regardless of tolerance): a visible mismatch badge appears beside the artwork, never covering it, plus an "Upload as-is" button the Artist must click to proceed and an optional reason field. This never blocks submission — it requires acknowledgment, not permission. Override is logged (who, which placement, timestamp, reason if given). 🔧

### LC-20 — Partial approval sheet submission and independent release
The Artist submits a subset of the JO's placements as one approval sheet — not required to be the full set. AD or CD clears that sheet; on approval, its placements release immediately to the Requestor and reflect as approved on the JO, without waiting on placements not yet submitted or still in review (INV-33). This is the mechanism behind rush scenarios — a Requestor's urgent placements can ship while slower placements on the same JO are still in layout or revision. Purchasing's visibility opens on this same per-sheet basis (see PU-06). 🔧

### LC-21 — Final auto-compiled sheet, mixed approver attribution
Once every placement on a JO has cleared — across however many partial sheets it took — the system auto-compiles a single final sheet covering all of them; this is generated automatically, not manually reassembled (INV-33). Each placement on the final sheet is stamped with whichever approver actually cleared it — AD or CD, independently per placement, since AD and CD routinely clear different placements on the same JO in parallel (INV-23's per-placement entry-lock is what makes this possible without a conflict). Mixed AD/CD attribution across one compiled sheet is the expected, normal case. 🔧

---

## Part 2 — Per-role scenarios

### Requestor (RQ)
| ID | Scenario | Status |
|---|---|---|
| RQ-01 | Files a JO for a single branch | ✅ |
| RQ-02 | Files a JO covering multiple branches, each with multiple floor/contact entries | ✅ |
| RQ-03 | Types a custom identity not in the roster (pending admin approval) | ✅ |
| RQ-04 | Is scoped to a single JO type — form only shows that type | ✅ |
| RQ-05 | Raises an External Review flag mid-pipeline, names the reviewer | ✅ |
| RQ-06 | Checks Pending Release status, adds a blocker note | ✅ |
| RQ-07 | Sees "Sent to Purchasing" instead of granular print status | ✅ |
| RQ-08 | Clicks "Closed this month" to see the closed-JO list | ✅ |
| RQ-09 | Reopens a closed JO with a typed reason | ✅ *(destination corrected — see LC-10/INV-25: goes to PC, not a Requestor-chosen stage)* |
| RQ-10 | Browses official placement/material bank, adds to personal bank | ✅ |
| RQ-11 | Edits personal bank entry independently of official record | ✅ |
| RQ-12 | Opens/forwards final deliverable link once populated | ✅ |
| RQ-13 | Enters a malformed phone number, gets flagged inline | ✅ *(built Round 16 as real-time guard, not just submit validation — CP#/landline reject non-matching characters while typing, pattern-checked against `09XX-XXX-XXXX` / landline formats on blur; formalized as DL-18)* |
| RQ-14 | Enters size in feet — no inches conversion shown to Requestor (Artist-side only) | ✅ *(Requestor side unchanged; the referenced Artist-side conversion is AR-03, which is NOT built — see D-056)* |
| RQ-15 | Uploads an unsupported file type on Reference/Mockup | ✅ *(resolved D-006: accepts jpg/jpeg/png/pdf; tiff reserved for Final Deliverable only; max file size enforced; other types go through the pasted link, not direct upload)* |
| RQ-16 | Edits a JO's branch/contact details while Artist is actively working on the layout | ✅ *(resolved D-007: edit lock held by PC during active work)* |
| RQ-17 | Browses a branch's Placement Library, selects which placements to append to the current request | ✅ *(resolved D-016/D-017: never auto-applied, Requestor manually pulls and selects)* |
| RQ-18 | Raises a revision after Pending Release — e.g. spots an error on the compiled sheet before printing | 🔧 *(new, D-023 — re-clears Internal Review, then auto-returns to the Requestor per INV-18; not a manual routing choice)* |
| RQ-20 | Checks what revisions are visible to them on their own JO | 🔧 *(new, INV-24 — sees revisions they raised, revisions Purchasing raised on their JO, and the final released version; does not see internal AD/CD back-and-forth)* |
| RQ-21 | Cancels or holds their own JO | 🔧 *(new, INV-26 — Requestor is one of four roles, alongside AD/CD/PC, who can cancel/hold without routing through the PC first; assignment itself stays PC-exclusive)* |
| RQ-22 | Switches between "My JO Requests" and "All JO Requests" to check for an existing/duplicate request | 🔧 *(new, INV-13 widened — same Requestor-tier visibility, different scope: mine vs. everyone's)* |
| RQ-23 | Browses the Placement Bank via a searchable popup, sorted by Mall → Branch, uses "Use this" to pull a placement into the current JO form without closing the modal — repeats for more, closes only on X, then edits any pulled-in field manually. Once the JO ships to its next stage, the placement (new or reused) auto-appends to the Universal Placement Bank | 🔧 *(new, concrete UI answer to D-016/D-017; corrects hierarchy per INV-29)* |
| RQ-24 | Flags a single placement (not the whole JO) as needing revision | 🔧 *(new, INV-34 — routes by JO state: ongoing JO goes straight to the Artist with the PC notified; fully closed JO routes to the PC first, who reassigns, same as a full reopen)* |
| RQ-25 | Views a JO's status on their dashboard/detail view | 🔧 *(new, INV-35 — always shown as a per-placement breakdown, e.g. "7 approved · 2 in revision · 1 pending," each entry drillable to its actual stage. Top-level "Closed" label only appears once literally every placement has cleared)* |
| RQ-26 | Types a remark on a multi-branch, multi-item-type JO (e.g. a banner at one branch, a voucher at another) | ✅ *(built Round 16, formalized Round 17 as INV-36 — no global JO remarks field exists; every item row/single-spec entry carries its own remarks field, tied to that placement only)* |
| RQ-27 | Types a width/height/quantity value on the JO form | ✅ *(built Round 16, formalized Round 17 as DL-18 — non-digit characters are rejected as typed, not caught on submit)* |
| 🆕 | *(add new Requestor scenarios here)* | |

### Artist (AR)
| ID | Scenario | Status |
|---|---|---|
| AR-01 | ~~Claims a JO from the unclaimed pool~~ **Removed — self-claim eliminated (INV-06/INV-26).** All assignment is PC-initiated; see PC-01. | ❌ *(superseded, Round 13)* |
| AR-02 | Is assigned via the PC (suggested-artist field is a Requestor hint, not a binding claim) | ✅ *(corrected wording — "directly assigned via suggested-artist field" read as bypassing PC assignment, which isn't the case)* |
| AR-03 | Sees feet-entered sizes with inches conversion shown alongside | ❌ *(corrected Round 17 — this was marked built for at least two rounds; a direct code check on July 29 found no conversion logic anywhere in the Artist view. Logged as D-056, genuinely outstanding, not yet built)* |
| AR-04 | Submits for Internal Review | ✅ |
| AR-05 | Receives a returned-for-revision note (internal channel) | ✅ |
| AR-06 | Replies to Requestor in the Requestor-facing channel | ✅ |
| AR-07 | Populates the final deliverable link | ✅ |
| AR-08 | Appears in the workload-imbalance alert | ✅ |
| AR-09 | Is reassigned mid-JO | ✅ *(not re-audited recently for dashboard/detail consistency)* |
| AR-10 | Artist is transferred/transitioned off a JO mid-work (never "abandoned") | ✅ *(resolved D-008: notifies PC with reason; PC reassigns, not automatic)* |
| AR-11 | Artist is assigned a specific placement within a JO, different from the JO's Primary Artist | ✅ *(resolved D-013/D-014: placement-level override, selector on the placement row)* |
| AR-12 | Artist self-raises a revision on a placement they already delivered | 🔧 *(new, INV-34 — if the JO is still ongoing, goes straight to Internal Review, skipping PC and Requestor entirely; if the placement was already approved and released, the Requestor is notified and the PC is notified too, even though the PC has no reassignment action to take here)* |
| 🆕 | *(add new Artist scenarios here)* | |

### Project Coordinator (PC)
| ID | Scenario | Status |
|---|---|---|
| PC-01 | Sees unclaimed JOs needing assignment | ✅ |
| PC-02 | Sees generic stage state only for internal AD/CD conversations | ✅ |
| PC-03 | Sees the workload-imbalance alert | ✅ |
| PC-04 | Sees deadline-breach flag | ✅ |
| PC-05 | Nav reads "What needs assigning?" | ✅ |
| PC-06 | Receives notification when Artist is transferred/transitioned off a JO (see AR-10), reassigns manually | ✅ *(resolved D-008)* |
| PC-07 | Assigns an artist to a Submitted JO — the only path into In Layout (LC-17) | 🔧 *(new, INV-06/INV-26 — no self-claim exists anymore)* |
| PC-08 | Receives a Purchasing-raised revision, triggers the artist | 🔧 *(new, INV-18 corrected — full chain is Purchasing → PC → Artist → Internal Review → Purchasing; PC never bypassed, Purchasing was never supposed to trigger the Artist directly)* |
| PC-09 | Receives a reopened JO, reassigns it (same or new artist) | 🔧 *(new, INV-25 — reopen destination is the PC, not a Requestor-chosen re-entry stage; see LC-10)* |
| PC-10 | Cancels or holds a JO | 🔧 *(new, INV-26 — PC retains this alongside AD/CD/Requestor; unlike assign/reassign, cancel/hold doesn't require PC exclusivity, it's just that PC also has it)* |
| PC-11 | Notified of a placement-level revision (RQ-24 or AR-12), even on the branches where the PC has no reassignment action | 🔧 *(new, INV-34 — keeps the PC in the loop across all placement-revision paths, matching the visibility-not-blocking pattern already used for revision routing elsewhere)* |
| 🆕 | *(add new PC scenarios here)* | |

### Art Director (AD)
| ID | Scenario | Status |
|---|---|---|
| AD-01 | Reviews artwork in Internal Review | ✅ |
| AD-02 | Approves → toward Pending Release or External Review | ✅ |
| AD-03 | Returns for revision | ✅ |
| AD-04 | Sees full internal comment thread | ✅ |
| AD-05 | Sees deadline-breach flag | ✅ |
| AD-06 | Nav reads "What needs my review?" | ✅ |
| AD-07 | Requests a second look from CD after AD has already approved, if AD wants CD's eyes before it moves on | 🔧 *(new, D-021 — either direction, AD→CD or CD→AD; needs a presence indicator so both reviewers can't approve into a conflicting state simultaneously)* |
| AD-08 | Tries to open Internal Review while CD already has it open | 🔧 *(corrected, INV-23 — entry-lock, not action-lock: AD is blocked from entering at all, shown "currently viewed by [CD's name]," not just blocked from approving while still able to look)* |
| AD-09 | Cancels or holds a JO | 🔧 *(new, INV-26 — AD is one of four roles who can do this without going through the PC)* |
| 🆕 | *(add new AD scenarios here)* | |

### Creative Director (CD)
| ID | Scenario | Status |
|---|---|---|
| CD-01 | Signs off at Pending Release via Approval Sheet | ✅ |
| CD-02 | Sees revision soft-cap flag | 🔧 *(confirm live counter, see LC-05)* |
| CD-03 | Sees workload-imbalance alert | ✅ |
| CD-04 | Sees deadline-breach flag | ✅ |
| CD-05 | Notified when a JO is reopened | ✅ *(scope corrected — reopen can be Requestor- or PC-triggered now, see LC-10/INV-25; CD is notified either way)* |
| CD-06 | Requests a second look from AD before signing off, or reviews after AD already has | 🔧 *(new, D-021 — see AD-07. If the second reviewer raises no revision, the first approval carries through stamped "also reviewed by [role]." If a revision is raised, both approvals stamp — first approval flagged "requested 2nd review" plus the second reviewer's revision-approval — and the first approver gets a go-signal acknowledgment before release, not a veto over the second review)* |
| CD-07 | Tries to open Internal Review while AD already has it open | 🔧 *(corrected, INV-23 — same entry-lock as AD-08, from the other direction)* |
| CD-08 | Cancels or holds a JO | 🔧 *(new, INV-26)* |
| 🆕 | *(add new CD scenarios here)* | |

### Purchasing (PU)
| ID | Scenario | Status |
|---|---|---|
| PU-01 | Sees full print-queue detail | ✅ |
| PU-02 | Pings Requestor on status change | ✅ |
| PU-03 | Closes a JO once printing/delivery completes | ✅ |
| PU-04 | Supplier rejects/flags an issue with the artwork | ✅ *(resolved D-009, corrected Jul 28 — Purchasing flags it and notifies the PC, who routes it to the Artist for revision, not Purchasing going direct; CD/AD/PC/Requestor/Artist all notified — Requestor sees generic state only, same two-channel model)* |
| PU-05 | Purchasing views print-queue detail vs. the custody rail | ✅ *(resolved D-048, Round 16 — one unified grant, not two. Purchasing has no visibility into a JO's existence at all until placements release to them; the same release event that opens rail visibility also opens sheet access)* |
| PU-06 | Purchasing receives a partial approval sheet — some placements on a JO released, others still in review | 🔧 *(new, INV-33 — Purchasing's view must show a pending-count indicator, e.g. "7 more placements pending approval," so a partial set is never mistaken for the full order)* |
| 🆕 | *(add new Purchasing scenarios here — being expanded properly, not left thin)* | |

### Admin (ADM)
*(Un-deferred — Ed's review, July 29: this is being built as the actual platform, not a demo, so nothing here stays intentionally thin. Status below reflects that these are scoped and real, just not yet built — not postponed.)*

| ID | Scenario | Status |
|---|---|---|
| ADM-01 | Approves a pending custom Requestor name into the roster | 🔧 *(UI shown, backend not confirmed)* |
| ADM-02 | Adds/removes an Artist from the fixed roster | 🔧 *(same)* |
| ADM-03 | Sets a Requestor's JO-type scope | 🔧 |
| ADM-04 | Manages the official placement/material bank | ✅ |
| ADM-05 | Deactivate / reactivate a user | 🔧 *(scoped — real account management, not a demo placeholder)* |
| ADM-06 | Rename a branch | 🔧 *(scoped)* |
| ADM-07 | Merge duplicate Requestor entries | 🔧 *(scoped)* |
| ADM-08 | Archive / restore an artist | 🔧 *(scoped)* |
| ADM-09 | Manage granular permissions beyond role | 🔧 *(scoped)* |
| ADM-10 | View audit logs | 🔧 *(scoped)* |
| ADM-11 | Organization-wide settings | 🔧 *(scoped)* |
| 🆕 | *(add new Admin scenarios here as they're specified)* | |

---

## Part 3 — Role-to-role interaction scenarios

| ID | Interaction | Scenario | Status |
|---|---|---|---|
| RX-01 | Requestor → PC | JO filed, lands in PC's assignment view | ✅ |
| RX-02 | PC → Artist | JO assigned or self-claimed | ✅ |
| RX-03 | Artist ↔ Requestor | Comment/reply thread — visible to both + AD/CD/PC (generic for PC) | ✅ |
| RX-04 | Artist ↔ AD/CD | Internal craft review, invisible to PC/Requestor | ✅ |
| RX-05 | AD → CD | Internal approval clears, JO eligible for CD sign-off | ✅ |
| RX-06 | CD → Purchasing | Sign-off auto-advances to Printing | ✅ |
| RX-07 | Purchasing → Requestor | Status ping on print/supplier changes | ✅ |
| RX-08 | Requestor → all internal roles | External Review flag raised | ✅ |
| RX-09 | Requestor → Artist/PC/AD/CD | Reopen notification fan-out | ✅ |
| RX-10 | PC ↔ CD | Workload-imbalance alert visible to both | ✅ |
| RX-11 | Requestor ↔ Artist | Requestor edits JO details while Artist is actively working | ✅ *(resolved D-007: PC-held edit lock during active work)* |
| RX-12 | PC ↔ Artist | Artist reassigned while a revision is actively in progress — who owns the existing comment thread, the old artist or the new one? | ✅ *(resolved D-010: new artist owns the thread)* |
| RX-13 | Any commenter ↔ thread participants | Comment is edited after posting | 🔧 *(new, INV-07 reversed — Ed's review, July 29. Edit shows a visible "edited" tag, expandable to the change; editing fires the same notification fan-out as a new comment)* |
| 🆕 | *(add new cross-role scenarios here)* | | |

---

## Part 4 — System-triggered events (no human initiates these)

| ID | Event | Trigger condition | Status |
|---|---|---|---|
| SYS-01 | Deadline-breach flag appears | JO passes filed+3 days without reaching In Layout | ✅ |
| SYS-02 | Workload-imbalance alert computes | Any artist's active count > team median × 1.5 (Printing/Closed/Pending Release excluded from "active") | ✅ |
| SYS-03 | Pending Release dormancy counter increments | Daily, while JO sits in Pending Release | ✅ |
| SYS-04 | Revision soft-cap flag appears | Revision count reaches 3 | 🔧 *(confirm live computation)* |
| SYS-05 | Auto-advance to Printing | CD signs off at Pending Release | ✅ |
| SYS-06 | Reminder/nudge sent 🆕 | Not currently spec'd to repeat — confirmed as flag-only, no repeat nudge (per earlier decision) | ✅ *(decision already made: passive, one-time flag, not a repeating reminder)* |
| SYS-07 | Auto-archive old uploads/attachments 🆕 | Not spec'd — flag if storage growth ever needs this | 🔧 |

---

## Part 5 — Notification Matrix

| Trigger | Recipients | Method | Priority | Dismissible? | Persistent? | Deep link? |
|---|---|---|---|---|---|---|
| JO submitted, unclaimed | PC (+ suggested Artist if named) | Dashboard flag | ACTION REQUIRED | — | Until claimed | To JO detail |
| Artist claims/assigned | Requestor | Ping | INFO | Yes | No | To JO detail |
| Internal Review return | Artist | In-thread (internal channel) | ACTION REQUIRED | — | Yes (thread entry) | To JO detail/Activity |
| External Review flag raised | Artist, PC, AD, CD | Dashboard/detail flag | INFO | No | While flag active | To JO detail |
| Deadline-breach | CD, AD, PC | Passive dashboard flag | ACTION REQUIRED | No | Until resolved | To JO detail |
| Workload-imbalance | PC, CD | Dashboard banner | ACTION REQUIRED | No | While over threshold | To Artist's queue |
| Revision soft-cap (3+) | CD, AD | Dashboard flag | ACTION REQUIRED | No | While ≥3 | To JO detail |
| Pending Release dormancy | CD | Counter on sign-off queue row | ACTION REQUIRED | — | While pending | To Approval Sheet |
| CD sign-off complete | Purchasing (auto-advance) | System transition | INFO | — | — | — |
| Sent to Purchasing | Requestor | Ping | INFO | Yes | No | To JO detail |
| Purchasing status change | Requestor | Ping | INFO | Yes | No | To JO detail |
| Supplier rejects artwork (PU-04) | CD, Purchasing (+ Artist once routed) | Dashboard/detail flag | BLOCKER | No | Until resolved | To JO detail |
| JO closed | Requestor | Passive (visible in Closed list) | INFO | — | — | To JO detail |
| Reopen triggered | Artist, PC, AD, CD | Notification fan-out | BLOCKER | Yes | No | To JO detail |
| Comment posted (Requestor-facing) | Requestor, Artist, AD, CD, PC (generic only) | In-thread + "✓ Posted" toast to poster | INFO | Toast: auto | Thread: yes, toast: no | To Activity |
| Comment posted (internal) | Artist, AD, CD only | In-thread | INFO | — | Yes | To Activity (internal tab) |

**Priority scale**: INFO (no action needed, just visibility) · ACTION REQUIRED (someone needs to do something, not urgent) · BLOCKER (actively stopping the JO from moving, e.g. reopen or a supplier rejection). This scale exists to support future notification filtering — not built yet, just categorized so it's ready when it is.

**Resolved (D-012)**: Dismissible/Persistent columns above are confirmed, not best-guess. Logic: any row representing an active, unresolved condition on the JO itself (breach, dormancy, imbalance, rejection) is never user-dismissible — it only clears when the underlying condition does. Any row that's just a heads-up ping (assigned, status change, reopen) is dismissible, since acknowledging it doesn't change any underlying state.

---

## Known open questions → see `EO_Changelog_v8.md` Decision Backlog for the formal tracked version.


