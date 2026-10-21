# The layers a team should watch

A subscriber does not buy a sandbox. They buy four decisions above it, and all four still belong to Perplexity after the October release.

The sandbox is public now and was never the hard question. Running code in an isolated machine is work several vendors do well. What a team depends on happens before the code runs. Which task becomes which steps. Which model answers each step. Which service gets reached, and whether that configuration can leave with the team.

## The four layers above the publication line

The rows come from the [timeline](../README.md), checked on 21 October 2026.

| Layer | What it decides for a subscriber | Published | What publication would hand over |
| --- | --- | --- | --- |
| Agent and planner | Which steps a goal becomes, and what runs | No | The logic a team could audit and change |
| Router | Which model answers each step, and at what cost | No | Control over model choice and spend |
| Connector catalog | Which apps are reachable, under whose credentials | No | The list, and the terms that go with it |
| Build surface | How a team declares an agent and reuses it | No | Definitions that travel between systems |

## The agent and the planner

The planner turns one instruction into a sequence of steps and hands parts to sub-agents. It decides how many steps a task takes and in what order. Perplexity's help center describes Computer as an agent that plans a goal and hands work to sub-agents ([help center](https://www.perplexity.ai/help-center/en/articles/13837784-what-is-computer)). None of that logic appears in a repository.

The planner is the difference between a tool a team configures and a tool it operates. The team can measure the output and cannot read why one plan beat another. Automations, added on 29 September 2026, make the point from the other side ([announcement](https://www.perplexity.ai/hub/blog/computer-adds-automations-for-ongoing-work)). A scheduled run repeats a plan the team did not write, on a dashboard it does not host.

## The router

Computer answers different steps with models from different labs, and the router chooses. That choice sets two things a buyer cares about: cost per task, and how much work depends on one vendor's model. Neither is visible.

A published router would let a team pin a model for a regulated workload, swap one out when a price changes, and run one task across two models without asking the vendor. A closed router turns "which model handled this" into a support question. The router is the narrowest of the four, so publishing it is the cheapest way a vendor can move this table, and the strongest signal if it comes first.

## The connector catalog

Connectors are how an agent reaches Gmail, Outlook, Linear, Slack and GitHub. The catalog decides which apps exist, what each connection may do, and whose credentials sit behind it. The Agent API added managed connectors on 28 September 2026, so one definition can name a connection and reuse it across applications ([announcement](https://www.perplexity.ai/hub/blog/agent-api-now-supports-reusable-agents)).

Managed connectors are convenient and not portable. The definition names a connection Perplexity holds, and the scope, token and audit trail stay on its side. A team with ten workflows there owns ten dependencies it cannot inspect, and the cost of leaving is set by a list it never saw.

## The build surface

Profiles and Skills are how a subscriber declares an agent once and reuses it. That layer is closest to something a team could own, because a definition is text: a name, a prompt, skills, a list of connectors. What keeps it closed is where the definition executes. Perplexity says the agent runs inside its cloud ([announcement](https://www.perplexity.ai/hub/blog/agent-api-now-supports-reusable-agents)). The text describes behavior that one runtime interprets.

A published build surface would be a schema and a runtime that reads it. A schema alone is not enough, because a vendor can publish a format and call the layer open while every execution stays on their machines. The test is whether a team can take its definitions elsewhere and get the same behavior.

## Where the local variant sits

Portable Computer puts the whole runtime, from the orchestrator down to the sandbox, on a subscriber's own NVIDIA GPU, as Perplexity's help center documents. The card is a DGX Spark or a 24 GB RTX, and the plan requirement does not move ([help center](https://www.perplexity.ai/help-center/en/articles/20260915-what-is-portable-computer)). It moves execution onto hardware the subscriber owns and changes nothing about who may read the code, which is why it sits beside the stack.

## Which single publication would change a buying decision

The planner. The router would answer a cost question and the connector catalog a portability question, and both are narrow. The planner is where a team's own judgment could enter the system, because a plan is the thing a reviewer can read and disagree with.

A published planner would make the other three layers auditable. A team could see which steps the router was asked to serve and which connectors a plan reached for. Publishing the router alone leaves the expensive decision inside the subscription, and hands the team a dial it cannot trace.

The test when a repository appears is in [how to date an open-source claim](./how-to-date-an-open-source-claim.md). Name the layer, run the code somewhere the vendor does not control, and see whether the behavior follows. A repository that fails the last step is a client, not a layer.

## The other way to arrange the same stack

Kortix is the open-source AI Operating System: your agents, their skills, your company memory, and every connector in one git repo you own, with the agents working on real cloud computers. One isolated sandbox per session. Session work reaches `main` through a change request, and merge is default-deny for agents. Agent definitions, skills and connector configuration sit in the repo beside the work they produce, which is what makes a review possible. Clone it, or try [Kortix](https://kortix.com).
