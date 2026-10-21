#!/usr/bin/env python3
"""Validate events.json.

Rules: every event has an ISO date (a day, or a month when the source names only
the month) that is not in the future, an https source, a scope from the enum, a
non-empty what_changed, newest-first ordering and no duplicate date+title pair.

Usage: python3 check.py
Exit codes: 0 clean, 1 at least one failure.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVENTS = HERE / "events.json"
SCOPES = {"sandbox", "agent", "router", "connectors", "device", "build-surface", "audit"}
DAY = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MONTH = re.compile(r"^\d{4}-\d{2}$")


def parse(value: str) -> date | None:
    try:
        if DAY.match(value):
            year, month, day = (int(part) for part in value.split("-"))
            return date(year, month, day)
        if MONTH.match(value):
            year, month = (int(part) for part in value.split("-"))
            return date(year, month, 1)
    except ValueError:
        return None
    return None


def main() -> int:
    events = json.loads(EVENTS.read_text(encoding="utf-8"))
    if not isinstance(events, list) or not events:
        print("events.json: expected a non-empty list")
        return 1

    failures: list[str] = []
    today = date.today()
    seen: set[tuple[str, str]] = set()
    previous: date | None = None

    for index, event in enumerate(events):
        label = event.get("date") or f"index {index}"
        stamp = parse(label)
        if stamp is None:
            failures.append(f"{label}: malformed date")
        elif stamp > today:
            failures.append(f"{label}: date is in the future")
        if not str(event.get("source_url", "")).startswith("https://"):
            failures.append(f"{label}: source_url must be https")
        if event.get("scope") not in SCOPES:
            failures.append(f"{label}: scope must be one of {sorted(SCOPES)}")
        if not str(event.get("what_changed", "")).strip():
            failures.append(f"{label}: empty what_changed")
        if not isinstance(event.get("published"), bool):
            failures.append(f"{label}: published must be true or false")
        key = (label, str(event.get("title", "")))
        if key in seen:
            failures.append(f"{label}: duplicate date and title")
        seen.add(key)
        if stamp is not None:
            if previous is not None and stamp > previous:
                failures.append(f"{label}: out of order")
            previous = stamp

    if failures:
        for failure in failures:
            print(failure)
        print(f"{len(failures)} failures")
        return 1
    print(f"events.json: {len(events)} events valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
