# Projects and Repositories

Every source code repository should include documentation that is specific to it (e.g., in a Wiki within the repository), while the project itself should include general documentation that is common to all its associated repositories (e.g., in a Wiki within the backlog management tool).

## Documentation specific to a repository

- Introduction
- Getting started
  - Onboarding
  - Setup: programming language, frameworks, platforms, tools, etc.
  - Sandbox environment
  - Working agreement
  - Contributing guide
- Structure: folders, projects, etc.
- How to compile, test, build, deploy the solution/each project
  - Different OS versions
  - Command line + editors/IDEs
- [Design Decision Logs](../../design/design_reviews/decision_log/decision_log.md)
  - [Architecture Decision Record (ADRs)](../../design/design_reviews/decision_log/decision_log.md#architecture_decision_record_(ADR))
  - [Trade Studies](../../design/design_reviews/trade_studies/trade_studies.md)

Some sections in the documentation of the repository might point to the project’s documentation (e.g., Onboarding, Working Agreement, Contributing Guide).

## Common documentation to all repositories

- Introduction
  - Project
  - Stakeholders
  - Definitions
  - Requirements
- [Onboarding](../../developer_experience/onboarding_guide_template.md)
- Repository guide
  - Production, Spikes
- [Crew Contracts]](../../agile_guide/beyond_the_basics/crew_contracts)
  - [Crew Manifesto](../../agile_guide/beyond_the_basics/crew_contracts/crew_manifesto.md)
    - Short summary of expectations around the technical way of working and supported mindset in the team.
    - E.g., ownership, respect, collaboration, transparency.
  - [Working Agreement](../../agile_guide/beyond_the_basics/crew_contracts/working_agreement.md)
    - How we work together as a team and what our expectations and principles are.
    - E.g., communication, work-life balance, scrum rhythm, backlog management, code management.
  - [Definition of Done](../../agile_guide/beyond_the_basics/crew_contracts/definition_of_done.md)
    - List of tasks that must be completed to close a user story, a sprint, or a milestone.
  - [Definition of Ready](../../agile_guide/beyond_the_basics/crew_contracts/definition_of_ready.md)
    - How complete a user story should be in order to be selected as candidate for estimation in the sprint planning.
- Contributing Guide
  - Repo structure
  - Design documents
  - [Branching and branch name strategy](../../source_control/naming_branches.md)
  - [Merge and commit history strategy](../../source_control/merge_strategies.md)
  - [Pull Requests](./pull_requests.md)
  - [Code Review Process](../../code_reviews/code_reviews.md)
  - [Code Review Checklist](../../code_reviews/process_guidance/reviewer_guidance.md)
- [Project Design](../../design/design_reviews/design_reviews.md)
  - [High Level / Game Plan](../../design/design_reviews/recipes/high_level_design_recipe.md)
  - [Milestone / Epic Design Review](../../design/design_reviews/recipes/milestone_epic_design_review_recipe.md)
- [Design Review Recipes](../../design/design_reviews/design_reviews.md#Recipes)
  - [Milestone / Epic Design Review Template](../../design/design_reviews/recipes/milestone_epic_design_review_template.md)
  - [Feature / Story Design Review Template](../../design/design_reviews/recipes/feature_story_design_review_template.md)
  - [Task Design Review Template](../../design/design_reviews/recipes/task_design_review_template.md)
  - [Decision Log Template](../../design/design_reviews/decision_log/doc/decision_log.md)
  - [Architecture Decision Record (ADR) Template](../../design/design_reviews/decision_log/decision_log.md#architecture_decision_record_(ADR)) ([Example 1](../../design/design_reviews/decision_log/doc/adr/0001_record_architecture_decisions.md),
    [Example 2](../../design/design_reviews/decision_log/doc/adr/0002_app_level_logging.md))
  - [Trade Study Template](../../design/design_reviews/trade_studies/template.md)
