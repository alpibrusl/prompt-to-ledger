# Cash Is Not Profit

Chapter 8 found the assumption Ledgerly's seed forecast leaned on hardest — a growth rate that turned out to be doing more work than it could defend. Fix that one number and the growth story gets more honest. It does not, on its own, fix the number this chapter is about, which turned out to be wrong for a completely different reason: the model never heard about a decision that had already been made.

## Burn and runway, precisely

**Burn rate** is how much cash a business spends beyond what it brings in, per month — costs minus revenue, on a cash basis, not the accrual-basis profit or loss from Chapter 2's income statement. Ledgerly's costs that month were €35,000; revenue collected was €20,000; burn rate was €15,000 for the month.

**Runway** is how many months of cash remain at the current burn rate: cash in the bank, divided by monthly burn. With €180,000 in the bank and a €15,000 monthly burn, the arithmetic gives twelve months, not eighteen.

Ledgerly's agent reported eighteen. The gap between twelve and eighteen was the same optimistic growth assumption Chapter 8 already caught, and it is worth seeing exactly what that assumption did. At ten percent a month, revenue passes €35,000 in the sixth month, the burn turns into a surplus, and the cash never runs out at all. The model had projected eighteen months forward, seen the balance still positive at the end, and reported the length of its own projection as though it were a runway — a horizon wearing a runway's clothes. Nobody had divided cash by burn. Run the same calculation with Chapter 8's four percent instead and the cash still lasts, but only just: revenue catches costs around the fifteenth month, with the balance bottoming out near €70,000 on the way there. That is a much thinner cushion than eighteen months sounded like, and it was still too generous because the model was missing something else.

## The decision the model never heard about

The rest of the gap was not a growth-rate problem at all. Ledgerly had already extended an offer to a new engineer, start date the following month, at a fully loaded cost of €7,000 per month. Nobody had gone back and told the model. It was still forecasting on €35,000 in monthly costs when the real, already-committed number — from next month onward — was €42,000.

Recompute runway honestly: Chapter 8's four percent growth, plus a cost line that includes the hire the company had already committed to, and the cash runs out in the eleventh month. Not eighteen. Not even the naive twelve — four percent growth buys back less than one hire costs. Same cash in the bank. Same company. A forecast seven months more reassuring than the one a founder should actually be planning against — not from any single dramatic error, but from two ordinary ones compounding quietly in the same direction.

<div style="margin:1.6rem 0;">
<svg viewBox="0 0 740 250" width="100%" style="display:block;" xmlns="http://www.w3.org/2000/svg">
<text x="200" y="24" font-family="EB Garamond, Georgia, serif" font-size="10.5" letter-spacing="0.06em" fill="#9a9a9a">RUNWAY, RECOMPUTED</text>
<text x="185" y="60" text-anchor="end" font-family="EB Garamond, Georgia, serif" font-size="11" fill="#666">Reported (a horizon, not a computation)</text>
<rect x="200" y="43" width="468" height="34" fill="#eee" stroke="#1a1a1a" stroke-width="1.2" stroke-dasharray="4,3"/>
<text x="678" y="65" font-family="EB Garamond, Georgia, serif" font-size="12" fill="#1a1a1a">18 months</text>
<text x="185" y="135" text-anchor="end" font-family="EB Garamond, Georgia, serif" font-size="11" fill="#666">Cash ÷ burn, no growth</text>
<rect x="200" y="118" width="312" height="34" fill="#ccc" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="522" y="140" font-family="EB Garamond, Georgia, serif" font-size="12" fill="#1a1a1a">12 months</text>
<text x="185" y="210" text-anchor="end" font-family="EB Garamond, Georgia, serif" font-size="11" fill="#666">+ 4% growth, + the committed hire</text>
<rect x="200" y="193" width="286" height="34" fill="#1a1a1a" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="496" y="215" font-family="EB Garamond, Georgia, serif" font-size="12" font-weight="600" fill="#1a1a1a">11 months — honest</text>
<text x="470" y="240" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" font-style="italic" fill="#444">The honest number sits below even the naive one: four percent growth buys back less than one hire costs.</text>
</svg>
</div>

This is the kind of wrong Chapter 1 warned about. Nothing in the eighteen-month number looked broken. It was a plausible size, produced by a model that ran without error, built from assumptions that each sounded reasonable stated alone. It was wrong twice over: nobody had computed it as cash divided by burn in the first place, and the model didn't know about a decision that had already been made. There was nothing in the number itself to reveal either gap.

## Working capital: the part that surprises people who've only read the income statement

One more piece of the cash picture rarely shows up until it does. **Working capital** is what's left on the balance sheet after subtracting what a business owes in the near term from what it owns in the near term — cash, money customers owe it, and similar, minus money it owes suppliers and other bills coming due soon. What actually moves that number month to month, and what a founder feels directly, is the timing gap underneath it: earning revenue versus actually collecting it, incurring a cost versus actually paying it. A business can be profitable on the income statement and still watch its cash shrink, if its customers are slow to pay while its own bills come due on schedule — exactly Chapter 2's Ledgerly example, generalised into an ongoing pattern rather than one confusing month.

Growth can make this worse before it makes anything better, specifically when customers pay after the business has already incurred the cost of serving them. A company growing quickly on thirty- or sixty-day payment terms is extending more credit every month than it's collecting from the customers it signed further back — a widening gap between doing the work and getting paid for it, even if every single customer eventually pays in full. Where customers pay upfront instead — an annual plan, a prepaid subscription — the effect can run the other way, with growth *improving* the cash position rather than straining it. Either way, a model that only asks "will we be profitable" and never asks "will collections keep pace with growth" can miss a cash shortage that a profitable, healthy-looking business is genuinely walking toward.

## What to ask for

> "What is our current burn rate, and what is our runway — cash divided by burn, not adjusted for any future revenue growth?"

The honest baseline, asked before any optimistic assumption gets layered on top of it.

> "Does this burn rate include every hire, contract, and cost we've already committed to, even ones that haven't shown up on a bill yet?"

The question that would have caught Ledgerly's gap. A model is only as current as what it was told, and a decision made in a conversation two weeks ago doesn't update a spreadsheet on its own.

> "If our growth continues, will working capital tie up more cash than it frees — will collections keep pace with new signups, or fall further behind?"

Surfaces the version of this problem that a profitable-looking income statement hides completely.
