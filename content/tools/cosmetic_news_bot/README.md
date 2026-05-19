# cosmetic_news_bot — 코스메틱 산업 뉴스 Slack 봇

기획서: [[cosmetic_news_bot_기획서]] (`wiki/industry/LAKA/cosmetic_news_bot_기획서.md`)

## 동작

- **트리거**: GitHub Actions cron `7,22,37,52 0-8 * * 1-5` (UTC) = 평일 09:07-17:52 KST 15분 간격 (비정시 — GitHub schedule skip 회피)
- **출처**: 5개 RSS (`sources.json`) — 코스인코리아 / 코스모닝 / 뷰티누리 / Google News KR `화장품` / Google News EN `K-beauty`
- **게시**: Slack `#cosmetic-news` (reperire 워크스페이스) — 링크 1줄만 (Slack OG unfurl이 카드 렌더)
- **상태**: **GitHub Actions Cache** (`cosmetic-news-bot-seen-*` 키). 매 실행마다 새 unique key로 save, restore-keys prefix로 가장 최근 cache fallback. branch push 없음 — Vercel 등 외부 CI 트리거 0.

## 파일

```
content/tools/cosmetic_news_bot/
├── README.md              (이 파일)
├── sources.json           # RSS 출처 정의
├── requirements.txt       # feedparser + requests
└── collect_and_post.py    # 본체

.github/workflows/
└── cosmetic-news-bot.yml  # GitHub Actions 워크플로
```

## 시크릿

- GitHub Repository Secret: **`SLACK_WEBHOOK_URL`**
- 발급: Slack App → Incoming Webhooks → `#cosmetic-news` 채널 선택
- 등록: https://github.com/luneneuf/knowledge-hub/settings/secrets/actions

## 부트스트랩

첫 실행(Actions Cache 없음 → `seen_links.json` 빈 배열) 시 모든 RSS 항목이 신규로 보여 폭주 위험. 자동 보호:

1. seen이 비어있으면 → 모든 발견 항목을 seen에 기록만, Slack 게시 0건
2. 시작 알림 1건만 게시 (`:robot_face: cosmetic-news-bot 시작 — N개 …`)
3. 다음 실행부터 신규 항목만 게시

cache TTL은 7일이지만 매 15분마다 access되므로 사실상 무한 보존.

## Rate limit·노이즈 보호

- `MAX_PER_RUN = 20` — 1회 실행 시 최대 20건 게시. 초과는 다음 실행으로 이월.
- `SLACK_GAP_SEC = 1.2` — 메시지 간 1.2초 sleep (Webhook 분당 ~1건 권장 안전)
- 신규 50건 폭주 시: 20건 게시 + "+30개 다음 실행으로" 1건 추가

## 로컬 테스트

```powershell
$env:SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/..."
cd C:\Users\laka\knowledge-hub\content\tools\cosmetic_news_bot
pip install -r requirements.txt
python collect_and_post.py
```

→ 같은 폴더에 `seen_links.json` 생성됨. 한 번 실행하면 부트스트랩, 두 번째 실행부터 정상 게시.

## 수동 실행 (Actions)

GitHub Actions 페이지 → `cosmetic-news-bot` 워크플로 → "Run workflow" (workflow_dispatch).

## 운영 한도

| 항목 | 값 |
|------|---|
| 일 실행 수 | 36회 (KST 09:00-17:45 매 15분) |
| 월 실행 수 | ~792회 (평일 22일 기준) |
| Actions 분 소비 | ~792분 / 2000분 무료 한도 |
| Slack 비용 | 0원 |

## 출처 추가·비활성화

`sources.json`의 `enabled: false`로 비활성화. 신규 추가는 같은 스키마로 entry 추가 후 commit.

## 관련 도구

- [`tools/safety_signals/`](../safety_signals/) — 안전·회수 전용 자매 도구 (PowerShell, 일 1회 배치). 출처·로직 일부 공유하지만 별도 운영.
