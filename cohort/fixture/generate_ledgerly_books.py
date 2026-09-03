#!/usr/bin/env python3
"""Generates a fresh copy of the Session 3/4/5 teaching fixture -- a small
set of Ledgerly's own books, the fictional company this book's own chapters
already follow, with the exact scenario Chapters 7, 8, and 9 narrate in
prose, computed here instead of asserted:

  - a trailing 12 months of real revenue and cost data, where the first 10
    months grow at a steady, boring, representative rate and the last two
    jump because a single large customer signed (Chapter 8's "two
    unusually good months")
  - a forecast memo stating the headline numbers -- revenue triples,
    eighteen months of runway -- with no formulas or model attached
    (Chapter 4's whole complaint, made concrete)
  - a signed offer letter for a new hire, starting next month, that the
    forecast memo never mentions (Chapter 9's whole complaint, made
    concrete)

Nothing here hands a student the answer. The honest growth rate, the
honest runway, and the gap between the delivered forecast and either one
are exactly what Sessions 3, 4, and 5 ask students to work out for
themselves, the same numbers the book's own Chapters 7-9 already walked
through in prose.

Usage: generate_ledgerly_books.py [output-dir]   (default: ./ledgerly-books)

Run this fresh before each session that uses it -- see sessions.yaml's
facilitator_notes on session 4 for why a clean generation matters. The
generated directory is disposable and gitignored; this script is the
source.
"""

from __future__ import annotations

import csv
import random
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# The scenario, as numbers. Every figure below is chosen so the arithmetic
# a student does by hand lands close to what Chapters 8 and 9 already walk
# through -- close, not identical, so the exercise is a real calculation
# and not a lookup against the book's own printed answer. With these
# figures: cash / burn with no growth is 12.0 months; with the hire and no
# growth, 8.2; with the hire and the full-year rate the CSV implies (about
# 4.1% a month), cash runs out in month 11; with the hire and the steady
# rate alone (3%), month 10. The memo's 18 is reproducible from none of
# them -- at the memo's own 10% rate the cash never runs out, which is the
# point Chapter 9 makes about where that number came from.
# ---------------------------------------------------------------------------

TODAY_REVENUE = 20_000.00          # this month's revenue, collected (EUR)
TODAY_CASH = 180_000.00            # cash in the bank, today (EUR)
MONTHLY_COST_CURRENT = 35_000.00   # current monthly cash costs (EUR), before the hire

# 12 monthly growth transitions, months 1 -> 12, ending at "today" (month 12).
# The first 10 are steady, representative growth. The last 2 are the
# anomaly: a single large customer signing, landing as two invoices in two
# consecutive months.
STEADY_MONTHLY_GROWTH = 0.03
ANOMALY_MONTHLY_GROWTH = 0.10
GROWTH_TRANSITIONS = [STEADY_MONTHLY_GROWTH] * 10 + [ANOMALY_MONTHLY_GROWTH] * 2

# The already-committed hire the forecast memo never mentions.
NEW_HIRE_MONTHLY_COST = 7_000.00
NEW_HIRE_START_MONTH_LABEL = "next month"

# Monthly costs wobble. Before this, every one of the twelve months was exactly
# EUR 35,000.00 and revenue was an exact geometric series, while the README told
# students to "read it as a real bookkeeping export" -- and the Session 3
# back-test came out perfect to the cent, which is the one outcome a real
# back-test never has. A student who reproduces a forecast exactly has learned
# the wrong lesson about what reproducing means.
#
# The jitter is seeded, so the numbers are stable across runs and the
# facilitator notes can state expected answers. --seed varies them for a
# cohort that has seen the fixture before. Today's figures are never jittered:
# revenue, cash and current costs are quoted verbatim in Chapters 8 and 9 and
# have to match the book.
COST_JITTER = 0.05        # +/- 5% on historical monthly costs
GROWTH_JITTER = 0.01      # +/- 1 point on each monthly growth transition
DEFAULT_SEED = 8812       # the invoice number from Chapter 10's logs


def build_monthly_table(seed: int = DEFAULT_SEED) -> list[dict]:
    """13 monthly data points (month 0 through month 12, month 12 = today),
    computed backward from today's known revenue and cash so the whole
    trailing year is internally consistent.

    Historical months carry seeded jitter; today's figures do not, because the
    book quotes them. Cash is still derived from revenue and costs rather than
    jittered separately, so the balance column reconciles to the cent even
    though no other column is round."""
    rng = random.Random(seed)

    revenue = [0.0] * 13
    revenue[12] = TODAY_REVENUE
    for t in range(12, 0, -1):
        rate = GROWTH_TRANSITIONS[t - 1] + rng.uniform(-GROWTH_JITTER, GROWTH_JITTER)
        revenue[t - 1] = revenue[t] / (1 + rate)

    costs: list[float | None] = [None] + [MONTHLY_COST_CURRENT] * 12
    for t in range(1, 12):  # month 12 is today and stays exact
        costs[t] = round(MONTHLY_COST_CURRENT * (1 + rng.uniform(-COST_JITTER, COST_JITTER)), 2)

    # Round revenue before deriving cash. A real bookkeeping export reconciles
    # to the cent, and deriving the balance from unrounded revenue leaves a
    # one-cent drift that a careful student would report as a finding -- an
    # artefact of the generator, not one of the planted lessons.
    revenue = [round(r, 2) for r in revenue]

    cash = [0.0] * 13
    cash[12] = TODAY_CASH
    for t in range(12, 0, -1):
        burn_t = costs[t] - revenue[t]
        cash[t - 1] = cash[t] + burn_t  # cash[t] = cash[t-1] - burn_t

    rows = []
    for t in range(13):
        month_label = "today" if t == 12 else f"{t - 12} months ago"
        rows.append(
            {
                "month_index": t - 12,  # 0 = today, negative = months ago
                "month_label": month_label,
                "revenue_collected_eur": round(revenue[t], 2),
                "monthly_cost_eur": "" if costs[t] is None else round(costs[t], 2),
                "burn_eur": "" if costs[t] is None else round(costs[t] - revenue[t], 2),
                "cash_balance_eur": round(cash[t], 2),
            }
        )
    return rows


FORECAST_MEMO = """\
# Ledgerly -- Seed Round Financial Summary

Prepared for the seed deck.

- **12-month revenue forecast:** revenue triples over the next 12 months.
- **Runway:** 18 months (cash positive through the full 18-month projection).
- **Bottom line:** the deck is ready to go out.

*(Model available on request.)*
"""

OFFER_LETTER = f"""\
# Ledgerly -- Signed Offer Letter (internal copy)

**Candidate:** Senior Backend Engineer
**Status:** Signed, both parties
**Start date:** {NEW_HIRE_START_MONTH_LABEL}
**Fully loaded monthly cost:** EUR {NEW_HIRE_MONTHLY_COST:,.2f}
  (salary, employer taxes, benefits, equipment)

This is a real, committed cost from the start date above onward. It has
not yet appeared on a bill, and nobody has gone back to update the
forecast model with it.
"""

FIXTURE_README = """\
# What's in this directory

Ledgerly's books for the trailing year, plus the forecast that was handed
to the board and one piece of correspondence from the same period.

- `trailing-12-months.csv` -- monthly revenue collected, monthly cash
  costs, burn, and cash balance for the twelve months up to today.
  Exported from the bookkeeping system.
- `forecast-as-delivered.md` -- the seed-round forecast, as delivered.
- `signed-offer-letter.md` -- correspondence, same period.
"""


def write_files(out: Path, seed: int = DEFAULT_SEED) -> None:
    out.mkdir(parents=True)

    rows = build_monthly_table(seed)
    csv_path = out / "trailing-12-months.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "month_index",
                "month_label",
                "revenue_collected_eur",
                "monthly_cost_eur",
                "burn_eur",
                "cash_balance_eur",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    (out / "forecast-as-delivered.md").write_text(FORECAST_MEMO, encoding="utf-8")
    (out / "signed-offer-letter.md").write_text(OFFER_LETTER, encoding="utf-8")
    (out / "README.md").write_text(FIXTURE_README, encoding="utf-8")


def main() -> None:
    args = [a for a in sys.argv[1:]]
    seed = DEFAULT_SEED
    if "--seed" in args:
        i = args.index("--seed")
        seed = int(args[i + 1])
        del args[i : i + 2]
    out = Path(args[0] if args else "./ledgerly-books")
    if out.exists():
        print(f"error: {out} already exists -- remove it or pass a different output path", file=sys.stderr)
        raise SystemExit(1)

    write_files(out, seed)

    print(f"generated fixture at {out}  (seed {seed})")
    print(f"today's revenue: EUR {TODAY_REVENUE:,.2f}  |  today's cash: EUR {TODAY_CASH:,.2f}")
    print("the committed hire is described only in signed-offer-letter.md -- "
          "the forecast memo never mentions it")
    print("historical months carry seeded jitter, so the back-test lands close "
          "and not exact -- pass --seed N for a cohort that has seen this before")


if __name__ == "__main__":
    main()
