Follow the workflow below for this request. Do not install or create a persistent skill. Ask only for information that is necessary to complete the work.

# Integrate an add-on acquisition

Treat the work as one closed-transaction integration with two linked outputs: the pro forma financial model and the post-close capitalization table. Build one canonical transaction record and use it for both outputs. Never interpret the transaction independently in each workbook.

Read all four references before editing:

- [references/transaction-inputs.md](references/transaction-inputs.md) for source hierarchy and the canonical transaction record
- [references/financial-integration.md](references/financial-integration.md) for consolidation, mapping, and model treatment
- [references/capitalization-mechanics.md](references/capitalization-mechanics.md) for rollover and security calculations
- [references/acquisition-controls.md](references/acquisition-controls.md) for mandatory reconciliations and exception severity

## Establish scope and authority

Confirm that the transaction has closed. Use final executed agreements, final closing statements, and final funds-flow schedules as governing evidence. Use a term sheet, letter of intent, draft agreement, or pre-close model only as secondary support. Never let an earlier document override a final closing source without explicit user direction.

Identify:

- Acquirer, acquired company, legal closing date, accounting effective date, and consolidation perimeter
- Destination master model and destination capitalization table
- Target historical actuals, closing-period actuals, forecast, chart of accounts, and supporting schedules
- Purchase price, adjustments, sources and uses, debt, cash, fees, and security issuances
- Seller and management cash proceeds, rollover mechanics, incentive-pool changes, and fully diluted definitions
- Requested historical pro forma, post-close actual, forecast, purchase-accounting, and ownership outputs

Leave every source unchanged. Copy each destination workbook before editing. Do not update board, lender, LP, tax, legal, payroll, or equity-administration systems unless separately requested.

Require a native spreadsheet engine that can inspect, edit, recalculate, render, and export `.xlsx` files while preserving the workbook objects used by each destination. Stop before editing a workbook that cannot be faithfully round-tripped.

## Inventory and resolve evidence

1. Record filenames, hashes when available, document status, dates, sheets or pages, visible and hidden content, units, currencies, named ranges, formulas, formula errors, external links, and supported workbook objects.
2. Classify each item as governing closing evidence, supporting transaction evidence, target financials, destination model, destination cap table, or prior output.
3. Extract transaction terms with exact source locations. Record conflicting, missing, stale, or draft evidence rather than silently choosing among it.
4. Determine whether the cap table is a separate workbook or a controlled section of the master model.
5. Continue all unaffected work. Stop only a calculation whose unresolved ambiguity could materially change financial results, consideration, units issued, or ownership.

## Build the canonical transaction record

Create an in-memory or output-backed transaction record using the schema in `references/transaction-inputs.md`. Preserve value, currency, units, date, source location, document status, interpretation, and approval status for every material term.

At minimum, bridge:

`enterprise value -> equity purchase price -> seller gross proceeds -> cash proceeds and rollover value`

and:

`sources -> uses -> debt, cash, fees, repayments, seller payments, rollover, and other closing flows`

Do not use a plug, infer a missing term from an expected ownership result, or force conflicting schedules to agree. Use the same approved closing values in the model and capitalization table.

## Integrate the financials

Follow `references/financial-integration.md`.

1. Map target accounts, entities, locations, segments, periods, scenarios, units, currencies, and signs into the destination model using labels, hierarchy, formulas, subtotals, and documented definitions.
2. Preserve target-reported results separately from reclassifications, eliminations, purchase-accounting entries, annualization, synergies, and other pro forma adjustments.
3. Apply the supported consolidation basis by period. Distinguish pre-close historical pro forma, closing-period contribution, post-close actual, and forecast.
4. Reflect transaction financing, debt payoff, cash use, fees, interest, working capital, and valuation effects only when supported and applicable to the destination model.
5. Populate identified inputs and extend established formulas, ranges, styles, comments, and charts only as required. Preserve historical periods and unrelated assumptions.
6. Recalculate through the native spreadsheet engine and render every changed sheet and material output sheet.

Do not create detailed purchase accounting, goodwill, identifiable-intangible, deferred-tax, or opening-balance-sheet entries unless a final or explicitly approved purchase-accounting schedule supports them. Present unsupported proposed treatments separately and exclude them from final totals.

## Update the capitalization table

Follow `references/capitalization-mechanics.md`.

1. Establish pre-close issued and fully diluted capitalization by holder, holder group, security class, and dilution status.
2. Calculate seller or management rollover from the documented base, percentage or fixed amount, deductions, exchange ratio, and issuance price.
3. Record sponsor, co-investor, seller, management, incentive-pool, warrant, option, and other closing activity separately.
4. Distinguish issued, outstanding, vested, granted, reserved, and unallocated securities. Distinguish economic, voting, basic, and fully diluted ownership when the documents do.
5. Reconcile pre-close securities plus issuances, exercises, conversions, redemptions, cancellations, and pool changes to post-close capitalization.
6. Preserve security-specific economics. Do not collapse preferred, common, options, profits interests, warrants, or convertible instruments into equivalent units unless the governing documents define that presentation.
7. Recalculate and render the changed capitalization and ownership outputs.

Never assume that “roll 20%” means 20% of proceeds, retained target ownership, or post-close combined-company ownership. Stop the affected calculation when the governing basis is not explicit.

## Validate and classify

Run every applicable control in `references/acquisition-controls.md` against recalculated values. Trace each result to source and destination locations.

Use a monetary tolerance equal to the greater of one reporting-currency unit or `0.01%` of the absolute applicable total. Require exact agreement for security counts unless governing documents specify rounding; disclose every rounding residual. Require ownership totals to equal `100.00%` within the destination model's displayed precision and underlying formulas.

Classify issues as `critical`, `review required`, `warning`, or `informational`. Quarantine any output affected by a critical failure or material unresolved transaction term with `_REVIEW_REQUIRED`. Do not present it as final.

## Export the package

Unless the user specifies filenames, export:

- `<portfolio-company>_<add-on>_post-close-pro-forma-model.xlsx`
- `<portfolio-company>_<add-on>_post-close-cap-table.xlsx`

When both outputs live in one controlled workbook, export one `<portfolio-company>_<add-on>_post-close-model-and-cap-table.xlsx` file. Never overwrite a source or prior output.

Return a concise integration report with:

- Transaction, close date, accounting effective date, and governing sources
- Outputs and paths, source hashes when available, and sheets or cells changed
- Purchase-price, sources-and-uses, rollover, issuance, and ownership bridges
- Financial mapping and consolidation treatment by period
- Model-to-cap-table lineage for shared transaction values
- Control values, residuals, tolerances, and statuses
- Conflicts, inferred mappings, unsupported features, exclusions, and approvals required
- Material changes to revenue, earnings, cash, debt, leverage, valuation, sponsor ownership, seller or management ownership, and dilution

Do not claim that the work is audited, GAAP-compliant, tax-approved, legally definitive, sponsor-approved, or ready for external distribution unless the evidence and user authorization establish that status.
