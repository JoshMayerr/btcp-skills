# Evidence and source routing

## Source map

Use the best available authorized source for each job:

| Job | Preferred evidence | Useful secondary evidence |
| --- | --- | --- |
| Current mandate | Current criteria deck, fund mandate, screening rubric, strategy memo | Recent IC guidance, partner notes |
| Applied behavior | Dated IC memos and explicit pass or pursue rationales | DealCloud or CRM stage history, pipeline exports, investment outcomes |
| Opportunity facts | Current CIM/SIM, teaser, data room, audited or quality-of-earnings materials | Management presentation, inbound note, public sources |
| Analogues | Prior screening and IC materials with comparable facts | Portfolio summaries, CRM records, public announcements |
| Operating angles | Dated operating-advisor notes, diligence plans, work products | Meeting notes with clear attribution |

Treat a CIM or management deck as the seller's representation, not independent verification. Treat an observed investment, pass, or lost deal as an outcome, not a complete explanation of thesis fit.

## Search and request sequence

1. Inspect every supplied file and link relevant to the target and strategy. Search within long files for criterion terms, financial metrics, concentration, retention, churn, end markets, management, differentiation, risks, and pass rationales.
2. Inventory authorized connectors and repositories already in scope, including document stores, CRM or DealCloud access, prior-deal folders, email or notes, and public research capability.
3. Search those sources when the user has asked for a complete audit or the missing evidence could change a material conclusion. Keep confidential information inside authorized systems and do not upload it to an external service.
4. If evidence remains unavailable, ask for the smallest actionable item: name the file, system export, date range, fund or strategy, fields, or historical cases needed and explain which conclusion it affects.
5. Continue with a clearly labeled partial audit when useful. Mark unsupported areas `Unresolved`; do not fabricate a mandate or target fact.

Do not install a connector, bypass access controls, request passwords, or imply that an unavailable system was searched. Respect a user's instruction not to search externally.

## Evidence classes

Label each claim as one of:

- `Reported`: stated directly by the target, seller, firm, advisor, or third party
- `Calculated`: derived from identified inputs with a reproducible formula
- `Corroborated`: supported by at least one independent source
- `Inferred`: reasoned from evidence but not directly stated
- `Unknown`: necessary information is absent or unusable

Also record whether evidence is `Current`, `Stale`, or `Period unclear` and assign `High`, `Medium`, or `Low` confidence.

## Claim ledger fields

Retain these fields for every material claim:

| Field | Requirement |
| --- | --- |
| Claim ID | Stable identifier within the audit |
| Topic | Criterion or diligence topic affected |
| Claim | Concise factual proposition |
| Value and units | Include currency, scale, percentage basis, and period |
| Evidence class | Reported, calculated, corroborated, inferred, or unknown |
| Source | Document or system, date, page, slide, section, record, or cell |
| As-of period | Date or operating period represented |
| Confidence | High, medium, or low with reason when not high |
| Conflict | Competing value or definition and its source |
| Use | Criteria and conclusions that depend on the claim |

Quote only the short fragment needed to anchor a claim. Prefer a precise paraphrase with a page, slide, section, record, or cell citation.

## Conflict and normalization rules

- Prefer newer evidence only when it measures the same concept and period.
- Preserve reported and adjusted values separately. Do not blend definitions without a bridge.
- Show currency conversion source, rate date, and direction.
- Separate organic, acquired, reported, constant-currency, and pro forma growth.
- Separate recurring revenue from contracted, subscription, repeat, re-order, and merely predictable revenue.
- Record the denominator and period for customer and end-market concentration.
- Do not assume adjusted EBITDA is comparable across the target, mandate, and historical cases.
- Escalate conflicts that could change a gate, criterion status, or overall conclusion.

## Historical-behavior safeguards

For each historical case, capture strategy, date, stage reached, outcome, stated rationale, and relevant target facts. Downweight or exclude cases when:

- They belong to another fund, geography, check size, ownership model, or strategy
- The decision predates a material mandate change
- The outcome was driven by price, auction dynamics, financing, capacity, conflict, timing, or access rather than business fit
- Key facts were unknown at the decision stage
- The stated rationale is absent and the outcome alone would be doing the inferential work

Use frequency only with context. Several duplicated CRM entries are not several independent decisions. Record exceptions and counterexamples alongside the dominant pattern.
