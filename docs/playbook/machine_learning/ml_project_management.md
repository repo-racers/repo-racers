# Agile Development Considerations for ML Projects

## Overview

When running ML projects, we follow the Agile methodology for software development with some adaptations, as we acknowledge that research and experimentation are sometimes difficult to plan and estimate.

## Goals

1. Run and manage ML projects effectively
2. Create effective collaboration between the ML team and the other teams working on the project

To learn more about how ISE runs the Agile process for software development teams, refer to this [doc](../agile_development).

Within this framework, the team follows these Agile ceremonies:

- [Backlog management](../agile_development/advanced_topics/backlog_management/backlog_management.md)
- [Retrospectives](../agile_development/core_expectations/core_expectations.md)
- [Scrum of Scrums](../agile_development/advanced_topics/effective_organization/scrum_of_scrums.md) (where applicable)
- [Sprint planning](../agile_development/core_expectations/core_expectations.md)
- [Stand-ups](../agile_development/core_expectations/core_expectations.md)
- [Working agreement](../agile_development/advanced_topics/team_agreements/working_agreements.md)

### Notes on Agile process during exploration and experimentation

1. While acknowledging the fact that ML user stories and research spikes are less predictable than software development ones, we strive to have a deliverable for every user story in every sprint.

2. User stories and spikes are usually estimated using [T-shirt sizes](../agile_development/core_expectations/core_expectations.md) or similar, and not in actual days/hours. See more [here](../agile_development/core_expectations/core_expectations.md) on story estimation.

3. ML design sessions should be included in each sprint.

#### Examples of ML deliverables for each sprint

- Working code (e.g. models, pipelines, exploratory code)
- Documentation of new hypotheses, and the acceptance or rejection of previous hypotheses as part of a Hypothesis Driven Analysis (HDA). For more information see [Hypothesis Driven Development on Barry Oreilly's website](https://barryoreilly.com/explore/blog/how-to-implement-hypothesis-driven-development/)
- Exploratory Data Analysis (EDA) results and learnings documented

## Notes on collaboration between ML team and software development team

- The ML and Software Development teams work together on the project. The team uses one backlog and attend the same Agile ceremonies. In cases where the project has many participants, we will divide into working groups, but still have the entire team join the Agile ceremonies.

- If possible, feasibility study and initial model experimentation takes place before the operationalization work kicks off.
- The ML team and dev team both share the accountability for the MLOps solution.
- The ML model interface (API) is determined as early as possible, to allow the developers to consider its integration into the production pipeline.
- MLOps artifacts are developed with a continuous collaboration and review of the ML team, to ensure the appropriate approaches for experimentation and
productization are used.
- Retrospectives and sprint planning are performed on the entire team level, and not the specific work groups level.