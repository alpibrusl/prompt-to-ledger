# Prompt to Ledger

**The financial literacy your AI agent assumes you already know.**

A short book for founders and operators who can now get an agent to build a
forecast, a budget, or a cap table on request, but never learned the
accounting and finance that used to come bundled with producing one by
hand. Reading a runway projection, catching the one assumption a whole
model rests on, understanding what a term sheet actually costs: the reader
runs a business, not a set of books, and wants to know what to ask before a
number drives a real decision.

Third in a series, same voice, same tooling, different subject each time.
[*Prompt to Production*](https://github.com/alpibrusl/prompt-to-production)
is software engineering discipline for people who cannot read code;
[*Prompt to Evidence*](https://github.com/alpibrusl/prompt-to-evidence) is
analytical discipline for people who are not mathematicians; this one is
financial discipline for people who are not accountants.

> The agent will build almost any model you ask for, and will rarely tell
> you which assumption inside it is doing all the work.

## Contents

| | Part | Chapters |
|---|---|---|
| **I** | The Ground | The handoff · where the money actually lives · the shape of a model |
| **II** | Trusting the Model | Make it compute, not guess · the tool, not the answer · borrowed, not reinvented · test it against what you already know |
| **III** | Making the Decision | Is this assumption doing all the work? · cash is not profit · confidence, not certainty · whose money is it |
| **IV** | Seeing and Trusting the Numbers | A chart is a claim · numbers you can trust |
| **V** | Working With the Agent | Asking the right question · the minimum bar |

**Status: complete draft.** All 15 chapters written; ~15,400 words, 31 defined terms, 76 pages.

## The four rules

Every chapter either builds toward these or applies them to a specific kind
of decision:

1. **Make the agent compute, never guess** — force a real formula, run and
   shown, not a plausible-sounding number typed as though it were derived.
2. **Write the general model; treat this month or this pitch as one input
   to it** — not a spreadsheet quietly tuned to look right for today.
3. **Use established accounting and financial conventions over reinvented
   definitions** — the same supply-chain trust logic as *Prompt to
   Production* chapter 2, aimed at standard statements and metric
   definitions instead of security.
4. **Test the model against numbers you already know, and stay suspicious
   of every assumption, not just the extreme-looking ones** — the scalable
   version is a consistency check: does this assumption agree with what you
   already know about your own business? An assumption that's conveniently
   exactly what you were hoping for fails that check as often as one that
   looks absurd on its face.

## The book is source

The manuscript is Markdown. The EPUB and PDF are build artifacts — derived
from the source, never committed, rebuilt on demand. This is
[bookkit](https://github.com/alpibrusl/content-kit)'s premise, shared with
this book's two companion volumes.

```bash
pip install "content-kit-core @ git+https://github.com/alpibrusl/content-kit@main#subdirectory=packages/core"
pip install "bookkit[epub] @ git+https://github.com/alpibrusl/content-kit@main#subdirectory=packages/bookkit"

make check     # lint the manuscript against the concept ledger
make epub      # → build/prompt-to-ledger.epub
make html      # → build/prompt-to-ledger.html
make pdf       # → build/prompt-to-ledger.pdf   (needs Pango, see below)
make audiobook # → build/audiobook/chapter_NN/  (audio source)
make all       # check + epub + html
```

`make pdf` needs WeasyPrint's system libraries, which pip cannot install —
`libpango-1.0-0` and `libpangoft2-1.0-0` on Debian/Ubuntu, `pango` via
Homebrew on macOS. It is deliberately left out of `make all` so the default
build works without them; CI installs them and builds all three formats.

## The concept ledger and the gate

Same mechanism as the companion volumes: `glossary.yaml` is the canon,
`scripts/check_terms.py` lints the manuscript against it and fails the build
if a term is used before its chapter defines it, and `GLOSSARY.md` is
generated rather than hand-written. See *Prompt to Production*'s README for
the full mechanics — this repository's tooling is a direct copy, unmodified.

## What this book is not

General financial literacy, not tax, legal, or regulatory advice specific
to any jurisdiction. Chapter 1 draws this line explicitly, and every later
chapter respects it — a claim that would change by country, or change every
time the law does, does not belong in a book meant to stay true for years.
Where a real decision needs that kind of advice, the book says so and hands
off to a professional, the same way *Prompt to Evidence* hands off to a
statistician for research-grade statistics.

## Licence

Manuscript: [CC BY-NC 4.0](COPYING.md). Code: [EUPL-1.2](LICENSE), matching
content-kit and this book's companion volumes. See [COPYING.md](COPYING.md).
