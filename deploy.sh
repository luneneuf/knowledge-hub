#!/bin/bash
set -e

rsync -av --delete \
  --exclude='.git' --exclude='.obsidian' --exclude='raw' \
  ~/obsidian-vaults/wiki/ ~/quartz/content/

cd ~/quartz
git add -A

if git diff --cached --quiet; then
  echo "No changes to commit. Skipping commit and push."
else
  git commit -m "content: $(date '+%Y-%m-%d %H:%M')"
  git push
  echo "Pushed to GitHub. Vercel auto-deploy triggered."
fi
