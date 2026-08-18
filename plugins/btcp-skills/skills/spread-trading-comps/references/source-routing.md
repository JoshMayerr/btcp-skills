# Source routing

Use one finance workflow regardless of how evidence is acquired. Normalize only the values needed for the current run and preserve material lineage in the workbook.

## Route sources

1. Inspect uploaded SIM/CIM materials, financial reports, investment criteria, and provider exports.
2. Inventory callable structured connectors and their available fields before using browser automation.
3. Use the analyst's preferred authorized connector when it covers the required data.
4. Supplement missing fields with another authorized structured source when available.
5. When no suitable connector exists, use the analyst's authenticated browser session for the selected provider.
6. Prefer supported Excel or CSV downloads over copying displayed values.
7. For public companies, use regulatory filings and investor-relations materials to verify material historical figures and definitions when practical.
8. Ask for a specific analyst export only after the authorized connector, browser, and applicable public-source routes fail.

Do not treat general web search as a substitute for an available licensed source. Do not require one source to supply every field.

## Apply field-specific authority

Use uploaded internal reporting as the primary source for a portfolio company's confidential target financials, subject to its stated period and definitions. Use public filings or company materials to verify public-company historical results. Use an authorized market-data source for price, share count, enterprise-value components, consensus estimates, and other date-sensitive fields.

Use company identity attributes such as legal name, ticker, exchange, and website domain to prevent same-name mismatches. Preserve the provider's stable company identifier when available.

For each material figure, retain the source name, page, document, cell, record, or URL as applicable; retrieval date; effective date or period; units; currency; and definition. A workbook Sources sheet is sufficient. Do not save a separate normalized dataset unless requested.

## Use browser fallback safely

- Use only an existing authorized session and the access the analyst already possesses.
- Never bypass CAPTCHA, authentication, entitlements, rate limits, robots controls, or download restrictions.
- Keep extraction proportionate to the analysis. Avoid bulk collection when the interface or license does not support it.
- Prefer the provider's search, comparison, screening, and export functions over fragile page scraping.
- Record the provider page or export, retrieval timestamp, and displayed as-of date.
- Stop and request an export when the browser cannot retrieve data reliably or repeated UI behavior risks incorrect transcription.

## Resolve conflicts

Compare source dates, metric definitions, period coverage, and adjustment policies before choosing a value. Do not resolve conflicts by provider name alone.

Prefer the source that is most authoritative for the specific field and date. Retain a material alternative value and explain the selection when reasonable sources disagree. Mark the item for analyst review when the difference could change a selected multiple, percentile, or implied valuation materially.

Label provider estimates, company guidance, agent calculations, and analyst assumptions distinctly. Never present an estimate as reported actual performance.
