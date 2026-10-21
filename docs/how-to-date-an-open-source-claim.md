# How to date an open-source claim

The sentence "Perplexity Computer is not open source" was true on 14 October 2026. It was half true on 16 October 2026. The words never changed. The world under them did, and that is the whole problem with an open-source claim that carries no date.

## Why a claim without a date cannot be audited

An undated claim about open source fails in three ways, and each one is common in the pages that rank for the question.

The first is staleness. A sentence written in March describes a product in March. A reader in October has no way to tell whether the vendor shipped something in between. The claim cannot be checked without redoing the research, so it either gets believed or ignored.

The second is layer collapse. "Open source" describes a specific body of code. A company can be open about one part of its stack and closed about the rest. A vendor can publish the execution layer, the client, the SDK or the schema. The same vendor can publish none of the logic that makes the product worth buying. A sentence that skips the layer lets the smallest publication stand in for the largest one.

The third is an unfalsifiable source. "Open source" is often supported by a marketing page, a launch post or another article that has no date and no repository either. A repository is falsifiable. A reader can clone it, run it, and see what is missing. A landing page is not.

## The three questions that date a claim

Any claim that survives a check answers three questions, in this order.

**What shipped?** The answer has to name a repository and the code inside it, not a feature. Perplexity's 15 October release names `perplexityai/SPACE`, and the announcement names what it does: run code in isolation, pause, resume, recover a session and branch it ([announcement](https://www.perplexity.ai/hub/blog/open-sourcing-space)). An answer that names a capability without a repository is a product announcement, however it is worded. An answer that names a repository without saying what part of the product it runs is incomplete.

**When did it ship?** A publication date, not a launch date and not the date of the article you read. The two differ more often than readers expect. Perplexity announced on 15 October 2026 that it had replaced its commercial sandbox vendor in July, so the change and the publication sit three months apart, and the [timeline](../README.md) carries both as separate rows. The date also has to be paired with the date you checked, because a claim is current only as of its last verification.

**At which layer?** The stack has to be named, top to bottom, and the answer has to say where the publication line falls. For Computer that line sits between the sandbox and the agent. Below it: a published platform with isolation, pause and resume, recovery and branching. Above it: an agent, a router and a connector catalog that execute inside Perplexity's cloud, plus a build surface that accepts Profiles and Skills without publishing the runtime that reads them.

Answer all three and the claim looks like this: as of 21 October 2026, Perplexity publishes the sandbox platform and nothing above it. That sentence can be checked in a minute. It stays true until someone publishes a repository, or a dated audit says otherwise.

## The second-order check

One more question decides whether the first three were answered honestly. Does the publication change what a buyer can do?

A repository a team can clone, run and modify changes what the team can do. A repository that only contains a client for a hosted service does not, even when the code is complete and readable. Perplexity's release passes the first test for the execution layer. Its own post is explicit that the agent, the router and the connectors are not part of it. The test is worth applying because it catches the case where a vendor publishes something adjacent and lets the announcement carry the rest.

## Keeping the answer current without re-reading everything

Re-reading the whole stack every month is how a record stops being maintained. A smaller habit works better. Keep one row per dated thing, and give it six fields.

- The date of the thing itself.
- A short statement of what changed, in words a reader can check.
- The layer it touches.
- Whether it was a publication or an audit.
- The page that says so, which should be the vendor's own announcement, repository or help center.
- The date you checked. That last field keeps the row honest as it ages.

Then re-check on a schedule tied to events rather than to a calendar. A vendor announcement is worth a check within the week, because announcements arrive in clusters and the second one is often the one that matters. A quarterly check covers the quiet periods, and it is where an audit row gets added. The 21 October 2026 row in the [timeline](../README.md) exists because September's rows described features.

Three signals tell you a check is due before an announcement does. A new repository under the vendor's organization. A changelog entry that mentions self-hosting or cloning. A documentation page that stops describing a hosted API and starts describing a deployable stack. Any one of them is worth reading the source for.

## What to write when you are done

Write the claim with the date inside it, and put the layer in the same sentence. "The sandbox is public as of 15 October 2026; the agent and the router are not" is a sentence a reader can verify, dispute and update. The alternative is a confident sentence with no date. It will be wrong within a quarter, and nobody will be able to tell when it stopped being right.
