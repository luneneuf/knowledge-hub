#!/bin/bash
FILE="$1"
VAULT="$HOME/obsidian-vaults/wiki"
LOG="$VAULT/ingest.log"

[[ "$FILE" != *.md ]] && exit 0
[[ "$FILE" == */wiki/wiki/* ]] && exit 0

sleep 2
[[ ! -f "$FILE" ]] && exit 0

LOCK="/tmp/wiki_ingest.lock"
if [ -f "$LOCK" ]; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] SKIP (already running): $FILE" >> "$LOG"
  exit 0
fi
touch "$LOCK"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] START: $FILE" >> "$LOG"

cd "$VAULT"
claude --print "raw 폴더에 새 파일이 추가됐어: $FILE

CLAUDE.md 규칙에 따라 ingest 실행해줘. 완료 후 index.md와 log.md도 갱신해줘.

중요: 내용이 적거나 테스트 파일이어도 질문하지 말고 그냥 넘어가줘. 절대 질문하지 말고 판단해서 바로 처리해줘." >> "$LOG" 2>&1

EXIT_CODE=$?
echo "[$(date '+%Y-%m-%d %H:%M:%S')] DONE (exit $EXIT_CODE): $FILE" >> "$LOG"

rm -f "$LOCK"
