# Financial validation controls

Apply a control only when the corresponding statements, schedules, or dimensions exist. Use the model's definitions and sign conventions, but normalize expense signs before comparing mathematically equivalent totals. Report every component, source cell, target cell, residual, and tolerance.

## Critical controls

### Source and period integrity

- Reconcile each loaded report subtotal to the values written into model input cells.
- Confirm that the new actual period matches the report and immediately follows the latest completed actual period.
- For monthly models, confirm that each TTM result contains exactly 12 distinct consecutive months. For quarterly models, confirm that each trailing result contains exactly four distinct consecutive quarters.
- Confirm that actual-versus-forecast labels and formulas still follow the model's existing convention.

### Formula and workbook integrity

- Compare formulas in the new period with the preceding period after accounting for expected relative-reference movement.
- Scan recalculated formulas for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`, unintended circular references, and broken external references.
- Confirm that edited sheets, named ranges, comments, formatting, hidden states, merged cells, and supported workbook objects remain present and that required ranges extend consistently.

### Consolidated financial statements

- Reconcile revenue through the model's stated earnings metric, including cost of sales, operating expenses, adjustments, and taxes when applicable.
- When a balance sheet exists, confirm that assets equal liabilities plus equity within the monetary tolerance.
- When cash-flow statements exist, confirm that beginning cash plus net cash movement equals ending cash.
- When debt schedules exist, reconcile ending debt and cash to the applicable balance-sheet or net-debt outputs.

### Branch and segment businesses

Identify the complete set of branches or segments from headers, labels, repeated sections, and consolidated formulas. Keep corporate or unallocated activity, intercompany eliminations, and pro forma adjustments distinct from operating segments.

Reconcile:

`sum(segment revenue) + corporate or unallocated revenue - intersegment eliminations + pro forma revenue adjustments = consolidated pro forma revenue`

`sum(segment operating expenses) + corporate expenses - intersegment expense eliminations + pro forma expense adjustments = consolidated pro forma expenses`

`sum(segment EBITDA) - corporate expenses + other corporate EBITDA contributions + pro forma EBITDA adjustments = consolidated pro forma EBITDA`

Adapt addition or subtraction to the workbook's displayed sign convention while preserving the economic meaning of each equation.

Fail the applicable control when any branch or segment is missing, a corporate expense is buried in one segment without an explicit allocation, corporate expense is both allocated and counted centrally, an elimination is omitted or double counted, a pro forma adjustment lacks a bridge, or the residual exceeds tolerance.

## Warning controls

Flag, but do not quarantine solely for:

- Material period-over-period or year-over-year revenue, expense, earnings, cash, or debt changes
- Sign changes, new accounts, zero-to-nonzero movements, or missing comparative values
- Margins or growth rates outside the model's historical range
- New adjustments, renamed accounts, or changes in segment mix that still reconcile

Explain the driver from workbook values and formulas. Do not invent a universal variance threshold; use an explicit threshold supplied by the user or a clearly labeled reasonableness judgment.

## Tolerance and status

For each monetary reconciliation, calculate:

`residual = calculated rollup - consolidated target`

`tolerance = max(1 reporting currency unit, abs(consolidated target) * 0.0001)`

Pass when `abs(residual) <= tolerance`; otherwise mark the control critical. Require exact agreement for structural preservation, formula-reference validity, and period membership. A warning may coexist with a pass.

Quarantine the output when any critical control fails. List every failure even when one failure is already sufficient to quarantine the workbook.
