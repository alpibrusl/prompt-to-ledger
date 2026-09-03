# Numbers You Can Trust

Every discipline in this book so far — compute properly, use standard definitions, test against known cases, find the load-bearing assumption — protects you from a good model applied to bad bookkeeping. None of it protects you from a good model applied perfectly to numbers that were wrong before any of it started. This chapter is the one link in the chain that everything else depends on and none of it can fix.

## The categories a transaction gets sorted into

A **chart of accounts** is the standard list of categories every transaction in a business gets sorted into — software subscriptions, payroll, travel, office supplies, revenue by product line. It sounds like bureaucracy. It is the entire foundation everything in this book rests on: a model can only be as accurate as the categorisation underneath it, and a transaction filed under the wrong category doesn't announce itself. It just quietly makes one number smaller and another one larger, and both of them look completely normal on their own.

The most common failure is not dramatic. A founder's own subscription to a personal tool, paid from the business card out of convenience, filed under "software" alongside the business's actual hosting costs. A trip that was half business and half personal, expensed in full because splitting it felt like more trouble than it was worth. None of these are fraud. They are the ordinary mess of a small business's books, and each one nudges a margin calculation, a cost-per-customer figure, or a burn rate slightly away from true — never enough to look wrong on its own, but enough that Chapter 6's carefully standard-defined metrics are computing the right formula against the wrong inputs.

## Reconciliation: checking the books against reality

**Reconciliation** is comparing the business's recorded transactions against an independent record of what actually happened — typically the bank or credit card statement — and confirming they match. It is Chapter 7's known-answer test, applied to the bookkeeping itself: the bank statement is the case where you already know the truth because the bank has no reason to record a transaction that didn't happen.

A business that reconciles monthly catches a miscategorised expense, a duplicate charge, or a transaction that was never recorded at all, while it's still a small, fixable thing. A business that doesn't reconcile discovers these the way Ledgerly discovered its missing new-hire cost in Chapter 9 — not through any single dramatic failure, but as a forecast that quietly stopped matching reality, with nothing pointing at where the mismatch actually started.

## When a number moves because the definition did

A metric that jumps or drops sharply for no business reason worth reporting deserves the same treatment Chapter 7 gave any startling result — but here the leading suspect is different: not a formula error, but a change in what's being categorised as what. A new bookkeeper who files a cost slightly differently than the last one did. A subscription that got reclassified from "software" to "cost of goods sold" partway through the year, quietly moving Chapter 6's gross margin calculation without the underlying business having changed at all. The number looks like news. It's often an artifact of a categorisation changing under the model's feet, on a date nobody thought to flag as relevant to anything being measured.

## Look at the books before you trust them

Checking this does not require an accounting background, only the discipline of actually looking, which is exactly the step that gets skipped when a deck is due tomorrow and the numbers look fine at a glance. Before trusting a model built on a business's real financial data: are there any transactions categorised as "uncategorised" or "other" that are large enough to matter? Are there personal-looking expenses mixed into business categories? Has the same category been used consistently across the whole period being modelled, or did the categorisation scheme change partway through?

None of these require statistical sophistication to catch. They require someone to have actually looked at the chart of accounts before building a forecast on top of it, which is exactly the step that turns "the model was correct" into "the model was correct and so were the numbers feeding it."

## What to ask for

> "Are the books for this period reconciled against the bank statement? If not, do that first."

The default request, before trusting any model built from historical bookkeeping data.

> "Show me everything categorised as 'uncategorised' or 'other' for this period, and how large it is relative to total spend."

The data-profiling habit, made concrete. A large uncategorised bucket means real numbers are hiding inside a category that tells you nothing.

> "Has the categorisation scheme — the chart of accounts — changed at all during the period this model covers?"

Catches a shifted definition before it gets mistaken for a real change in the business.
