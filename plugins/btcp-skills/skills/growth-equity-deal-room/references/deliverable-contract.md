# Production deliverable contract

This contract is mandatory for a full deal-room run. It exists to prevent silent consolidation, shallow substitutes, and formatting failures.

## Canonical folder and files

Create one deal-specific output folder. Use these filenames unless the user provides an established convention:

1. `00_Source_Register_and_Open_Items.xlsx`
2. `01_Customer_ARR_and_Cohort_Analysis.xlsx`
3. `02_Minority_Investment_and_Cap_Table_Model.xlsx`
4. `03_IC_Evidence_and_Investment_Criteria.docx`
5. `04_Public_Data_Intelligence_Brief.docx`
6. `04_Public_Data_Source_Workbook.xlsx`
7. `05_Value_Creation_Portfolio_Monitoring_and_Hiring.docx`
8. `06_Management_Triangulation.docx`
9. `07_Legal_and_Contract_Diligence.docx`
10. `08_IC_Synthesis.docx`
11. `deliverable_manifest.json`
12. `validation_report.json`

Create an additional NDA review or redline as `07A_NDA_Review_and_Redline.docx` when an NDA or suitable agreement is provided. A convenience ZIP may contain the folder after validation.

## Manifest

Create `deliverable_manifest.json` before analysis with this structure and update it throughout the run:

```json
{
  "deal_name": "Target Company",
  "as_of_date": "YYYY-MM-DD",
  "run_type": "real|demonstration",
  "roles": {
    "source_register": {"path": "00_Source_Register_and_Open_Items.xlsx", "status": "planned"},
    "customer_arr": {"path": "01_Customer_ARR_and_Cohort_Analysis.xlsx", "status": "planned"},
    "minority_model": {"path": "02_Minority_Investment_and_Cap_Table_Model.xlsx", "status": "planned"},
    "ic_evidence": {"path": "03_IC_Evidence_and_Investment_Criteria.docx", "status": "planned"},
    "public_data_brief": {"path": "04_Public_Data_Intelligence_Brief.docx", "status": "planned"},
    "public_data_workbook": {"path": "04_Public_Data_Source_Workbook.xlsx", "status": "planned"},
    "value_creation_hiring": {"path": "05_Value_Creation_Portfolio_Monitoring_and_Hiring.docx", "status": "planned"},
    "management_triangulation": {"path": "06_Management_Triangulation.docx", "status": "planned"},
    "legal_diligence": {"path": "07_Legal_and_Contract_Diligence.docx", "status": "planned"},
    "ic_synthesis": {"path": "08_IC_Synthesis.docx", "status": "planned"}
  }
}
```

Allowed final statuses are `complete` and `scoped`. `scoped` means the artifact exists and clearly states the missing evidence, consequence, next-best diligence procedure, and open request. A missing or empty file is never `scoped`. Use `not_applicable` only with a written reason in the role entry and only where the workstream is objectively irrelevant; the validator treats it as a warning requiring investor review.

Every role must use a unique path. One workbook or document cannot satisfy multiple roles. Do not list the same file twice under different names or create thin pointer files whose only purpose is to evade separation.

## Minimum substantive contents

Each core Word document must contain: scope and evidence used; methodology; detailed findings; quantitative or comparative evidence where applicable; evidence supporting the finding; contradictory or limiting evidence; source references; unresolved questions; and investor implications without an imposed recommendation. The IC synthesis can be shorter but must cross-reference the detailed files.

Each workbook must contain a read-me or sources tab, calculation lineage, visible checks, and the workstream-specific schedules required by its reference. The customer workbook must include entity resolution and ARR/cohort schedules. The minority model must include operating cases, cap table, ownership/dilution, returns, sensitivities, and checks. The public-data workbook must include source registry, row-level or worked observations, join logic, signal calculations, limitations, and checks.

## Validation

Run:

```text
python scripts/validate_deliverables.py <deal-output-folder>
```

If the normal Python alias is unavailable, use the environment's bundled Python executable. The script creates `validation_report.json` and exits nonzero on blocking errors. Fix all errors and rerun. Warnings require review and disclosure but do not automatically block delivery.

The validator checks separation, extensions, existence, nontrivial file sizes, Word OOXML font/size declarations, obvious dark-fill/dark-text combinations, and Excel style contrast. It cannot judge investment reasoning or rendered layout. Therefore also perform the visual and analytical QA in `output-quality.md`.
