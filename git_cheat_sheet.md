# Git Cheat Sheet 🚀

A comprehensive reference for Git commands and workflows.

## 📋 Table of Contents
- [Basic Setup](#basic-setup)
- [Repository Management](#repository-management)
- [Basic Workflow](#basic-workflow)
- [Branching](#branching)
- [Remote Repositories](#remote-repositories)
- [Viewing History](#viewing-history)
- [Undoing Changes](#undoing-changes)
- [Advanced Commands](#advanced-commands)
- [Common Workflows](#common-workflows)

---

## 🛠️ Basic Setup

### First-time Git setup
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

### Check your configuration
```bash
git config --list                    # View all settings
git config user.name                 # View specific setting
```

---

## 📁 Repository Management

### Initialize a new repository
```bash
git init                            # Create new Git repo in current folder
git init project-name               # Create new folder and Git repo
```

### Clone existing repository
```bash
git clone https://github.com/user/repo.git           # Clone via HTTPS
git clone https://github.com/user/repo.git my-folder # Clone to specific folder
git clone git@github.com:user/repo.git               # Clone via SSH
```

---

## 🔄 Basic Workflow

### Check repository status
```bash
git status                          # Show working directory status
git status -s                       # Short status format
```

### Add files to staging area
```bash
git add filename.txt                # Add specific file
git add .                          # Add all files in current directory
git add *.js                       # Add all JavaScript files
git add -A                         # Add all files (including deleted)
```

### Commit changes
```bash
git commit -m "Your commit message"  # Commit with message
git commit -am "Message"            # Add and commit tracked files
git commit --amend                  # Modify last commit
git commit --amend -m "New message" # Change last commit message
```

### View differences
```bash
git diff                           # Show unstaged changes
git diff --staged                  # Show staged changes
git diff filename.txt              # Show changes in specific file
```

---

## 🌿 Branching

### Branch management
```bash
git branch                         # List local branches
git branch -a                      # List all branches (local + remote)
git branch new-feature             # Create new branch
git branch -d branch-name          # Delete branch (safe)
git branch -D branch-name          # Force delete branch
git branch -m old-name new-name    # Rename branch
```

### Switch branches
```bash
git checkout branch-name           # Switch to existing branch
git checkout -b new-branch         # Create and switch to new branch
git switch branch-name             # Modern way to switch branches
git switch -c new-branch           # Create and switch (modern syntax)
```

### Merge branches
```bash
git merge branch-name              # Merge branch into current branch
git merge --no-ff branch-name      # Merge with merge commit
git merge --squash branch-name     # Squash merge
```

---

## 🌐 Remote Repositories

### Remote management
```bash
git remote                         # List remotes
git remote -v                      # List remotes with URLs
git remote add origin https://github.com/user/repo.git  # Add remote
git remote remove origin           # Remove remote
git remote rename origin upstream   # Rename remote
```

### Push and pull
```bash
git push                           # Push to default remote/branch
git push origin main               # Push to specific remote/branch
git push -u origin main            # Push and set upstream
git push --all                     # Push all branches
git push --tags                    # Push all tags

git pull                           # Fetch and merge from default remote
git pull origin main               # Pull from specific remote/branch
git pull --rebase                  # Pull with rebase instead of merge
```

### Fetch updates
```bash
git fetch                          # Download changes (don't merge)
git fetch origin                   # Fetch from specific remote
git fetch --all                    # Fetch from all remotes
```

---

## 📜 Viewing History

### View commits
```bash
git log                            # Show commit history
git log --oneline                  # Compact one-line format
git log --graph                    # Show branch graph
git log --oneline --graph --all    # Pretty graph of all branches
git log -5                         # Show last 5 commits
git log --author="John Doe"        # Filter by author
git log --since="2 weeks ago"      # Filter by date
git log filename.txt               # Show commits for specific file
```

### Show specific commit
```bash
git show                           # Show last commit details
git show commit-hash               # Show specific commit
git show HEAD~2                    # Show commit 2 steps back
```

---

## ↩️ Undoing Changes

### Unstage files
```bash
git reset filename.txt             # Unstage specific file
git reset                          # Unstage all files
```

### Discard changes
```bash
git checkout -- filename.txt      # Discard changes in file
git checkout .                     # Discard all unstaged changes
git restore filename.txt           # Modern way to discard changes
git restore .                      # Restore all files
```

### Reset commits
```bash
git reset --soft HEAD~1            # Undo last commit, keep changes staged
git reset HEAD~1                   # Undo last commit, keep changes unstaged
git reset --hard HEAD~1            # Undo last commit, discard changes
git reset --hard origin/main       # Reset to match remote branch
```

### Revert commits
```bash
git revert commit-hash             # Create new commit that undoes changes
git revert HEAD                    # Revert last commit
git revert HEAD~2..HEAD            # Revert last 2 commits
```

---

## 🔧 Advanced Commands

### Stash changes
```bash
git stash                          # Stash current changes
git stash save "Work in progress"  # Stash with message
git stash list                     # List all stashes
git stash apply                    # Apply last stash
git stash apply stash@{2}          # Apply specific stash
git stash drop                     # Delete last stash
git stash pop                      # Apply and delete last stash
git stash clear                    # Delete all stashes
```

### Tags
```bash
git tag                            # List tags
git tag v1.0.0                     # Create lightweight tag
git tag -a v1.0.0 -m "Version 1.0" # Create annotated tag
git push origin v1.0.0             # Push specific tag
git push origin --tags             # Push all tags
git tag -d v1.0.0                  # Delete local tag
```

### Cherry-pick
```bash
git cherry-pick commit-hash        # Apply specific commit to current branch
git cherry-pick branch-name        # Apply latest commit from branch
```

### Rebase
```bash
git rebase main                    # Rebase current branch onto main
git rebase -i HEAD~3               # Interactive rebase last 3 commits
git rebase --continue              # Continue rebase after resolving conflicts
git rebase --abort                 # Cancel rebase
```

---

## 🔥 Common Workflows

### New Project Setup
```bash
mkdir my-project
cd my-project
git init
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit"
git remote add origin https://github.com/user/my-project.git
git push -u origin main
```

### Feature Branch Workflow
```bash
git checkout main                  # Start from main branch
git pull                          # Get latest changes
git checkout -b feature/new-login  # Create feature branch
# ... make changes ...
git add .
git commit -m "Add new login feature"
git push -u origin feature/new-login
# ... create pull request ...
git checkout main                  # Switch back to main
git pull                          # Get merged changes
git branch -d feature/new-login   # Delete local feature branch
```

### Fix Merge Conflicts
```bash
git merge branch-name              # Attempt merge
# ... conflicts occur ...
git status                         # See conflicted files
# ... edit files to resolve conflicts ...
git add .                         # Stage resolved files
git commit                        # Complete merge
```

### Emergency Hotfix
```bash
git checkout main
git pull
git checkout -b hotfix/critical-bug
# ... make fix ...
git add .
git commit -m "Fix critical bug"
git push -u origin hotfix/critical-bug
# ... merge to main immediately ...
```

---

## ⚠️ Important Notes

### Safe Practices
- **Always** `git pull` before starting new work
- **Never** force push to shared branches: `git push --force`
- **Always** create branches for new features
- **Write** clear, descriptive commit messages
- **Review** changes before committing: `git diff --staged`

### PowerShell vs Bash
Most commands work the same, but some differences:
```powershell
# PowerShell (Windows)
git log --oneline | Select-Object -First 5

# Bash (Linux/Mac)
git log --oneline | head -5
```

### Useful Aliases
Add to your Git config for shortcuts:
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'
```

---

## 🆘 Emergency Commands

### "I messed up" scenarios
```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Completely undo last commit
git reset --hard HEAD~1

# I committed to wrong branch
git reset --soft HEAD~1    # Undo commit
git stash                  # Save changes
git checkout correct-branch
git stash pop              # Apply changes

# I want to go back to how remote looks
git fetch origin
git reset --hard origin/main

# I accidentally deleted a file
git checkout HEAD -- filename.txt
```

Remember: Git is very forgiving - most mistakes can be undone! 🙂
