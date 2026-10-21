#!/usr/bin/env python3
"""Render the timeline table in README.md from events.json.

The table lives between `<!-- timeline:start -->` and `<!-- timeline:end -->`:
Date | title | scope | link. `--check` exits 1 when the README is stale.

Usage:
  python3 render.py
  python3 render.py --check
  python3 render.py --json        # write timeline.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
README = HERE / "README.md"
EVENTS = HERE / "events.json"
TIMELINE = HERE / "timeline.json"
START = "<!-- timeline:start -->"
END = "<!-- timeline:end -->"


def label(url: str) -> str:
    if "/hub/blog" in url:
        return "announcement"
    if "/help-center" in url:
        return "help center"
    return "source"


def table(events: list) -> str:
    lines = [START, "", "| Date | What changed | Scope | Source |", "| --- | --- | --- | --- |"]
    for event in events:
        scope = f"`{event['scope']}`"
        link = f"[{label(event['source_url'])}]({event['source_url']})"
        lines.append(f"| {event['date']} | {event['title']} | {scope} | {link} |")
    lines.extend(["", END])
    return "\n".join(lines)


def main() -> int:
    events = json.loads(EVENTS.read_text(encoding="utf-8"))
    rendered = table(events)
    readme = README.read_text(encoding="utf-8")

    if "--json" in sys.argv:
        payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "events": events,
        }
        TIMELINE.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"{TIMELINE.name}: {len(events)} events written")
        return 0

    if START not in readme or END not in readme:
        print(f"{README.name}: timeline markers missing")
        return 1

    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    current = f"{head}{rendered}{tail}"

    if "--check" in sys.argv:
        if current != readme:
            print(f"{README.name}: timeline is stale")
            return 1
        print(f"{README.name}: timeline matches events.json")
        return 0

    README.write_text(current, encoding="utf-8")
    print(f"{README.name}: timeline rewritten, {len(events)} events")
    return 0


if __name__ == "__main__":
    sys.exit(main())
