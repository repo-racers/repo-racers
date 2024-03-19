# Definition of Ready

When the development crew picks a product backlog item (PBI) from the top of the backlog, the product backlog item (PBI) needs to have enough detail to estimate the work needed to complete the story within the sprint. If it has enough detail to estimate, it is Ready to be developed.

> If a product backlog item (PBI) is not Ready in the beginning of the Sprint it increases the chance that the story will not be done at the end of this sprint.

## What it is

*Definition of Ready* is the agreement made by the crew around how complete a product backlog item (pbi) should be in order to be selected as candidate for estimation in the sprint planning. These can be codified as a checklist in work items using [GitHub Issue Templates](https://help.github.com/en/github/building-a-strong-community/configuring-issue-templates-for-your-repository) or [Azure DevOps Work Item Templates](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/work-item-template?view=azure-devops&tabs=browser).

It can be understood as a checklist that helps the Product Owner to ensure that the product backlog item (PBI) they wrote contains all the necessary details for the crew to understand the work to be done.

### Examples of ready checklist items

- Does the description have the details including any input values required to implement the product backlog item (PBI)?
- Does the product backlog item (PBI) have clear and complete acceptance criteria?
- Does the product backlog item (PBI) address the business need?
- Can we measure the acceptance criteria?
- Is the product backlog item (PBI) small enough to be implemented in a short amount of time, but large enough to provide value to the customer?
- Is the product backlog item (PBI) blocked? For example, does it depend on any of the following:
  - The completion of unfinished work
  - A deliverable provided by another crew (code artifact, data, etc...)

## Who writes it

The ready checklist can be written by a Product Owner in agreement with the development crew and the Process Lead.

## When should a Definition of Ready be updated

Update or change the definition of ready anytime the crew observes that there are missing information in the product backlog items (PBI) that recurrently impacts the planning.

## What should be avoided

The ready checklist should contain items that apply broadly. Don't include items or details that only apply to one or two product backlog items (PBIs). This may become an overhead when writing the product backlog item (PBIs).

## How to get product backlog items (PBIs) ready

In the case that the highest priority work is not yet ready, it still may be possible to make forward progress. Here are some strategies that may help:

- [Backlog Refinement](../backlog_management/backlog_management.md) sessions are a good time to validate that high priority product backlog items (PBIs) are verified to have a clear description, acceptance criteria and demonstrable business value. It is also a good time to breakdown large stories will likely not be completable in a single sprint.
- Prioritization sessions are a good time to prioritize product backlog items (PBIs) that unblock other blocked high priority work.
- Blocked product backlog items (PBIs) can often be broken down in a way that unblocks a portion of the original stories scope. This is a good way to make forward progress even when some work is blocked.
