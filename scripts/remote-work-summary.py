#!/usr/bin/env python3
"""Starter learning template: summarise a remote work security checklist CSV.

Usage:
    python3 scripts/remote-work-summary.py remote-work-security-checklist.csv

Reads a CSV with columns: item, category, status, priority, owner, note.
Status must be one of: Done, In progress, Not started.
Prints the total items, the counts by status, the percentage complete,
the counts by category, and the high-priority items that are not done
yet. Sample data only; it is not a production tool. Always check the
checklist against the real systems it describes before trusting it.
"""
import argparse
import csv
import sys
from collections import defaultdict

VALID_STATUSES = ("Done", "In progress", "Not started")


def load_rows(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"item", "category", "status", "priority"}
        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            print(f"CSV must have columns: {', '.join(sorted(required))}")
            raise SystemExit(1)
        for line_no, row in enumerate(reader, start=2):
            status = row["status"].strip()
            if status not in VALID_STATUSES:
                print(f"Line {line_no}: status '{status}' is not one of "
                      f"{', '.join(VALID_STATUSES)}.")
                raise SystemExit(1)
            rows.append({
                "item": row["item"].strip(),
                "category": row["category"].strip(),
                "status": status,
                "priority": row["priority"].strip(),
            })
    return rows


def print_table(title, groups):
    print(title)
    for name in sorted(groups, key=lambda k: groups[k], reverse=True):
        print(f"  {name:<15} {groups[name]}")
    print()


def main():
    ap = argparse.ArgumentParser(
        description="Summarise a remote work security checklist CSV.")
    ap.add_argument("csv_file", help="path to the CSV file to summarise")
    args = ap.parse_args()

    try:
        rows = load_rows(args.csv_file)
    except FileNotFoundError:
        print(f"File not found: {args.csv_file}")
        raise SystemExit(1)

    if not rows:
        print("No data rows found in the CSV.")
        raise SystemExit(1)

    total = len(rows)
    by_status = defaultdict(int)
    by_category = defaultdict(int)
    for row in rows:
        by_status[row["status"]] += 1
        by_category[row["category"]] += 1

    done = by_status.get("Done", 0)
    percent = 100.0 * done / total

    print(f"Items: {total}")
    print(f"Done: {done} ({percent:.1f}% complete)")
    print()
    print_table("By status:", by_status)
    print_table("By category:", by_category)

    outstanding = [r for r in rows
                   if r["priority"] == "High" and r["status"] != "Done"]
    print("Outstanding high-priority items:")
    if outstanding:
        for row in outstanding:
            print(f"  [{row['status']}] {row['item']}")
    else:
        print("  None - all high-priority items are done.")
    print()
    print("Check before using: walk the list against the real systems.")
    print("A checklist only helps if every row has actually been done.")


if __name__ == "__main__":
    main()
