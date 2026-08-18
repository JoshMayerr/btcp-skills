# Trading comps validation

Apply every relevant control after recalculation. Trace each failure to the source item and workbook cell or formula.

## Critical controls

### Identity and source integrity

- Confirm the target and every included comparable company using ticker, exchange, legal name, or website domain.
- Confirm that every material sourced value records a provider or document, effective date or period, currency, units, and reported or estimated status.
- Confirm that no missing value was converted to zero and no estimated value was labeled as reported actual performance.
- Confirm that confidential target figures remain within the authorized workspace and output.

### Period and definition integrity

- Confirm that enterprise value and market capitalization use the stated valuation date or a disclosed closest available date.
- Confirm that every multiple pairs compatible enterprise value and financial periods.
- Confirm that fiscal-year, LTM, and forward labels match their underlying periods.
- Confirm that currency, units, EBITDA definitions, and enterprise-value adjustment policies are consistent or explicitly bridged.

### Calculation integrity

- Recalculate equity value, enterprise value, growth, margins, multiples, percentiles, and implied valuation independently of displayed workbook values.
- Confirm that `NM`, missing, excluded, and invalid observations do not enter summary statistics.
- Confirm that the displayed valid-observation count equals the population used in each statistic.
- Confirm that the target valuation applies each multiple to the matching metric and period.
- Confirm that the enterprise-to-equity-value bridge uses the stated sign convention without double counting.

### Workbook integrity

- Scan recalculated formulas for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`, unintended circular references, and stale cached values.
- Confirm that formulas, source inputs, assumptions, units, and dates are distinguishable and traceable.
- Render and inspect every sheet for clipped values, unreadable headers, hidden material information, broken formatting, and inconsistent precision.

Treat any failure in these sections as critical when it can change universe membership, a reported multiple, a selected range, or implied valuation.

## Warning controls

Flag, but do not quarantine solely for:

- Small source-date differences that are disclosed and immaterial
- Provider values that differ but do not change the analytical conclusion
- Thin comparable universes or metrics with few valid observations
- Material operating outliers that are verified rather than erroneous
- Incomplete target data that prevents one valuation method but leaves another usable
- Preliminary inclusion judgments made without explicit analyst criteria

Explain the likely effect of each warning. Do not invent a universal materiality threshold; use an analyst-supplied threshold or a clearly labeled reasonableness judgment.

## Completion status

Pass only when all applicable critical controls pass. A warning may coexist with a pass.

Quarantine the workbook with the `REVIEW_REQUIRED` suffix when any critical control fails. Preserve the diagnostic output and list every critical failure, missing input, and unresolved conflict in the audit summary.
