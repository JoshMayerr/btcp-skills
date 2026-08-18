#!/usr/bin/env python3

import csv
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("analyze_customer_history.py")


class AnalyzeCustomerHistoryTest(unittest.TestCase):
    def run_analysis(self, rows, *extra_args):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        source = root / "source.csv"
        output = root / "output"
        with source.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["customer", "period", "value", "parent", "currency"])
            writer.writeheader()
            writer.writerows(rows)
        result = subprocess.run(
            [
                "python3", str(SCRIPT), "--input", str(source), "--output-dir", str(output),
                "--parent-column", "parent", "--currency-column", "currency", *extra_args,
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        return result, output

    def test_movements_retention_and_reactivation(self):
        rows = [
            {"customer": "A", "period": "2025-01", "value": "100", "parent": "Group A", "currency": "USD"},
            {"customer": "A", "period": "2025-02", "value": "120", "parent": "Group A", "currency": "USD"},
            {"customer": "A", "period": "2025-03", "value": "0", "parent": "Group A", "currency": "USD"},
            {"customer": "B", "period": "2025-01", "value": "50", "parent": "Group B", "currency": "USD"},
            {"customer": "B", "period": "2025-02", "value": "25", "parent": "Group B", "currency": "USD"},
            {"customer": "B", "period": "2025-03", "value": "40", "parent": "Group B", "currency": "USD"},
            {"customer": "C", "period": "2025-01", "value": "0", "parent": "Group C", "currency": "USD"},
            {"customer": "C", "period": "2025-02", "value": "30", "parent": "Group C", "currency": "USD"},
            {"customer": "C", "period": "2025-03", "value": "0", "parent": "Group C", "currency": "USD"},
            {"customer": "D", "period": "2025-01", "value": "10", "parent": "Group D", "currency": "USD"},
            {"customer": "D", "period": "2025-02", "value": "0", "parent": "Group D", "currency": "USD"},
            {"customer": "D", "period": "2025-03", "value": "12", "parent": "Group D", "currency": "USD"},
        ]
        result, output = self.run_analysis(rows)
        self.assertEqual(result.returncode, 0, result.stderr)
        with (output / "retention_summary.csv").open(encoding="utf-8", newline="") as handle:
            retention = list(csv.DictReader(handle))
        self.assertEqual(retention[0]["new"], "30")
        self.assertEqual(retention[0]["expansion"], "20")
        self.assertEqual(retention[0]["contraction"], "25")
        self.assertEqual(retention[0]["churn"], "10")
        self.assertEqual(retention[0]["grr"], "0.78125")
        self.assertEqual(retention[0]["nrr"], "0.90625")
        self.assertEqual(retention[0]["bridge_residual"], "0")
        with (output / "customer_movements.csv").open(encoding="utf-8", newline="") as handle:
            movements = list(csv.DictReader(handle))
        d_march = next(row for row in movements if row["customer"] == "D" and row["period"] == "2025-03")
        self.assertEqual(d_march["movement"], "reactivation")

    def test_incomplete_matrix_requires_explicit_zero_policy(self):
        rows = [
            {"customer": "A", "period": "2025-Q1", "value": "10", "parent": "", "currency": "USD"},
            {"customer": "A", "period": "2025-Q2", "value": "10", "parent": "", "currency": "USD"},
            {"customer": "B", "period": "2025-Q2", "value": "5", "parent": "", "currency": "USD"},
        ]
        result, _ = self.run_analysis(rows)
        self.assertEqual(result.returncode, 2)
        self.assertIn("--missing-as-zero", result.stderr)


if __name__ == "__main__":
    unittest.main()
