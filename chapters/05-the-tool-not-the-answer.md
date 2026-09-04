# The Tool, Not the Answer

Chapter 3 introduced the move: separate the assumptions from the formulas, and check what each input actually deserves to be trusted. Ledgerly's forecast failed that test twice over, and both failures have the same root.

## The test that matters

Here is the concrete question to ask about any model built for you: **if the growth rate turned out to be different, or the hiring plan changed, would this same model still work — or would someone have to rebuild it?**

A spreadsheet built to answer one specific pitch has that pitch's assumptions baked into its own formulas. Ask for "the runway forecast for the seed deck" and it is entirely possible to get back a spreadsheet that works, produces a plausible-looking eighteen months for this exact hiring plan and this exact growth rate, and would need to be rebuilt — not re-run, rebuilt — the moment either one changes. That spreadsheet is not a model. It is one answer wearing a spreadsheet, and it carries every weakness a bare number carries: nothing about it was ever checked, because a second scenario was never available to check it against.

A **parameter** is the part that separates cleanly: the values that change from one run to the next — the growth rate, the hiring plan, the price — kept apart from the formulas that compute the answer once those values are supplied. "Runway, for a given growth rate and hiring plan" is a model with two parameters. "Runway assuming ten percent monthly growth and no new hires" is that same model with the parameters already baked in and welded shut. The formulas inside the two can be character for character the same. Only one of them can be handed four percent instead of ten and asked what happens.

## Why this is not a matter of taste

This files easily under spreadsheet hygiene — tidier, more elegant, worth doing when there is time. It is not that. Three things break without it, and Ledgerly's memo shows two of them.

**You lose the ability to test it.** Ledgerly has twelve months of its own collected revenue sitting in a file. That is a case where the right answer is already known, and Chapter 7 is about running a model against one of those before trusting it on a year nobody has lived yet.

Running it requires a model that will accept a starting month and a growth rate and produce the twelve months between. A sheet with ten percent welded into its formulas will not do that. It cannot be asked what the last year would have looked like at four percent, because there is no place to put the four. The check that would have caught the forecast — nine point five nine percent a month predicts about €36,525 today against the €20,000 actually collected — is unavailable, not because it is difficult, but because the sheet has no slot to run it in.

Parameters are not a second good habit alongside testing. They are the thing that makes testing possible at all.

**Comparing scenarios quietly breaks.** If "the eighteen-month forecast" is rebuilt from scratch every time an assumption changes, rather than the same model re-run with new parameters, nothing guarantees the underlying formulas stayed the same between versions — a rounding choice, a definition of "customer," a treatment of a one-time cost, each rewritten slightly differently without anyone deciding to change it. The board comparing this quarter's forecast to last quarter's is comparing two models that were never actually built the same way, which is a subtler, quieter version of the unfair comparison this whole book is trying to help you avoid.

**Assumptions stay hidden.** Chapter 3 made this point; here is where it gets fixed. A model that takes parameters has to name what it needs, and naming an assumption is most of what it takes to argue with one.

Ledgerly signed an offer letter for a senior backend engineer at €7,000 a month, fully loaded, starting next month. The cost is committed and it appears in no version of the forecast. Nothing about the sheet's shape asked for a headcount input, so nobody noticed there was nowhere to put one — and a €7,000 monthly cost is the difference between a company with eighteen months and a company out of money in month ten.

## What to look for

You do not need to open the spreadsheet yourself to apply this chapter. You need to be able to ask one question and recognise whether the answer describes a real model or an answer wearing a spreadsheet as a costume:

**"What are the parameters — the things that would change if the assumptions changed — and what's the logic that stays fixed regardless?"**

A real model answers this cleanly: here are the three or four inputs, here is what happens to them once supplied. A disguised one-off spreadsheet produces a hedge, a re-explanation of this specific pitch, or a file where the values you'd expect to be parameters turn out to be typed directly into the middle of a formula. That is the tell. Nothing past it needs opening.

## What to ask for

> "Don't just build this forecast — build it so growth rate, hiring plan, and pricing are parameters at the top of the sheet, so I can change any of them and see the whole model update."

The default request, not a special one reserved for when you already suspect a problem.

> "What are the parameters here, and what would I need to change to run this for a different growth assumption or a different hiring plan?"

The verification question. A clean, short answer means you got a real model. A shrug, or an answer describing what the sheet does specifically for this pitch, means you didn't.

> "Now run this same model against last year's actual numbers as the assumptions, and show me what it would have predicted."

The cheapest real test of whether it's actually reusable — asking it to prove the claim rather than state it, and the direct setup for Chapter 7.
