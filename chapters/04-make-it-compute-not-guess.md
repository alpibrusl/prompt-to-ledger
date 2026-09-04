# Make It Compute, Not Guess

Chapter 3 named the computation link in the chain, and gave it one line: arithmetic done by narration instead of by running an actual formula. This chapter is that line, in full because it is the single most avoidable way a forecast in this book's sense fails to become one.

If you have read *Prompt to Evidence*, the next four chapters will feel familiar — the same discipline, chapter for chapter, aimed at a spreadsheet instead of code or a statistical result. That's deliberate, not an accident of reusing an outline: it's the same gap between capability and judgement, showing up in a third place. Recognising the pattern is itself part of the point.

## Why the agent is worst at exactly the thing it sounds most confident about

The forecast Ledgerly took to its seed round closes with a parenthesis: *(Model available on request.)* Nobody requested it. It is worth being precise about what that half-line was quietly standing in for.

An agent writes a response one piece at a time, each piece picked because it is the most plausible thing to write next given everything already written. Across most of a sentence, plausible and correct are the same thing — which is exactly why the memo reads as well as it does. Across a chain of arithmetic twelve months deep, they separate, and prose has no way of showing where.

A spreadsheet formula does not predict what a column of numbers sums to. It computes it, mechanically, the same way on the millionth calculation as on the first. An agent asked to state a model's output in the middle of a sentence, without actually running the calculation, is doing something different: producing the number that *looks like* the kind of number that would follow, built from patterns in similar-sounding numbers it has seen before, not from mechanically evaluating the formula chain the way a spreadsheet does by construction. For short, simple arithmetic this usually lands close enough anyway because the pattern and the truth line up often enough. Chain a dozen line items together — revenue by month, compounding growth, a headcount ramp with a hiring plan layered on top — and the pattern and the truth have far more room to separate, quietly, with nothing in the tone of the answer to tell you it happened.

The separation is measurable on Ledgerly's own books. "Revenue triples over the next 12 months" is 9.59 percent a month, compounded. Started from the €12,175 the company actually collected a year ago, that rate says Ledgerly should be collecting about €36,525 a month today. It collected €20,000.

A number wrong by that much arrived in the same flat, unhedged sentence a correct one would have used. No stammer, no qualifier, no visible seam. That is why the fix below is mechanical rather than a matter of asking more carefully — there is no tone to listen for.

## The fix is mechanical, not motivational

Asking the agent to "double-check" or "be careful" does not reliably help, because the thing that produced the wrong number — pattern completion — is also the thing that would "double-check" it, using the same mechanism, sometimes landing on the same wrong number again and sometimes a different, equally confident, equally wrong one.

What works instead is a change of method: **have the agent build the model as an actual spreadsheet or a script that computes each value from its inputs, rather than stating a forecast's numbers in conversation.** A cell holding `=B12*1.0959` does the multiplication the same way every time it is opened, whether the answer comes out flattering or ruinous. It cannot be talked into €36,525 by the sentence that came before it.

That is not the same result reached more tidily. It is a categorically different process, and it is the one whose arithmetic actually deserves your trust — not because building it this way guarantees a correct model, only because it guarantees an actual computation happened rather than a guess dressed as one. Whether that computation used the right formula at all is a separate question — Chapters 6 and 7 are what answer it.

## What "trivial" means

This does not mean demanding a full spreadsheet to answer "how many customers do we currently have." That is retrieval, not inference — the agent is reading a count from your existing data, not deriving one through several layers of assumptions, and the risk this chapter is about does not apply to it in the same way.

Genuine computation is different: anything with more than one input feeding a formula, anything projected forward across time, anything where a rate compounds. That is where the rule applies without exception, and it is worth being precise about what the rule actually buys you: not proof that the model is correct, only proof that an actual computation happened rather than a plausible-sounding number typed as though it had been derived. If you are ever unsure which category something falls into, treat it as the second one. Asking for a real spreadsheet on a calculation that never needed one costs a minute and mild embarrassment. Skipping the ask on one that did need it costs what Ledgerly's memo cost: a growth rate nobody could see, carried into a room where people were deciding whether to raise.

## How to tell whether it actually happened

You cannot audit a financial model well enough to verify that every formula is correct — that is a real skill, and Chapters 6 and 7 are what to do about it instead (standard definitions, and testing against a case where you already know the answer). But there is a much lower bar you can check yourself, right now: **did an actual model get built at all.**

Ask directly, and expect one of two things back: an actual spreadsheet or file you can open, with formulas you can click into and see, or a plain statement of what tool built it and where it lives. "Send me the actual spreadsheet, with the formulas visible, not a description of what it contains" is a fair, answerable request regardless of your own comfort with formulas — you are not being asked to judge whether every formula is right, only whether a real model exists behind the number, rather than the number having been typed as though a model had produced it. *(Model available on request.)* If the request produces nothing, that parenthesis was never describing a file. Treat the numbers above it as a guess in a forecast's clothes, however well they read.

## What to ask for

> "Don't tell me the forecast directly — build it as an actual spreadsheet with real formulas, and send me the file."

The core instruction. Ask for it by default on anything past a simple lookup, not only when a number looks suspicious.

> "Was this number calculated in an actual spreadsheet, or estimated from a pattern? If it was estimated, rebuild it properly."

A direct question with a direct answer, useful for anything that arrived without a file attached.

> "Calculate this two ways — in two separate tabs, built independently — and confirm the two results actually match."

Cheap, and it catches the case where the model itself has a formula error rather than the number being an outright guess; Chapter 7 is the fuller version of this habit.
