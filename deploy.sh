#!/bin/bash
set -e

rsync -av --delete \
  --exclude='.git' --exclude='.obsidian' --exclude='raw' \
  ~/obsidian-vaults/wiki/ ~/quartz/content/

cd ~/quartz
git add -A
git commit -m "content: $(date '+%Y-%m-%d %H:%M')"
git push
