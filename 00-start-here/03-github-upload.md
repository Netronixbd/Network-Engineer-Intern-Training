# GitHub-এ Repository Upload (Windows / Linux)

## Option A: Browser upload
1. GitHub → **New repository** → name `network-engineer-intern-training-bangla` (or preferred) → Public/Private choose করো।
2. ZIP unzip করে **folder-এর ভিতরের সব files/folders** upload করো, enclosing folder নয়, যাতে `README.md` repository root-এ থাকে।
3. GitHub **Add file → Upload files** → files select (web UI-তে folder support/browser behavior vary)।
4. Commit changes. Confirm README image/diagrams and Bengali character rendered।

## Option B: Git CLI (recommended)
```bash
# unzip folder-এর root-এ terminal open
# Set identity (use YOUR GitHub account's identity, do not copy samples)
git config --global user.name "YOUR_NAME"
git config --global user.email "YOUR_VERIFIED_GITHUB_EMAIL"

git init
git add .
git commit -m "Initial Bengali network intern training guide"
git branch -M main
# First create an EMPTY repository on GitHub, then replace URL below
git remote add origin https://github.com/YOUR_USERNAME/network-engineer-intern-training-bangla.git
git push -u origin main
```

**If Git says `Author identity unknown`:** `git config --global user.name` and `.email` set করো। GitHub privacy চাইলে verified noreply email ব্যবহার করতে পারো।

**Windows CRLF warning:** `LF will be replaced by CRLF` often line-ending notice, usually fatal error নয়। Repository `.gitattributes` provides normalized text. Git Bash, PowerShell, Linux terminal-এ commands work (Git installed required)।

## Updating repo
```bash
git status
git add .
git commit -m "Add new intern labs"
git push
```

## Pre-upload checklist
- [ ] Secrets, SSH private keys, real customer details, access credentials absent
- [ ] `README.md` root visible
- [ ] Mermaid diagrams rendered in GitHub
- [ ] Markdown relative paths click correctly
- [ ] Lab code tested on intended virtual platform (examples are educational)
- [ ] Licensing and attribution reviewed

## Troubleshooting Git
- **remote origin already exists:** `git remote -v`, then if intentional `git remote set-url origin <YOUR_URL>`।
- **Push rejected:** `git status`, `git pull --rebase` only after reviewing the remote history; avoid forced push।
- **Authentication failed:** GitHub account authentication via supported credential manager/PAT/SSH; account password not pasted into terminal prompt meant for token।
- **README not displayed:** likely files one directory too deep; move README to repo root।
