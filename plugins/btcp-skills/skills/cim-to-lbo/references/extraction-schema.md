# Extraction Schema

Use this as the working shape for CIM extraction. A separate JSON file is optional, but the final
workbook should preserve this information in a CIM Inputs, Source, or Audit tab.

## Deal Metadata

- `company`: target name as presented.
- `source_doc`: CIM or presentation filename.
- `currency`: currency used in the document.
- `units`: dollars, thousands, or millions.
- `periods`: exact historical and projected period labels from the CIM.
- `pages_reviewed`: page range or sections reviewed.

## Historical Financials

Capture the stated historical periods, oldest to newest. Treat the last historical or LTM period as
the entry EBITDA anchor unless the deal document clearly says otherwise.

For each period:

- `label`
- `revenue`
- `gross_profit` if presented or useful to the model
- `reported_ebitda`
- `adjusted_ebitda`
- `capex`
- `net_working_capital`
- `page`
- `notes`

Do not backsolve missing historicals unless the source gives enough components to make the formula
auditable in Excel.

## EBITDA Add-Backs

For each add-back:

- `label`
- `amount_by_period`
- `description`
- `support`: supported, unsupported, or unclear
- `support_reason`
- `page`

Use supportable EBITDA as a quality check: reported EBITDA plus only supported add-backs.

## Supportable EBITDA Analysis

Build this analysis for the LTM or entry EBITDA period. Put it in the workbook using the prior
model's style, usually on the returns, summary, add-back, or CIM Inputs tab.

Required lines:

- `reported_ebitda`
- `supported_addbacks`
- `unsupported_or_unclear_addbacks`
- `adjusted_ebitda_as_presented`
- `supportable_ebitda`: reported EBITDA plus supported add-backs only
- `entry_enterprise_value`
- `entry_multiple_on_adjusted_ebitda`
- `entry_multiple_on_supportable_ebitda`

Useful optional lines:

- unsupported add-backs as a percentage of reported EBITDA
- supportable EBITDA haircut versus adjusted EBITDA
- MOIC or IRR case with unsupported EBITDA removed, clearly labeled as a rough downside check

Do not treat this as a separate operating case unless the model supports it cleanly. It is primarily
an audit view that translates add-back quality into valuation impact.

## Projections and Operating Drivers

For each forecast period:

- `label`
- `revenue`
- `revenue_driver` if disclosed
- `gross_margin` or `gross_profit` if disclosed
- `adjusted_ebitda`
- `ebitda_margin` if disclosed
- `capex`
- `net_working_capital` or working-capital driver
- `page`
- `notes`

Preserve explicit drivers when the prior LBO has room for them. If the CIM only provides totals,
do not fabricate a driver build.

## Deal Assumptions

Separate document-stated assumptions from assumptions inherited from the prior LBO.

- `purchase_price` or `entry_multiple`
- `transaction_fees`
- `financing_fees`
- `debt_tranches`
- `cash_to_balance_sheet`
- `management_rollover`
- `interest_rates`
- `amortization`
- `exit_multiple`
- `hold_period`
- `tax_rate`
- `source`: CIM, prior LBO, user, or agent assumption
- `page` where applicable

## Missing Information

Track missing items that would change model confidence:

- monthly or quarterly financials
- customer concentration
- revenue detail by segment, customer, product, or geography
- churn, retention, ARR, backlog, or pipeline definitions
- pricing history
- maintenance versus growth capex
- working-capital detail
- debt-like items
- management rollover and compensation

## Source Tab Minimum

The workbook should let a reviewer trace:

- each material CIM input to a page
- each model assumption to CIM, prior LBO, user, or agent assumption
- each unsupported add-back to a flag
- supportable EBITDA and related multiples to reported EBITDA, add-backs, and entry enterprise value
- each missing diligence item to the questions list
