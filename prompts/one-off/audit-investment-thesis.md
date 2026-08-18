Follow the workflow below for this request. Do not install or create a persistent skill. Ask only for information that is necessary to complete the work.

# Audit an investment thesis

Create a decision-useful audit, not an investment recommendation. Keep source facts, calculations, inferred mandate, historical behavior, unknowns, and analyst judgment separate. Never let an aggregate score hide a hard gate, conflict, or missing critical evidence.

Read these references before building the audit:

- [references/evidence-and-source-routing.md](references/evidence-and-source-routing.md)
- [references/audit-methodology.md](references/audit-methodology.md)
- [references/output-schema.md](references/output-schema.md)

## Establish the assignment

Identify the target, decision stage, relevant fund or strategy, as-of date, requested deliverable, and available source set. Inventory the opportunity materials, stated criteria, historical cases and dispositions, portfolio examples, operating-advisor work, and authorized CRM or document sources.

Proceed when the target and applicable strategy are reasonably clear. If a material input is missing, follow the search-and-request sequence in `references/evidence-and-source-routing.md`: inspect supplied materials, search authorized sources in scope, then ask the user for the smallest specific set of missing files or context. Do not quietly substitute a generic buyout thesis.

## Learn the mandate

Build a criterion register for the applicable strategy before scoring the target. Capture each criterion's definition, type, priority, threshold or preferred range, exceptions, provenance, effective period, and confidence.

Use stated current criteria as the primary mandate. Use prior memos, passes, investments, and CRM history to reveal applied thresholds, recurring exceptions, and actual emphasis. Treat behavior as evidence, not ground truth: fund strategy, date, deal stage, price, process, diligence findings, and data quality can explain outcomes unrelated to thesis fit.

Distinguish:

- Mandatory gates from weighted preferences and supplemental considerations
- Explicit criteria from behaviorally inferred criteria
- Current-strategy evidence from stale or different-strategy evidence
- Thesis fit from price, process, financing, or execution considerations

Do not infer a durable rule from an outcome alone. Cite the cases and reason codes that support every behavioral inference, record contradictory cases, and lower confidence when the sample is sparse or biased.

## Extract the opportunity evidence

Create a claim ledger from the target materials before applying criteria. Cover situation, business model and quality, financial profile, customers and revenue model, markets, management, differentiation, risks, and deal dynamics when disclosed.

For each material claim, retain its source location, as-of period, evidence class, confidence, and any conflict. Label management assertions as assertions unless corroborated. Show formulas and source inputs for derived metrics. Never convert missing disclosure into a favorable or unfavorable fact.

Normalize definitions only for this audit. Reconcile units, currency, periods, organic versus acquired growth, reported versus adjusted EBITDA, gross versus net retention, and customer or end-market concentration definitions before comparison.

## Apply the thesis

Map each criterion directly to target evidence and classify it as:

- `Fit`
- `Exception`
- `Unresolved`
- `Potential disqualifier`
- `Not applicable`

Apply the scoring and coverage rules in `references/audit-methodology.md`. Weight mandatory and repeatedly decision-driving criteria more heavily than supplemental criteria, but preserve the original weight and show any behavior-based adjustment. Exclude unresolved criteria from the evidence-covered score and report their missing weight separately; never score an unknown as neutral or zero.

Use the firm's stated pass or escalation thresholds when available. If none exist, do not invent an official cutoff. Present any calculated score as an analytical aid, label it provisional when evidence coverage is insufficient, and give the criterion-level conclusion precedence.

Surface:

- Clear fits and the evidence supporting them
- Exceptions the firm has historically accepted or rejected
- Questions that could resolve material unknowns
- Potential disqualifiers and whether they are confirmed or merely indicated
- Conflicting evidence, definitional mismatches, and sensitivity to adjustments

## Compare behavior and analogues

Compare the target only with relevant prior opportunities, investments, passes, and portfolio companies. Match on strategy, business model, revenue model, end market, size, growth, margin, concentration, situation, and the issue being tested. Explain both similarities and differences.

Link applicable operating-advisor angles to the criterion or risk they address. Preserve attribution and distinguish a reusable diligence angle from a fact about the current target. If the record lacks suitable cases or advisor work, state that no supportable comparison was available and request or search for it when material.

## Conclude and deliver

Assign an overall conclusion of `Strong fit`, `Conditional fit`, `Borderline`, `Poor fit`, or `Insufficient evidence`. A confirmed mandatory disqualifier overrides the weighted score. A suspected disqualifier remains a diligence item until the evidence supports confirmation.

Use the deliverable structure in `references/output-schema.md`. Include:

- Executive conclusion, evidence coverage, and decision framing
- Mandate provenance and any behaviorally inferred rules
- Criterion-by-criterion scorecard with weights, evidence, status, and confidence
- Confirmed fits, exceptions, unresolved questions, and potential disqualifiers
- Comparable historical cases and relevant operating-advisor angles
- Sources, conflicts, calculations, assumptions, and limitations
- Prioritized next questions, requested files, and recommended diligence actions

Return the audit in the user's requested format. If none is specified, produce a concise Markdown screening memo with tables. Do not alter source documents, update DealCloud, or make an investment decision unless the user separately authorizes that action.
