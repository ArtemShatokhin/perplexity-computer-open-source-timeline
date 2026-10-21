# What changed in October 2026

Perplexity published the platform that runs Computer's code on 15 October 2026. It kept the part that decides what the code should do. The announcement says so once you read past its title.

## What the release actually contains

SPACE is Perplexity's sandbox platform, and the code is at `perplexityai/SPACE` ([announcement](https://www.perplexity.ai/hub/blog/open-sourcing-space)). The announcement lists four capabilities it gives Computer: "isolated code execution, pause and resume, recovery, and session branching." Read that list closely. It describes the life of a workspace, which starts, runs code, stops, comes back with its state, and splits into a second copy.

The post also states where the boundary sits: "SPACE treats the sandbox as untrusted and manages network access and platform-held credentials outside the sandbox." That is a precise claim about the machine. Code inside it is assumed hostile. The credentials and the outbound routes are held somewhere the code cannot reach.

What the release does not contain is anything that chooses. The agent is not in the repository. The router that picks a model for each step is not in it. The catalog of connectors that reach Gmail, Outlook, Linear, Slack and GitHub is not in it either. The 21 October audit in the [timeline](../README.md) records that check, and nothing above the sandbox has appeared since.

## The sentence the announcement promises

One line in the post carries the argument: "Agent governance is an engineering problem, and open source is essential to solving it."

That sentence is about governing agents. It says developers who can inspect and adapt a system will find its weaknesses. Read it next to the paragraph above and the scope narrows. The code that shipped governs the workspace the agent's code runs in. Governing an agent means deciding four things: what it may attempt, which model answers a step, which services it can reach, and whose credentials carry the call. Three of those four decisions happen above the sandbox, where no code was published in October.

Perplexity's own account of the release describes SPACE as "the first component of Perplexity's Agentic Runtime Platform" ([Perplexity on Threads, 15 October 2026](https://www.threads.com/@perplexity/post/Dehc3KPmpzn/space-is-the-first-component-of-perplexitys-agentic-runtime-platform-were-open)). "First component" is the company calling the release a piece of a set. A set implies other pieces exist. The announcement never suggests they were in this publication.

The timing makes the boundary easier to see. Two features arrived above the line in the weeks before the release, and both stayed inside the product. Automations, on 29 September 2026, let a Computer task run on a schedule or wake on an event in Slack, Gmail, Outlook, Linear or GitHub ([announcement](https://www.perplexity.ai/hub/blog/computer-adds-automations-for-ongoing-work)). Runs are kept on a dashboard. The Agent API, on 28 September 2026, began accepting versioned Profiles, Skills and managed connectors ([announcement](https://www.perplexity.ai/hub/blog/agent-api-now-supports-reusable-agents)). A subscriber can declare an agent once and reuse it across applications. Neither feature came with a repository, and both execute inside Perplexity's cloud.

## Why the popular summary is wrong

"Perplexity open-sourced its agent" is the sentence that spread. Three checks break it.

The first is the repository. Nothing in it plans a goal into steps, chooses a model or holds a connection to another app. A team that clones it gets an execution layer and has to write the agent themselves.

The second is the product's own recent history. Profiles and Skills in the Agent API are the closest thing to an agent definition. They were published as API features with no code, less than three weeks before the sandbox release, and that release left them where they were.

The third is the local variant, which sounds like the strongest counter-example until you read the help center. Portable Computer, documented on 15 September 2026, runs the orchestrator, the planner, the scheduler and the sandbox on the subscriber's own NVIDIA GPU. The hardware is a DGX Spark or a 24 GB RTX card. A Pro or Max plan is still required ([help center](https://www.perplexity.ai/help-center/en/articles/20260915-what-is-portable-computer)). Closed code on hardware you own shortens the distance your data travels. It does not hand over the code, and it does not let a team change what runs.

## The sentence to use instead

A summary that survives checking has three parts: the layer, the date, and what stayed closed. Perplexity publishes its sandbox platform as of 15 October 2026. The agent, the router and the connector catalog remain inside the product. Anyone who wants the short form can have it, as long as the date travels with it.

That date is also why the record starts where it does. Before October, the honest answer was that Perplexity had published nothing around Computer. The July entry marks the sandbox replacement, announced later without being a publication. After October the answer has a shape. One layer is open, everything above it is closed, and the company calls the release the first component of a larger platform without saying which piece comes next.
