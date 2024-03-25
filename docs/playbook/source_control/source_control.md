# Overview

There are many options when working with Source Control. At Repo Racers we use [GitHub](https://github.com/) for all our repositories.

## Sections within Source Control

* [Merge Strategies](merge_strategies.md)
* [Branch Naming](naming_branches.md)
* [Versioning](component_versioning.md)
* [Working with Secrets](secrets_management.md)
* [Git Guidance](./git_guidance/git_guidance.md)

## Goal

* Following industry best practice to work in geo-distributed teams which encourage contributions from all of Repo Racers as well as the broader OSS community
* Improve code quality by enforcing reviews before merging into main branches
* Improve traceability of features and fixes through a clean commit history

## General Guidance

Consistency is important, so agree to the approach as a team before starting to code. Treat this as a design decision, so include a design proposal and review, in the same way as you would document all design decisions (see [Working Agreements](../agile_guide/beyond_the_basics/crew_contracts/working_agreement.md) and [Design Reviews](../design/design_reviews/design_reviews.md)).

## Creating a new repository

When creating a new repository, the team should at least do the following

* Agree on the **branch**, **release** and **merge strategy**
* Define the merge strategy ([linear or non-linear](merge_strategies.md))
* Lock the default branch and merge using [pull requests (PRs)](../code_reviews/pull_requests.md)
* Agree on [branch naming](naming_branches.md) (e.g. `user/your_alias/feature_name`)
* Establish [branch/PR policies](../code_reviews/pull_requests.md)
* For public repositories the default branch should contain the following files:
  * LICENSE
  * README.md
  * CONTRIBUTING.md

## Contributing to an existing repository

When working on an existing project, `git clone` the repository and ensure you understand the team's branch, merge and release strategy (e.g. through the projects [CONTRIBUTING.md file](https://blog.github.com/2012-09-17-contributing-guidelines/)).

## Mixed DevOps Environments

For most engagements having a single hosted DevOps environment (i.e. Azure DevOps) is the preferred path but there are times when a mixed DevOps environment (i.e. Azure DevOps for Agile/Work item tracking & GitHub for Source Control) is needed due to customer requirements. When working in a mixed environment:

* Manually tag PR's in work items
* Ensure that the scope of work items / tasks align with PR's

## Resources

* [Git](https://git-scm.com/) `--local-branching-on-the-cheap`
* [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/)
* [GitHub - Removing sensitive data from a repository](https://help.github.com/articles/removing-sensitive-data-from-a-repository/)
* [How Git Works Pluralsight course](https://www.pluralsight.com/courses/how-git-works)
* [Mastering Git Pluralsight course](https://www.pluralsight.com/courses/master-git)
