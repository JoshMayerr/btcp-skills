# Prior LBO Review

Use the prior LBO as the actual base workbook. The output should remain basically the same as the
example workbook, updated with new deal inputs and only necessary structural changes.

## What to Preserve

- Tab order and naming conventions by default.
- Layout, row order, column widths, formatting, colors, fonts, merged cells, row spacing, section
  headers, notes placement, and summary style.
- The overall flow from inputs to operating model to debt schedule to returns.
- Formula style, sign conventions, and link conventions.
- Assumption blocks and sensitivity layout.
- The degree of detail expected by the user.
- Existing formulas and references where they can be updated safely.
- Existing page setup, print areas, hidden rows/columns, and presentation tabs unless clearly stale.
- Defined names, circularity switches, calculation settings, data validation, conditional
  formatting, tables, charts, images, and cached formula results.

## Required Baseline Audit

Before making any edit, record:

- File type and macro status.
- Sheet names, order, visibility, and used ranges.
- Formula count by sheet.
- Defined names and their resolved targets.
- Row heights, column widths, merged cells, freeze panes, and gridline state.
- Style IDs or equivalent style fingerprints for the model tab.
- Data validation, conditional formatting, charts, images, print areas, and page setup.
- External links, iterative calculation, and calculation mode.
- Every designated hardcode, same-sheet formula, cross-sheet link, external link, assumption,
  warning, diligence-item, and output style, including any conventions that vary locally by sheet
  or section.

Use this exact baseline after modeling. Unexplained drift is a failed deliverable.

## What to Change

Change line items only when the new CIM or deal requires it and an existing row cannot be
responsibly repurposed:

- Revenue build: product, customer, volume/price, ARR, locations, backlog, or simple growth.
- Margin build: gross margin, labor, COGS, SG&A, add-backs, or segment EBITDA.
- Capex: maintenance/growth split, facility expansion, software capitalization, or simple capex.
- Working capital: percent of sales, percent of revenue growth, DSO/DIO/DPO, or explicit NWC.
- Debt: one tranche, multiple tranches, revolver, PIK, seller note, earnout, or rollover.
- Returns: sponsor-only, management rollover, multiple cases, or operating-case sensitivities.

Remove or hide old rows only when they would mislead the user or distort the model. If a row can be
renamed and reused without breaking the model, reuse it. Before hiding or removing a row, trace
whether it feeds active formulas.

## Fast Inspection Pass

For each important sheet, identify:

- Which cells are inputs, formulas, links, and hardcodes.
- Which rows are company-specific.
- Which assumptions should carry over because they are generic house style.
- Which assumptions are old-deal specific and must be cleared.
- Which formulas reference old company tabs, hidden sheets, or external workbooks.
- Whether calculations require Excel iterative calculation, macros, or add-ins.

## Adaptation Principle

Aim for "same workbook, new deal." The finished workbook should look and behave like the prior LBO
with updated company facts, assumptions, labels, and source support. Any visible structural change
should have a reason tied to the CIM or deal structure.

"Same workbook" is literal. A workbook rebuilt from sampled conventions is not the same workbook.
If a usable template exists, generation of a lookalike is prohibited.
