---
title: "Notion 칸반 자동화 테스트"
type: summary
axis: history
tags: [history/uwo]
created: 2026-04-11
updated: 2026-04-11
status: draft
publish: false
---

# Notion 칸반 자동화 테스트

`raw/uwo/test_notion_card.md` 파일을 통해 Notion 칸반 자동화 파이프라인이 정상 동작하는지 확인하기 위한 테스트 기록.

## 파이프라인 개요

- `raw/` 폴더에 새 `.md` 파일 저장 → `watch_raw.sh` 감지 → `notion_card.py` 실행
- "시작 안 함" 컬럼에 카드 자동 생성

관련: [[moc]]
