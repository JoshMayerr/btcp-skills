# Trading comps methodology

Use the target's business and the assignment's purpose to choose comparable companies. Favor a defensible universe over a large one.

## Select comparable companies

Evaluate business model, products and services, revenue model, customer type, end markets, geography, scale, growth, margin profile, capital intensity, cyclicality, and maturity. Apply analyst-supplied investment criteria as explicit gates or preferences.

Show every candidate considered. Assign an inclusion or exclusion decision with a concise rationale. Use relevance scoring only as a transparent aid; show the component criteria and do not allow a score to override a clear qualitative mismatch.

## Normalize periods and definitions

- State the valuation date and use market values from that date or the closest supported date.
- Identify each company's fiscal year end and the source periods underlying historical, LTM, and forward metrics.
- Prefer provider-supplied consensus periods when definitions are consistent. Otherwise calendarize only when the necessary quarterly data exists and disclose the method.
- Convert currency using a stated FX rate and date. Do not imply greater precision than the source supports.
- Keep reported EBITDA, adjusted EBITDA, EBIT, and other earnings measures distinct.
- Use a consistent lease-liability, preferred-equity, pension, and non-controlling-interest policy across the universe when data permits. Disclose exceptions.

## Calculate market values and multiples

Use a consistently diluted equity value when the required share and security data is available.

`enterprise value = equity value + total debt + preferred equity + non-controlling interests - cash and cash equivalents`

Add other adjustments only when they are defined, sourced, and applied consistently. Do not double count a provider-supplied enterprise value and its component adjustments.

Calculate:

- `revenue growth = current-period revenue / prior-period revenue - 1`
- `EBITDA margin = EBITDA / revenue`
- `EV/revenue = enterprise value / corresponding revenue`
- `EV/EBITDA = enterprise value / corresponding EBITDA`

Display `NM` and exclude the observation from statistics when the denominator is zero or negative, the numerator and denominator dates are incompatible, the metric definition is materially inconsistent, or the resulting multiple is not economically meaningful. Do not convert missing values to zero.

## Summarize the universe

Calculate minimum, 25th percentile, median, mean, 75th percentile, and maximum for each valid metric. Show the count of valid observations. Keep excluded and `NM` observations visible but outside the statistics.

Do not remove an outlier solely because it changes the mean. Explain and visibly flag any analytical exclusion. Let the analyst distinguish an operating outlier from a data error.

## Triangulate target valuation

Apply low, midpoint, and high selected multiples only to the corresponding target metric and period. Show revenue- and EBITDA-based indications separately.

`implied enterprise value = selected multiple * target metric`

`implied equity value = implied enterprise value - debt - preferred equity - non-controlling interests + cash and cash equivalents`

Show a target's observed or transaction multiple only when the associated valuation and financial metric are known on a compatible basis. Do not manufacture an observed multiple for a private target.

Explain why the selected range differs from the peer median or quartiles. Consider relative growth, margin, scale, recurring revenue, customer concentration, capital intensity, and risk, but keep qualitative premiums and discounts separate from sourced facts.

## Build the workbook

Create at least these sheets:

1. `Summary` — target profile, selected universe, operating comparison, valuation ranges, equity bridge, and key caveats
2. `Trading comps` — source inputs, derived financial metrics, multiples, inclusion status, and summary statistics
3. `Target financials` — target periods, definitions, adjustments, and valuation inputs
4. `Screening` — investment criteria, candidate companies, gate results, relevance considerations, and rationales
5. `Sources` — field or grouped-field lineage, retrieval dates, as-of dates, definitions, conflicts, and assumptions

Use formulas for derived values. Separate sourced inputs, formulas, and analyst assumptions visually. Include currency, units, valuation date, period labels, and fiscal-year conventions in headers. Freeze useful panes, apply readable number formats, and avoid decorative formatting that impairs auditability.
