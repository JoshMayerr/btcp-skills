#!/usr/bin/env python3
"""Analyze complete customer-period recurring-value snapshots.

Input must be a long-form CSV with one row per customer and period. By default the
required columns are `customer`, `period`, and `value`. Supported period formats are
YYYY-MM, YYYY-Qn, or YYYY, used consistently throughout the file.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path


PERIOD_PATTERNS = {
    "monthly": re.compile(r"^(\d{4})-(0[1-9]|1[0-2])$"),
    "quarterly": re.compile(r"^(\d{4})-Q([1-4])$", re.IGNORECASE),
    "annual": re.compile(r"^(\d{4})$"),
}
TOP_NS = (1, 3, 5, 10, 20)


class InputError(ValueError):
    """Raised when source data cannot safely support the analysis."""


@dataclass(frozen=True)
class Record:
    customer: str
    period: str
    value: Decimal
    parent: str


def decimal_text(value: Decimal | None) -> str:
    if value is None:
        return ""
    normalized = value.normalize()
    return format(normalized, "f") if normalized != 0 else "0"


def ratio_text(numerator: Decimal | int, denominator: Decimal | int) -> str:
    if denominator == 0:
        return ""
    return decimal_text(Decimal(numerator) / Decimal(denominator))


def parse_period(value: str) -> tuple[str, tuple[int, int]]:
    value = value.strip()
    for cadence, pattern in PERIOD_PATTERNS.items():
        match = pattern.fullmatch(value)
        if not match:
            continue
        year = int(match.group(1))
        position = int(match.group(2)) if match.lastindex and match.lastindex > 1 else 1
        if cadence == "monthly":
            return cadence, (year, position)
        if cadence == "quarterly":
            return cadence, (year, position * 3)
        return cadence, (year, 12)
    raise InputError(f"Invalid period {value!r}; use YYYY-MM, YYYY-Qn, or YYYY.")


def missing_periods(periods: list[str], cadence: str) -> list[str]:
    keys = {parse_period(period)[1] for period in periods}
    missing: list[str] = []
    start_year, start_position = min(keys)
    end_year, end_position = max(keys)
    step = {"monthly": 1, "quarterly": 3, "annual": 12}[cadence]
    year, position = start_year, start_position
    while (year, position) <= (end_year, end_position):
        if (year, position) not in keys:
            if cadence == "monthly":
                missing.append(f"{year:04d}-{position:02d}")
            elif cadence == "quarterly":
                missing.append(f"{year:04d}-Q{position // 3}")
            else:
                missing.append(f"{year:04d}")
        position += step
        if position > 12:
            year += 1
            position -= 12
    return missing


def read_records(args: argparse.Namespace) -> tuple[list[Record], list[str], str, str | None]:
    source = Path(args.input)
    if not source.is_file():
        raise InputError(f"Input file does not exist: {source}")

    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise InputError("Input CSV has no header row.")
        required = {args.customer_column, args.period_column, args.value_column}
        if args.parent_column:
            required.add(args.parent_column)
        if args.currency_column:
            required.add(args.currency_column)
        missing_columns = sorted(required - set(reader.fieldnames))
        if missing_columns:
            raise InputError(f"Missing required columns: {', '.join(missing_columns)}")

        records: list[Record] = []
        seen: set[tuple[str, str]] = set()
        cadence: str | None = None
        currencies: set[str] = set()
        periods: set[str] = set()

        for line_number, row in enumerate(reader, start=2):
            customer = (row.get(args.customer_column) or "").strip()
            period = (row.get(args.period_column) or "").strip()
            raw_value = (row.get(args.value_column) or "").strip().replace(",", "")
            parent = (row.get(args.parent_column) or "").strip() if args.parent_column else ""
            if not customer or not period or raw_value == "":
                raise InputError(f"Line {line_number} has a blank customer, period, or value.")
            row_cadence, _ = parse_period(period)
            if cadence and row_cadence != cadence:
                raise InputError("Mixed monthly, quarterly, or annual period formats are not supported.")
            cadence = row_cadence
            try:
                value = Decimal(raw_value)
            except InvalidOperation as exc:
                raise InputError(f"Line {line_number} has invalid value {raw_value!r}.") from exc
            if not value.is_finite() or value < 0:
                raise InputError(f"Line {line_number} value must be finite and non-negative.")
            key = (customer, period)
            if key in seen:
                raise InputError(f"Duplicate customer-period row at line {line_number}: {key}.")
            seen.add(key)
            periods.add(period)
            if args.currency_column:
                currency = (row.get(args.currency_column) or "").strip().upper()
                if not currency:
                    raise InputError(f"Line {line_number} has a blank currency.")
                currencies.add(currency)
            records.append(Record(customer, period, value, parent))

    if not records or cadence is None:
        raise InputError("Input CSV contains no data rows.")
    if len(currencies) > 1:
        raise InputError(f"Mixed currencies are not supported: {', '.join(sorted(currencies))}")
    ordered_periods = sorted(periods, key=lambda item: parse_period(item)[1])
    gaps = missing_periods(ordered_periods, cadence)
    if gaps:
        raise InputError(f"Missing {cadence} periods: {', '.join(gaps)}")
    return records, ordered_periods, cadence, next(iter(currencies), None)


def complete_matrix(
    records: list[Record], periods: list[str], missing_as_zero: bool
) -> tuple[dict[tuple[str, str], Decimal], dict[str, str], int]:
    values = {(record.customer, record.period): record.value for record in records}
    customers = sorted({record.customer for record in records})
    parents_by_customer: dict[str, set[str]] = defaultdict(set)
    for record in records:
        if record.parent:
            parents_by_customer[record.customer].add(record.parent)
    conflicting = {customer: parents for customer, parents in parents_by_customer.items() if len(parents) > 1}
    if conflicting:
        detail = "; ".join(f"{customer}: {sorted(parents)}" for customer, parents in conflicting.items())
        raise InputError(f"Customers map to multiple parents: {detail}")
    parent_map = {
        customer: next(iter(parents_by_customer[customer]), "") for customer in customers
    }
    missing = [(customer, period) for customer in customers for period in periods if (customer, period) not in values]
    if missing and not missing_as_zero:
        preview = ", ".join(f"{customer}/{period}" for customer, period in missing[:10])
        suffix = " ..." if len(missing) > 10 else ""
        raise InputError(
            f"Customer-period matrix has {len(missing)} missing rows ({preview}{suffix}). "
            "Supply explicit zeroes or rerun with --missing-as-zero after confirming omissions mean zero."
        )
    for key in missing:
        values[key] = Decimal(0)
    return values, parent_map, len(missing)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_outputs(
    values: dict[tuple[str, str], Decimal], periods: list[str], parent_map: dict[str, str]
) -> dict[str, tuple[list[str], list[dict[str, object]]]]:
    customers = sorted({customer for customer, _ in values})
    first_positive: dict[str, int | None] = {}
    for customer in customers:
        first_positive[customer] = next(
            (index for index, period in enumerate(periods) if values[customer, period] > 0), None
        )

    normalized_rows: list[dict[str, object]] = []
    movement_rows: list[dict[str, object]] = []
    for customer in customers:
        for index, period in enumerate(periods):
            value = values[customer, period]
            normalized_rows.append(
                {
                    "customer": customer,
                    "ultimate_parent": parent_map[customer],
                    "period": period,
                    "value": decimal_text(value),
                    "cohort_period": periods[first_positive[customer]] if first_positive[customer] is not None else "",
                }
            )
            beginning = values[customer, periods[index - 1]] if index else Decimal(0)
            movement = "no_movement"
            amount = Decimal(0)
            if index == 0 and value > 0:
                movement, amount = "opening", value
            elif index > 0 and beginning == 0 and value > 0:
                movement = "reactivation" if any(values[customer, p] > 0 for p in periods[: index - 1]) else "new"
                amount = value
            elif index > 0 and beginning > 0 and value > beginning:
                movement, amount = "expansion", value - beginning
            elif index > 0 and beginning > 0 and 0 < value < beginning:
                movement, amount = "contraction", beginning - value
            elif index > 0 and beginning > 0 and value == 0:
                movement, amount = "churn", beginning
            movement_rows.append(
                {
                    "customer": customer,
                    "period": period,
                    "beginning_value": decimal_text(beginning),
                    "ending_value": decimal_text(value),
                    "movement": movement,
                    "movement_amount": decimal_text(amount),
                }
            )

    retention_rows: list[dict[str, object]] = []
    for index, period in enumerate(periods[1:], start=1):
        prior = periods[index - 1]
        beginning_values = {customer: values[customer, prior] for customer in customers}
        ending_values = {customer: values[customer, period] for customer in customers}
        beginning = sum(beginning_values.values(), Decimal(0))
        ending = sum(ending_values.values(), Decimal(0))
        beginning_logos = sum(value > 0 for value in beginning_values.values())
        retained_logos = sum(
            beginning_values[customer] > 0 and ending_values[customer] > 0 for customer in customers
        )
        totals = defaultdict(Decimal)
        for row in movement_rows:
            if row["period"] == period:
                totals[str(row["movement"])] += Decimal(str(row["movement_amount"]))
        expansion = totals["expansion"]
        contraction = totals["contraction"]
        churn = totals["churn"]
        new = totals["new"]
        reactivation = totals["reactivation"]
        bridge_ending = beginning + new + expansion - contraction - churn + reactivation
        retention_rows.append(
            {
                "period": period,
                "beginning_value": decimal_text(beginning),
                "new": decimal_text(new),
                "expansion": decimal_text(expansion),
                "contraction": decimal_text(contraction),
                "churn": decimal_text(churn),
                "reactivation": decimal_text(reactivation),
                "ending_value": decimal_text(ending),
                "bridge_residual": decimal_text(ending - bridge_ending),
                "beginning_logos": beginning_logos,
                "retained_logos": retained_logos,
                "churned_logos": beginning_logos - retained_logos,
                "logo_retention": ratio_text(retained_logos, beginning_logos),
                "grr": ratio_text(beginning - contraction - churn, beginning),
                "nrr": ratio_text(beginning + expansion - contraction - churn, beginning),
            }
        )

    concentration_rows: list[dict[str, object]] = []
    for period in periods:
        levels = [("account", {customer: values[customer, period] for customer in customers})]
        if any(parent_map.values()):
            parent_values: dict[str, Decimal] = defaultdict(Decimal)
            for customer in customers:
                parent_values[parent_map[customer] or customer] += values[customer, period]
            levels.append(("ultimate_parent", dict(parent_values)))
        for level, entities in levels:
            positive = sorted((value for value in entities.values() if value > 0), reverse=True)
            total = sum(positive, Decimal(0))
            row: dict[str, object] = {
                "period": period,
                "analysis_level": level,
                "positive_customers": len(positive),
                "total_value": decimal_text(total),
                "hhi": ratio_text(sum(value * value for value in positive), total * total),
            }
            for top_n in TOP_NS:
                row[f"top_{top_n}_concentration"] = ratio_text(sum(positive[:top_n], Decimal(0)), total)
            concentration_rows.append(row)

    cohort_rows: list[dict[str, object]] = []
    cohort_indices = sorted({index for index in first_positive.values() if index is not None})
    for cohort_index in cohort_indices:
        cohort_customers = [customer for customer in customers if first_positive[customer] == cohort_index]
        original_period = periods[cohort_index]
        original_value = sum((values[customer, original_period] for customer in cohort_customers), Decimal(0))
        original_logos = len(cohort_customers)
        for period_index in range(cohort_index, len(periods)):
            period = periods[period_index]
            current_value = sum((values[customer, period] for customer in cohort_customers), Decimal(0))
            remaining_logos = sum(values[customer, period] > 0 for customer in cohort_customers)
            cohort_rows.append(
                {
                    "cohort_period": original_period,
                    "period": period,
                    "cohort_age": period_index - cohort_index,
                    "original_logos": original_logos,
                    "remaining_logos": remaining_logos,
                    "logo_retention": ratio_text(remaining_logos, original_logos),
                    "original_value": decimal_text(original_value),
                    "current_value": decimal_text(current_value),
                    "value_index": ratio_text(current_value, original_value),
                }
            )

    return {
        "normalized_customer_period.csv": (
            ["customer", "ultimate_parent", "period", "value", "cohort_period"], normalized_rows
        ),
        "customer_movements.csv": (
            ["customer", "period", "beginning_value", "ending_value", "movement", "movement_amount"],
            movement_rows,
        ),
        "retention_summary.csv": (
            [
                "period", "beginning_value", "new", "expansion", "contraction", "churn",
                "reactivation", "ending_value", "bridge_residual", "beginning_logos",
                "retained_logos", "churned_logos", "logo_retention", "grr", "nrr",
            ],
            retention_rows,
        ),
        "concentration_summary.csv": (
            [
                "period", "analysis_level", "positive_customers", "total_value", "hhi",
                "top_1_concentration", "top_3_concentration", "top_5_concentration",
                "top_10_concentration", "top_20_concentration",
            ],
            concentration_rows,
        ),
        "cohort_summary.csv": (
            [
                "cohort_period", "period", "cohort_age", "original_logos", "remaining_logos",
                "logo_retention", "original_value", "current_value", "value_index",
            ],
            cohort_rows,
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate movements, retention, concentration, and cohorts from complete recurring-value snapshots."
    )
    parser.add_argument("--input", required=True, help="Long-form UTF-8 CSV input path.")
    parser.add_argument("--output-dir", required=True, help="New or empty directory for CSV and JSON outputs.")
    parser.add_argument("--customer-column", default="customer")
    parser.add_argument("--period-column", default="period")
    parser.add_argument("--value-column", default="value")
    parser.add_argument("--parent-column", help="Optional stable ultimate-parent column.")
    parser.add_argument("--currency-column", help="Optional currency column; mixed currencies are rejected.")
    parser.add_argument(
        "--missing-as-zero",
        action="store_true",
        help="Treat absent customer-period rows as zero only after confirming the source is a complete population.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        records, periods, cadence, currency = read_records(args)
        values, parent_map, imputed_zeroes = complete_matrix(records, periods, args.missing_as_zero)
        output_dir = Path(args.output_dir)
        if output_dir.exists() and any(output_dir.iterdir()):
            raise InputError(f"Output directory must be empty: {output_dir}")
        output_dir.mkdir(parents=True, exist_ok=True)
        outputs = build_outputs(values, periods, parent_map)
        for filename, (fieldnames, rows) in outputs.items():
            write_csv(output_dir / filename, fieldnames, rows)
        manifest = {
            "source": str(Path(args.input).resolve()),
            "cadence": cadence,
            "periods": periods,
            "currency": currency,
            "customers": len(parent_map),
            "input_rows": len(records),
            "imputed_zero_rows": imputed_zeroes,
            "missing_as_zero_authorized": bool(args.missing_as_zero),
            "outputs": sorted(outputs),
            "limitations": [
                "First positive period is a first-observed cohort unless source history is known to be complete.",
                "Commercial movements do not isolate FX, acquisitions, migrations, or data corrections.",
            ],
        }
        (output_dir / "analysis_manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )
        print(f"Wrote {len(outputs) + 1} files to {output_dir}")
        return 0
    except (InputError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
