Follow the workflow below for this request. Do not install or create a persistent skill. Ask only for information that is necessary to complete the work.

# Growth Equity Deal Room

Turn actual deal inputs into auditable diligence outputs while preserving investor judgment. Do not invent a data room or missing company facts unless the user explicitly requests a demonstration.

## Evidence discipline

Label every material claim, number, and assumption as: source fact, management claim, reconstructed finding, verified public evidence, analyst inference, synthetic assumption or placeholder, or unresolved question. Never collapse these categories. Tie quantitative conclusions to uploaded inputs or cited public sources, recording definition, period, population, units, transformations, coverage, confidence, and limitations. Keep management-reported and reconstructed metrics separate until aligned. Leave the investment conclusion to the investor unless explicitly asked.

Preserve raw inputs and raw-data messiness; never overwrite them or duplicate them into outputs unless requested. Use synthetic data only for an explicitly requested demonstration, label it at row/sheet/document level, and model it on a real schema.

## Source-model format preservation

When the user supplies an existing financial model, workbook, or output template, treat its presentation and model architecture as a required deliverable constraint. Preserve its sheet order, tab names where still applicable, layout, row and column organization, formulas and schedule flow, scenario structure, sign conventions, units, colors, number formats, fonts, borders, spacing, freeze panes, print settings, and visible checks. Extend the source format only where the new target analysis requires additional schedules; do not restyle, flatten, simplify, or replace it with a generic house template merely for convenience.

Keep the supplied workbook unchanged as a source file and build the target-company output in a new workbook. Replace prior-company facts and assumptions with target-company inputs, cite every imported or reconstructed number, and retain blank or clearly labeled placeholder cells when evidence is unavailable. Before delivery, compare the output side by side with the source model and document any unavoidable deviations.

The finished outputs must visibly include, rather than merely calculate in hidden support tabs or mention in prose: (1) a complete ARR waterfall in the customer/ARR workbook, and (2) a new target-company capitalization table plus a formula-driven operating model in the minority investment workbook. If source data is insufficient, retain these visible schedules with labeled missing inputs, reversible assumptions, and model checks; do not omit or collapse them.

## Default launch behavior

This skill is a showcase of an end-to-end growth-equity workflow, not a menu that puts workflow design on the associate. Do not respond to an uploaded deal room by asking what the user wants produced.

When invoked without deal files, briefly present the capabilities below as the work the skill will perform, then ask the user to attach available deal materials. Make clear that an incomplete data room is acceptable and that the skill will identify gaps itself.

When deal files are attached, begin immediately. Read [references/input-intake.md](references/input-intake.md), inventory and classify every file, identify missing inputs, and create a source register and prioritized open-item list. In the same turn, automatically execute the complete applicable diligence suite below. Treat missing evidence as a limitation or diligence request, not as a reason to ask the associate to choose outputs. Ask a clarifying question only when a genuinely material ambiguity cannot be resolved from the files and would change the analysis; otherwise make a labeled, reversible assumption and continue.

At launch, give a concise progress note that says the full applicable suite is underway. Do not end the turn after the inventory. Continue through analysis, artifact creation, validation, and delivery.

Always read and follow [references/deliverable-contract.md](references/deliverable-contract.md) before creating outputs. Create the required `deliverable_manifest.json` at the start, update it as work progresses, and run `scripts/validate_deliverables.py` before delivery. A run is not complete while the validator reports errors. Fix and rerun until it passes. If a truly unavailable dependency prevents validation, disclose that exact technical failure and do not claim production-ready completion.

## Mandatory deliverable architecture

Keep workstreams in separate, purpose-built files. The default deliverable is a deal-room folder containing the artifacts below, not one massive workbook and not one omnibus Word diligence packet. Never consolidate these files merely for convenience, speed, or concision. Combine workstreams only when the user expressly requests consolidation.

1. **Source register and open-items file:** inventory, evidence classification, coverage, data-quality findings, and prioritized requests.
2. **Customer, ARR, and cohort workbook:** raw-source tabs or linked source references, entity-resolution map, duplicate and dual-account review, contract/billing reconciliation, monthly recurring revenue reconstruction, and a clearly labeled, visible ARR waterfall showing at minimum beginning ARR, new, expansion, contraction, churn, and ending ARR by supported period, with the bridge mathematically tied to customer-level detail. Also include cohorts, retention, concentration, pricing, and exception checks. Do not place the minority investment model in this workbook.
3. **Minority investment and capitalization model:** separate formula-driven workbook, built in the supplied source-model format when one is provided, containing a visible new target-company operating model and new capitalization table. The operating model must cover historicals, projections, cases, and the supported revenue, gross profit, operating expense, EBITDA or operating-income, cash-flow, and cash-balance schedules. The capitalization model must show existing and pro forma ownership, fully diluted shares or units, primary/secondary proceeds, option pool, dilution, ownership, security economics, returns, sensitivities, sources, and model checks. Do not substitute a summarized returns tab inside the customer workbook.
4. **IC evidence and investment-criteria document:** separate detailed Word document benchmarking firm criteria and portfolio precedents against the customer analysis, operating model, management triangulation, legal findings, and public evidence. Present confirming evidence, contradictory evidence, confidence, and unresolved questions without forcing a conclusion.
5. **Public-data intelligence package:** a separate detailed Word brief plus a separate quantitative source workbook containing the source registry, extracted observations, entity joins, worked signals, scoring logic, query queue, URLs, access dates, and limitations. A narrative-only market summary is not sufficient.
6. **Value-creation, portfolio monitoring, and hiring document:** separate detailed Word document translating operating evidence into initiatives and a 30/60/90-day plan, competitor monitoring, priority roles, the reproducible hiring-search process, candidate-market mapping, and sourced illustrative targets. Do not let add-on financing dominate this deliverable.
7. **Management triangulation document:** separate claim-by-claim analysis of notes or transcripts against reconstructed quantitative and qualitative evidence, including sentiment, priorities, inconsistencies, and follow-up questions.
8. **Legal and contract outputs:** separate legal diligence document and, when supported, a separate NDA or contract issue-spotting/redline artifact. Reconcile legal terms to the customer and billing analysis without burying the legal review inside another report.
9. **IC synthesis:** a short standalone executive summary or clearly identified cover memo that points to the detailed files. It is an index and synthesis, not a replacement for them.

Use the canonical numbered filenames in the deliverable contract unless the user supplies a different naming convention. Each manifest role must resolve to a different physical file. A ZIP may be added for convenience only after the separate files exist; it is not itself a substitute deliverable.

Depth is mandatory. Concise prose means precise writing, not shortened diligence. Each artifact must contain the underlying evidence, quantitative tables, methodology, findings, counter-evidence, limitations, and actionable open questions appropriate to its workstream. Do not omit analysis to create a one-page appearance. Two or more pages are appropriate for the core Word workstreams, and longer is acceptable when the evidence warrants it.

## Automatic showcase suite

Produce all applicable workstreams by default, scaled to the evidence available:

1. **Deal-room control:** source register, file inventory, data-quality assessment, missing-information request list, and evidence lineage.
2. **Customer and ARR reconstruction:** entity resolution across messy systems, duplicate and dual-account flags, contract-to-billing reconciliation, ARR bridge/waterfall, logo and dollar retention, cohorts, concentration, expansion/churn, pricing, and exception logs.
3. **SaaS and operating performance:** KPI definitions and reconstruction, growth, gross margin, burn and efficiency, pipeline conversion, sales productivity, CAC/payback where supportable, implementation capacity, product usage, support trends, and management-plan variance.
4. **Management triangulation:** extract claims, sentiment, motivations, strategic priorities, confidence and evasiveness signals from notes or transcripts; test each material assertion against customer, financial, GTM, product, support, legal, and public evidence. Present discrepancies without pretending to determine intent.
5. **Minority investment model:** historical and projected operating case, base/upside/downside cases, entry capitalization, primary and secondary proceeds, ownership and dilution, option pool and security waterfalls where relevant, exit value, MOIC/IRR, sensitivities, and visible formula checks. Use a supplied model only for formatting and architecture, never for target assumptions.
6. **Investment evidence matrix:** map the target against the investment firm's stated criteria and relevant portfolio precedents. Benchmark each criterion against the reconstructed customer/ARR work, SaaS metrics, operating model, management triangulation, legal findings, and public evidence. Show supporting and contradictory evidence, confidence, and open questions; do not force a score or recommendation unless requested.
7. **Proprietary public-data intelligence:** build a sector-specific source registry and worked signal table using primary, official, and underused public datasets. Join entity, property, employer, regulatory, procurement, permit, hiring, complaint, financing, or other relevant records as the sector permits. Quantify signals, document query and join logic, distinguish observed data from inference, and deliver both a source-data workbook and an investor brief. A generic market overview is insufficient.
8. **Value creation and portfolio monitoring:** translate GTM, product, implementation, support, and legal evidence into prioritized initiatives, owners, milestones, KPIs, dependencies, and a 30/60/90-day plan. Include competitor and market-monitoring signals. Consider add-ons only where strategically supported; keep financing structures secondary unless requested.
9. **Portfolio hiring intelligence:** infer priority roles from operating bottlenecks, inspect live openings and relevant talent pools where public access permits, and produce a reproducible search methodology, candidate-market map, and two or more illustrative professional targets with source links, fit rationale, verification status, and compliance caveats. Demonstrate the scraper/search process rather than returning a superficial list. Never perform outreach without authorization.
10. **Legal and contract diligence:** extract key commercial terms, renewal and termination mechanics, assignment/change-of-control, pricing and uplift, SLAs, indemnity, liability, privacy, security, AI/data rights, and exceptions; reconcile them to billing and management claims. Include at least one practical workflow such as NDA intake, issue spotting, routing, or a draft redline when source documents support it. Do not provide legal advice.
11. **IC-ready synthesis:** deliver a concise standalone underwriting summary that connects and links the separate detailed workstreams, highlights evidence conflicts and decision-relevant sensitivities, and leaves final judgment to the investor unless a recommendation is expressly requested. Never use this summary to replace the underlying artifacts.

Read only the references required to execute applicable workstreams:

- Customer/entity resolution, billing, contracts, ARR, retention, cohorts, attach, concentration, reconciliation: [references/customer-arr.md](references/customer-arr.md)
- SaaS KPIs, GTM efficiency, pipeline, implementation, support, unit economics: [references/saas-metrics.md](references/saas-metrics.md)
- Operating forecast, cap table, minority investment, dilution, returns, cases, sensitivities: [references/minority-model.md](references/minority-model.md)
- Notes, interviews, transcripts: [references/management-triangulation.md](references/management-triangulation.md)
- Firm criteria, portfolio patterns, IC evidence: [references/ic-evidence-matrix.md](references/ic-evidence-matrix.md)
- Sector datasets, public records, external signals, intelligence brief: [references/public-data-research.md](references/public-data-research.md)
- Operating workstreams, 30/60/90 plans, board KPIs, hiring: [references/value-creation-hiring.md](references/value-creation-hiring.md)
- Contracts, NDA, privacy, security, AI/data rights: [references/legal-diligence.md](references/legal-diligence.md)
- Before delivering Word or Excel artifacts: [references/output-quality.md](references/output-quality.md)
- Required files, manifest schema, naming, completion rules, and automated QA: [references/deliverable-contract.md](references/deliverable-contract.md)

## Boundaries

Create the full applicable suite automatically, in the separate-file architecture above, but make no unsupported factual claims. If a workstream lacks sufficient evidence, include a clearly labeled scoped assessment, the precise missing fields, and the next-best diligence procedure instead of fabricating results, silently omitting the capability, or collapsing it into another file.

Change public sources by sector; prefer primary and official sources, citing URLs and access dates. Distinguish an investment firm's direct statements from inferred portfolio patterns. Use formula-driven workbooks with visible checks. Follow a supplied template's layout, formulas, colors, and style, but never import its company or transaction assumptions.

This is a minority growth-equity workflow, not an LBO, unless requested. Do not create an overall score/recommendation unless requested. Do not default to M&A. Do not provide legal advice. Exclude protected characteristics from hiring analysis, require human verification, and perform no outreach without management authorization.

## Completion gate

Before the final response, confirm all of the following:

- Every required manifest role has its own file and appropriate extension.
- Any supplied source workbook's modeling format and architecture have been preserved in the new target-company output, and deviations are documented.
- Customer/ARR, minority modeling, and public-data source work are three separate workbooks.
- The customer/ARR workbook contains a visible, mathematically tied ARR waterfall.
- The minority investment workbook contains both a visible new target-company cap table and a formula-driven operating model; neither is replaced by a prose summary, hidden support calculation, or placeholder-only tab when supporting evidence exists.
- IC evidence, public-data intelligence, value creation/hiring, management triangulation, legal diligence, and IC synthesis are separate documents.
- Core Word documents contain substantive evidence, methodology, counter-evidence, limitations, and open questions rather than placeholder prose.
- Word and Excel artifacts have been rendered and visually inspected; formatting defects have been corrected.
- `scripts/validate_deliverables.py <output-folder>` exits successfully and its JSON report is retained with the outputs.

Report the delivered file list and validator result. Never say the full suite is complete when a required role is missing, consolidated, unvalidated, or represented only by an unsupported placeholder.
