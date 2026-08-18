# Model Checks

Use the checks that apply to the adapted workbook. The goal is validation discipline, not forcing
every prior LBO into one standardized test harness.

## Source Integrity

- CIM-sourced numbers have page citations.
- Prior-model assumptions are clearly distinguishable from CIM inputs.
- Agent-chosen assumptions are yellow or otherwise labeled.
- No material input still references the old company.
- No formulas point to broken external workbooks.
- Any hidden sheets, macros, iterative calculation, or add-ins are identified.
- Reported EBITDA, adjusted EBITDA, supportable EBITDA, pro forma EBITDA, and future synergies are
  not mislabeled or combined.
- Prospective synergies are excluded from supportable EBITDA and the base case unless the user
  explicitly requested a separate synergy case.

## Prior Workbook Parity Check

Before finalizing, compare the output against the prior LBO:

- Same core tabs are retained unless removal is necessary.
- Same tab order is preserved or changes are clearly justified.
- Same major sections remain in the same locations where practical.
- Same row and column structure is retained for schedules that remain active.
- Same colors, fonts, borders, number formats, merged cells, and widths are preserved where
  practical.
- Same presentation style is preserved for returns, sensitivities, summaries, and print-ready pages.
- Old company name and old-company-specific commentary are removed or replaced.
- No stale old-company assumptions remain in active model areas.
- Broken inherited artifacts are fixed, removed, or flagged without changing the overall workbook
  look.
- Any hidden or relabeled old rows are traced so they do not still feed active formulas incorrectly.
- The output was created from a literal copy of the source workbook, not from a newly generated
  lookalike workbook.
- Sheet names, order, hidden states, used ranges, merged cells, freeze panes, gridline state, row
  heights, and column widths match the source except for documented, deal-required changes.
- Model-tab style IDs or equivalent style fingerprints have zero unexplained mismatches.
- Defined names, data validation, conditional formatting, print areas, charts, images, and
  calculation settings remain intact.
- The total formula count reconciles to the source formula count plus documented formula
  completions and minus documented removals.
- Every hardcoded input uses the template's native hardcode style; every formula and cross-sheet
  link uses the template's native formula or link style.
- Firm-native formatting conventions take precedence over every generic color convention.
- Where conventions vary across sheets or sections, each edited cell follows the applicable local
  convention rather than a workbook-wide palette imposed by the modeler.
- No standard blue/black/green/red/yellow palette was imposed where the workbook supplied a
  different identifiable convention.
- Any generic fallback styling is limited to genuinely new cells with no native analogue and is
  disclosed in the handoff.
- No existing formula was replaced by a hardcoded result.

## Operating Model

- Historical periods match the CIM labels.
- LTM or latest-period EBITDA used for entry value is the intended anchor.
- Revenue, EBITDA, capex, and working-capital rows link from source inputs or assumptions.
- Newly added line items flow through subtotals and downstream schedules.
- Removed or hidden old-deal lines no longer affect totals.
- Forecast margins and growth rates calculate correctly from visible rows.

## Sources and Uses

- Sources equal uses.
- Purchase price or enterprise value ties to the selected entry multiple or stated price.
- Fees calculate from the intended base.
- Cash to balance sheet, rollover, seller notes, debt-like items, and transaction adjustments are
  included only when supported or clearly assumed.

## Debt Schedule

- Beginning debt rolls from prior-period ending debt.
- Mandatory amortization, cash sweep, PIK, revolver draws, or repayments flow through ending debt.
- Debt does not go negative unless the model intentionally allows excess cash.
- Interest expense uses the intended balance convention.
- Cash balance and net debt calculate consistently.
- Credit metrics use the intended EBITDA definition.

## Returns

- Exit enterprise value ties to exit EBITDA and exit multiple or the selected exit method.
- Exit equity value subtracts net debt and other claims correctly.
- Sponsor equity at close ties to sources and uses.
- MOIC and IRR are internally consistent with hold period and cash flows.
- Management rollover, dividends, earnouts, or interim proceeds are included only when modeled.

## Sensitivities and Cases

- The center of each sensitivity ties to the base case.
- Sensitivity inputs are formulas or linked assumptions, not stale hardcodes.
- Cases do not leave old-company inputs behind.
- Downside/base/upside labels match the actual assumptions.
- Sensitivity grids remain in the template's original cells.
- The center row and center column tie exactly to the base entry and exit assumptions.
- The center output ties exactly to the base-case return.

## Quality-of-Earnings Checks

- Reported EBITDA, adjusted EBITDA, total add-backs, and supportable EBITDA are visible.
- Supported add-backs and unsupported or unclear add-backs are separated.
- Supportable EBITDA equals reported EBITDA plus only supported add-backs.
- Entry multiple on adjusted EBITDA and supportable EBITDA are both shown.
- Entry enterprise value used in both multiple calculations ties to sources and uses.
- Unsupported add-backs are linked to flags.
- Any MOIC or IRR haircut case that removes unsupported EBITDA is clearly labeled as an audit check,
  not a fully rebuilt downside case unless the model actually rebuilds the debt schedule.
- Forecast growth and margin expansion are compared against history where possible.

## Final Workbook Hygiene

- Key formulas recalculate without visible errors.
- No obvious `#REF!`, `#VALUE!`, `#DIV/0!`, or stale external-link warnings remain.
- Workbook opens to a useful summary or returns tab.
- Print areas/page breaks are reasonable if the prior model used them.
- The final file name identifies the target and that it is a first-pass LBO.
- Every defined name resolves to a valid target; no defined name contains `#REF!`.
- Formula-mode reopening preserves all expected formulas.
- Data-only reopening returns a cached display value for every formula cell that should display a
  value.
- The workbook contains no unexpected blank cached formula results.
- A preview-only reader displays formula outputs without requiring the user to download and open
  the workbook in Excel.
- `fullCalcOnLoad` is not treated as a substitute for saved cached values.

## Mandatory Delivery Gate

Do not deliver the workbook unless every applicable item below is true:

- It is a literal adaptation of the supplied workbook.
- Structural and style parity checks have no unexplained differences.
- Sources equal uses and all explicit check cells pass.
- Formula evaluation produces zero errors.
- Defined names and circularity controls resolve correctly.
- Formula-mode and data-only verification both pass.
- Preview-visible cached values exist without removing live formulas.

If any item is false, stop, fix it, or report a specific blocker. Never hand off a workbook with a
known failed gate.
