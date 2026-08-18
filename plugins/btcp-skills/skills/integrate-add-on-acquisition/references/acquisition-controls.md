# Acquisition controls

Run every applicable control against recalculated workbook values. Record inputs, formulas, calculated value, governing target, residual, tolerance, status, and source and destination locations.

## Transaction controls

Require:

`enterprise value + documented equity-value adjustments = equity purchase price`

`seller gross proceeds - debt payoff - deductions - escrow or holdback = distributable proceeds`

`cash proceeds + rollover value + other documented noncash consideration = applicable seller consideration`

`total sources = total uses`

Trace every source and use to the canonical transaction record. Detect rollover presented both as noncash consideration and cash funding, debt counted as both assumed and repaid, and fees included in more than one category.

## Financial controls

Require, as applicable:

- Target source totals equal mapped destination inputs.
- Mapped detailed accounts equal mapped subtotals.
- Entity and segment totals plus corporate, eliminations, and adjustments equal consolidated results.
- Reported, reclassified, eliminated, purchase-accounting, transaction, annualization, and synergy layers bridge to final pro forma results.
- Closing-period contribution matches the legal and accounting effective-date treatment.
- Balance sheet balances after supported acquisition entries.
- Cash-flow change in cash agrees with opening and closing cash.
- Debt draws, repayments, cash use, fees, and interest agree with the closing transaction and debt schedules.
- Forecast and historical pro forma periods do not double count target results or adjustments.
- Purchase-accounting entries agree with the approved opening-balance-sheet schedule when one is used.

Treat an unbalanced output as critical. Do not use goodwill, cash, debt, equity, or another account as an unsupported plug.

## Capitalization controls

Require, by holder and security class:

`pre-close + issuances + exercises + conversions - redemptions - cancellations - forfeitures = post-close`

Require:

- Rollover basis times the documented percentage, or the documented fixed amount, equals rollover value.
- Rollover contribution value divided by issuance price equals issued units when value-based issuance applies.
- Exchange-ratio calculations agree with eligible surrendered securities.
- Sponsor and co-investor contributions agree with sources and uses.
- Incentive-pool increase agrees with the documented pre-money or post-money definition.
- Basic and fully diluted denominators include only the instruments required by their definitions.
- Holder ownership equals holder securities divided by the applicable denominator.
- Ownership totals equal 100% within displayed precision and underlying formulas.
- Rounding follows the governing rule and every residual is disclosed.

## Cross-output controls

Require shared values to agree across the financial model, cap table, canonical transaction record, and closing evidence:

- Purchase price and seller consideration
- Acquirer cash and equity funding
- New debt and debt repayment
- Rollover value
- Sponsor and co-investor equity
- Issuance price or exchange ratio
- Security counts and post-close ownership
- Transaction fees when represented in both outputs

Do not accept equal totals composed of inconsistent underlying holders, classes, sources, or uses.

## Workbook-integrity controls

Require:

- Source workbooks remain unchanged.
- Expected destination sheets, formulas, named ranges, charts, tables, and links remain present.
- No new formula errors, broken references, or stale calculated values exist.
- No unintended historical, forecast, assumption, holder, or security cells change.
- Changed formulas follow established neighboring patterns.
- Rendered outputs preserve readable labels, units, dates, and ownership percentages.

## Severity

Classify as `critical`:

- Sources and uses do not balance.
- The model balance sheet or cash flow fails.
- Governing closing values do not agree with either output.
- Security rollforward or ownership does not reconcile.
- A material holder, class, source, use, entity, or period is omitted or double counted.
- Workbook structure or formulas are damaged.
- A required unsupported plug is present.

Classify as `review required`:

- Two plausible source, account, rollover, issuance, dilution, or effective-date interpretations remain.
- A material input is supported only by a draft or secondary source.
- Purchase accounting or fully diluted treatment lacks final support.
- An inferred mapping or unapproved adjustment materially affects results.

Classify as `warning`:

- A mathematically valid variance, margin, leverage, dilution, or ownership change is unusual.
- An immaterial residual remains within tolerance.
- A noncritical workbook feature could not be preserved or validated.

Classify harmless naming, formatting, or presentation differences as `informational`.
