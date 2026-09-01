# The Shape of a Model

Someone asks for next year's forecast. The agent opens a spreadsheet, fills in eighteen tabs of linked formulas, and hands back a number — clean, plausible, two decimal places of confidence. Only later does it come out that one cell, buried four tabs deep, assumes every customer renews, and nobody actually checked whether that was true.

Nothing broke. Every formula calculated correctly. The chain connecting the question to the forecast simply had a weak joint, and a weak joint produces a perfectly well-formed wrong answer.

## The chain, revisited

Chapter 1 named it: a decision to make, then assumptions, then a model applied to those assumptions, then a computation, then a forecast, then the decision made on the strength of it. The point of this chapter is what happens at each link — because "the forecast is wrong" is not a diagnosis, it is a shrug with extra steps. *Which link* is wrong is a question with a checkable answer, and knowing the shape is what lets you ask it.

## What a model actually is

A **financial model** is a set of assumptions connected by formulas to produce a forecast — revenue, costs, cash, whatever the question calls for. Underneath the tabs and formatting, it is exactly two kinds of cell doing two different jobs.

An **input** is a number someone typed in because they believe it to be true, or expect it to become true: a price, a headcount, a growth rate, a rate of customers who cancel each month. Nothing calculates an input. It is the model's opinion about the world, stated as a number.

Everything else is a **formula** — a cell whose value is computed from other cells, ultimately tracing back to inputs. Revenue is a formula: price times customers, and customers is itself a formula built from last month's customers plus new ones minus the ones who left. Follow any formula back far enough and you land on inputs, every time.

This distinction is the single most useful thing you can ask an agent to make visible. A model where you can't tell which cells are inputs and which are formulas is a model you can't audit — you don't know what you're actually trusting versus what was actually calculated.

## Check that your inputs deserve the trust the model gives them

Having the shape visible is only half the move. The other half, easy to skip because it feels like a formality, is asking whether each input is something anyone actually verified, or something that felt reasonable enough to type in and move on.

An input that came from an actual signed contract, an actual current headcount, an actual bill you already received — that's a fact wearing an input's clothes, and it deserves full trust. An input that's a guess about next quarter's growth rate, dressed in the same cell formatting as the verified ones, is not the same kind of thing, and the spreadsheet gives you no visual difference between them. Chapter 8 is entirely about finding the input where this distinction matters most — the one the whole forecast is most sensitive to.

None of this shows up as a model error. The formulas run. The forecast comes back in a plausible range. The mismatch between an input that's a fact and an input that's a hope is invisible from the output alone — which is exactly why it has to be checked *before* the forecast is trusted, not inferred afterward from whether the number feels right.

## The rest of the chain, briefly

The other links get full treatment later; here is where each tends to snap.

**Assumptions.** Guessed instead of grounded, or grounded in a moment that's no longer representative — Chapter 8's whole subject.

**Model.** Reinvented instead of borrowed, using a homemade definition of a standard term — Chapter 6.

**Computation.** Arithmetic done by narration instead of by running an actual formula — Chapter 4.

**Forecast.** A forecast is the output of the first four links, nothing more. It is not yet something you can act on — Chapter 1 already made this the whole book's opening point, and the rest of this chapter is what "not yet" actually consists of.

**Decision.** The only link that was ever the actual goal. Everything before it exists to make this one defensible.

<div style="margin:1.6rem 0;">
<svg viewBox="0 0 704 190" width="100%" style="display:block;" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="ptl2-arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto" markerUnits="userSpaceOnUse">
<path d="M0,0 L6,3 L0,6" fill="none" stroke="#1a1a1a" stroke-width="1.1"/>
</marker>
</defs>
<text x="12" y="20" font-family="EB Garamond, Georgia, serif" font-size="10.5" letter-spacing="0.06em" fill="#9a9a9a">THE CHAIN, LINK BY LINK</text>
<rect x="12" y="50" width="98" height="50" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="61" y="80" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="14" font-weight="600" fill="#1a1a1a">DECISION</text>
<line x1="110" y1="75" x2="127" y2="75" stroke="#1a1a1a" stroke-width="1.1" marker-end="url(#ptl2-arrow)"/>
<rect x="128" y="50" width="98" height="50" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="177" y="80" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="14" font-weight="600" fill="#1a1a1a">ASSUMPTIONS</text>
<text x="177" y="118" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" fill="#666">Chapter 8</text>
<line x1="226" y1="75" x2="243" y2="75" stroke="#1a1a1a" stroke-width="1.1" marker-end="url(#ptl2-arrow)"/>
<rect x="244" y="50" width="98" height="50" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="293" y="80" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="14" font-weight="600" fill="#1a1a1a">MODEL</text>
<text x="293" y="118" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" fill="#666">Chapter 6</text>
<line x1="342" y1="75" x2="359" y2="75" stroke="#1a1a1a" stroke-width="1.1" marker-end="url(#ptl2-arrow)"/>
<rect x="360" y="50" width="98" height="50" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="409" y="80" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="14" font-weight="600" fill="#1a1a1a">COMPUTATION</text>
<text x="409" y="118" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" fill="#666">Chapter 4</text>
<line x1="458" y1="75" x2="475" y2="75" stroke="#1a1a1a" stroke-width="1.1" marker-end="url(#ptl2-arrow)"/>
<rect x="476" y="50" width="98" height="50" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="525" y="80" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="14" font-weight="600" fill="#1a1a1a">FORECAST</text>
<text x="525" y="118" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" fill="#666">Chapter 1</text>
<line x1="574" y1="75" x2="591" y2="75" stroke="#1a1a1a" stroke-width="1.1" marker-end="url(#ptl2-arrow)"/>
<rect x="592" y="50" width="98" height="50" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="641" y="80" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="14" font-weight="600" fill="#1a1a1a">DECISION</text>
<text x="352" y="160" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" font-style="italic" fill="#444">Each link tends to snap in a different way — the shape of the wrongness is a clue to which one to check first.</text>
</svg>
</div>

## Diagnosing a joint, not guessing at the whole

The useful habit this chapter is building toward: when a forecast feels off, you are not stuck choosing between "trust it" and "distrust it" as a single vague judgement. You can ask which specific link is the suspect, and the kind of "off" tells you where to look first.

A forecast that looks suspiciously *good* — growth that outpaces anything the business has actually shown, margins better than any comparable company reports — points first at the assumptions: something is being extrapolated from too little, or too optimistic a moment. A forecast that is suspiciously *bad*, or simply doesn't match reality, points first at the model itself: a formula is probably wrong, or built on a misunderstanding of how the business actually works. Chapter 7 makes this into a full habit; the point to take now is narrower — the shape of the wrongness is itself a clue about where in the chain to look, and "somewhere" is never the only available answer.

## What to ask for

> "Show me which cells in this model are inputs — typed by a person — and which are formulas calculated from other cells."

Forces the shape into the open, where you can actually inspect it.

> "For each input: is this a verified fact, or a guess? If it's a guess, what is it based on?"

The input-trust check, asked directly rather than hoped for.

> "If this forecast turns out to be wrong, which link — an assumption, the model itself, the arithmetic — is most likely where it broke?"

Turns a vague doubt into a specific, checkable place to look next.
