# Is This Assumption Doing All the Work?

Back to the opening example: Ledgerly's agent, asked for the seed deck, produced a forecast where revenue triples in twelve months. Everything in this chapter is about finding the one number inside that model actually responsible for the tripling — and asking whether it deserves to be.

## Not every input matters equally

A model can have forty inputs and still have its entire output controlled by one or two of them. Price might move the forecast a little if it's off. Office rent barely moves it at all. But a growth rate, compounded over twelve months, moves it enormously — and that's before asking whether the growth rate itself was ever a defensible number to begin with.

Ledgerly's model assumed ten percent month-over-month growth, carried forward for a full year. Compounded — not added, multiplied, month over month over month — that's enough to turn a modest starting revenue into a little over three times itself by month twelve: a genuinely dramatic-sounding claim that, once you look underneath it, rests on nothing more than two unusually good months, driven by a single large customer who happened to sign in that window. Ten percent monthly sustained for a full year is not a small ask — compounded over twelve straight months it works out to well over 200% annual growth, the kind of run a handful of companies manage in their single best year, not the kind most sustain for twelve months running — and the model was treating it as the baseline for every month going forward.

Run the same model with a growth rate of four percent a month — still real, meaningful growth, and much closer to what Ledgerly's own history can actually support — and the twelve-month forecast changes from *revenue triples* to *revenue grows about sixty percent*. Both are real numbers computed by the same correctly-built model. Only one of them is the story Ledgerly can actually stand behind in front of an investor who will ask where ten percent came from.

## Finding the load-bearing assumption

A **load-bearing assumption** is the input a model's conclusion is most sensitive to — the one where a modest, realistic change in the number produces a large change in the answer. Most consequential models have one or a few inputs that deserve to be treated this way, whether or not anyone building the model has actually identified them, and it is rarely the input that gets the most attention while building the model. Growth rate, churn rate, and the timing of a major cost are the usual suspects in a young company's forecast, because each one compounds: a small error in a rate applied every month for a year is not a small error by month twelve.

Finding it does not require rebuilding the model. It requires one deliberate move: **sensitivity analysis** — changing one input at a time, holding everything else fixed, and watching how much the output moves. Halve the growth rate. Does the headline conclusion survive, or does it collapse? Double the churn rate. Does runway shrink by a month, or by a year? The inputs that barely move the answer when changed are not where your scrutiny belongs. The one or two that swing the whole story are exactly where it belongs, and a spreadsheet built with real parameters — Chapter 5's whole argument — makes this check take minutes instead of a rebuild.

## The question that actually matters, once you've found it

Identifying the load-bearing assumption is only useful if you then ask the harder question: is this number defensible, or is it just convenient?

A defensible growth rate is one grounded in a representative stretch of the business's actual history, or in a comparable company's documented experience, stated with the reasoning attached. A convenient one is whatever number made the forecast say what the deck needed it to say, arrived at by working backward from the conclusion rather than forward from the evidence. The two can look identical in a spreadsheet cell. The only way to tell them apart is to ask where the number came from, out loud, and see whether the answer is a reason or a hope.

This is not a call to distrust every optimistic assumption — a young company that never assumed real growth would never raise money or take a real risk. It's a call to know, specifically, which assumption your whole story is standing on, and to have a real answer ready for the person who is going to ask about exactly that one.

## What to ask for

> "Run a sensitivity analysis on this model — change each major input up and down by a realistic amount, one at a time, and show me which ones actually move the headline number."

The core instruction. Do this before presenting any forecast that will drive a real decision, not after someone else asks the question first.

> "Which one or two assumptions is this forecast's headline conclusion most sensitive to?"

The direct version, useful when you don't have time for the full sensitivity table and just need to know where to focus.

> "Where does this growth rate actually come from — a representative stretch of real history, or the best window we could find? Show me the data it's based on."

The defensibility question. An answer that names a specific, representative source is a good sign. An answer that amounts to "it felt achievable" is worth a hard second look before it goes in front of anyone else.
