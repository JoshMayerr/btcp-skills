Use /skill-creator to install the “Financial data sourcing” skill in my personal skills directory.

Use this exact canonical SKILL.md as the source:

```markdown
---
name: financial-data-sourcing
description: Acquire financial, market, company, transaction, credit, research, news, and document data through authorized sources. Use whenever an agent needs external financial data from providers such as Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, Egnyte, or Box, including when deciding between an installed connector, a logged-in provider website, browser automation, or an analyst-provided export.
---

# Source financial data

Use authorized sources only. Preserve the source, retrieval date, effective date or period, units, currency, and material metric definitions with the resulting analysis.

## Route each request

1. Inventory the callable financial-data connectors and choose the provider that best covers the requested fields.
2. Try the real, authorized connector first. Make a connector call before using a browser unless no relevant connector is callable or the requested source is clearly outside every connector's coverage.
3. If the connector is unavailable, unauthenticated, not entitled, or missing required fields, use the analyst's existing logged-in browser session with local browser automation. Do not ask the analyst to repeat a connector attempt that already failed.
4. In the browser, prefer the provider's supported search, screening, comparison, and Excel or CSV export features over scraping or manual transcription.
5. If both connector and browser routes are unavailable or unreliable, request the narrowest specific export or fields needed from the analyst.

Use a second authorized source to fill field-level gaps rather than abandoning an otherwise suitable primary source. For public-company historical figures, verify material values against regulatory filings or issuer materials when practical.

## Use the browser fallback

1. Open the provider in the local browser profile that contains the analyst's logged-in session. Reuse an existing authenticated tab when possible; do not start in an isolated browser that cannot access the session.
2. Confirm the provider, account state, company identity, ticker or stable identifier, requested period, currency, units, and as-of date before collecting values.
3. Navigate with the provider's own search, screening, comparison, filings, transcript, or company-profile interfaces. Set filters explicitly and wait for each page or table refresh before reading it.
4. Prefer a native Excel or CSV export. Download it through the browser, inspect the resulting file, and retain the provider page URL, export name, retrieval time, and displayed as-of date.
5. When no export exists, extract only the required fields from the rendered table or detail page. Work in small batches, preserve row and column labels, expand pagination deliberately, and capture the source URL for each batch.
6. Verify the extracted entity and period after navigation or pagination. Reconcile totals where available and spot-check at least one material value against the rendered page before using the data downstream.
7. If a value is missing, change the provider view or retrieve it from a second authorized source rather than interpreting a blank as zero. Keep reported values, estimates, calculated values, and analyst assumptions distinct.
8. Record why the connector failed, which browser route succeeded, and any fields that remain unavailable in the final source notes.

If the session is signed out, the interface repeatedly fails, or extraction risks incomplete or incorrectly transcribed data, stop and request the narrowest provider export needed from the analyst.
```

Preserve every supplied instruction, trigger, safeguard, script, reference, and asset. Do not rewrite or omit behavior. Install the skill in the default personal skills directory for this environment and validate the completed installation.

After installing it, tell me:
- Where it was installed
- Whether validation passed
- How to invoke it
- Whether I need to start a new task for it to become available

Then ask whether I also want to install the complete BTCP plugin, which includes the rest of the BTCP finance skills and its useful optional connectors. The plugin is great for financial workflows to make automation more reliable.
