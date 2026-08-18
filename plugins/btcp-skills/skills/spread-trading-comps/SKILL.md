---
name: spread-trading-comps
description: Build an auditable public-company trading comparables analysis and editable .xlsx valuation workbook for a private equity portfolio-company exit or external investment target. Use when an analyst needs to select and screen comparable companies, source target and public-company data from uploaded SIM/CIM materials, installed data connectors, authenticated browser sessions, provider exports, or public filings, calculate EV/revenue and EV/EBITDA multiples, benchmark growth and margins, and triangulate an indicative valuation range for IC work.
---

# Spread trading comps

Create a review-ready trading comparables workbook for one target. Treat the work as valuation analysis, not an investment recommendation. Keep source evidence, assumptions, adjustments, and analyst judgments visible.

Read all three references before acquiring data or building the workbook:

- [references/source-routing.md](references/source-routing.md)
- [references/comps-methodology.md](references/comps-methodology.md)
- [references/validation.md](references/validation.md)

## Establish the assignment

Identify the target, valuation date, purpose, reporting currency, available target materials, investment criteria, and requested output path. Determine whether the target is:

- An internal portfolio company supported primarily by uploaded SIM/CIM, management, or portfolio reporting materials
- An external target supported by authorized provider data, public information, and any uploaded investment criteria

Treat an internal target as confidential. Do not search for or expose internal figures outside the authorized workspace. For an external target, distinguish public facts from estimates and analyst-supplied assumptions.

Proceed with reasonable defaults when the target identity, valuation date, and financial basis are clear. Ask only when an unresolved ambiguity could change the comparable universe or valuation materially.

## Inspect available capabilities and evidence

Inventory uploaded files, callable structured data connectors, spreadsheet capabilities, browser access, and public research tools before choosing a source route. Use the routing order and safeguards in `references/source-routing.md`.

Use installed, authorized connectors when they provide the required fields. If no suitable connector is available, use the analyst's logged-in browser session. Prefer a provider's supported Excel or CSV export over transcribing a rendered page. Supplement missing fields at the field level rather than discarding an otherwise useful source.

Do not install a connector, bypass an access control, or request credentials. If authorized sources remain inaccessible, identify the exact export or fields the analyst must provide.

## Build and screen the universe

Create the target profile from the best available evidence. Build a candidate public-company universe using business model, customer base, end market, geography, size, growth, profitability, revenue model, and other criteria supplied by the analyst.

Separate:

- Eligibility: whether the company belongs in the universe
- Comparability: how closely it resembles the target
- Valuation influence: whether its multiple should affect the selected range

Keep included and excluded candidates visible with concise rationales. Do not use an opaque score as a substitute for analyst judgment. When no explicit criteria are supplied, infer a defensible preliminary universe and label the selection as preliminary.

## Normalize only for the current run

Normalize source values in memory before calculating. Do not create a persistent mapping, reusable normalized dataset, or intermediate data-contract artifact unless the user requests one.

For every material figure, retain enough context to distinguish:

- Company and source
- Currency and units
- Valuation or retrieval date
- Fiscal period and historical, LTM, or forward basis
- Reported, provider-derived, agent-derived, or analyst-supplied status
- Metric definition and any adjustment

Never treat a missing value as zero. Never combine revenue, EBITDA, enterprise value, or estimates that use incompatible dates or definitions without an explicit bridge.

## Spread and triangulate

Build an editable `.xlsx` workbook using the calculations, statistics, and default sheet structure in `references/comps-methodology.md`. Preserve formulas for derived values so an analyst can trace and update the analysis.

Calculate applicable EV/revenue and EV/EBITDA multiples, revenue growth, EBITDA margin, and summary statistics. Display economically meaningless multiples as `NM`; do not allow them into valuation statistics.

Apply selected low, midpoint, and high multiples to the target's corresponding financial metrics. Show the bridge from implied enterprise value to implied equity value when target cash, debt, preferred equity, and non-controlling interests are available. Present revenue- and EBITDA-based outputs separately before triangulating them.

Do not invent target financials. If the target lacks a required metric, show the available benchmark and identify the missing input instead of fabricating a complete valuation.

## Validate and export

Run every applicable control in `references/validation.md` against recalculated workbook values. Render and inspect every output sheet. Classify unresolved source, identity, period, definition, calculation, and workbook-integrity issues as critical or warning.

On a clean critical-control result, export:

`<target-stem>_trading-comps_<YYYY-MM-DD>.xlsx`

When a critical control fails, retain the diagnostic workbook as:

`<target-stem>_trading-comps_<YYYY-MM-DD>_REVIEW_REQUIRED.xlsx`

Return a concise audit summary containing:

- Target, purpose, valuation date, reporting currency, and output path
- Included and excluded comparable companies and the governing criteria
- Sources used, source dates, browser or connector fallbacks, and material conflicts
- Target financial basis, selected multiple ranges, and implied valuation outputs
- Applicable controls, warnings, critical failures, and missing inputs
- Material judgments that an analyst should revisit before using the work in an IC memo
