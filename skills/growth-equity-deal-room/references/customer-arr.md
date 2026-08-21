# Customer and ARR analysis

Resolve legal entities, operator parents, customers, properties/assets, products, contracts, and billing accounts without deleting source identity. Preserve source system/ID/name, canonical ID/name, relationship, match method/evidence, confidence, review status, and exception reason. Flag duplicates, multiple bill-to accounts, conflicting parents, missing keys, customer/property ambiguity, legal-name mismatch, acquisitions/dispositions, and orphan invoices. Prefer deterministic keys, then normalized exact matches, then explainable fuzzy candidates requiring review; never silently merge ambiguity.

Identify currencies/units, credits, disputes, ramps, signed-not-live contracts, missing contracts, cancellations, and contract-to-billing variance. Define treatment of recurring charges, usage, services, credits, partial months, ramps, FX, and amendments before calculating ARR.

Where supported, build raw tabs, mappings, canonical masters, monthly ARR, opening-to-ending waterfall (opening + new logo + expansion - contraction - churn = ending), cohorts, attach, concentration, contracted/live/billed reconciliation, exceptions, management reconciliation, checks, and concise outputs. Show customer/property counts, GRR, NRR, logo retention, cohorts, attach, concentration, and source coverage only where grain supports them.

Show management and reconstructed metrics side-by-side with definition, period, population, coverage, variance, confidence, and open issues. Checks cover roll-forward, duplicate assignments, unmapped rows, missing periods, currency/units, contract/billing ties, row/dollar lineage, and management KPI reconciliation.
