"""코스메틱 뉴스 → Slack 게시 봇.

GitHub Actions 워크플로가 호출. 동작:
1. ./seen_links.json 로드 (워크플로가 state 브랜치에서 미리 가져옴, 없으면 빈 배열)
2. sources.json의 RSS 폴링
3. 신규 링크만 Slack 게시 (링크 1줄 — Slack OG unfurl이 카드 렌더)
4. seen_links.json 갱신 (워크플로가 state 브랜치로 force-push)

부트스트랩 보호: seen이 비어있으면 모든 항목을 seen에 기록만 하고 게시 0건
(시작 알림 1건만). 다음 실행부터 신규만.
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import feedparser
import requests

SOURCES_PATH = Path(__file__).parent / "sources.json"
STATE_PATH = Path("seen_links.json")  # cwd (workflow가 미리 배치)
WEBHOOK = os.environ.get("SLACK_WEBHOOK_URL", "").strip()
USER_AGENT = "cosmetic-news-bot/1.0 (+https://github.com/luneneuf/knowledge-hub)"
MAX_PER_RUN = 20            # Slack rate limit·노이즈 보호
SEEN_CAP = 10000            # state 파일 크기 폭주 방지
SLACK_GAP_SEC = 1.2         # Incoming Webhook 분당 ~1건 권장 → 여유 있게


def load_seen() -> set[str]:
    if not STATE_PATH.exists():
        return set()
    try:
        return set(json.loads(STATE_PATH.read_text(encoding="utf-8")))
    except Exception as e:
        print(f"[WARN] state file unreadable, treating as empty: {e}", file=sys.stderr)
        return set()


def save_seen(seen: set[str]) -> None:
    arr = list(seen)
    if len(arr) > SEEN_CAP:
        arr = arr[-SEEN_CAP:]
    STATE_PATH.write_text(json.dumps(arr, ensure_ascii=False), encoding="utf-8")


def fetch_source(src: dict) -> list[dict]:
    headers = {"User-Agent": USER_AGENT}
    r = requests.get(src["url"], headers=headers, timeout=20)
    r.raise_for_status()
    parsed = feedparser.parse(r.content)
    items: list[dict] = []
    for e in parsed.entries:
        link = e.get("link")
        title = e.get("title")
        if not link or not title:
            continue
        items.append({"title": title, "link": link, "source": src["id"]})
    return items


def post_text(text: str) -> bool:
    r = requests.post(WEBHOOK, json={"text": text}, timeout=10)
    if r.status_code != 200:
        print(f"[WARN] slack post failed: {r.status_code} {r.text[:200]}", file=sys.stderr)
        return False
    return True


def main() -> int:
    if not WEBHOOK:
        print("ERROR: SLACK_WEBHOOK_URL not set", file=sys.stderr)
        return 1

    sources = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    seen = load_seen()
    is_bootstrap = len(seen) == 0

    new_items: list[dict] = []
    for src in sources:
        if not src.get("enabled", True):
            continue
        try:
            items = fetch_source(src)
        except Exception as ex:
            print(f"[WARN] source {src['id']} failed: {ex}", file=sys.stderr)
            continue
        for it in items:
            if it["link"] in seen:
                continue
            new_items.append(it)
            seen.add(it["link"])

    if is_bootstrap:
        post_text(
            f":robot_face: cosmetic-news-bot 시작 — {len(new_items)}개 기존 항목 부트스트랩 완료. "
            f"다음 실행부터 신규 항목만 게시합니다."
        )
        save_seen(seen)
        print(f"bootstrap: seeded {len(new_items)} items", file=sys.stderr)
        return 0

    to_post = new_items[:MAX_PER_RUN]
    overflow = len(new_items) - len(to_post)

    posted = 0
    for it in to_post:
        if post_text(it["link"]):
            posted += 1
        time.sleep(SLACK_GAP_SEC)

    if overflow > 0:
        post_text(f"_(+{overflow}개 항목은 다음 실행에서 게시)_")

    save_seen(seen)
    print(f"new={len(new_items)} posted={posted} overflow={overflow}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
