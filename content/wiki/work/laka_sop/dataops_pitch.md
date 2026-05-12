---
title: "LAKA S&OP × DataOps — 영입 피치 (Genspark / PPT for Claude 입력용)"
type: log
axis: work
tags: [work/sop, work/recruiting, laka, dataops, pitch]
created: 2026-05-12
updated: 2026-05-12
status: draft
publish: false
---

# LAKA S&OP × DataOps — 앞으로 이런 일을 하게 됩니다

> **사용 안내** — 이 문서는 Genspark / PPT for Claude 등 슬라이드 자동 생성 도구에 입력하기 위한 원고입니다. 각 `##` 헤딩이 슬라이드 1장에 대응하도록 구성되어 있습니다.
>
> **분량 가정**: 약 8장 (S&OP 30초 + 책임 6 카테고리 + 로드맵).
>
> **연관 페이지**: [[sop_overview]] · [[laka_sop_v1]]

---

## 1. S&OP가 뭔지 30초

> "매월 1회 임원이 모여 **product family 단위**로 **15~36개월** **demand·supply를 units + 달러로** 균형 맞추는 의사결정 프로세스" — Wallace

**5-step 월간 사이클**:

```
Day 1-3   Step 1: Data Gathering        ← DataOps의 매월 1차 출력
Day 3-7   Step 2: Demand Planning       ← DataOps가 baseline forecast 제공
Day 4-10  Step 3: Supply Planning       ← DataOps가 ODM 슬롯·capacity 결합
Day 13    Step 4: Pre-Meeting (Heavy Lifting)
Day 15    Step 5: Executive Meeting     ← DataOps의 1페이지 임원 대시보드
```

**참석**: CEO + 마케팅·글로벌사업·SCM·프로덕트 본부장 + CFO (6명). CEO는 월 **1.5시간**만 commit.

---

## 2. DataOps 책임 카테고리 1 — 데이터 인제스트 파이프라인

**무엇을**: 매월 Day 1-3 "Data Gathering" 단계의 모든 raw input을 자동 수집·정합화.

**소스 후보**:

| 소스 | 종류 | 비고 |
|------|------|------|
| 자사 ERP | sell-in, 출하, 재고 | 한국·일본·미국 법인별 |
| 세포라 retailer portal | sell-out, POS | 미국 80매장 |
| 부츠 EDI | 발주, sell-out | 영국 91매장 |
| Qoo10 일본 | 채널 sell-out | 株式会社JT 경유 |
| 한국 온라인 (자사몰, 올리브영, 쿠팡 등) | sell-out | 매체별 API/리포트 |
| 한국콜마·코스맥스 | 슬롯·생산·QA 결과 | 현재 사람이 엑셀로 수신 |
| 재무 시스템 | 매출·원가·환율 | 분기 → 월간으로 |

**산출**: 단일 원시 데이터 레이크 + 정제된 fact 테이블 + 매월 SLA(예: Day 2 EOD까지 완성).

---

## 3. DataOps 책임 카테고리 2 — 마스터 데이터·거버넌스

**무엇을**: "**one set of numbers**" 원칙을 깨뜨리지 않는 단일 source of truth 구축.

**핵심 마스터**:

- **Family ↔ SKU 매핑**: Volume 단위(컬러군·카테고리) ↔ Mix 단위(SKU·컬러). 신컬러 launch 시 즉시 등록
- **채널 코드**: CH-US-SEPH, CH-UK-BOOTS, CH-JP-Q10, CH-KR-OL 등
- **ODM 코드**: 공급사·라인·MOQ·리드타임
- **환율 시나리오**: 기본·낙관·비관 3종
- **컬러 변형**: 채널별 라벨 변형 SKU 통합 관리

**거버넌스**:
- 변경 감사 로그 (누가·언제·왜)
- 마스터 변경 시 영향받는 family·채널·KPI 자동 알림
- 임원 회의 직후 결정사항이 마스터에 반영되는 워크플로

---

## 4. DataOps 책임 카테고리 3 — 수요 예측 엔진

**무엇을**: Step 1에 들어갈 통계적 기준 예측 (statistical baseline). 사람(BM/PM)이 override할 베이스라인을 자동 생산.

**예측 대상**:

| 카테고리 | 패턴 | 모델 후보 |
|----------|------|-----------|
| 베스트셀러 립글로스 컬러 | 시즌성·트렌드 | ARIMA/Prophet 베이스 + 채널별 가중치 |
| 신컬러 launch (NPI) | launch curve + 잠식률 | 유사 컬러 launch 곡선 매칭 |
| 글로벌 채널 한정 SKU | 신규·데이터 부족 | top-down (Volume에서 분배) |
| 시즌 한정 컬러 | 한정 기간·재고 소진 | 사람 override 비중 큼, baseline은 단순화 |

**FVA(Forecast Value Add)와의 연동**: 모델 예측 → BM 조정 → 글로벌사업 조정 → 임원 합의 각 단계마다 정확도를 측정해, "누가 forecast를 더 좋게/나쁘게 만들었나"를 정량화.

---

## 5. DataOps 책임 카테고리 4 — Planning 워크북·UI

**무엇을**: 임원·BM/PM이 매월 실제로 들여다볼 Planning workspace 자체를 0에서 설계·구축. Volume(family) view·Mix(SKU) view·신컬러 launch tracker·FVA 추적 — 매월 회의 흐름에 맞게 다 본인이 만든다.

**다뤄야 할 뷰 (예시)**:

| 뷰 | 내용 |
|----|------|
| Family 18개월 view | 수요·공급·재고·매출 (units + 달러), Wallace "Sally Smith Spreadsheet" 패턴 |
| NPI Tracker | 신컬러 launch curve, 채널별·시나리오별 잠식률 |
| FVA Tracking | Forecast layer별(통계·BM·글로벌·임원) 부가가치 |
| 임원 1페이지 | Step 5 Executive Meeting 표지 — 매월 갱신 |
| Operating view | BM/PM·SCM 운영 뷰 (drill-down 가능) |

**참고 자료** (시작점은 아님): 1차 자료 학습 단계에서 작성한 Excel 워크북 v0 — Wallace 워크샵의 Sally Smith Spreadsheet 패턴을 한국 K-뷰티 family 구조에 맞게 변환한 데모. 5시트·수식 51개. **본 자료는 워크북에 무엇이 들어가야 하는지 보여주는 참고용으로만 활용**, 새 담당자가 처음부터 다시 설계.

**진화 grain**:

```
Phase 1-2 (3개월) ─ MVP 워크북 v1 (스택 미정, DataOps가 결정)
Phase 3   (4개월) ─ 전 family 확장 + 임원 뷰·운영 뷰 분리
Phase 4   (2개월) ─ 재무 통합 + 시나리오 시뮬레이션 모듈
Phase 4+        ─ IBP(Integrated Business Planning) 확장
```

---

## 6. DataOps 책임 카테고리 5 — KPI·FVA 대시보드

**임원 1페이지 (매월 Executive Meeting 표지)**:

- Forecast Accuracy (family·채널별)
- Forecast Bias
- **FVA** — 각 forecast 레이어(통계·BM·글로벌·임원)의 부가가치
- OTD (On-Time Delivery)
- 재고 회전·재고 일수
- ODM 슬롯 이용률
- 신컬러 launch 90일 누적 vs plan
- 채널별 매출 actual vs plan (환율 영향 분리)

**거버넌스 뷰** (Process Owner·CEO 전용):
- 회의 결정사항 이행률
- Demand Time Fence 위반 건수
- 마스터 데이터 변경 빈도·승인자

→ 임원이 회의 자리에서 "왜 이 family forecast가 빗나갔는지" 1분 안에 drill-down 가능.

---

## 7. DataOps 책임 카테고리 6 — What-if 시나리오 엔진

**무엇을**: 임원 회의 중 즉석 시나리오 응답.

**예시 질의**:
- "환율이 1,400 → 1,300으로 가면 글로벌 채널 마진은?"
- "세포라 #207 모브에 30% 더 밀면 한국 재고는 언제 바닥?"
- "코스맥스가 한국콜마 슬롯의 30% 대체 가능하면 OTD는?"
- "신컬러 launch를 1개월 미루면 분기 매출 impact는?"

**기술 요구**:
- 시나리오 정의 DSL 또는 GUI
- 의존성 그래프 (family ↔ ODM ↔ 채널 ↔ 재무)
- 1-2분 내 응답 (회의 흐름 끊지 않게)

---

## 8. 8~12개월 로드맵 (Wallace 4-Phase)

```
[T+0]     ── Phase 1 — Executive Briefing ────────  60-90분
[T+1주]   ── Kickoff ─────────────────────────────  반나절
[T+1~3월] ── Phase 2 — Live Pilot (2 family) ────  90일
[T+3~7월] ── Phase 3 — Expansion ────────────────  4개월
[T+7~9월] ── Phase 4 — Financial Integration ───  2개월
```

**DataOps의 월별 grain**:

| 월 | Phase | DataOps deliverable |
|----|-------|---------------------|
| M1 | Phase 1 | 데이터 소스 인벤토리·SLA 합의·인프라 셋업·스택 결정 |
| M2-M4 | Phase 2 (Pilot) | 2 family × 3 채널 인제스트 파이프라인·baseline forecast·MVP Planning 워크북·임원 1페이지 v1 |
| M5-M8 | Phase 3 (Expansion) | 전 family로 확장·Planning 워크북 정식 버전·what-if 엔진 v1 |
| M9-M10 | Phase 4 | 재무 통합·시나리오 시뮬레이션·거버넌스 대시보드 |
| M11+ | Beyond | IBP·ML 예측 고도화·외부 데이터(트렌드·구글 트렌드 등) 통합 |

**Go/No-Go gate 2개**:
- Gate #1 (Phase 1 후): CEO Live Pilot 진행 동의
- Gate #2 (Phase 2 후): CEO Phase 3 Expansion 동의

---

*— 끝.*
