---
name: Google Drive 세션 동기화
description: ~/.claude/projects가 Google Drive로 심링크되어 모든 Claude 세션이 자동 백업됨
type: project
originSessionId: 8d84ee16-5027-4991-86ba-601d71c51a58
---
`~/.claude/projects` → `/Users/chunsb/Library/CloudStorage/GoogleDrive-chun.sb@reperire.co.kr/내 드라이브/claude-sessions` 심링크 연결 (2026-05-14 설정).

모든 Claude 세션 기록이 Google Drive에 자동 저장된다.

**Why:** 맥과 윈도우 노트북 간 세션 공유. 윈도우에서는 Google Drive 설치 후 `C:\Users\[이름]\.claude\projects`를 같은 Drive 폴더로 junction 연결하면 됨.

**How to apply:** 세션 데이터는 별도로 백업할 필요 없음. memory 파일만 레포(.claude/memory/)에도 커밋해두면 git + Drive 이중 백업.
