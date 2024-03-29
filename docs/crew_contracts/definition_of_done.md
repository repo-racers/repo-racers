# Our Crew's Definition of Done

Our Definition of Done (DoD) establishes clear, agreed-upon criteria that signify the completion of work at different stages of our development cycle. It ensures quality, completeness, and alignment with our project goals and customer expectations. At Repo Racers, we adhere to a two-tiered DoD to encapsulate the essential checkpoints for our development process: one at the **Pull Request** level and another at the **Release** level.

## Pull Request Level

The DoD at the pull request level focuses on ensuring that individual changes or feature implementations are complete, thoroughly tested, and meet our quality standards before being merged into our main codebase. This level of DoD helps us maintain a clean, efficient, and robust development workflow.

[GitHub Documentation](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

- Scope complete as described in the work item's [Definition of Ready](./definition_of_ready.md).
- Application architecture complies with the [12 Factor App Checklist](./12_factor_app_checklist.md).
- Infrastructure architecture complies with the [Azure Deployment Checklist](./azure_deployment_checklist.md).
- Group or individual codeowners identified int the project  `.github/CODEOWNERS` file for all artefacts on the branch to be merged.
- Any new CICD pipelines have been commited to the `.github/workflows` directory.
- Any new makefiles have been commited to the `./make` directory or a remote git repository containing shared makefiles.
- Solution has been documented in markdown files within the `./docs` directory of the repository root on the branch to be merged.
- Git commit messages reference an issue ID by hashtag on the branch to be merged.
- The final commit message on the branch to be merged will result in gerneration of [CHANGELOG](https://github.com/repo-racers/repo-racers/blob/main/CHANGELOG.md) entries by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator) eg:
  - adr: *"commit message goes here"* (#*"issue number goes here"*)
  - devops: *"commit message goes here"* (#*"issue number goes here"*)
  - document: *"commit message goes here"* (#*"issue number goes here"*)
  - feature: *"commit message goes here"* (#*"issue number goes here"*)
  - fix: *"commit message goes here"* (#*"issue number goes here"*)
  - performance: *"commit message goes here"* (#*"issue number goes here"*)
  - refactor: *"commit message goes here"* (#*"issue number goes here"*)
  - test: *"commit message goes here"* (#*"issue number goes here"*)

- CICD pipeline for the branch to be merged exists. has been peer reviewed, executes all tests, and has status `passed`.
- Pull request has a clearly defined description and refers to one or many issue IDs.

## Release Level

The DoD at the release level encompasses a broader scope, verifying that a collection of features and fixes assembled for a release meet our criteria for functionality, performance, security, and user experience. This ensures that our product increments deliver value and adhere to our high standards of quality and reliability.

[GitHub Documentation](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository)

- Scope complete as described in the work item's [Definition of Ready](./definition_of_ready.md).
- Application architecture complies with the [12 Factor App Checklist](./12_factor_app_checklist.md).
- Infrastructure architecture complies with the [Azure Deployment Checklist](./azure_deployment_checklist.md).
- Full spectrum automated tests pass *"consistently"* without failure for entire code base.
- Technical and user documentation are localized and HTML documentation has been generated.
- Consumers of APIs have been notified of any incompatible API changes.
- Repository has been tagged in accordance with the rules of [Semantic Versioning 2.0.0](https://semver.org/#semantic-versioning-200).
- Release notes have been written, localized, and associated with the repository tag.
- [CHANGELOG](https://github.com/repo-racers/repo-racers/blob/main/CHANGELOG.md) has been generated from code commits within the repository, peer reviewed and any additional release notes included.
- GitHub 'Release' has been given a descriptive and self-explanatory title.
- GitHub 'Release' has been associated with a project milestone (if appropriate).
- Asset links to any built binaries, or other related materials have been included in the GitHub 'Release'.
