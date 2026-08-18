# Evidence and confidence

Use this framework to keep extraction, enrichment, and calculation claims proportional to the evidence.

## Evidence hierarchy

| Grade | Typical sources | Permitted use |
| --- | --- | --- |
| Authoritative | Complete customer-level billing or recurring-value ledger; system export with defined fields and periods | Calculate supported financial and retention metrics after reconciliation |
| Corroborating | Signed contracts, amendments, invoices, CRM records, approved management schedules | Validate identity, dates, terms, values, and classifications; calculate only when population completeness is established |
| Indicative | Board decks, customer overviews, case studies, sales materials, management commentary | Form directional observations and identify follow-up questions |
| Unverified | Website logos, search results, third-party databases, inferred company matches | Discover or enrich possible customers; never establish population completeness, financial value, retention, or churn |

A source can be authoritative for one field and weak for another. A signed contract may be authoritative for contracted price and term but not for live status, realized revenue, or a complete customer population.

## Claim types

Label material fields and conclusions as one of:

- `reported`: stated directly in a cited source
- `calculated`: derived reproducibly from cited inputs and a stated formula
- `classified`: assigned using the taxonomy and cited evidence
- `inferred`: reasoned from indirect evidence and accompanied by rationale

Do not convert an inferred statement into a reported fact through repetition.

## Confidence

Assign field-level confidence:

- `high`: explicit, current, internally consistent evidence from an authoritative or corroborating source
- `medium`: credible indirect evidence or multiple consistent lower-grade sources
- `low`: ambiguous text or logo recognition, weak name matching, stale information, or a single unverified source
- `unresolved`: conflicting evidence or more than one materially plausible treatment

Confidence does not replace coverage. A high-confidence customer match from a website still does not prove the website shows all customers.

## Identity-resolution precedence

Resolve customer identities in this order:

1. Explicit customer ID or legal entity mapping supplied by the company
2. Contracting or billing entity and documented parent relationship
3. Exact normalized name plus corroborating domain, address, or registration information
4. Documented rename, acquisition, subsidiary, or brand relationship
5. Reasoned fuzzy match supported by at least one independent attribute

Retain the raw label, canonical label, match method, evidence, confidence, and reviewer status. Do not merge on fuzzy name similarity alone. Keep account-level and ultimate-parent-level views available when consolidation changes concentration or retention materially.

## Web and logo evidence

Use public sources only to fill a defined gap or corroborate an identity or classification. Record the URL, page title, access date, extracted text or image location, and the exact field supported.

Treat a logo as evidence only that the company publicly associated itself with the depicted organization at the observed time. It does not by itself establish a current paid relationship, revenue, customer start date, contract status, or churn. Search for a first-party case study, press release, or customer statement before increasing confidence.

## Population and survivorship controls

Before calculating financial metrics, determine whether the source includes:

- All customers or only selected, active, largest, referenceable, or renewed customers
- All periods or only current and selected historical periods
- Zero and churned customers or only positive balances
- All products, entities, currencies, and sales channels
- Historical customer names or only current canonical names

Mark calculations unavailable when the missing population could materially bias the result. Use directional language only when the limitation is quantified or bounded.
