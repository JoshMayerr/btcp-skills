---
name: roll-forward-portfolio-model
description: Roll forward a private equity portfolio company's existing .xlsx master financial model from one new monthly or quarterly .xlsx financial report. Use when an analyst needs to add the latest actual period, refresh TTM or quarterly metrics, reconcile branch or segment results, isolate corporate expenses, preserve the submitted model's formulas and formatting, and produce an auditable updated workbook without rebuilding the model.
---

# Roll forward a portfolio model

Use the submitted master workbook as the only template. Copy it, edit the copy, and preserve its structure and conventions. Never overwrite the master, recreate it as a standardized workbook, add a control sheet, save a reusable mapping, or update downstream files.

Read [references/financial-validation.md](references/financial-validation.md) before inspecting either workbook.

## Require the right inputs

Require exactly one `.xlsx` master model and one `.xlsx` financial report. Treat the master as the destination and the report as the source of new actuals.

Require a native spreadsheet engine that can inspect, edit, recalculate, render, and export `.xlsx` files while preserving supported workbook objects. Stop before editing when the engine cannot faithfully round-trip the master, recalculate formulas, or expose the workbook features needed to validate the result.

Reject `.xls`, `.xlsm`, CSV, PDF, and multiple-master or multiple-report runs. Ask only when the file roles, reporting period, cadence, units, sign conventions, or account mapping remain materially ambiguous after inspection.

## Inspect and map each run

1. Record the source paths, file hashes when available, sheet inventory, named ranges, hidden sheets and ranges, merged cells, tables, charts, external links, formulas, formula errors, and used ranges.
2. Inspect displayed values and formulas around each likely input, calculation, and output area. Render every sheet that may be edited and every sheet containing a key output.
3. Identify the model's monthly or quarterly cadence, latest completed period, next target period, units, signs, actual-versus-forecast convention, primary earnings metric, and TTM or trailing-quarter calculations.
4. Map the report to the model using labels, period headers, hierarchy, neighboring formulas, subtotal relationships, and branch or segment dimensions. Rebuild this semantic mapping in memory on every run; do not write a mapping file or workbook metadata.
5. Stop without creating a modified workbook when two plausible mappings remain, the target period is already populated, a necessary account is absent, or an unsupported feature could be damaged.

## Roll forward the copied master

1. Copy the master and leave the original byte-for-byte unchanged.
2. If the target period already exists as an intentionally blank actual period, populate its approved input cells. Otherwise extend the immediately preceding actual period following the model's existing row, column, formula, style, comment, conditional-formatting, and range patterns.
3. Write report values only into identified input cells. Preserve derived values as formulas and retain the model's established currency, units, signs, adjustment definitions, and input-color conventions.
4. Do not change historical periods, forecasts, assumptions, charts, named ranges, external links, formulas outside the required extension, or unsupported workbook objects unless the new period necessarily extends their existing range.
5. Recalculate through the native spreadsheet engine. Do not rely on stale cached formula values.

Proceed automatically when the mapping is unambiguous. Do not pause for a preview approval.

## Validate and classify the result

Run every applicable control in `references/financial-validation.md` against recalculated values. Trace failures to source and target cells and distinguish critical failures from warnings.

Treat structural damage, formula errors, source-to-model differences, incomplete trailing periods, and failed accounting or branch/segment reconciliations as critical. Treat unusual but mathematically valid variances, growth rates, or margins as warnings.

Use a monetary tolerance equal to the greater of one reporting currency unit or `0.01%` of the absolute consolidated target. Require exact agreement for workbook structure and formula integrity.

## Export and report

On a clean critical-control result, export one workbook as:

`<master-stem>_<YYYY-MM-or-YYYY-Q#>_rolled-forward.xlsx`

When any critical control fails, retain the diagnostic workbook but quarantine it as:

`<master-stem>_<YYYY-MM-or-YYYY-Q#>_rolled-forward_REVIEW_REQUIRED.xlsx`

Return a concise audit report with:

- Master and report filenames, hashes when available, cadence, reporting period, and output path
- Sheets and cells changed, report labels loaded, formulas or ranges extended, and source-to-target lineage
- Applicable controls, calculated values, target values, residuals, tolerances, and pass, warning, or critical status
- Ambiguities, unsupported features, and manual review items
- Changed revenue, earnings, cash, debt, valuation, and operating KPIs that may feed valuation models, LP reports, board materials, or debt schedules

Keep downstream impact analysis read-only. Do not search external drives or modify another file.
