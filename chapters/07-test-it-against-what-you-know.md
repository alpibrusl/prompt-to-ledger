# Test It Against What You Already Know

Everything so far has been about lowering the odds that a model is wrong. Lowered odds are not zero, and what follows is how the wrong ones get caught anyway — using nothing but a year the company has already lived through.

## The known-answer test

A **known-answer test** is running a model against a case where you already know what the correct result should be, before trusting it on the case where you don't. Point Ledgerly's forecasting model at last year's actual starting numbers, run it forward twelve months, and compare what it predicts against what actually happened. Run it on Ledgerly's actual trailing year and the seed memo's central claim does not survive the afternoon. "Revenue triples over the next 12 months" is nine point five nine percent a month. Started from the €12,175 the company genuinely collected twelve months ago, that rate says Ledgerly should be collecting about €36,525 today. It collected €20,000.

No expertise produced that. A rate, a starting number, twelve multiplications, and a year the company had already lived.

This is what Chapter 5's insistence on parameters was for. A sheet that only answers this pitch has nowhere to put last year, so the check above cannot be run on it at all. A model that takes a scenario will take any scenario, including one whose ending you can already look up.

The known case can be modest. Last year's real numbers if they exist; a toy business whose ending cash you can work out on paper if they don't.

What it must not be is graded only on where it finishes. Ledgerly's trailing year can be described by more than one rate, and the two candidates disagree about which of them passed. The rate implied by the full year lands on today's revenue *exactly* and is still five percent out in an average month. The rate from the first ten months misses today by thirteen percent and tracks every month before it to within two. A test that compares only the final number passes the first and fails the second — and the first is the worse description of the year, because it reproduces the destination and not the journey.

Check the path, not just the endpoint. A model can arrive at the right answer having been wrong every month on the way.

## Suspicion is not a special mode

Extreme forecasts are not the ones most worth doubting. They are the ones that announce themselves. "Revenue triples" is startling enough to provoke a second look without anyone having to remember to take one.

The eighteen-month runway sitting in the same memo is the harder case. Eighteen months is an unremarkable number for a company that has just raised, so it passes on the strength of sounding ordinary — and it is wrong for exactly the reasons the tripling is wrong because it was computed from the same growth rate. What an extreme number earns is not more scrutiny than an ordinary one. Only a louder reminder to apply it.

Doubting everything would be exhausting if it meant rebuilding every model. It does not. The sustainable form is the known-answer test run continuously rather than once: a **consistency check** — does this number agree with something else already known, arrived at another way?

Ledgerly's books offer several, none requiring a spreadsheet. Does the forecast's growth rate match what the last twelve rows of the revenue file actually did? Does the headcount cost in the model match the payroll leaving the bank? Does the signed offer letter in the folder appear anywhere in the numbers? That last one takes about ten seconds and finds €7,000 a month that the model has never heard of.

When two things that ought to agree do not, the disagreement is the finding — even when neither number looked wrong on its own.

None of those questions requires knowing finance. Each is *does this agree with that*, and the answer does not depend on which of the two you arrived more inclined to believe.

## Suspicion cuts both ways

One version of this is common enough, and easy enough to get backwards, to be worth naming. The forecast lands either much better than hoped or much worse. One of those produces relief and the other produces alarm, and neither produces a check.

Treat both the same way. **A suspiciously good forecast and a suspiciously bad one get identical treatment: stop, and look for an assumption or a formula error before you believe either one.**

The reasoning underneath this is not superstition, it's arithmetic about how often things actually happen. Genuinely transformative quarters are rare — most real businesses move a few percentage points at a time, not a multiple. Assumption errors and formula mistakes, on the other hand, are common; an optimistic growth rate carried too far, a double-counted cost, a formula that references the wrong row, all of these are far more frequent events than a real result several times better than anything you've seen before. So an extreme forecast is more likely a common error in an exciting costume than a rare breakthrough in a plain one. Ledgerly's tripling turned out to be two good months, extrapolated for a year.

The habit to watch for in yourself is asymmetric relief: checking the discouraging forecasts harder than the encouraging ones because the encouraging ones feel as though they have already made their case. Flattering a hope is not evidence of being right.

## What checking looks like

Chapter 3 already gave you the diagnostic habit — the *shape* of a wrong-feeling forecast points at a different link in the chain. For the extreme case specifically: a suspiciously good forecast, check the assumptions first — something is probably being extrapolated from too little or too optimistic a moment. A suspiciously bad one, check the formulas first — something in the model likely broke. For an ordinary forecast that merely failed a consistency check, find the link where the two numbers part company, rather than assuming the newer or less familiar one is at fault. Ledgerly's memo and Ledgerly's revenue file part company at exactly one number, and it is not in the memo — the memo never states a rate at all.

## What to ask for

> "Before you run this on next year, build the model against last year's actual starting numbers, run it forward, and show me that it reproduces what actually happened."

The default request — not something reserved for forecasts that already look suspicious.

> "This forecast seems unusually [good / bad] compared to what we'd normally expect. Before I act on it, check the assumptions and the formulas for an error — don't just re-explain why the number makes sense."

The extreme-result instruction. Asked to *explain* a suspicious forecast, an agent will produce a story that fits it; asked to *check*, it has to go and look.

> "Even though this doesn't look unusual, does it agree with what the bank statement shows, what last quarter's trend would predict, or what the pipeline actually supports? If they don't roughly match, find out why before either one gets used."

The consistency check, asked as a matter of routine rather than when something already feels wrong. That, rather than the extreme-result case, is what this chapter is for.
