# Audit output schema

## Executive conclusion

State:

- Target, strategy or fund, decision stage, and as-of date
- Overall conclusion: `Strong fit`, `Conditional fit`, `Borderline`, `Poor fit`, or `Insufficient evidence`
- Evidence-covered score and evidence coverage when a numeric rubric is supportable
- Top three fits, exceptions or risks, and unresolved high-impact questions
- Confirmed mandatory failures separately from suspected disqualifiers

Do not use a score without its coverage percentage and mandatory-gate status.

## Mandate basis

Summarize the sources used to learn the mandate and their effective dates. List:

- Explicit current rules
- Behaviorally inferred rules and the cases supporting them
- Contradictions, strategy drift, sparse samples, and stale evidence
- Weight adjustments from the stated thesis to the applied rubric

## Thesis scorecard

Use this table or an equivalent structured representation:

| Priority | Criterion | Definition or threshold | Weight | Target evidence | Status | Score | Confidence | Provenance and notes |
| --- | --- | --- | ---: | --- | --- | ---: | --- | --- |

For unresolved criteria, leave `Score` blank and identify the exact missing evidence. Flag mandatory gates visually or textually. Keep base and behavior-adjusted weights visible when they differ.

## Exceptions and disqualifiers

Use separate sections:

### Exceptions

| Criterion | Miss | Historical tolerance | Compensating factor | Validation needed |
| --- | --- | --- | --- | --- |

### Potential disqualifiers

| Issue | Gate or severe risk | State | Evidence | What confirms or clears it |
| --- | --- | --- | --- | --- |

Use `Confirmed`, `Indicated`, or `Possible` for state.

## Historical analogues and operating angles

| Case or advisor work | Why relevant | Similarities | Differences | Original outcome or angle | Implication for this target |
| --- | --- | --- | --- | --- | --- |

Preserve source attribution. Do not imply that a prior operating angle has been validated for the current target.

## Priority diligence queue

| Rank | Question or request | Criterion and weight | Current evidence | Decision impact | Requested source or analysis |
| ---: | --- | --- | --- | --- | --- |

Order the queue by decision impact, not document order.

## Source and calculation appendix

Include:

- Claim ledger or a link to it
- Source inventory with dates and locations searched
- Definitions, period bridges, currency conversions, and calculations
- Material conflicts and how they were treated
- Missing or inaccessible sources, including systems not searched
- Assumptions and limitations

## Structured export

When the user requests machine-readable output, preserve these top-level objects:

```text
assignment
mandate_sources[]
criteria[]
claims[]
historical_cases[]
operating_angles[]
exceptions[]
potential_disqualifiers[]
diligence_questions[]
summary
limitations[]
```

Use stable criterion and claim IDs so evidence can be traced without duplicating prose. Keep source locations human-readable. Do not expose hidden reasoning; provide concise rationales and cited evidence.
