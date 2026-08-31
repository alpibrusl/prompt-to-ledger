# Project conventions

## What this book is and who it is for

*Prompt to Ledger* teaches financial literacy to founders and operators who
can now get an agent to build a forecast, a budget, or a cap table on
request, but never learned the accounting and finance that used to come
bundled with producing one by hand. Reading a runway projection, deciding
whether an assumption in a model is doing too much work, understanding what
a term sheet actually costs — the kind of concrete decisions this book is
written toward. The reader is comfortable running a business, not an
accountant, and wants to know what to ask before a number drives a real
decision.

Third companion volume, same voice and structure, different subject:
[*Prompt to Production*](https://github.com/alpibrusl/prompt-to-production)
is software engineering discipline for people who cannot read code;
[*Prompt to Evidence*](https://github.com/alpibrusl/prompt-to-evidence) is
analytical discipline for people who are not mathematicians; this one is
financial discipline for people who are not accountants. All three teach
vocabulary and judgement, not a credential.

**Scope, held deliberately narrow.** This book covers general financial
literacy — reading and directing a model, not tax law, securities
regulation, or jurisdiction-specific compliance. Chapter 1 draws this line
explicitly and every later chapter respects it: a claim that would change
by country or change every time the law does does not belong in prose meant
to stay true for years. When a chapter would otherwise need one, it names
the boundary and says to get a real professional instead, the same way
*Prompt to Evidence* hands off to a statistician for research-grade work.

The spine is four rules, and every chapter either builds toward them or
applies them to a specific kind of decision:

1. Make the agent compute, never guess — force a real formula, run and
   shown, not a plausible-sounding number typed as though it were derived.
2. Write the general model; treat this month or this pitch as one input to
   it, not a spreadsheet quietly tuned to look right for today.
3. Use established accounting and financial conventions over reinvented
   definitions — the same supply-chain trust logic as *Prompt to
   Production* chapter 2, aimed at standard statements and metric
   definitions instead of security.
4. Test the model against numbers you already know, and stay suspicious of
   every assumption, not just the extreme-looking ones — the scalable
   version is a consistency check: does this assumption agree with what you
   already know about your own business? An assumption that's conveniently
   exactly what you were hoping for fails that check as often as one that
   looks absurd on its face.

## Author identity — do not guess

The author is:

    Alfonso Sastre <alfonso@alpibru.com>

Same person, same convention as the companion volumes. Use exactly this for
`book.yaml`, git commit authorship, and anywhere an author is named. If a
field about a real person is unknown, leave it blank and ask — do not infer.

## The manuscript is source

Markdown in `chapters/` is the source; everything in `build/` is derived and
gitignored, as is `GLOSSARY.md`. Never edit `GLOSSARY.md` by hand — it is
generated from `glossary.yaml` by `make glossary`.

## The concept ledger and the gate

`glossary.yaml` is the canon: every term the book teaches, with one
definition, one committed analogy, the defining chapter, and prerequisite
terms.

`make check` lints the manuscript against it and exits 8 on error. It runs
in CI on every push and pull request. When adding prose:

- Define a term before using it, or signpost the forward reference
  explicitly with "(Chapter N)" — the linter allows a signposted one and
  rejects a bare one.
- Add any new term to `glossary.yaml` rather than defining it only in prose.
- Keep an analogy consistent with the one the ledger commits to.
- Chapter numbers in the rendered book come from `book.yaml`'s per-chapter
  `title` override (`"Chapter N — Title"`), not from the Markdown H1.

## Absolutes

Distinguish a prescription from an assertion. "Never let a model's headline
number stand without a range" is a rule of practice and its force is the
point — keep it. A claim about the world takes a softer edge, so a reader
absorbs the lesson instead of arguing with the sentence. Check `never`,
`always`, `only`, `every`, `exactly`, `not negotiable` when editing: keep
them in rules, soften them in claims.

## Numbers in prose

Every worked example uses the running case study (Ledgerly, the same
fictional invoicing company from *Prompt to Production*) with specific,
internally consistent figures. When a number recurs across chapters, it has
to match — this book asks its reader to reconcile a model against numbers
that agree with each other, and it holds itself to the same standard.

## Build

    make check    # the gate
    make epub / make html / make pdf
    make all      # check + epub + html (pdf needs Pango, see README)

## Audio

`make audiobook` emits a podcastkit project under `build/audiobook/` —
derived, gitignored, one episode per chapter. Rendering it to MP3 needs a
TTS backend and is not wired into CI, because it costs money per character
on the paid backends and hours of CPU on the free ones.

## Licences

Manuscript CC BY-NC 4.0; code EUPL-1.2. New files under `scripts/` need an
`SPDX-License-Identifier: EUPL-1.2` header. See `COPYING.md`.
