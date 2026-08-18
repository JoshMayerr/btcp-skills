# Metric definitions and controls

Use management definitions when they are explicit, consistent, and disclosed. Otherwise apply these defaults and state every departure.

## Required recurring-value basis

Calculate GRR, NRR, and recurring-value cohorts from comparable customer-level recurring-value snapshots such as MRR or ARR. Do not use bookings, total contract value, invoice amounts, cash receipts, or total revenue as a silent substitute. When only revenue is available, label the outputs as revenue retention or revenue cohorts and explain seasonality and non-recurring effects.

Use one currency and a consistent FX policy. Prefer constant currency for operating retention and report FX separately when FX is material.

## Period movement classification

For customer value `B` at the beginning of a period and `E` at the end:

| Condition | Classification | Amount |
| --- | --- | ---: |
| No value before the period and `E > 0` | New | `E` |
| Previously positive, `B = 0`, and `E > 0` | Reactivation | `E` |
| `B > 0` and `E > B` | Expansion | `E - B` |
| `B > 0` and `0 < E < B` | Contraction | `B - E` |
| `B > 0` and `E = 0` | Churn | `B` |
| `B = E` | No movement | `0` |

Do not infer new or reactivation until history coverage is established. If the first observed period may be a truncated history, label its positive balances as opening population, not new business.

## Retention

For the beginning-period customer population:

```text
Logo retention = retained beginning logos / beginning logos
Logo churn = churned beginning logos / beginning logos
GRR = (beginning value - contraction - churn) / beginning value
NRR = (beginning value + expansion - contraction - churn) / beginning value
```

Exclude new and reactivated value from standard NRR. Present reactivation separately. Exclude customers with zero beginning value from the denominator. State the treatment of pauses, credits, minimum commitments, acquisitions, divestitures, migrations, and negative balances.

## Growth decomposition

Reconcile:

```text
Ending value = beginning value
             + new
             + expansion
             - contraction
             - churn
             + reactivation
             + FX
             + acquired or divested value
             + identified migrations and corrections
             + residual
```

Never force the residual to zero. Quantify and investigate it. Treat changes caused only by customer-parent remapping, currency conversion, or data correction separately from commercial movements.

## Cohorts

Assign each customer to its first active recurring-value period only when history coverage supports that conclusion. Otherwise call it the first observed period and disclose the limitation.

For each cohort and age, show:

- Original and remaining logos
- Original and current recurring value
- Logo retention
- Gross value retention when movements are available
- Current value divided by original value
- Expansion, contraction, and churn contributions

Do not combine cohorts with different period lengths without normalization. Do not interpret an incomplete recent period as a mature cohort result.

## Concentration

For positive customer value in a period:

```text
Top-N concentration = value from the N largest customers / total customer value
HHI = sum of each customer's squared share
```

Show top 1, 3, 5, 10, and 20 where the population is large enough. Calculate by account and ultimate parent when parent consolidation is material. Reconcile customer value to the applicable reported total and disclose excluded or unattributed value.

## Pricing

Distinguish:

- Contracted price: stated contract, order-form, or amendment economics
- Realized price: billed or recognized value divided by a supported unit or usage measure
- ACV: annualized committed contract value under the stated convention
- ARPA or ARPU: recurring value divided by supported accounts or units

Separate price, volume, product mix, contract duration, and discount changes where the data permits. Do not call an increase in customer value a price increase without stable quantity and product evidence.

## Validation controls

Run all applicable controls:

1. Reconcile customer-period totals to reported company totals.
2. Reconcile ending value to beginning value and classified movements.
3. Reconcile beginning logos to retained and churned logos.
4. Reconcile cohort totals to the normalized customer population.
5. Reconcile segment and concentration totals to the same population.
6. Check duplicate customer-period rows, missing periods, negative values, invalid dates, mixed currencies, and unexplained restatements.
7. Recalculate all published formulas and inspect rendered tables and charts.

Use an explicit monetary tolerance equal to the greater of one reporting currency unit or `0.01%` of the applicable absolute total unless the source precision requires a larger tolerance. Require exact agreement for logo counts and classification completeness.
