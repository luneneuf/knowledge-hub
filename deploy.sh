#!/bin/bash
set -e

# Sync uwo vault wiki → content/uwo/
mkdir -p ~/quartz/content/uwo
rsync -av --delete \
  --exclude='.git' --exclude='.obsidian' \
  ~/obsidian-vaults/uwo/wiki/ ~/quartz/content/uwo/

# Sync business vault wiki → content/business/
mkdir -p ~/quartz/content/business
rsync -av --delete \
  --exclude='.git' --exclude='.obsidian' \
  ~/obsidian-vaults/business/wiki/ ~/quartz/content/business/

cd ~/quartz
git add -A

if git diff --cached --quiet; then
  echo "No changes to commit. Skipping commit and push."
else
  git commit -m "content: $(date '+%Y-%m-%d %H:%M')"
  git push
  echo "Pushed to GitHub. Vercel auto-deploy triggered."
fi
