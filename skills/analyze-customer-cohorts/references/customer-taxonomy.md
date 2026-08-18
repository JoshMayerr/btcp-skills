# Customer taxonomy

Classify each dimension independently. Preserve the reported label and add a normalized label, evidence, confidence, and rationale.

## Industry

Use the customer's primary operating industry, not the function that uses the product. Prefer a supplied sponsor taxonomy; otherwise use a concise hierarchy such as sector and subsector. Keep `unknown` rather than forcing a weak match.

## Business function served

Classify the primary buyer or workflow enabled:

- Executive and strategy
- Finance and accounting
- Sales and revenue operations
- Marketing and communications
- Customer success and support
- Product and design
- Engineering and IT
- Security, risk, and compliance
- Legal and procurement
- People and human resources
- Operations and supply chain
- Other or cross-functional
- Unknown

Allow multiple functions only when the evidence shows distinct deployments. Do not infer the function solely from the customer's industry.

## Customer size

Prefer a user-supplied definition. Otherwise classify using the best consistent field available and disclose it:

| Segment | Employees | Annual revenue |
| --- | ---: | ---: |
| SMB | Fewer than 250 | Less than $50 million |
| Mid-market | 250-1,999 | $50 million-$999 million |
| Enterprise | 2,000 or more | $1 billion or more |

Do not mix employee- and revenue-based labels silently. Store the observed value, measurement date, source, and size basis. Use `unknown` when evidence is unavailable.

## Geography

Keep contracting or billing geography separate from headquarters and deployment geography. Normalize country and region only to the precision supported by the evidence.

## Product, use case, and channel

Keep these distinct:

- `product`: purchased product, module, tier, or SKU
- `use case`: job performed or outcome sought
- `channel`: direct, reseller, referral, marketplace, embedded, or unknown
- `relationship`: paid customer, trial, partner, reseller, end customer, reference customer, former customer, or unknown

Do not assign revenue to an end customer when a reseller is the contracting party unless the source provides an allocation. Do not count a partner logo as a customer without evidence of a paid customer relationship.

## Classification controls

- Reconcile segment counts and value to the unsegmented population.
- Show `unknown` as its own bucket rather than excluding it.
- Preserve multiple views when a classification date changes over time.
- Flag classifications that rely only on public estimates or model inference.
- Avoid false precision in employee, revenue, and geography estimates.
