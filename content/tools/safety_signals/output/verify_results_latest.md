# 안전관리 시그널 출처 검증 결과

> **실행 시각**: 2026-05-18
> **목적**: 수집 후보 출처의 실제 동작 여부 및 콘텐츠 품질 검증
> **방법**: PowerShell `Invoke-WebRequest` + `[xml]` 파싱 / `Invoke-RestMethod` JSON

---

## 검증 요약

| ID | Tier | 국가 | 결과 | 형식 | 비고 |
|----|------|------|------|------|------|
| **gnews_kr_recall** | A | KR | ✅ 64 items | RSS | LAKA 직접 관련성 매우 높음 |
| **gnews_kr_safety** | A | KR | ✅ 100 items | RSS | 노이즈 있음, 키워드 후필터 필요 |
| **gnews_en_recall** | B | US/INT | ✅ 100 items | RSS | MoCRA·글로벌 동향 |
| **gnews_en_fda_cos** | B | US | ✅ 71 items | RSS | FDA Warning Letter·MoCRA |
| **gnews_en_kbeauty** | B | INT | ✅ 58 items | RSS | K-뷰티 회수·UK·해외 동향 |
| **gnews_uk_opss** | B | UK | ✅ 55 items | RSS | OPSS·UK 안전 동향 |
| **uk_opss_atom** | B | UK | ✅ 20 items | Atom | 화장품 외 항목 많음, 필터 필요 |
| **uk_govuk_search** | B | UK | ✅ 10 items | JSON API | OPSS 발표문 정밀 검색 |
| **pubmed_eutils** | C | INT | ✅ 5 items | JSON (2-step) | 학술 — esearch+esummary |
| **kcia_notice_html** | A | KR | ⚠️ 스크래퍼 필요 | HTML | notice.php 구조 확인됨, 정적 파싱 가능 |
| **mfds_recall_html** | A | KR | ❌ 동적 로딩 | HTML | JS 렌더링이라 정적 스크래핑 불가, Google News 우회 권장 |
| **fda_direct_rss** | B | US | ❌ 404 다수 | — | FDA RSS 페이지 개편됨, Google News(`gnews_en_fda_cos`)로 대체 |
| **eu_safety_gate_rss** | B | EU | ❌ 404 | — | RAPEX 후신 시스템에서 공개 RSS 미제공, Google News 검토 또는 weekly alerts 페이지 스크래퍼 필요 |
| **japan_pmda_rss** | B | JP | ❌ URL 미확인 | — | 한국어 번역 부담도 있어 1단계 보류 |

→ **즉시 사용 가능**: 9개 RSS/API 자동 + 1개 HTML 스크래퍼 = **10개 자동 수집 소스 확보**

---

## 콘텐츠 품질 평가 (실제 샘플 기반)

### gnews_kr_recall (LAKA 관련성 ⭐⭐⭐)

5개 샘플 중 LAKA 직접 시그널 다수:

- 2026-02-19: 지난해 국내 화장품 회수·폐기 **3.2배 급증**, 식약처 화장품 관리체계 강화 영향
- 2026-02-09: 식약처, **'스칼렛레드' 색소 검출 화장품 회수** 조치 → 색소 안전성 이슈 ([[2026-02-W2_SCM주간업무보고]] 수단레드 사건과 동류)
- 2026-02-09: **발암 성분(스칼렛 레드) 함유 화장품 2종, 전량 회수·폐기 명령** → Tier A 즉시 알림 대상

### gnews_en_kbeauty (LAKA 관련성 ⭐⭐⭐)

- "K-beauty growth without guardrails? Rising recalls trigger tighter oversight" — 글로벌 규제 강화
- "Inside K-Beauty's Gateway to the UK - Vogue" — UK 시장 확대 (LAKA 부츠 진출과 직결)
- "Fake K-beauty surges overseas as global popularity soars" — 위조품 이슈

### gnews_en_fda_cos (LAKA 관련성 ⭐⭐⭐)

MoCRA 관련 보도 다수:
- 2026-05-01: "How MoCRA Is Reshaping FDA Oversight of Cosmetics in 2026"
- 2026-05-08: "FDA Issues Warning Letter to Wellness Platform IBeautyStore" — K-뷰티 입장에서 직접 시그널
- 2026-04-08: "Cosmetics Under the Microscope: FDA's Expanding Regulatory Reach Under MoCRA"

### gnews_kr_safety (관련성 ⭐⭐, 노이즈 ⭐⭐)

- 진성 시그널: "미국 화장품 MoCRA 규제 최신 업데이트: FDA, 화장품 부작용 사례 실시간 조회 플랫폼(FAERS) 공개"
- 노이즈: "같이 쓰면 '상극'인 화장품 성분", "당뇨병 부작용 치료성분 EGF..." 등 일반 건강 기사

→ **2단계에서 AI 키워드 필터로 노이즈 제거 필요**.

### uk_opss_atom (관련성 ⭐)

OPSS 전체 발행물이라 화장품 외 항목 다수:
- "Asbestos in consumer products"
- "Designated standards: recreational craft"
- "Product safety and legal metrology regulations"

→ 화장품 관련만 골라내려면 후처리 필터 필요. 또는 `gnews_uk_opss`로 대체.

### pubmed_eutils (관련성 ⭐⭐, 활용도 별도)

- "Analysis of mercury content in cosmetic products available on the Polish market" (2026-05-11)
- "Efficacy of an Instructional Module on Awareness of the Side Effects of Cosmetic Products"

→ 학술 시그널은 즉각 LAKA 영향 X, 장기 동향 모니터링용으로 가치.

---

## 기술 스택 권고 (검증 후 수정)

### 즉시 사용 가능 — 추가 설치 없이 PowerShell 5.1 + .NET XML 파싱

PowerShell `Invoke-WebRequest` + `[xml]` 캐스팅 + `ConvertFrom-Json`으로 위 9개 자동 소스 모두 처리 가능.

### Python 설치 필요 시점

PowerShell만으로 충분하나, 다음 경우 Python 도입 고려:
- 한국어 형태소 분석 후 키워드 정밀 필터 (KoNLPy 등)
- Claude API 호출로 자동 요약 (2단계)
- 대량 텍스트 정규화 처리
- KCIA 등 HTML 스크래핑 BeautifulSoup 사용

설치: `winget install Python.Python.3.12`

### MFDS 회수 공고 — 별도 대응

`nedrug.mfds.go.kr/pbp/CCBBJ01` 페이지는 JavaScript로 동적 렌더링 → 정적 fetch로 회수 항목 추출 불가. 대안:
1. **Google News `gnews_kr_recall`로 우회** — 언론 보도가 회수 공고를 즉시 인용 (1차 권고)
2. Playwright/Selenium 등 헤드리스 브라우저 사용 (오버엔지니어링)
3. 김건 책임이 nedrug 공고 페이지를 별도 즐겨찾기로 일일 수동 확인 (최종 보완)

---

## 다음 단계

1. 수집 스크립트 `collect.ps1` 작성 — 위 10개 소스를 한 번에 가져와 JSON·Markdown으로 저장
2. 출력 형식: 출처별 마지막 N개 항목 + 발행일 + 제목 + 링크
3. 정기 실행 — Windows 작업 스케줄러로 일 1회 실행 (Slack 연동은 2단계로 보류)
4. 결과 누적 폴더 (`output/daily/YYYYMMDD/`) 구조로 보관
