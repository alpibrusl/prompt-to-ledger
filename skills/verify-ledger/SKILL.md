---
name: verify-ledger
description: Use this skill before telling a non-technical founder or operator that a financial model, forecast, runway number, or fundraise term is solid, ready to present, or ready to act on — and whenever the user directly asks something like "is this model solid," "can I present this forecast," "is our runway number right," "can I trust this cap table." Runs the pre-decision checklist from the book *Prompt to Ledger* against the actual model — real formulas, real scenarios, real reconciliation — not the narrated summary of it, and is explicit about which items it verified versus which it can't and must ask a human about. Do not use it for routine mid-task modeling work (adjusting a formula, exploring a what-if) that isn't heading toward a claim someone will present or act on — only when a forecast or financial claim is about to be treated as decision-ready.
---

# Verify Ledger

This skill exists because a spreadsheet that's internally consistent and a
forecast that's actually trustworthy are different things, and presenting
the first while implying the second is exactly the failure mode *Prompt to
Ledger* (this repo's own manuscript, under `chapters/`) teaches non-finance
founders to watch for. This skill is that book's closing checklist, run by
the agent on the model it just built or is about to hand back, before the
human has to ask for it.

## The one rule that matters more than the checklist

Check the actual model — real formulas, real cell references, real
scenario branches — not the sentence summarizing what it shows. "Runway is
eighteen months" and a spreadsheet whose burn formula actually computes
that number correctly from real assumptions are different claims. Where a
checklist item is about the model's own mechanics (a standard metric
definition, a sensitivity to one assumption, a range of scenarios), trace
the actual formula and say specifically what it does, not a generic
reassurance that "the model looks solid."

A separate group of items describes something that happened *outside* the
model entirely — a reconciliation against the real bank statement, a
professional's review of a fundraise's legal terms, a founder's actual
understanding of what an option pool does to their ownership before they
sign. A model that is internally tidy is not evidence any of this happened.
Never let a well-built model imply these boxes are checked — they're
exactly the items most likely to get silently skipped because the
spreadsheet looks so convincing, which is why the book puts them in the
checklist at all.

## Workflow

1. **Decide the scope.** A forecast about to be presented to a board,
   investor, or used for a real hiring/spending decision warrants the full
   checklist. A quick sanity check mid-conversation can use the short
   version in `references/minimum-bar-checklist.md`. If it's ambiguous
   which is warranted, ask rather than guessing — the book's whole framing
   question ("what happens if this forecast is wrong, and who finds out
   when it's too late to matter?") is exactly how to decide.

2. **Read `references/minimum-bar-checklist.md`** for the full item list,
   each tagged `[checkable]`, `[ask-human]`, or `[mixed]`, with notes on
   what to actually look for in the model.

3. **For checkable items, trace the actual formulas**, not a summary of
   them. Name what you found specifically — "burn is defined as `opex -
   revenue`, which omits the payroll tax line in row 14" is useful; "the
   burn calculation looks reasonable" is not. Reproduce the headline
   number yourself from the model's own inputs — cash divided by burn
   for a runway, the compounded rate for a growth claim — and compare it
   with the number as stated; a headline that cannot be regenerated from
   the inputs was narrated, not computed, whatever the spreadsheet next
   to it looks like. Identify the single assumption the headline number
   is most sensitive to, and say plainly whether a documented reason for
   its value exists.

4. **For ask-human and the human half of mixed items, actually ask** —
   especially the outside-the-model items (bank reconciliation, legal/tax
   review, real understanding of dilution before signing). Don't award a
   pass because the model itself contains nothing that contradicts it.

5. **Report the results** using the format below, then close with the
   book's own framing question.

## Output format

One table per checklist section actually run, one row per item:

| Item | Status | Detail |
|---|---|---|
| Real formulas, not narrated | ✅ Done | `Model.xlsx`, Runway tab, formulas live and traceable |
| Standard metric definitions | ❌ Not done | "Burn" (cell C14) is defined as `opex - revenue`, which omits the payroll tax line — understates burn by ~9% |
| Reconciled against bank statement | ❓ Ask | Not visible in the model — confirm whether this was done for the period covered |
| ... | | |

Four statuses, used honestly:

- **✅ Done** — checkable, and the model shows it.
- **❌ Not done** — checkable, and it's missing or the model shows a
  problem. Name the specific formula or gap, not just its absence.
- **➖ N/A** — the item doesn't apply (e.g. "If money is changing hands"
  when no fundraise or grant is involved) — say what would make it apply.
- **❓ Ask** — a fact only a human can confirm, or a `[mixed]` item whose
  in-model half wasn't found. Don't round this up to ✅ because the model
  looks fine, and don't round it down to ❌ — say plainly it's unconfirmed.

Then close with, verbatim or close to it:

> **Which assumption is this decision standing on — and what happens if
> it's wrong?**
>
> That's the question this whole checklist unpacks. The gaps above are
> where the answer is currently "we don't, yet" — weigh them against what's
> actually riding on this number: an internal working estimate can carry
> more open items than a forecast going to a board, an investor, or driving
> a hiring or spending decision.

Don't soften a real problem — an invented metric definition, an assumption
nobody can defend, a fundraise term nobody outside the model has actually
reviewed — to make the summary read better. That's precisely the kind of
number this skill exists to catch before it goes in a deck.
