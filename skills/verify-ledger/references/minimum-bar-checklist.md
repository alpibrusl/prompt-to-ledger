# The Minimum Bar — checklist with inspection guidance

This is the checklist from *Prompt to Ledger*, chapter 15 ("The Minimum
Bar"), verbatim in substance. Each item is tagged with how the skill should
actually resolve it:

- **[checkable]** — the model itself (its formulas, structure, or outputs)
  settles it. Go look at the actual spreadsheet or code, not the narrated
  summary of it.
- **[ask-human]** — describes something that happened outside the model —
  a manual reconciliation against a bank statement, a professional's
  review, a founder's understanding before signing something. Ask, don't
  infer from the model looking clean.
- **[mixed]** — checkable if the relevant step is visible inside the model
  itself (a labeled scenario, a documented sensitivity check); if it isn't
  visible, that's a signal, not proof — confirm with a question.

"The model" here means whatever artifact actually produced the number —
a spreadsheet with real formulas, or code that generates one. A sentence
like "runway is eighteen months" is not the same artifact as the model that
computed it, and this skill's job is to check the model, not the sentence.

## Getting a real model

- **The forecast was computed with an actual spreadsheet or script,
  formulas visible — not narrated as a number.** [checkable] — is there a
  real model (spreadsheet with live formulas, or code) behind the number,
  or only a stated figure with no visible mechanism producing it?
- **The model is built with real parameters — growth rate, hiring plan,
  pricing — not a one-off sheet quietly tuned to today's numbers.**
  [checkable, needs real reading] — look for hardcoded outputs, or
  parameters that appear to have been reverse-engineered from a desired
  headline number rather than set independently and then computed forward.
- **Standard definitions were used for margin, CAC, LTV, and burn — not
  formulas invented for this spreadsheet.** [checkable] — read the actual
  formula for each metric used and compare it against the standard
  definition (e.g. burn = cash out minus cash in for the period, not net
  income, not revenue minus only some costs). Name the specific formula
  found if it diverges.
- **The model was tested against a case with a known answer — last year's
  real numbers — and reproduced it, before being trusted on the year that
  matters.** [mixed] — checkable if a back-test against last year's
  actuals appears in the model; if it doesn't appear, ask whether it
  happened elsewhere rather than assuming it didn't.

## Not fooling yourself

- **The forecast passed a consistency check against something else already
  known — the bank statement, the pipeline, a board member's sense of the
  business.** [ask-human] — this is specifically a check against something
  *outside* the model. A model that's internally consistent with itself is
  not evidence it was cross-checked against reality. Ask whether this
  happened.
- **An unusually good or unusually bad forecast specifically was checked
  for an assumption or formula error before it was believed.** [mixed] —
  look for evidence of that investigation; ask if it isn't visible,
  especially if the forecast is notably optimistic.
- **The load-bearing assumption has been identified, and it's one you can
  defend with a reason, not just a hope.** [checkable, needs real reading]
  — this is the single highest-value item to actually verify. Find which
  single assumption the headline number moves the most on (run the
  sensitivity yourself if the model allows it, or trace the formula chain),
  name it specifically, and check whether a stated reason for that
  assumption's value exists anywhere — or whether it's just carried forward
  from an early guess.
- **Every already-committed hire, contract, or cost is reflected in the
  model, not just the current snapshot.** [mixed] — checkable against any
  documented commitments (signed offers, contracts) if they're available;
  if commitment records aren't provided, ask explicitly what's already been
  committed to that the model might not reflect yet.
- **You have a range — base, worse, better — not just a single headline
  number, and it's narrow enough to actually plan against.** [checkable] —
  does the model show multiple scenarios, or only one path?

## Knowing what you're looking at

- **The underlying bookkeeping has been reconciled against the bank
  statement for the period the model covers.** [ask-human] — an event
  fact about work done outside the model; a model that looks internally
  tidy is not evidence this happened.
- **Personal or miscategorised expenses have been checked for and cleaned
  out of the numbers feeding the model.** [ask-human] — same pattern.
- **A chart's axis, date range, and choice of what to include would tell
  the same story drawn the plain, unflattering way.** [checkable, if a
  chart exists] — inspect the actual chart for a truncated axis, a
  favorable date range, or selectively included categories.

## If money is changing hands

- **You understand what any fundraise or equity grant actually does to
  your ownership, including any option pool, before signing.** [ask-human]
  — a genuine-understanding fact, not a property of a spreadsheet. If a
  cap-table calculation exists, it's fine to check the math is correct
  (that part is checkable), but whether the human actually understands
  what it means before signing is not something to assume from the
  spreadsheet being right.
- **Anything with real legal, tax, or regulatory exposure has been
  reviewed by an actual professional, not settled from a model alone.**
  [ask-human] — always ask this one directly. A well-built model is
  explicitly not a substitute for this, per the book's own chapter 1 and
  11 — don't let a good model imply this box is checked.

## The short version (five highest-value items)

For a lighter sanity check rather than a full pre-decision review:

1. Computed with a real spreadsheet, formulas visible, not narrated.
   [checkable]
2. Tested against a known case — last year's actuals — before being
   trusted on this year. [mixed]
3. Survives a consistency check against something else already known — the
   bank statement, the pipeline — not just checked because it looked
   unusual. [ask-human]
4. A range exists, and it includes every commitment already made.
   [checkable]
5. Anything with real legal or tax exposure has gone to an actual
   professional. [ask-human]

Notice that two of the five highest-value items — the outside-consistency
check and the professional review — are pure ask-human items. That's the
same pattern as the other books in this series: the cheapest, most
consequential gaps are disproportionately the ones a model can't answer
about itself.
