# Is Perplexity Computer open source? A timeline that carries dates

Kortix is open source. It is the open-source AI Operating System. This repository is a dated, sourced record of what Perplexity has published around Computer and what it has kept closed, so the open-source question can be answered with a date on it instead of a sentence with no date at all.

Six entries cover July 2026 through 21 October 2026. Every row names the layer it touches and links to the page that says it, so a reader can check any line in under a minute.

- `events.json` is the record. One object per dated thing, with its scope, what changed, whether it was a publication, its source and the date it was checked.
- `check.py` validates the record, prints one line per failure, and exits 1 if any rule breaks.
- `render.py` writes the table below from the record, and `--check` fails when the table has drifted.
- `timeline.json` carries the same events plus a `generated_at` stamp, for anything that would rather read JSON than Markdown.

<!-- timeline:start -->

| Date | What changed | Scope | Source |
| --- | --- | --- | --- |
| 2026-10-21 | Audit: agent, planner, router and connector catalog still closed | `agent` | [help center](https://www.perplexity.ai/help-center/en/articles/13837784-what-is-computer) |
| 2026-10-15 | SPACE, the sandbox platform behind Computer, is published | `sandbox` | [announcement](https://www.perplexity.ai/hub/blog/open-sourcing-space) |
| 2026-09-29 | Automations ship in the product, with no repository | `agent` | [announcement](https://www.perplexity.ai/hub/blog/computer-adds-automations-for-ongoing-work) |
| 2026-09-28 | Agent API adds reusable Profiles, Skills and managed connectors | `build-surface` | [announcement](https://www.perplexity.ai/hub/blog/agent-api-now-supports-reusable-agents) |
| 2026-09-15 | Portable Computer documented: closed code on your own GPU | `device` | [help center](https://www.perplexity.ai/help-center/en/articles/20260915-what-is-portable-computer) |
| 2026-07 | Perplexity replaces its sandbox vendor with SPACE | `sandbox` | [announcement](https://www.perplexity.ai/hub/blog/open-sourcing-space) |

<!-- timeline:end -->

The table is generated from `events.json`: the date, the event's `title`, its `scope`, and its `source_url`.

## The question this answers, dated

The answer splits. Perplexity published SPACE, the platform where Computer's sessions execute, on 15 October 2026. The repository runs code in isolation, and it can pause, resume, recover and branch a whole session. It does not hold the agent, the router that picks its models, or the connector catalog that reaches other apps. The sandbox is public. The product is not.

That date is the one to quote. Before 15 October 2026, no layer of Computer had a public repository. After it, exactly one layer does, and it is the layer below every decision a subscriber pays for.

Four things would change the answer: the planner published, the router published, the connector catalog published, or a documented interface at the agent layer that a team can build against and rely on across releases. None had happened as of 21 October 2026, and the audit row above is the dated record of that check.

The longer argument, layer by layer, is on [Is Perplexity Computer open source?](https://opensourceperplexitycomputer.com/is-perplexity-computer-open-source).

## How to read the timeline

`scope` names the layer an event touches, from a fixed list. `sandbox` is where a session's code runs, and it is the layer published in October. `agent` covers the planner and the automations that decide what work happens. `router` is model selection. `connectors` is the catalog that reaches other apps. `build-surface` is how a team declares an agent through the API. `device` is code running on hardware a subscriber owns. `audit` marks a dated re-check rather than a publication.

A row with `published: false` is an audit, and it exists so the record shows what stayed closed. Shipping and publishing are different events. Automations arrived in the product on 29 September 2026 with a dashboard, a schedule and an event trigger, and no repository came with them. Portable Computer shipped on a subscriber's own GPU on 15 September 2026, and the code that runs there is still closed. Both rows record a feature that shipped without a repository, which is the shape a reader is most likely to mistake for a publication.

One row is dated `2026-07` rather than a full day. The announcement names the month it replaced its commercial sandbox vendor and says every Computer session has run on SPACE since; it gives no day.

## Run it

Python 3.9 or newer, standard library only. No dependencies, no network calls.

```bash
python3 check.py
python3 render.py --check
python3 render.py
```

`check.py` validates `events.json`: every date is ISO and not in the future, every `source_url` is https, every `scope` is in the enum, every `what_changed` is non-empty, rows run newest first, and no two rows share a date and title. It prints one line per failure with a count at the end, and exits 1 on any failure. A clean file prints nothing and exits 0.

```bash
$ python3 check.py
2026-11-02: date is in the future
2026-09-28: duplicate date and title
2 failures
$ echo $?
1
```

`render.py --check` compares the table in this file with the one `events.json` produces, and exits 1 when this file is stale. Bare `render.py` rewrites the table between the two markers and leaves the rest of the file alone.

```bash
$ python3 render.py --check
README.md: timeline is stale
$ python3 render.py
README.md: timeline rewritten, 6 events
$ python3 render.py --check
README.md: timeline matches events.json
```

To add an entry, put a row in `events.json` at its date-ordered position, run `check.py`, then `render.py`. A `published: false` row needs the page that supports the negative, which is usually the vendor's own docs or help center rather than a news article about them.

## The other arrangement

Kortix runs the same stack in the opposite order: agents, skills, company memory and connectors are files in one git repo a team owns, one isolated machine per session, and the work lands as a change request a person merges. The code that decides what runs is in the repository the team keeps, next to the work it produces.

Read the code, or get started with [Kortix](https://kortix.com).
