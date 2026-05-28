# Git Coordination Notes for Two Computers

## Overview

This note summarizes a Git/GitHub coordination issue between two computers working on the same project repository:

```text
automate_study_hub3e22
```

The main problem was that the iMac and MacBook Pro were not showing the same Git state. One computer had work on a feature branch, while the other computer was still on the `main` branch.

---

## Situation Observed

### On the iMac

The iMac was on the feature branch:

```bash
add-topic-stats
```

A new commit had been created:

```bash
Add chapter topic statistics script
```

The branch also showed a local change in:

```text
tools/web_scraping/README.md
```

This means the iMac had newer feature work that needed to be pushed to GitHub.

---

### On the MacBook Pro

The MacBook Pro was on:

```bash
main
```

It did not yet have the newest `add-topic-stats` branch work from the iMac.

The MacBook Pro also showed edits in `README.md`, so those local changes needed to be protected before switching branches or pulling from GitHub.

---

## Key Git Concept

GitHub only coordinates work that has been:

```text
saved → committed → pushed
```

Local unsaved or uncommitted changes on one computer do not automatically appear on the other computer.

The normal workflow should be:

```bash
git status
git pull --ff-only
# make changes
git add .
git commit -m "Clear message"
git push
```

---

## Recommended Workflow for the iMac

Check the current Git status:

```bash
git status
```

If the README change belongs to the current feature, commit it:

```bash
git add tools/web_scraping/README.md
git commit -m "Update README for topic stats feature"
```

Push the feature branch to GitHub:

```bash
git push -u origin add-topic-stats
```

In VS Code or GitLens, this corresponds to:

```text
Push
```

If VS Code asks to publish the branch, choose:

```text
Publish Branch
```

---

## Recommended Workflow for the MacBook Pro

First check the current status:

```bash
git status
```

If there are local README changes that should be kept but not committed yet, stash them:

```bash
git stash push -m "MacBook README changes before syncing"
```

In VS Code or GitLens, this corresponds to:

```text
Stash → Stash
```

Then fetch the newest information from GitHub:

```bash
git fetch --all --prune
```

In VS Code or GitLens, this corresponds to:

```text
Fetch
```

Then switch to the feature branch:

```bash
git switch add-topic-stats
```

If the local branch does not exist yet, create it from the remote branch:

```bash
git switch -c add-topic-stats --track origin/add-topic-stats
```

In VS Code or GitLens, this corresponds to:

```text
Checkout to...
```

Then choose:

```text
origin/add-topic-stats
```

---

## VS Code / GitLens Menu Reference

| VS Code / GitLens item | Similar Git command                     | Purpose                                                                |
| ---------------------- | --------------------------------------- | ---------------------------------------------------------------------- |
| Pull                   | `git pull`                              | Download and merge remote changes into the current branch              |
| Push                   | `git push`                              | Upload local commits to GitHub                                         |
| Fetch                  | `git fetch --all --prune`               | Check GitHub for new commits and branches without changing local files |
| Checkout to...         | `git switch <branch>`                   | Switch to another branch                                               |
| Commit                 | `git commit`                            | Save staged changes into Git history                                   |
| Changes                | `git status`, `git add`                 | View, stage, discard, or compare changed files                         |
| Pull, Push             | Pull/push variations                    | Combined sync actions                                                  |
| Branch                 | `git branch`, `git switch`, `git merge` | Manage branches                                                        |
| Remote                 | `git remote`                            | Manage remote repositories                                             |
| Stash                  | `git stash`                             | Temporarily save local changes                                         |
| Show Git Output        | Git command log                         | See exact Git commands and errors                                      |

---

## Important Warning About Pull

The VS Code menu item:

```text
Pull
```

usually runs:

```bash
git pull
```

This may create a merge commit if local and remote history have diverged.

For safer two-computer work, use:

```bash
git pull --ff-only
```

This command only updates the branch if Git can do so cleanly.

A useful global setting is:

```bash
git config --global pull.ff only
```

After this setting, normal pull operations become safer because Git refuses automatic messy merges.

---

## Practice Recommendation

It is a good idea to create a separate small Git practice repository before experimenting on the real project.

Example:

```bash
mkdir git_practice_lab
cd git_practice_lab
git init
echo "# Git Practice Lab" > README.md
git add README.md
git commit -m "Initial commit"
```

Then create a GitHub repository and connect it:

```bash
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

A good practice setup is:

```text
GitHub repository
├── iMac clone
└── MacBook Pro clone
```

Then practice:

```bash
# Computer A
git pull --ff-only
# edit file
git add .
git commit -m "Edit from computer A"
git push

# Computer B
git pull --ff-only
# edit file
git add .
git commit -m "Edit from computer B"
git push
```

---

## Core Git Commands to Learn First

Focus on these commands before studying more advanced Git:

```bash
git status
git add
git commit
git log --oneline
git branch
git switch
git fetch
git pull --ff-only
git push
git stash
```

---

## Daily Two-Computer Rule

Before starting work on either computer:

```bash
git status
git pull --ff-only
```

After finishing work:

```bash
git add .
git commit -m "Clear message"
git push
```

This habit helps keep the iMac, MacBook Pro, and GitHub coordinated.

---

## Next Step

Push the `add-topic-stats` branch from the iMac first. Then fetch and check out the same branch on the MacBook Pro.
