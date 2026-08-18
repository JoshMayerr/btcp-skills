# Financial controls

Apply the controls that are relevant to the supplied statements, schedules, and reporting basis. Record the inputs, calculation, target, residual, tolerance, provenance, and result for each applicable control. Mark unavailable controls as `not tested` with the missing input; never mark them as passed.

## Default tolerances

Use a sponsor-specified tolerance when available. Otherwise use a monetary tolerance equal to the greater of one reporting currency unit or `0.01%` of the absolute comparison target. Require exact agreement for entity and period coverage, mapping completeness, formula integrity, and workbook structure. Treat rounding differences separately from unexplained differences.

## Source integrity and coverage

- Confirm company, entity, period, scenario, cadence, currency, and unit from the source rather than the filename alone.
- Detect missing or duplicate companies, entities, periods, statements, segments, and schedules.
- Compare conflicting versions using content, timestamps, approval markers, and the user's reporting instructions; do not assume the newest filename is authoritative.
- Identify hidden rows, columns, sheets, filtered data, external links, formula errors, stale formula caches, and hard-coded values inside calculated ranges.
- Verify totals against visible and hidden inputs.
- For OCR or image-derived numbers, validate material values against a second representation such as a visible total, repeated schedule, or manual visual comparison. Mark material uncertainty `review required`.

## Statement controls

Test as applicable:

`assets = liabilities + equity`

`beginning cash + net cash movement = ending cash`

`ending cash on cash flow statement = balance sheet cash`

`gross profit = revenue - cost of sales`

`operating income = gross profit - operating expenses`

`net income = pretax income - taxes`, adjusted only for the source's stated presentation

Recalculate all presented subtotals from mapped detail. Confirm that current-period balance sheet values are point-in-time values and are not summed across months or quarters.

## Period and scenario controls

- Reconcile monthly detail to quarterly and YTD totals.
- Reconcile quarterly detail to annual or LTM totals when all required periods exist.
- Keep actual, budget, forecast, prior-year, and run-rate measures distinct.
- Confirm fiscal calendars before comparing or aggregating companies.
- Prevent partial-period results from being presented as complete periods.
- Recalculate variances, growth, margins, and per-unit KPIs from standardized values rather than trusting displayed source percentages.

## Segment and consolidation controls

Identify the complete population of legal entities, operating segments, branches, corporate activity, and eliminations.

As applicable, reconcile:

`sum(segments) + corporate/unallocated - intersegment eliminations = consolidated reported result`

`sum(company standardized results) + portfolio eliminations = portfolio standardized result`

`standardized reported result + approved adjustments = pro forma result`

Fail the control when an entity or segment is missing, corporate activity is buried or double counted, an elimination is omitted or duplicated, or an adjustment lacks a complete bridge.

## Cash, debt, and covenant controls

- Agree cash across statements, liquidity schedules, and reporting summaries.
- Agree debt principal by instrument to the balance sheet and debt schedule.
- Keep drawn principal, available capacity, letters of credit, accrued interest, and fees distinct.
- Recalculate net debt, gross leverage, net leverage, fixed-charge coverage, and other covenants from the governing definitions supplied.
- Do not substitute a generic covenant definition when governing definitions are absent; label the metric as proposed or not tested.
- Confirm maturity dates, interest rates, amortization, and covenant test dates before external reporting.

## KPI controls

- Preserve numerator, denominator, unit, population, and period for every KPI.
- Recalculate derived KPIs from the standardized inputs when possible.
- Do not aggregate ratios by simple addition or averaging unless the metric definition permits it; use weighted numerators and denominators.
- Keep bookings, billings, revenue, ARR, customers, locations, units, headcount, and other similarly named measures distinct.
- Flag definition changes and discontinuities across reporting periods or companies.

## Currency controls

- Preserve local-currency and reporting-currency values separately.
- Record the FX source, rate type, date or period, and translation method.
- Translate income statement flows and balance sheet stocks according to the supplied policy.
- Keep translation effects visible and reconcile them to consolidated results.
- Do not invent an FX policy or use a current spot rate for historical reporting without explicit authorization.

## Pro forma and adjustment controls

For every adjustment, verify source support, amount, sign, period, category, rationale, recurring status, approval status, and whether it overlaps another adjustment.

Reconcile:

`company-reported result + reclassifications = sponsor-standardized reported result`

`sponsor-standardized reported result + eliminations + approved adjustments = final pro forma result`

Keep acquisition annualization, synergies, run-rate savings, owner expenses, transaction costs, discontinued operations, and accounting reclassifications in distinct categories. Do not net unsupported offsets or double count an item in both reported results and adjustments.

## Source-to-output and presentation controls

- Trace every material output to source values and explicit transformations.
- Reconcile standardized outputs to the normalized layer and the normalized layer to source submissions.
- Recalculate formulas in the native engine and scan for formula errors.
- Compare output workbook structure and protected objects with the copied template.
- Render and inspect every published sheet or page for clipping, broken charts, hidden errors, illegible labels, incorrect units, stale periods, and accidental internal-only content.
