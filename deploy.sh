#!/bin/bash
set -e

# deploy.sh — quartz/content가 단일 소스
# Claude가 quartz/content를 직접 편집 → 이 스크립트 실행으로 Vercel 배포
# Obsidian은 ~/quartz/content/ 를 vault로 열면 됨

cd ~/quartz

git add -A

if git diff --cached --quiet; then
  echo "변경사항 없음. 배포 스킵."
else
  git commit -m "content: $(date '+%Y-%m-%d %H:%M')"
  git push
  echo "GitHub 푸시 완료. Vercel 자동 배포 트리거됨."
fi
