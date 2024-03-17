# Backlog Management

## External feedback

Various stakeholders can provide feedback to the working product during a project, beyond any formal
review and feedback sessions required by the organization. The frequency and method of collecting
feedback through reviews varies depending on the case, but a couple of good practices are:

- Capture each review in the backlog as a separate user story.
- Standardize the tasks that implement this user story.
- Plan for a review user story per Epic / Feature in your backlog proactively.

## Minimalism slices

### Always deliver your work using minimal valuable slices

- Split your work item into small chunks that are contributed in incremental commits.

- Contribute your chunks frequently. Follow an iterative approach by regularly providing updates and changes to the crew. This allows for instant feedback and early issue discovery and ensures you are developing in the right direction, both technically and functionally.

- Do NOT work independently on your task without providing any updates to your crew.

#### Example

Imagine you are working on adding UWP (Universal Windows Platform) application building functionality for existing continuous integration service which already has Android/iOS support.

##### Bad approach

After six weeks of work you created PR with all required functionality, including portal UI (build settings), backend REST API (UWP build functionality), telemetry, unit and integration tests, etc.

##### Good approach

You divided your feature into smaller user stories (which in turn were divided into multiple tasks) and started working on them one by one:

- As a user I can successfully build UWP apps using current service
- As a user I can see telemetry when building the apps
- As a user I have the ability to select build configuration (debug, release)
- As a user I have the ability to select target platform (arm, x86, x64)
- ...

You also divided your stories into smaller tasks and sent PRs based on those tasks.
E.g. you have the following tasks for the first user story above:

- Enable UWP platform on backend
- Add `build` button to the UI (build first solution file found)
- Add `select solution file` dropdown to the UI
- Implement unit tests
- Implement integration tests to verify build succeeded
- Update documentation
- ...

#### Resources

- [Minimalism Rules](http://minifesto.org/)

## Risk management

Agile methodologies are conceived to be driven by risk management principles, but no methodology can eliminate all risks.

### Goal

Anticipation is a key aspect of software project management, involving the proactive identification and assessment of potential risks and challenges to enable effective planning and mitigation strategies.

The following guidance aims to provide decision-makers with the information needed to make informed choices, understanding trade-offs, costs, and project timelines throughout the project.

### General guidance

- **Identify** risks in every activity such as a planning meetings, design and code reviews, or daily standups. All team members are responsible for identifying relevant risks.
- **Assess** risks in terms of their likelihood and potential impact on the project. Use [issues](https://github.com/nestle-platform-engineering/nestle-platform-engineering-runbook/issues) to report and track risks. Issues represent unplanned activities.
- **Prioritize** them based on their severity and likelihood, focusing on addressing the most critical ones first.
- **Mitigate** or reduce the impact and likelihood of the risks.
- **Monitor** continuously to ensure the effectiveness of the mitigation strategies.
- Prepare **contingency plans** for high-impact risks that may still materialize.
- **Communicate and report** risks to keep all stakeholders informed.

### Opportunity management

The same process can be applied to opportunities, but while risk management involves applying mitigation actions to decrease the likelihood of a risk, in opportunity management, you enhance actions to increase the likelihood of a positive outcome.
