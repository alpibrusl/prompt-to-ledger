#!/usr/bin/env python3
"""Generate WORKED-EXAMPLE.md from the cohort fixture.

The book argues for the known-answer test in every chapter that touches a
model -- build it, run it against a period you already know, check it
reproduces reality -- and never once performs one. This appendix performs it,
on Ledgerly's own forecast and Ledgerly's own trailing year.

Every figure in the output is computed here, from a fixture generated fresh
into a temporary directory. The book's numbers and the bootcamp's are
therefore the same numbers by construction.

Run by `make example`, which `make pdf`/`epub`/`html` imply.
"""

from __future__ import annotations

import csv
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
GENERATOR = BOOK / "cohort" / "fixture" / "generate_ledgerly_books.py"
OUT = BOOK / "WORKED-EXAMPLE.md"


def generate(into: Path) -> Path:
    target = into / "books"
    result = subprocess.run(
        [sys.executable, str(GENERATOR), str(target)], capture_output=True, text=True
    )
    if result.returncode != 0:
        sys.exit(f"fixture generator failed:\n{result.stderr}")
    return target


def project(cash: float, revenue: float, cost: float, growth: float, extra: float = 0.0):
    """Month-by-month cash, from today forward. Returns (month, revenue, cash) rows."""
    rows = []
    for month in range(1, 37):
        revenue *= 1 + growth
        cash -= (cost + extra) - revenue
        rows.append((month, revenue, cash))
    return rows


def outcome(cash: float, revenue: float, cost: float, growth: float, extra: float = 0.0) -> str:
    rows = project(cash, revenue, cost, growth, extra)
    gone = next((m for m, _, c in rows if c <= 0), None)
    if gone:
        return f"out of cash in month {gone}"
    month, low = min(((m, c) for m, _, c in rows), key=lambda r: r[1])
    return f"survives; lowest at €{low:,.0f} in month {month}"


def build(fixture: Path) -> str:
    rows = list(csv.DictReader((fixture / "trailing-12-months.csv").open(encoding="utf-8")))
    revenue = [float(r["revenue_collected_eur"]) for r in rows]
    today = rows[-1]
    cash = float(today["cash_balance_eur"])
    rev_now = float(today["revenue_collected_eur"])
    cost_now = float(today["monthly_cost_eur"])
    burn = cost_now - rev_now

    steps = [b / a - 1 for a, b in zip(revenue, revenue[1:])]
    early = statistics.mean(steps[:10])
    late = statistics.mean(steps[-2:])
    year = (revenue[-1] / revenue[0]) ** (1 / 12) - 1
    triples = 3 ** (1 / 12) - 1

    def backtest(growth: float) -> tuple[float, float, float]:
        path = [revenue[0] * (1 + growth) ** i for i in range(len(revenue))]
        endpoint = path[-1] / revenue[-1] - 1
        errors = [abs(p / a - 1) for p, a in zip(path, revenue)]
        return path[-1], endpoint, statistics.mean(errors)

    t_pred, t_end, t_mean = backtest(triples)
    e_pred, e_end, e_mean = backtest(early)
    y_pred, y_end, y_mean = backtest(year)

    hire = 7000.0
    with_hire = project(cash, rev_now, cost_now, early, hire)
    hire_gone = next(m for m, _, c in with_hire if c <= 0)
    low_month, low_cash = min(((m, c) for m, _, c in
                               project(cash, rev_now, cost_now, early)), key=lambda r: r[1])

    return f"""# One Model, Checked Against the Year It Already Has

The forecast Ledgerly took to its seed round fits on half a page.

> **12-month revenue forecast:** revenue triples over the next 12 months.
> **Runway:** 18 months (cash positive through the full 18-month projection).
> **Bottom line:** the deck is ready to go out.

Nothing about it is obviously wrong, and there is nothing in it to disagree
with — which is the difficulty. It states conclusions and no workings, so the
only way to find out whether it holds is to rebuild it and run it against
something already known.

Ledgerly has exactly that: `trailing-12-months.csv`, twelve months of its own
collected revenue and cash costs. The forecast makes a claim about the future.
The same claim, pointed backwards, makes a claim about that year — and that
one can be checked.

## Turning the claim into a number

"Triples over 12 months" is a growth rate wearing a word. Tripling in twelve
months is **{triples:.2%} a month**, compounded. That is the assumption the
whole forecast rests on, and it was never written down as a number anyone
could argue with.

## Running it on the year already in hand

Start at the revenue Ledgerly actually collected twelve months ago,
€{revenue[0]:,.0f}, grow it at {triples:.2%} a month, and see where it says the
company should be today.

| growth rate | predicts today | actual | endpoint error | mean monthly error |
|---|---:|---:|---:|---:|
| The forecast's, {triples:.2%} | €{t_pred:,.0f} | €{revenue[-1]:,.0f} | **{t_end:+.0%}** | {t_mean:.0%} |
| The full year's, {year:.2%} | €{y_pred:,.0f} | €{revenue[-1]:,.0f} | {y_end:+.1%} | {y_mean:.0%} |
| The first ten months', {early:.2%} | €{e_pred:,.0f} | €{revenue[-1]:,.0f} | {e_end:+.0%} | **{e_mean:.0%}** |

The forecast's rate puts Ledgerly at €{t_pred:,.0f} a month today. It collected
€{revenue[-1]:,.0f}. A model that misses a year it can see by
{t_end:+.0%} is not a model of Ledgerly; whatever it describes, this company
is not it.

The other two rows are the more useful finding, because they disagree about
which of them passed. The full-year rate lands on today's revenue exactly and
is still {y_mean:.0%} out in an average month — it reproduces the destination
and not the journey. The first-ten-months rate misses today by
{e_end:+.0%} and tracks every month before that to within
{e_mean:.0%}. A test that checks only the final number would pass the first and
fail the second, and the first is the worse description of the year.

## What the last two months did

| | growth |
|---|---:|
| First ten months, on average | {early:+.2%} a month |
| Last two months, on average | {late:+.2%} a month |

Revenue grew about {late / early:.1f} times faster in the last two months than
in the ten before them. That is visible in the file and it is the whole reason
the two candidate rates disagree.

What it is not is an explanation. Two unusually good months are two unusually
good months: a new trend, one large customer, a seasonal spike, or a billing
change that moved collections between periods. The books cannot tell you
which, and the difference decides whether {triples:.2%} is defensible or
absurd. Somebody at Ledgerly knows. That question goes to them, and it is not
one a model or an agent can close on its own.

## What it does to the runway

Today Ledgerly holds €{cash:,.0f}, collects €{rev_now:,.0f} a month and spends
€{cost_now:,.0f} — burning €{burn:,.0f}.

| assumption | outcome |
|---|---|
| No growth at all | {outcome(cash, rev_now, cost_now, 0.0)} |
| The first ten months' {early:.2%} | {outcome(cash, rev_now, cost_now, early)} |
| The full year's {year:.2%} | {outcome(cash, rev_now, cost_now, year)} |
| The forecast's {triples:.2%} | {outcome(cash, rev_now, cost_now, triples)} |

The forecast is not lying about its own arithmetic. At {triples:.2%} a month
Ledgerly really is cash positive throughout, and "18 months" understates it.
Every number in that memo follows correctly from its assumption. The
assumption is the entire forecast, and it is the one thing the memo does not
state.

At the rate the year actually shows it survives, but on a low of €{low_cash:,.0f} in month {low_month} — about {low_cash / cash:.0%} of what is in the bank today, and a number worth seeing before rather than after.

## The cost that is in no version of the model

`signed-offer-letter.md` is a signed, countersigned offer for a senior backend
engineer starting next month at €{hire:,.0f} a month fully loaded. It has not
appeared on a bill, so it is in none of the numbers above, and nobody has gone
back to update the model.

| assumption, with the signed hire | outcome |
|---|---|
| No growth at all | {outcome(cash, rev_now, cost_now, 0.0, hire)} |
| The first ten months' {early:.2%} | {outcome(cash, rev_now, cost_now, early, hire)} |
| The full year's {year:.2%} | {outcome(cash, rev_now, cost_now, year, hire)} |

A memo claiming eighteen months and cash positive throughout describes a
company that, on its own trailing year and its own signed commitments, is out of money in month {hire_gone}.

## What actually found it

Not expertise, and not distrust of whoever wrote the memo. Three things, in
order: turning the claim into a number, running that number against a period
where the answer was already known, and asking what changed in the two months
that carried it.

None of that required rebuilding the model the memo was based on. It required
a model — any model — and a year to test it against.
"""


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        text = build(generate(Path(tmp)))
    if OUT.exists() and OUT.read_text(encoding="utf-8") == text:
        print(f"{OUT.name} already current")
        return
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.name}")


if __name__ == "__main__":
    main()
