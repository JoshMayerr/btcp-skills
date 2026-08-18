Follow the workflow below for this request. Do not install or create a persistent skill. Ask only for information that is necessary to complete the work.

# CIM to LBO

Create a new LBO workbook for a target company by updating a copy of the prior LBO workbook.
Use two inputs:

1. The CIM or similar deal document as the source for company-specific facts.
2. A prior LBO workbook as the actual base file.

The output should be basically the same workbook as the prior LBO: same tabs, same layout, same
formatting, same model architecture, same section order, same returns presentation, and same
formula style, updated for the new deal. Treat line-item changes as exceptions, not creative
opportunities.

## Core Rules

- Never invent a financial figure. Use CIM-sourced inputs, prior-model assumptions, or clearly
  labeled assumptions.
- Cite the CIM page for every CIM-sourced number.
- Keep Excel formulas live. Do not paste hardcoded outputs where a formula belongs.
- Preserve the prior LBO's workbook structure by default.
- Change existing rows, tabs, formulas, formatting, or assumptions only when needed for the CIM or
  deal structure.
- Prefer repurposing existing rows and sections over adding new ones.
- Do not rebuild the model from scratch unless the user explicitly asks or the prior workbook cannot
  be used without breaking.
- Flag contradictions and missing information instead of smoothing them over.
- If a prior workbook is supplied, NEVER generate a new workbook that merely resembles it. Start
  from a literal file copy of that workbook and modify the copy in place.
- NEVER deliver a workbook whose formulas have not been calculated and saved with cached results.
  A workbook that works only after the user downloads and opens it is incomplete.
- NEVER change a cell's style merely because its value or formula is being updated. Preserve the
  template's exact style object unless the user explicitly requests a formatting change.

## Non-Negotiable Template Integrity

When a prior LBO or template is supplied, exact-template mode is mandatory. "Match the template"
means preserve the actual workbook, not approximate its appearance.

### Required construction method

1. Make a literal copy of the source workbook.
2. Open and edit only the copy.
3. Populate the template's intended input cells and incomplete formula cells.
4. Preserve every existing formula that remains applicable.
5. Add a tab or row only when required information has no responsible location in the template.

The following methods are PROHIBITED unless the user expressly authorizes a rebuild after being
told why exact adaptation is technically impossible:

- Creating a new workbook from scratch.
- Using a format profiler or style sampler to create a lookalike workbook.
- Reconstructing the template with newly created rows, columns, or cells.
- Copying only labels, colors, fonts, or number formats into a different workbook.
- Replacing formulas with calculated hardcodes.
- Moving model sections to make implementation easier.

### Structure that MUST be preserved

Preserve, without unexplained drift:

- Workbook file type and macro content.
- Sheet names, sheet order, hidden sheets, hidden rows, and hidden columns.
- Used-range dimensions and the location of every model section.
- Row heights, column widths, merged cells, freeze panes, and gridline state.
- Cell styles, font colors, fills, borders, alignments, and number formats.
- Existing formulas, formula conventions, and sign conventions.
- Defined names, tables, data validation, conditional formatting, charts, images, print areas,
  page setup, and calculation settings.
- Sensitivity-table locations, axes, center cases, and output cells.

Any necessary structural difference MUST be identified before delivery, tied to a specific deal
requirement, and disclosed to the user. Convenience is NEVER a valid reason for structural drift.

### Cell-type and firm-native formatting discipline

The supplied workbook's native modeling conventions ALWAYS take precedence over generic finance
conventions. Before writing any value, infer the firm's actual conventions by inspecting multiple
representative existing cells for hardcodes, same-sheet formulas, cross-sheet links, external links,
assumptions, warnings, diligence items, and outputs. Then enforce those conventions exactly:

- Hardcoded inputs MUST use the template's native hardcode/input style and color.
- Same-sheet formulas MUST use the template's native formula style and color.
- Cross-sheet links MUST use the template's native internal-link style and color.
- External links MUST use the template's native external-link style and color.
- Assumptions, warnings, diligence items, and outputs MUST use their native template styles.
- If conventions vary by sheet, section, period, or formula type, preserve the applicable local
  convention. NEVER force one sheet's convention across the entire workbook.
- NEVER impose blue hardcodes, black formulas, green internal links, red external links, yellow
  assumptions, or any other standard palette when the supplied workbook uses a different system.
- A formula cell MUST NOT be replaced by a hardcoded result.
- A blank cell MUST NOT be treated as an input merely because it is blank. Confirm its style,
  neighboring formulas, row purpose, and corresponding periods first.

Use a generic finance color convention only if all of the following are true: no reliable native
convention can be inferred after inspecting the workbook; the cells genuinely require new styles;
and no analogous styled cells exist anywhere in the template. In that limited fallback case, use
blue hardcodes, black same-sheet formulas, green internal links, red external links, and clearly
identify the fallback in the handoff. The fallback MUST NOT modify existing styled cells.

Assign values or formulas without overwriting the existing style. After editing, compare style IDs
or equivalent style properties against the source workbook. The model tab MUST have zero
unexplained style mismatches.

### Formula completion

Templates may contain deliberately blank formula cells. Fill every formula required to make the
model operate, using the surrounding row and column conventions. Do not assume the template is
complete merely because it contains some formulas.

For each completed formula block:

- Confirm formulas are consistent across periods.
- Confirm the last forecast or next-fiscal-year column is populated where returns require it.
- Confirm debt balances, interest, cash flow, balance sheet, returns, and sensitivities all link.
- Confirm sensitivity center cells tie exactly to the base case.
- Confirm no formula references a deleted, renamed, nonexistent, or out-of-range cell or sheet.

### Defined names and workbook internals

Inspect every defined name before relying on the model. A broken defined name such as `#REF!` is a
model error even when the visible cells appear correct. Repair a broken inherited name only when
its intended target is unambiguous from the workbook; otherwise stop and report the blocker.

After any sheet rename, verify and, where necessary, update:

- Defined names and circularity switches.
- Formulas containing sheet names.
- Data validation and conditional-format references.
- Charts, print areas, and external links.

Prefer preserving the original sheet name. Renaming a sheet for presentation is prohibited when it
can break workbook internals.

## Calculation and Preview Compatibility

Formula text and calculated display values are separate workbook artifacts. Many previewers do not
run Excel; they display only the last saved cached value. Therefore all of the following are
mandatory before delivery:

1. Recalculate the complete workbook with a compatible calculation engine.
2. Preserve every live formula after recalculation.
3. Save a cached value for every formula cell, including formulas outside the visible summary.
4. Reopen the finished workbook twice: once with formulas visible and once in `data_only` mode.
5. Verify that formula mode still contains the expected formulas.
6. Verify that data-only mode contains the expected displayed values.
7. Verify there are no unexpected blank cached results.
8. Verify there are no `#REF!`, `#VALUE!`, `#DIV/0!`, `#NAME?`, `#NUM!`, or circularity errors.

Setting `fullCalcOnLoad` or expecting Excel to calculate after download is NOT sufficient. Delivery
is prohibited if a preview-only reader would show blank formula cells.

If the available calculation engine cannot save cached values while preserving formulas, use a
validated OOXML-level cache update only after independently calculating the workbook. NEVER remove
or replace the formula nodes. Reopen the patched file in both formula and data-only modes and rerun
all checks.

If no safe recalculation-and-cache path is available, STOP and report the blocker. Do not deliver a
workbook that appears blank in preview.

## Template Fidelity Requirement

The prior LBO workbook is the output template, not just inspiration.

Default behavior:

- Duplicate the prior workbook and edit the copy.
- Preserve tab names, tab order, layout, row order, column widths, formatting, colors, fonts,
  merged cells, section headers, notes placement, sensitivities, and presentation style.
- Replace old-company values, labels, assumptions, and commentary with target-company equivalents.
- Keep formulas, row structure, and schedules intact wherever they can still function.
- The finished workbook should look almost identical to the prior workbook at first glance, except
  for new company name, numbers, source notes, diligence flags, and necessary deal-specific changes.
- The finished model tab should compare cell-for-cell against the source template with zero
  unexplained style, dimension, or layout mismatches.

Do not rebuild a clean model merely because:

- The prior workbook is company-specific.
- Some assumptions are stale.
- Some chart names or defined names are broken.
- The old business model differs from the new target.
- The workbook contains irrelevant rows that can be relabeled, hidden, or footnoted.

Do not use a convention-matching generator as a substitute for editing the supplied workbook.
Convention matching is allowed only when no usable workbook was supplied or the user explicitly
approves a rebuild after a documented technical blocker.

Rebuild only when adapting the copied workbook is technically infeasible or would materially mislead
the user. If rebuilding, explain the specific blocking reason and preserve the prior workbook's
visual structure as closely as possible.

Color and style priority is absolute:

1. Use the supplied workbook's native convention.
2. If conventions differ locally, use the convention of the applicable sheet or section.
3. Use a generic finance palette only when no native or analogous convention can be determined.

The generic fallback is blue hardcodes, black same-sheet formulas, green internal links, red
external links, yellow assumption highlighting, and red diligence warnings. This fallback NEVER
overrides an identifiable firm-native convention and MUST be disclosed when used.

## Missing Inputs

Stop before modeling if either required input is missing.

Required inputs:

- A CIM, teaser, offering memo, management presentation, or similar deal document.
- A prior LBO Excel workbook to use as the base file.

If only the CIM is present, ask for the prior LBO. If only the prior LBO is present, ask for the
CIM. If neither is present, ask for both. Do not create a generic example model unless the user
explicitly asks for a demonstration.

## Workflow

### 1. Inspect the prior LBO

Open the prior workbook before building anything. Read
`references/prior-lbo-review.md` if the model structure is unfamiliar or complex.

Identify the workbook's:

- Key tabs and model flow.
- Historical and projected operating drivers.
- Sources and uses, debt schedule, returns summary, and sensitivities.
- Input color conventions and formula/link conventions.
- Assumption cells that should remain editable.
- Rows that are company-specific and likely need replacement.

Always begin by duplicating the prior LBO and adapting the copy. Treat rebuilding from scratch as an
exception that requires a clear blocker.

Before editing, record a structural baseline: sheet names and order, used ranges, formula count,
defined names, hidden states, row heights, column widths, merged cells, style IDs or equivalent
style fingerprints, external links, calculation settings, and sensitivity locations. Use this
baseline for the mandatory final parity check.

### 2. Extract the CIM

Extract only what the CIM states. Use `references/extraction-schema.md` as the working shape for
the extraction, even if you do not create a separate JSON file:

- Company name, currency, units, and period labels.
- Historical revenue, gross profit if relevant, reported EBITDA, adjusted EBITDA, capex, and net
  working capital.
- EBITDA add-backs with amount, description, page, and support status.
- Management projections and stated operating drivers.
- Deal assumptions such as purchase price, entry multiple, leverage, interest rate, fees, rollover,
  exit assumptions, or hold period.
- Missing diligence items that matter to the model.

For add-backs, mark support strictly:

- Supported: evidenced by executed contracts, completed transactions, invoice trails, third-party
  reports, signed severance, settled legal matters, or departures that already happened.
- Unsupported: asserted, projected, annualized, normalized to an unstated benchmark, or based on a
  plan not yet completed.
- Unclear: genuinely impossible to judge from the CIM.

Read `references/diligence-flags.md` before finalizing flags.

Never conflate reported EBITDA, adjusted EBITDA, supportable EBITDA, pro forma EBITDA, or future
synergies. Each must be separately labeled and traced. Prospective synergies, run-rate savings, and
uncompleted actions MUST be excluded from supportable EBITDA and from the base case unless the user
explicitly requests a separate synergy case.

### 3. Adapt the model

Work in a copy of the prior LBO. The goal is not a model inspired by the prior LBO; the goal is the
same workbook updated for a new deal.

- Replace the old company's inputs with CIM-sourced inputs.
- Keep prior-model assumptions where they are generic and still appropriate.
- Keep the same tabs, row order, row hierarchy, formatting, formulas, and presentation style unless a
  specific change is required.
- Replace irrelevant operating lines with target-specific drivers only when keeping the old line
  would make the model wrong or misleading.
- Add new line items only when the CIM requires them and no existing line can be responsibly
  repurposed.
- Remove or hide old line items only when they no longer fit the deal and would otherwise distort the
  model.
- Keep formulas in the same style and location wherever possible; update references rather than
  redesigning calculations.
- Include a supportable EBITDA analysis in the prior model's style: reported EBITDA, supported
  add-backs, unsupported or unclear add-backs, supportable EBITDA, entry multiple on adjusted
  EBITDA, and entry multiple on supportable EBITDA.
- Add source support and flags inside existing tabs if the prior model already has natural places
  for them. Add new CIM Inputs / Source or Flags / Diligence tabs only when needed.

If the prior workbook is too brittle, broken, or mismatched to adapt safely, stop and explain the
issue. Do not create a clean simple LBO unless the user approves that fallback.

Populate the original template's designated cells. Do not transplant the model into a generated
workbook. Preserve all existing styles when assigning new values or formulas.

### 4. Check the workbook

Before returning the file, read `references/model-checks.md` and verify the workbook against the
checks that apply to the adapted model.

Delivery is prohibited until all applicable checks pass, including exact-template parity, defined
name integrity, formula evaluation, and cached preview visibility. A failed check is a blocker, not
an item to omit from the handoff.

## Reporting Back

Keep the final response short:

1. Lead with the highest-impact diligence flags.
2. State the workbook path and whether it was adapted from the copied prior LBO or, by exception,
   rebuilt after a blocker.
3. Give one headline returns line, clearly separating CIM inputs, prior-model assumptions, and any
   assumptions you chose.

This is a first-pass screen. Do not present it as IC-ready.

## References

- `references/prior-lbo-review.md`: checklist for reading and adapting the prior workbook.
- `references/extraction-schema.md`: lightweight structure for CIM extraction and source support.
- `references/diligence-flags.md`: checklist for CIM quality-of-earnings and diligence flags.
- `references/model-checks.md`: validation checklist before handing back the workbook.
