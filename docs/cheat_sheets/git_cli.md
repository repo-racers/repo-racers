# Git CLI

## Configuring Git

### Set up your user name and email address

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

### List all Git configuration settings

```bash
git config --list
```

## Creating and Cloning Repositories

### Initialize a new Git repository

```bash
git init
```

### Clone an existing repository

```bash
git clone https://github.com/username/repo-name.git
```

## Basic snapshotting

### Check the status of your files

```bash
git status
```

### Add a file to the staging area

```bash
git add filename
```

### Add all changed files to the staging area

```bash
git add .
```

### Commit changes in the staging area

```bash
git commit -m "Commit message"
```

### Remove file from the working directory and staging area

```bash
git rm filename
```

### Rename or move a file or directory

```bash
git mv old-name new-name
```

## Branching and Merging

### List all branches

```bash
git branch
```

### Create a new branch

```bash
git branch branch-name
```

### Switch to a different branch

```bash
git checkout branch-name
```

### Create a new branch and switch to it

```bash
git checkout -b new-branch-name
```

### Merge a branch into your current branch

```bash
git merge branch-name
```

### Delete a branch

```bash
git branch -d branch-name
```

## Sharing and updating projects

### Add a remote repository

```bash
git remote add origin https://github.com/username/repo-name.git
```

### View information about the remote repository

```bash
git remote -v
```

### Fetch changes from the remote repository

```bash
git fetch origin
```

### Pull changes from the remote repository

```bash
git pull origin branch-name
```

### Push changes to the remote repository

```bash
git push origin branch-name
```

## Inspection and comparison

### View commit history

```bash
git log
```

### View changes

```bash
git diff
```

### Show changes between two branches

```bash
git diff branch-one branch-two
```

### Show metadata and content changes of the specified commit

```bash
git show commit-id
```

## Stashing and cleaning

### Stash changes in a dirty working directory

```bash
git stash
```

### Apply stashed changes back to your working directory

```bash
git stash apply
```

### List all stashed changesets

```bash
git stash list
```

### Clear your working directory by removing untracked files

```bash
git clean -n  # Dry run to show which files will be removed
git clean -f  # Force the removal of untracked files
```

## Tagging

### List all tags

```bash
git tag
```

### Create a new tag

```bash
git tag -a tag-name -m "Tag message"
```

### Show the commit that was tagged

```bash
git show tag-name
```

### Delete a tag

```bash
git tag -d tag-name
```
