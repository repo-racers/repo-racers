![Margaret Hamilton](../assets/images/heroes/margaret_hamilton.webp)
<p align="right"><sub><a href="https://en.wikipedia.org/wiki/Margaret_Hamilton_(software_engineer)" target="_blank">Margaret Elaine Hamilton</a> (AI Generated Artwork)</sub></p>

# Contribution Guidelines

## Contributions to this repo are very welcome

All contributions accepted by the project crew will be released to the public under the project's open source license.

Please note that this project is released with a [Contributor Code of Conduct](../crew_contracts/code_of_conduct.md). By participating in this project you agree to abide by its terms.

For a great article with advice and inspiration regarding how to contribute to open source projects we recommend this [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).

## Step by step guide

### File a GitHub issue

Before starting any work, we recommend filing a GitHub [issue](https://github.com/repo-racers/repo-racers/issues) on the repo's [project board](https://github.com/orgs/repo-racers/projects/11). This is your chance to ask questions and
get feedback from the maintainers and the community before you sink a lot of time into writing (possibly the wrong)
code. If there is anything you're unsure about, just ask!

### Fork and clone this repo

Click on the 'Fork' button at the top right corner of the repository page. This will create a copy of the repository in your GitHub account.

### Make your changes

Perform the necessary edits, additions, or deletions to files in your local repository.

### Commit your changes

Commit your changes with a clear and descriptive [commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

### Push changes to your fork

Push the changes to your GitHub fork.

### Submit a Pull Request

On your fork's GitHub page, use the "Compare & pull request" button to submit your Pull Request.

### Tips for increasing the likelihood your Pull Request will be accepeted

- Adhere to any contribution guidelines provided by this project.
- Ensure your Pull Request title and description effectively communicate the purpose and content of your changes.
- Smaller, more focused Pull Requests are easier to review and more likely to be accepted.
- Match the coding style of this project, including naming conventions and documentation.
- Thoroughly test your changes to ensure they work correctly and do not introduce new issues.
- Be prepared to make adjustments based on feedback from the project maintainers.

## Crew contributions

We follow a fairly standard [pull request
process](https://docs.github.com/en/pull-requests) for contributions, subject to the following guidelines:

1. [File a GitHub issue](#file_a_github_issue)
1. [Create a development branch](#create_a_development_branch)
1. [Create a codespace](#create_a_codespace)
1. [Update the documentation](#update_the_documentation)
1. [Update the tests](#update_the_tests)
1. [Update the code](#update_the_code)
1. [Definition of Done](#definition_of_done)
1. [Create a pull request](#create_a_pull_request)
1. [Merge and release](#merge_and_release)
1. [Clean up development resources](#clean_up_development_resources)

### File a GitHub issue for peer review

File a GitHub [issue](https://github.com/repo-racers/repo-racers/issues) on the repo's [project board](https://github.com/orgs/repo-racers/projects/11).

### Create a development branch

After filing a GitHub issue, the next step is to [create a branch to work on your issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-a-branch-for-an-issue).
This branch will serve as the foundation for your work, enabling you to make changes without affecting the main branch.

Here's an example of the branch naming convention we use:

```plaintext
<user alias>/<branch type>/<work item ID>-<title>
```

Branch types can be one of the folllowing categories:

- adr
- devops
- document
- feature
- fix
- performance
- refactor
- test

Which could translate to something as follows:

```plaintext
devopskev/feature/271-make-all-the-things
```

### Create a codespace

After creating your development branch, the next step is to set up your development environment.
We recommend using [GitHub Codespaces](https://github.com/features/codespaces) for this, creating a new codespace specific to the development branch of th newly created issue.
Codespaces provides a fully configured development environment in the cloud, which you can use to develop and test your contributions.
This ensures that all contributors are working in a consistent environment, reducing the ["it works on my machine"](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/) problem.

### Update the documentation

We recommend updating the documentation *before* updating any code (see [Readme Driven
Development](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html)). This ensures the documentation
stays up to date and allows you to think through the problem at a high level before you get lost in the weeds of
coding.

### Update the tests

We also recommend updating the automated tests *before* updating any code (see [Test Driven
Development](https://en.wikipedia.org/wiki/Test-driven_development)). That means you add or update a test case,
verify that it's failing with a clear error message, and *then* make the code changes to get that test to pass. This
ensures the tests stay up to date and verify all the functionality in this repo, including whatever new
functionality you're adding in your contribution.

### Update the code

At this point, make your code changes and use your new test case to verify that everything is working. As you work,
please consider backwards compatibility.

#### Backwards compatibility

Please make every effort to avoid unnecessary backwards incompatible changes. If a backwards incompatible change cannot be avoided, please make sure to call that out when you submit a pull request, explaining why the change is absolutely necessary.

### Definition of Done

Before submitting a pull request, take the time to review our [Definition  of Done](../crew_contracts/definition_of_done.md).

Our definition of done describes the list of criteria that must be met before any work is considered 'done.' Failure to comply with any of these conditions means work is not complete and will probably result in your pull request being refused.

Upon receipt of a pull request, the maintainers of this repo will review code submitted against the [Definition  of Done](../crew_contracts/definition_of_done.md) before accepting that pull request into the codebase.

We describe our [Definition  of Done](../crew_contracts/definition_of_done.md) at two levels:

1. Merge Pull Request
1. Tag Release

### Create a pull request

[Create a pull request](https://docs.github.com/en/pull-requests) with your changes. Please make sure
to include the following:

1. A description of the change, including a link to your GitHub issue.
1. The output of your automated test run, preferably in a [GitHub Gist](https://docs.github.com/en/github/writing-on-github/editing-and-sharing-content-with-gists/creating-gists).
1. Any notes on backwards incompatibility.

### Merge and release

The maintainers for this repo will review your code and provide feedback. If everything looks good, they will merge the
code and release a new version, which you'll be able to find in the [releases page](https://github.com/repo-racers/repo-racers/releases).

### Clean up development resources

After your contribution has been successfully merged and released, it's important to clean up your development resources to keep the project repository and GitHub tidy.
This involves deleting your development branch and the GitHub Codespace you created for your work.

#### Delete the development branch

1. Navigate to the main page of the repository on GitHub.
2. Click on the "Branches" tab.
3. Find the branch you used for your contribution. There should be a delete button (trash can icon) next to it if the branch has been merged.
4. Click on the delete button to remove the branch.

You can also delete the branch directly from your local git repository using the following commands:

```sh
git branch -d <branch name> # Deletes the branch locally
git push origin --delete <branch name> # Deletes the branch on GitHub

```

#### Delete the codespace

1. Navigate to the "Codespaces" tab in your GitHub profile or repository page.
2. Find the codespace you created for your contribution.
3. Click on the three dots menu (More actions) next to the codespace you want to delete.
4. Select "Delete codespace" and confirm the deletion.
