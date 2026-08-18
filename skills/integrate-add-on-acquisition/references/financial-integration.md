# Financial integration

## Determine the presentation basis

Separate these bases by period and do not label one as another:

- Target-reported historical results before close
- Historical pro forma results as though ownership began earlier
- Closing-period reported contribution after the accounting effective date
- Post-close actual consolidated results
- Combined-company forecast
- Annualized or run-rate presentation
- Approved synergies or other pro forma adjustments

For a mid-period close, do not insert a full month into reported post-close actuals unless the destination model and accounting policy explicitly require it. Preserve any pre-close stub, post-close stub, or full-period pro forma view separately.

## Map the target

Map using this precedence:

1. Destination-model definitions and explicit sponsor instructions
2. Approved acquisition or company-specific mapping
3. Exact labels and documented aliases
4. Account hierarchy, formulas, subtotals, neighboring labels, and dimensional relationships
5. Reasoned inference supported by the source

Never map solely by row or column position. Record source account, destination line, period, entity or segment, mapping status, rationale, and source location. Classify mappings as `approved`, `exact`, `inferred`, or `ambiguous`.

Preserve and reconcile:

- Revenue, cost of sales, operating expenses, and EBITDA or the destination earnings measure
- Depreciation, amortization, interest, taxes, and net income when applicable
- Cash, debt, working capital, fixed assets, and other balance-sheet accounts
- Cash-flow classifications and noncash items
- Entity, segment, location, department, corporate, and elimination dimensions

Do not bury corporate costs in an operating segment or omit intercompany eliminations.

## Maintain adjustment layers

Keep these components distinct:

1. Target-reported value
2. Reclassification
3. Intercompany elimination
4. Purchase-accounting entry
5. Transaction or financing entry
6. Annualization or run-rate adjustment
7. Synergy or cost-saving adjustment
8. Final pro forma value

Require each adjustment to state amount, period, category, source, rationale, recurring status, and approval status. Exclude unsupported or unapproved adjustments from final totals.

Prevent double counting when a forecast already includes an acquisition, synergy, refinancing, or cost reduction. Trace whether each item is included in the target source, portfolio-company forecast, transaction model, or destination formulas before adding it.

## Reflect the closing transaction

When supported and applicable, update:

- Cash purchase consideration and balance-sheet cash
- Debt draws, repayments, fees, amortization, interest rates, and interest expense
- Sponsor, co-investor, or rollover equity funding
- Transaction, financing, integration, and advisory fees according to the model's definitions
- Working-capital and other purchase-price adjustments
- Acquired cash, assumed debt, and debt-like items
- Valuation, leverage, covenant, and returns schedules that directly depend on changed inputs

Use the canonical transaction record for all shared values. Do not copy a model-derived number into the cap table when the governing transaction schedule provides the value.

## Limit purchase accounting

Populate goodwill, identifiable intangible assets, fair-value marks, deferred taxes, opening equity eliminations, and amortization only from a final or explicitly approved purchase-accounting or opening-balance-sheet schedule.

If no such schedule exists:

- Preserve any supported cash, debt, and transaction entries.
- Show the unsupported opening-balance-sheet allocation as an exception.
- Do not create a balancing goodwill plug and call it final purchase accounting.
- Quarantine any balance-sheet output that cannot balance without the missing schedule.

## Preserve workbook integrity

Copy the destination and inspect formulas and displayed values around every input and output area. Write source values only into identified input cells. Preserve formulas for derived results and follow established formula, style, comment, conditional-formatting, and input-color patterns.

Extend charts, named ranges, tables, and forecast or returns formulas only when the acquisition integration necessarily expands their existing scope. Recalculate through a native engine and inspect rendered changes for clipped labels, hidden errors, broken formulas, or inconsistent units.
