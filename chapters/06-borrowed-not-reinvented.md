# Borrowed, Not Reinvented

Ask Ledgerly's agent for the company's margin, or its cost of acquiring a customer, and it will very happily compute one — using whatever definition seemed reasonable in the moment. Whether that definition is one an investor, a lender, or your own board would recognise is a separate question entirely, and "it computed a number" is not evidence either way.

## What a common definition buys you

**Gross margin** is revenue minus the direct cost of delivering what was sold, divided by revenue — for Ledgerly, what's left of a customer's subscription payment after paying for the hosting and support that customer actually consumes, as a share of that payment. This book uses that version because it is the one most investors and lenders reach for by default, not because it is the only version anyone credible uses — a company with a genuinely different cost structure may reasonably draw the line between "direct" and "overhead" somewhere else, and different industries have their own conventions about what belongs on which side. What actually matters, and what a homemade spreadsheet usually skips, is stating which line you drew and why, so the number means the same thing to you as it does to whoever reads it next.

Writing the formula fresh, with no stated convention at all, is the real problem this chapter is about — not deviating from one canonical formula, since for several of these terms no single canonical formula exists. It is a judgement call about what counts, made silently by whoever built the spreadsheet, checked by nobody, compared against nothing, and impossible for the next reader to even see was made. An explicit, commonly recognised definition has had that judgement call argued over already by people who do this for a living. Borrowing theirs, and saying out loud that you did, is not deference. It's the difference between a number someone else can check and one they can only take your word for.

## Two more that get reinvented constantly

**Customer acquisition cost** — CAC — is everything spent to acquire a customer over a period, divided by the number of customers acquired in that period. The everything is where reinvention happens: a spreadsheet that counts only ad spend and quietly excludes the sales team's salary is computing a real number, just not the one most people asking about CAC would expect. The common version counts the full cost of acquiring — marketing spend, sales salaries, tools — over customers actually won, not customers merely reached. Reasonable teams draw the line on what counts as "acquisition" slightly differently — whether onboarding cost belongs here or elsewhere is a genuine judgement call — which is exactly why stating your version matters more than which specific version you picked.

**Lifetime value** — LTV — is the total gross margin a customer generates over the whole time they stay a customer, before they cancel. Two numbers feed it: how much margin a customer generates per period, and how long a customer typically stays — the second of which is commonly estimated from the **churn rate**, the share of customers who cancel in a given period, by taking its reciprocal: a five percent monthly churn rate implies an average customer lifetime of about twenty months. This is the simple, widely used version of the estimate, and it is worth knowing what it assumes: a fairly stable churn rate over time. A real business's churn often isn't that tidy — newer customers typically cancel at a different rate than customers who have stuck around for years — and where that gap is large, the simple reciprocal will be optimistic. It remains a reasonable starting estimate for the audience this book is written for; treat it as a first pass, not a guarantee, and get an actual finance professional involved before a number this sensitive drives a large decision.

LTV compared against CAC is one of the most quoted ratios in a pitch deck, and it is also one of the easiest to inflate quietly — a churn rate estimated from your three best customers, or a margin figure that skips a real cost, moves the ratio a long way without any single number looking obviously wrong.

None of these are exotic, and none of them has exactly one legally correct formula. They are common, widely recognised vocabulary that lets a forecast be checked by someone who wasn't in the room when it was built — which is the entire point of using an explicit, recognisable version instead of a homemade one nobody else can audit.

## Using a recognisable definition does not mean using it right

One caution, because it is easy to over-trust the moment a familiar term appears: naming the metric correctly is necessary, not sufficient. Chapter 3's input-trust check still applies fully — a correctly defined LTV, built on a churn rate that was estimated from two good months instead of a representative stretch, produces a wrong answer just as confidently as a homemade formula would. A common, explicit definition gives you much stronger reason to trust that the *arithmetic* means what most people reading it would expect. It does not promise that the *inputs* feeding it were the right ones, or that they were representative of the whole business rather than its best moment. Those checks still have to happen; borrowing a recognisable definition is one link in the chain, not the whole of it.

## What to ask for

> "What exact definition of margin, CAC, or LTV did you use — name the formula, term by term, and which costs are included or excluded — or did you build one from scratch for this spreadsheet?"

The direct question. A formula you can name and compare against a common version is a good sign. A number with no stated formula behind it is worth a follow-up.

> "Recompute this using the common, widely recognised definition — full acquisition cost, not just ad spend; churn from a representative period, not the best one — and show me whether the answer changes."

Cheap, and it turns a vague worry into a concrete comparison — if the two agree, that's real reassurance; if they don't, you've just found something worth understanding before you present either one.

> "Is the churn rate behind this LTV estimated from a representative stretch of customers, or from a small, recent, unusually good group?"

Closes the gap this chapter's second half is about — a standard formula is not automatically a reason to relax about what was fed into it.
