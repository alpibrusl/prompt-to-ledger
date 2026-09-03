# The Tool, Not the Answer

Chapter 3 introduced the move: separate the assumptions from the formulas, and check what each input actually deserves to be trusted. This chapter is what that actually looks like in practice, and how to tell whether you got it.

## The test that matters

Here is the concrete question to ask about any model built for you: **if the growth rate turned out to be different, or the hiring plan changed, would this same model still work — or would someone have to rebuild it?**

A spreadsheet built to answer one specific pitch has that pitch's assumptions baked into its own formulas. Ask for "the runway forecast for the seed deck" and it is entirely possible to get back a spreadsheet that works, produces a plausible-looking eighteen months for this exact hiring plan and this exact growth rate, and would need to be rebuilt — not re-run, rebuilt — the moment either one changes. That spreadsheet is not a model. It is the answer, dressed up as a spreadsheet, and it inherits every weakness a plain one-off number has: nobody checked what it assumes, because there was never a second scenario to check it against.

A **parameter** is the part that separates cleanly: the values that change from one run to the next — the growth rate, the hiring plan, the price — kept apart from the formulas that compute the answer once those values are supplied. "Runway, for a given growth rate and hiring plan" is a model with two parameters. "Runway assuming ten percent monthly growth and no new hires" is that same model with the parameters already baked in and welded shut. The formulas inside might be identical in both cases. Only one of them can be handed a different growth rate without being rebuilt from scratch.

## Why this is not a matter of taste

It would be easy to file this under spreadsheet hygiene — cleaner, more elegant, a nice-to-have. It isn't. Three concrete things go wrong without it, none of them cosmetic.

**You lose the ability to test it.** Chapter 7 is about checking a model against a case where you already know the right answer before trusting it on the case you don't. That only works if the model can *take* a different case as input. A spreadsheet wired to one specific growth rate and one specific hiring plan cannot be pointed at last year's actual numbers to see if it reproduces them — there is nothing to point, because nothing about it takes a scenario as an input in the first place. Testing and parameters are not two separate good habits. The second is a precondition for the first.

**Comparing scenarios quietly breaks.** If "the eighteen-month forecast" is rebuilt from scratch every time an assumption changes, rather than the same model re-run with new parameters, nothing guarantees the underlying formulas stayed the same between versions — a rounding choice, a definition of "customer," a treatment of a one-time cost, each rewritten slightly differently without anyone deciding to change it. The board comparing this quarter's forecast to last quarter's is comparing two models that were never actually built the same way, which is a subtler, quieter version of the unfair comparison this whole book is trying to help you avoid.

**Assumptions stay hidden.** Chapter 3 already made this point once; it is worth restating here because this is where it actually gets fixed. A real model has to declare, as parameters, what it needs — which forces the assumptions behind it into a form you can actually see and question. A one-off spreadsheet can bury the same assumption three tabs deep inside a formula nobody is looking at, because nothing about its shape demands it be stated up front.

## What to look for

You do not need to open the spreadsheet yourself to apply this chapter. You need to be able to ask one question and recognise whether the answer describes a real model or an answer wearing a spreadsheet as a costume:

**"What are the parameters — the things that would change if the assumptions changed — and what's the logic that stays fixed regardless?"**

A real model answers this cleanly: here are the three or four inputs, here is what happens to them once supplied. A disguised one-off spreadsheet produces a hedge, a re-explanation of this specific pitch, or a file where the values you'd expect to be parameters turn out to be typed directly into the middle of a formula. That is the tell, and you do not need to read a single further cell to have caught it.

## What to ask for

> "Don't just build this forecast — build it so growth rate, hiring plan, and pricing are parameters at the top of the sheet, so I can change any of them and see the whole model update."

The default request, not a special one reserved for when you already suspect a problem.

> "What are the parameters here, and what would I need to change to run this for a different growth assumption or a different hiring plan?"

The verification question. A clean, short answer means you got a real model. A shrug, or an answer describing what the sheet does specifically for this pitch, means you didn't.

> "Now run this same model against last year's actual numbers as the assumptions, and show me what it would have predicted."

The cheapest real test of whether it's actually reusable — asking it to prove the claim rather than state it, and the direct setup for Chapter 7.
