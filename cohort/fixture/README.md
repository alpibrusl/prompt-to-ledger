# The fixture

One generated set of books, reused across Sessions 3, 4, and 5 rather than
inventing new numbers each time -- students meet the same trailing year of
Ledgerly's own history from three different angles, the same three
chapters the book itself spends on it.

It's Ledgerly's own books -- the fictional company this book's chapters
already follow -- covering the exact trailing year Chapters 7, 8, and 9
draw their own numbers from: a forecast memo claiming revenue triples and
runway is eighteen months, a trailing-twelve-months revenue and cost
history where the last two months jump because a single large customer
signed, and a signed offer letter for a new hire that the forecast memo
never mentions. Anyone who's read the book meets a familiar scenario made
concrete and computable, not a new example to learn from scratch.

## Generate it

```bash
python3 generate_ledgerly_books.py                    # -> ./ledgerly-books
python3 generate_ledgerly_books.py /path/to/output     # or choose where
```

Run this **fresh before each session** that uses the fixture, not once at
the start of the cohort — a clean directory, so nobody is working from a
copy someone else has already annotated.

The numbers are the same every run, deliberately: they are seeded, so the
facilitator notes can state the expected answers. For a cohort that has
seen this fixture before, `--seed N` produces a different trailing year
with the same shape and the same lessons — the growth anomaly, the
committed hire, the memo's unreproducible runway — but different figures
to work through.

Today's revenue, cash and monthly costs are never varied: Chapters 8 and 9
quote them, so they have to match the book. Everything behind today
wobbles the way a real bookkeeping export does, which is why the Session 3
back-test lands close rather than exact. A back-test that reproduces a
forecast to the cent has taught the wrong lesson about what reproducing
means.

The generated directory is disposable: this script is the source, the
directory it produces is a build artifact, and `.gitignore` here keeps it
out of the repository the same way `cohort/build/` stays out of the
book's own build.

## What's in it, and which session uses it

- **`trailing-12-months.csv`** -- monthly revenue collected, monthly cash
  costs, burn, and cash balance for the twelve months leading up to
  today. The first ten months grow at a steady, boring, representative
  rate. The last two jump, because a single large customer signed and
  landed as two consecutive invoices -- Chapter 8's "two unusually good
  months," as real rows in a spreadsheet instead of a sentence in a
  chapter.
- **`forecast-as-delivered.md`** -- the headline forecast exactly as it
  was handed over: revenue triples, eighteen months of runway, no visible
  formula, no attached model. Chapter 4's complaint, made concrete enough
  to hand to a student and ask "is this something you can act on."
- **`signed-offer-letter.md`** -- a real, already-committed hire, starting
  next month, at a real fully-loaded monthly cost -- that
  `forecast-as-delivered.md` never mentions. Chapter 9's complaint, in the
  room.

Session by session:

- **Session 3** -- students calibrate a simple growth model on the first
  half of the trailing year (steady, no anomaly) and check whether it
  predicts the second half. The point isn't a perfect prediction; it's
  confirming the model's own mechanics are sound *before* asking whether
  the assumption fed into it deserves to be.
- **Session 4** -- students compute two growth rates from the same CSV: a
  naive one from just the last two months, and a representative one from
  the full trailing year. Then they ask which one the delivered forecast
  actually used, and whether that one is defensible.
- **Session 5** -- students find the offer letter, recompute burn and
  runway honestly -- the real cost including the hire, a defensible
  growth rate instead of the naive one -- and compare the honest number
  against the eighteen months `forecast-as-delivered.md` claims.
- **Session 8 (capstone)** -- a real target for the `verify-ledger` skill,
  for anyone without a model of their own to point it at.

Nothing in these files is labeled as the finding. Working out the load-
bearing assumption and the honest runway is the exercise, not something
the fixture hands over in advance.
