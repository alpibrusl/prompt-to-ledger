# Test It Against What You Already Know

Every chapter so far has been about reducing the chance a model is wrong. This one is about catching it anyway, because reducing the chance is never the same thing as reaching zero, and the last line of defence is the cheapest one in this entire book.

## The known-answer test

A **known-answer test** is running a model against a case where you already know what the correct result should be, before trusting it on the case where you don't. Point Ledgerly's forecasting model at last year's actual starting numbers, run it forward twelve months, and compare what it predicts against what actually happened. If it gets that case right, that's real evidence, not proof, but real evidence, that it will handle next year's forecast honestly too. If it gets the known case wrong, you have just been saved from trusting it on the year that matters, for the cost of an afternoon.

This is precisely why Chapter 5 insisted on a model with parameters rather than a one-off spreadsheet. A model that only knows how to answer this specific pitch cannot be pointed at last year's actuals instead — there is nowhere to point it. A model built to take a scenario as input can be handed *any* scenario, including one you already know the true outcome of, run first, cheaply, before it ever touches the forecast you're actually deciding something from.

Building the known case does not need to be elaborate. Twelve months of last year's real numbers, if you have them. A simplified toy business where you can compute the ending cash balance by hand. A textbook example with a published answer. The bar is not rigor — it's simply *having something to check against*, which is a bar almost every spreadsheet handed to a founder currently clears zero times.

## Suspicion is not a special mode

Extreme forecasts are not the only ones worth doubting. They are simply the ones that announce themselves — a hockey-stick growth curve or a runway number that seems too comfortable is startling enough to trigger doubt without you having to go looking for it. An ordinary, unremarkable-looking forecast can be wrong for exactly the same reasons — a bad assumption, a formula error, an unfair comparison — and it gets a pass for no better reason than that it happened to land somewhere plausible. The honest posture is not *trust it unless something about it looks extreme*. It's suspicion as the default setting for every forecast, and what an extreme one actually earns is not a monopoly on scrutiny — only how loudly it demands it.

Constant suspicion sounds exhausting, and would be, if it meant rebuilding every model from first principles. It doesn't have to. The workable version is the same discipline as the known-answer test above, run continuously instead of once: a **consistency check** — does this forecast agree with something else you already know, arrived at a different way? Does this month's actual revenue land near what last quarter's trend would have predicted, even though nothing about it looks dramatic on its own? Does the bottom-up headcount cost match the top-down payroll total from the bank statement? Does this growth assumption roughly match what a board member, an investor who's seen a hundred companies like yours, or your own gut sense of the pipeline would have predicted before seeing the model? When two things that should roughly agree don't, that disagreement deserves exactly the attention an extreme forecast gets — even though neither number, looked at alone, seemed wrong.

This is deliberately more sustainable than treating distrust as an occasional event reserved for outliers. A consistency check needs no particular expertise. The question is simply *does this agree with that*, and a mismatch is the finding, regardless of which of the two you would have been inclined to trust more going in.

## Suspicion cuts both ways

One instance of this is common enough, and easy enough to get exactly backwards, that it earns its own name: the forecast comes back, and it's either much better than expected or much worse — and one of those two reactions is relief, and the other is alarm, and neither one is *checking*.

Treat both the same way. **A suspiciously good forecast and a suspiciously bad one get identical treatment: stop, and look for an assumption or a formula error before you believe either one.**

The reasoning underneath this is not superstition, it's arithmetic about how often things actually happen. Genuinely transformative quarters are rare — most real businesses move a few percentage points at a time, not a multiple. Assumption errors and formula mistakes, on the other hand, are common; an optimistic growth rate carried too far, a double-counted cost, a formula that references the wrong row, all of these are far more frequent events than a real result several times better than anything you've seen before. When a forecast is extreme, the honest calculation is that it is more likely to be one of the common causes wearing an exciting costume than a rare, genuine breakthrough wearing an ordinary one.

The failure mode to watch for in yourself is asymmetric relief: quietly re-checking the bad-looking forecasts harder than the good-looking ones, because the good ones feel like they've already earned belief. They haven't. A number that flatters what you were hoping for is not thereby more likely to be correct.

## What checking actually looks like

Chapter 3 already gave you the diagnostic habit — the *shape* of a wrong-feeling forecast points at a different link in the chain. For the extreme case specifically: a suspiciously good forecast, check the assumptions first — something is probably being extrapolated from too little or too optimistic a moment. A suspiciously bad one, check the formulas first — something in the model likely broke. For an ordinary-looking forecast that simply failed a consistency check, the diagnostic habit is the same one, applied more broadly: find the specific link where the two disagreeing numbers diverge, rather than assuming the newer or less-trusted one is automatically the culprit.

## What to ask for

> "Before you run this on next year, build the model against last year's actual starting numbers, run it forward, and show me that it reproduces what actually happened."

The default request — not something reserved for forecasts that already look suspicious.

> "This forecast seems unusually [good / bad] compared to what we'd normally expect. Before I act on it, check the assumptions and the formulas for an error — don't just re-explain why the number makes sense."

The extreme-result instruction. Asking it to "explain" a suspicious forecast invites a plausible-sounding story; asking it to check invites an actual answer.

> "Even though this doesn't look unusual, does it agree with what the bank statement shows, what last quarter's trend would predict, or what the pipeline actually supports? If they don't roughly match, find out why before either one gets used."

The consistency check, asked routinely rather than only when something already feels wrong — which is the actual point of this chapter, not just the extreme-result case.
