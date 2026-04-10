#!/bin/bash
VAULT="$HOME/obsidian-vaults/wiki"
HANDLER="$VAULT/scripts/ingest_handler.sh"
LOG="$VAULT/ingest.log"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Watcher started. Monitoring: $VAULT/raw/" >> "$LOG"

fswatch -0 \
  --event Created \
  --event Updated \
  --latency 3 \
  "$VAULT/raw/" \
| xargs -0 -I {} bash "$HANDLER" "{}"
