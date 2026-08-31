# Borrowed, Not Reinvented

Ask Ledgerly's agent for the company's margin, or its cost of acquiring a customer, and it will very happily compute one — using whatever definition seemed reasonable in the moment. Whether that definition is the one an investor, a lender, or your own board actually means by the same word is a separate question entirely, and "it computed a number" is not evidence either way.

## What a standard definition actually buys you

**Gross margin** is revenue minus the direct cost of delivering what was sold, divided by revenue — for Ledgerly, what's left of a customer's subscription payment after paying for the hosting and support that customer actually consumes, as a share of that payment. Ask three finance people what belongs in "the direct cost of delivering it" for a software business and you will get near-identical answers: hosting, payment processing, customer support tied directly to serving customers. Ask three founders building their own spreadsheet from scratch and you will get three different answers, some of which quietly exclude a real cost because it made the number look better.

Writing the formula fresh is not more rigorous. It is a fresh judgement call about what counts, made by whoever built the spreadsheet, checked by nobody, compared against nothing. An established definition has had exactly that judgement call made already, argued over for decades, and settled on by the accountants and investors who actually use the number to make decisions. Using theirs is not a matter of deference. It's a matter of the number meaning the same thing to you as it does to whoever reads it next.

## Two more that get reinvented constantly

**Customer acquisition cost** — CAC — is everything spent to acquire a customer over a period, divided by the number of customers acquired in that period. The everything is where reinvention happens: a spreadsheet that counts only ad spend and quietly excludes the sales team's salary is computing a real number, just not the one anyone asking about CAC actually means. The standard version counts the full cost of acquiring — marketing spend, sales salaries, tools — over customers actually won, not customers merely reached.

**Lifetime value** — LTV — is the total gross margin a customer generates over the whole time they stay a customer, before they cancel. Two numbers feed it: how much margin a customer generates per period, and how long a customer typically stays — the second of which is usually estimated from the **churn rate**, the share of customers who cancel in a given period, by taking its reciprocal: a five percent monthly churn rate implies an average customer lifetime of about twenty months. LTV compared against CAC is one of the most quoted ratios in a pitch deck, and it is also one of the easiest to inflate quietly — a churn rate estimated from your three best customers, or a margin figure that skips a real cost, moves the ratio a long way without any single number looking obviously wrong.

None of these are exotic. They are the standard vocabulary that lets a forecast be checked by someone who wasn't in the room when it was built — which is the entire point of using them instead of a homemade version that happens to compute something similar.

## Using the standard definition does not mean using it right

One caution, because it is easy to over-trust the moment a familiar term appears: naming the metric correctly is necessary, not sufficient. Chapter 3's input-trust check still applies fully — a correctly defined LTV, built on a churn rate that was estimated from two good months instead of a representative stretch, produces a wrong answer just as confidently as a homemade formula would. The standard definition gives you much stronger reason to trust that the *arithmetic* means what everyone agrees it means. It does not promise that the *inputs* feeding it were the right ones, or that they were representative of the whole business rather than its best moment. Those checks still have to happen; borrowing the correct definition is one link in the chain, not the whole of it.

## What to ask for

> "What exact definition of margin, CAC, or LTV did you use — name the formula, term by term — or did you build one from scratch for this spreadsheet?"

The direct question. A formula you can compare against the standard one is a good sign. A number with no stated formula behind it is worth a follow-up.

> "Recompute this using the standard definition — full acquisition cost, not just ad spend; churn from a representative period, not the best one — and show me whether the answer changes."

Cheap, and it turns a vague worry into a concrete comparison — if the two agree, that's real reassurance; if they don't, you've just found something worth understanding before you present either one.

> "Is the churn rate behind this LTV estimated from a representative stretch of customers, or from a small, recent, unusually good group?"

Closes the gap this chapter's second half is about — a standard formula is not automatically a reason to relax about what was fed into it.
