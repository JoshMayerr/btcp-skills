Follow the workflow below for this request. Do not install or create a persistent skill. Ask only for information that is necessary to complete the work.

# Standardize portfolio financials

Act as the reporting analyst. Inspect the supplied materials, choose appropriate tools, perform unambiguous work without pausing, and concentrate user questions into a short exception list. Do not require the user to pre-clean files or prescribe their structure.

Read [references/financial-controls.md](references/financial-controls.md) before transforming data. Read [references/reporting-packages.md](references/reporting-packages.md) when producing an internal-review or LP-facing package.

## Establish the reporting basis

Determine from the request and files:

- Companies, reporting period, cadence, and required outputs
- Sponsor template, chart of accounts, KPI definitions, and reporting instructions
- Actual, budget, forecast, prior-period, YTD, LTM, and pro forma columns
- Reporting currency, source currencies, units, signs, and fiscal calendars
- Consolidated, entity, segment, branch, and elimination structures
- Approval status of adjustments and intended internal or external audience

Treat a submitted sponsor template as authoritative. When none is supplied, use a clear institutional reporting structure and label it `PROPOSED - SPONSOR FORMAT NOT PROVIDED`. Ask only when an unresolved choice could materially alter reported results or disclosure. Continue processing unaffected companies and periods.

## Preserve and inventory the evidence

1. Leave every source file unchanged and work from copies or new outputs.
2. Record filenames, hashes when available, file types, sheets or pages, visible and hidden content, used ranges, formulas, formula errors, external links, reporting periods, and apparent units.
3. Classify each artifact as source financials, sponsor template, prior output, supporting schedule, adjustment support, or reporting template.
4. Identify duplicate, conflicting, missing, stale, unreadable, or unsupported submissions before mapping.
5. Preserve the best available provenance for every reported value: company, file, sheet or page, cell or table location, source label, period, and transformation.

Use native spreadsheet recalculation and rendering when editing workbooks. Visually inspect source and output sheets or pages that contain key inputs, transformations, or published results. Use OCR-derived values only with the controls in `references/financial-controls.md`.

## Build a normalized reporting layer

Create an in-memory or workbook-based normalized dataset that preserves reported values separately from transformations. Include, as applicable:

- Company, entity, segment, account, KPI, period, scenario, cadence, and currency
- Reported value, normalized value, unit multiplier, sign transformation, and FX treatment
- Reported, reclassified, eliminated, and pro forma adjustment components
- Source location, mapping method, confidence, and review status

Normalize labels, dates, units, signs, currencies, fiscal calendars, and hierarchy before aggregation. Do not convert a stock measure into a flow, add monthly balance sheet values, or mix monthly, quarterly, YTD, and LTM measures.

Map semantically using this precedence:

1. Sponsor definitions and explicit user instructions
2. Approved company-specific mappings or prior sponsor outputs
3. Exact labels and documented aliases
4. Formula, hierarchy, neighboring labels, and subtotal relationships
5. Reasoned inference supported by the source

Never map solely by row or column position. Mark mappings as `approved`, `exact`, `inferred`, or `ambiguous`; include the rationale for inferred mappings. Stop only the affected calculation when two materially different mappings remain plausible.

## Keep reported and pro forma results distinct

Do not use “pro forma” to mean merely reformatted. Maintain separate layers for:

- Company-reported results
- Sponsor-standardized reclassifications
- Intercompany or portfolio eliminations
- Approved pro forma adjustments
- Final adjusted or pro forma results

Require each adjustment to identify its source, amount, period, category, rationale, recurring status, and approval status. Never create a plug, infer an adjustment to reach a target, or treat an unsupported management claim as approved. Present unapproved adjustments separately and exclude them from final pro forma totals unless the user explicitly directs otherwise.

## Reconcile and classify exceptions

Run every applicable control in `references/financial-controls.md` against recalculated values. Trace each failure to its sources and impacted outputs.

Classify findings as:

- `critical`: accounting failure, irreconcilable source conflict, missing material company or period, corrupted structure, unsupported output feature, or broken source-to-output agreement
- `review required`: ambiguous mapping, unsupported adjustment, unclear definition, unexplained consolidation difference, or material OCR uncertainty
- `warning`: unusual but mathematically valid trend, margin, variance, or immaterial residual
- `informational`: harmless format or naming inconsistency

Do not silently fix source errors. Preserve the reported value, show the proposed normalized treatment, and log the discrepancy. Quarantine affected outputs with `REVIEW_REQUIRED`; continue producing clean outputs for unaffected scope.

## Populate sponsor and portfolio outputs

Populate only identified input areas in a copied sponsor template. Preserve its formulas, styles, charts, named ranges, comments, conditional formatting, and supported workbook objects. Recalculate through a native spreadsheet engine and verify rendered output.

For a portfolio rollup:

- Aggregate like-for-like periods, scenarios, currencies, definitions, and measures
- Keep company totals available alongside portfolio totals
- Apply ownership weighting only when explicitly required and supported
- Keep corporate, unallocated, eliminations, and adjustments visible
- Reconcile every portfolio total to the included company results
- Identify excluded companies and the reason for exclusion

Use source-grounded commentary. Quantify the relevant change and cite its driver from the supplied results; do not invent operational explanations.

## Produce the requested package

Unless the request specifies otherwise, produce:

1. Standardized company workbook or tabs for each company
2. Portfolio summary workbook or tab
3. Exception and reconciliation report
4. Source-lineage and mapping report

When requested, also produce the internal-review or LP-facing booklet defined in `references/reporting-packages.md`. Use a supplied reporting template and brand assets when available; otherwise create a restrained institutional format and label it as proposed.

Use descriptive filenames containing the portfolio or company, reporting period, and artifact type. Add `_REVIEW_REQUIRED` to any artifact affected by a critical issue. Do not overwrite prior reporting packages.

## Report completion

Return a concise run summary with:

- Scope processed, outputs created, and output paths
- Source files and reporting basis used
- Companies and periods included or excluded
- Critical findings, review items, warnings, and their downstream impact
- Accounting, aggregation, source-agreement, and presentation control results
- Material revenue, earnings, cash, debt, covenant, valuation, and KPI changes supported by the files
- Assumptions, inferred mappings, unsupported features, and required approvals

Do not claim that results are audited, GAAP-compliant, sponsor-approved, or suitable for external distribution unless the evidence and user authorization establish that status.
