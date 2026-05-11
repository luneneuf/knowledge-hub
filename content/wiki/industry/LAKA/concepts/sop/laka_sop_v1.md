---
title: "LAKA S&OP v1 — Live Pilot Playbook (시뮬레이션)"
type: concept
axis: work
tags: [work/sop, s&op, laka, live-pilot, playbook, master-scheduling-policy, executive-briefing, simulation]
created: 2026-05-11
updated: 2026-05-11
status: draft
publish: false
---

# LAKA S&OP v1 — Live Pilot Playbook

> ⚠️ **시뮬레이션 — 실제 적용 시 보정 필요**
>
> 본 페이지는 **실제 LAKA 임원진 인터뷰·현장 데이터 없이 추정 기반으로 작성된 시뮬레이션**입니다. Wallace ([[src_wallace_executive_guide_book|책]] p84) 경고: *"Build it and they will come은 낮은 성공 확률. Hold the high ground — 처음부터 top management 끌어들여라."* 실제 도입 시:
> - LAKA Executive Briefing이 선행되어야 함
> - 본 문서의 모든 가정 (Family·MOQ·환율·cadence)이 실제 데이터로 보정 필요
> - 거버넌스 매트릭스는 CEO·이사회 승인 후 효력
>
> **목적**: 5-step 전체 사이클을 끝까지 시뮬레이션해 W1~W6의 fact transfer를 운영 매뉴얼 형태로 정리. 빈 부분 식별 + W8 시뮬레이션 운영의 base.
>
> **연관 Linear 이슈**: [COM-26](https://linear.app/luneneuf) W7

---

## 0. 가정 명시

본 시뮬레이션의 LAKA 측 가정:

| 영역 | 가정 |
|------|------|
| **시작 시점** | 가상 — 2026년 7월 1일 Executive Briefing (Phase 1) |
| **CEO commitment** | 이지철 대표 Process Owner 동의 (월 1.5h commit) |
| **국내사업 본부장** | 임시로 CEO가 owner 역할 (현재 공석) |
| **Live Pilot Family** | F01 (립글로스 컬러군 A, 베스트셀러) + F08 (글로벌 전용 SKU) = **2개 family** |
| **Live Pilot Channel** | CH-US-SEPH (세포라 미국) + CH-JP-Q10 (Qoo10 일본) + CH-KR-OL (한국 온라인) = **3개 채널** |
| **Phase 2 기간** | 90일 = 3 monthly cycle |
| **ODM** | 한국콜마 (F01, F08의 50%) + 코스맥스 (F08 dual sourcing 일부) |
| **마스터 데이터** | [[data_gathering\|1.]] §3 6 영역 사전 정의 완료 가정 |
| **운영 도구** | 📎 [laka_sop_template_v0.xlsx](./laka_sop_template_v0.xlsx) (확장: family 1개 → 2개) |

---

## 1. Wallace 4-Phase Implementation Path — LAKA 적용

```
[T+0]      ─── Phase 1 — Executive Briefing ──────────────  60-90분
[T+1주]    ─── Kickoff Session ────────────────────────────  반나절
[T+1~3월]  ─── Phase 2 — Live Pilot (2 family × 3 cycle) ──  90일
[T+3~7월]  ─── Phase 3 — Expansion & Replication ────────  4개월
[T+7~9월]  ─── Phase 4 — Integration of Financials ───────  2개월
```

→ **총 8-12개월, <$100K** (Wallace 정량 가이드 [[sop_overview|W1]] §13).

**Go/No-Go gate 2개**:
- Gate #1 (Phase 1 후): CEO가 Live Pilot 진행 동의?
- Gate #2 (Phase 2 후): CEO가 Phase 3 Expansion 동의?

---

## 2. Phase 1 — Executive Briefing (60-90분)

### 2.1 참석자 (6 essential + 2 supporting)

| 역할 | 인물 | 사전 commitment |
|------|------|-----------------|
| **President / Process Owner** | 이지철 CEO | 월 1.5h commit 의향 |
| **VP Operations** | 김중찬 SCM 본부장 | Process Owner 직접 |
| **VP Marketing** | 안일홍 마케팅 본부장 | Demand 인풋 owner |
| **VP Sales (Global)** | 손여진 글로벌사업 본부장 | 글로벌 채널 인풋 |
| **VP Product Development** | 이정미 프로덕트 본부장 | NPI 인풋 |
| **VP Finance** | 이종영 CFO | 재무 통합 |
| (Supporting) Demand Manager 후보 | 마케팅 BM/PM 파트장 | 운영 owner |
| (Supporting) Process Owner 후보 | SCM SC기획팀장 | 운영 owner |

→ 국내사업 본부장 공석으로 CEO 임시 owner.

### 2.2 60분 Agenda

| Min | Section | Material |
|-----|----------|----------|
| 0-10 | LAKA가 왜 S&OP인가 — Designer/Distributor 매핑 | [[sop_overview\|W1]] §"왜 LAKA에 S&OP인가" |
| 10-20 | 핵심 프레임워크 — Volume/Mix, 4-tier 호라이즌, 5-step | [[sop_overview\|W1]] §3·4·5 |
| 20-30 | LAKA 현재 진단 — Stage 1-2, 18개월 목표 Stage 3 | [[sop_overview\|W1]] §10 |
| 30-40 | 위험 패턴 — Wallace 3 Impediments + Broken Process 7 신호 | [[sop_failure_patterns\|W6]] §1·2 |
| 40-50 | **샘플 워크북 시연** — F01_Sally_Smith 시트 라이브 데모 | 📎 [laka_sop_template_v0.xlsx](./laka_sop_template_v0.xlsx) |
| 50-60 | Implementation Path 4 Phase + Go/No-Go #1 결정 | 본 페이지 §1 |

### 2.3 핵심 인용 (60분 동안 사용할 5개 sound bite)

1. *"공장 소유 여부는 중요하지 않다 — demand/supply는 여전히 균형이 필요하다."* (Wallace, LAKA Designer/Distributor 정당성)
2. *"President는 매월 1.5시간만 투자하면 된다."* (CEO 진입 장벽)
3. *"Hold the high ground — 처음부터 top management 끌어들여라."* (CEO 스폰서십 우선)
4. *"보통 1년에 1-2번만 일어나는 strategic process에 매월 life를 가져온다."* (Adam Szczepanski, CFO 가치 제안)
5. *"60% 변화관리 / 30% 프로세스 / 10% 기술."* (SCI, 도구 도입 후순위 정당성)

### 2.4 예상 반론 + 대응 6개

| 반론 | 대응 |
|------|------|
| "분기 budget 사이클로 충분하지 않나?" | 분기는 1-2회·매월은 12회. K-뷰티 트렌드 사이클 너무 빠름 + 글로벌 채널 PO 변동 |
| "월 1.5시간이 진짜 가능한가?" | 다른 ad-hoc 의사결정 회의 시간이 줄어든다. 한 group VP 인용: *"It's the most highly leveraged use of my time."* |
| "이미 SCM이 forecast 운영하는데" | Volume vs Mix 분리 — SCM이 Mix 운영, S&OP는 Volume + cross-functional. 새 책임 신설 아님 |
| "8부문 다 끌어들이면 너무 무거움" | 6 essential만 매월. 나머지는 분기 review. Live Pilot은 2 family·3 채널만 |
| "도구·SW 비용은?" | Phase 1·2는 Excel만. Phase 3 이후 ToolsGroup/o9 검토. <$100K |
| "ODM이 협조 안 하면?" | 한국콜마는 LAKA 5% 지분. 슬롯 정보 공유는 협상 가능. 단, 분기 confirmation까지 진행 |

### 2.5 Go/No-Go #1 결정 양식

| 항목 | YES 조건 |
|------|----------|
| CEO commitment | 월 1.5h commit 명시 + 1년 Exec Meeting 일정 사전 잡기 동의 |
| VP commitment | 6 essential 5명 이상 commit |
| Pilot scope 합의 | F01 + F08 + 3 채널 동의 |
| Process Owner 임명 | SCM SC기획팀장 임명 |
| Demand Manager 임명 | 마케팅 BM/PM 파트장 임명 |
| Kickoff 일정 확정 | 1주일 내 |

→ 6/6 YES면 진행. 4-5/6면 missing 항목 1주일 내 보완. 3 이하면 No-Go (W6 Re-implementation 경로 검토).

---

## 3. Kickoff Session (반나절, T+1주)

### 3.1 목적

- Phase 2 Live Pilot 운영 룰 합의
- Master Scheduling Policy (거버넌스 문서) 초안 sign-off
- 첫 cycle 시작 일자 확정
- Demand Manager·Process Owner onboarding

### 3.2 4시간 Agenda

| Time | Section | 참석 |
|------|----------|------|
| 0-30분 | Implementation Path 4 Phase 재확인 | 전원 |
| 30-90분 | **Master Scheduling Policy 초안 review·sign-off** | 전원 |
| 90-120분 | Live Pilot Scope 상세화 (Family·Channel·KPI 목표) | 전원 |
| 120-180분 | Step 1·2·3 운영 룰 review (working day 1-10) | 운영진 |
| 180-210분 | Pre-meeting·Exec Meeting cadence 확정 | 전원 |
| 210-240분 | 첫 cycle 시작 — 데이터 수집 책임 배분 | 전원 |

---

## 4. Master Scheduling Policy (거버넌스 공식 문서)

Wallace ([[src_wallace_executive_guide_book|책]] Glossary): *"Top management 승인 문서. demand/supply 양쪽의 역할·책임·decision rights·time zone별 권한을 명시."*

### 4.1 LAKA S&OP Master Scheduling Policy v1 (Draft)

**문서 정보**:
- 발효: 2026-07-15 (Kickoff Session 일자)
- 승인: 이지철 CEO + 6 본부장
- 차기 review: 분기 (3개월마다)
- Owner: SCM SC기획팀

### 4.2 7개 핵심 조항

#### 조항 1 — Process Definition

LAKA S&OP는 **매월 1회 운영되는 cross-functional 의사결정 프로세스**로, **15-18개월 호라이즌**에서 **Product Family 단위** demand·supply 균형을 **units + KRW**로 의사결정한다.

#### 조항 2 — Scope

- **Volume planning** (Family 단위): S&OP 영역
- **Mix planning** (SKU 단위): Master Scheduling 영역, S&OP 외부
- **Strategic planning** (3-5년): 별도 프로세스, S&OP 인풋

#### 조항 3 — Roles & Responsibilities

| 역할 | 부문/인력 | 핵심 책임 |
|------|------------|------------|
| **Process Owner** | SCM SC기획팀장 | 5-step 전체 cadence·자료 통합·Pre-meeting 운영 |
| **Demand Manager** | 마케팅 BM/PM 파트장 | Step 1 통계 baseline·Step 2 Demand Consensus 운영 |
| **Supply Planning Owner** | SCM 본부장 | Step 3 Operations Plan·Capacity check |
| **VP Sales (Global)** | 손여진 글로벌사업 | 글로벌 채널 demand 인풋·sell-through 데이터 제공 |
| **VP Sales (Domestic)** | 임시 CEO (공석) | 국내 채널 demand 인풋 |
| **VP Marketing** | 안일홍 | Marketing adjustment·캠페인 일정·NPI 일정 검토 |
| **VP Product Development** | 이정미 | NPI 인풋·BOM·라벨링 변형 |
| **VP Finance** | 이종영 CFO | 환율·단가·재무 영향·Volume → $ 환산 |
| **Master Data Steward** | SCM SC기획팀 | Family·SKU·Channel·UoM·Lead Time 거버넌스 |

#### 조항 4 — Time Zone & Decision Rights

| Zone | 기간 | 변경 권한 | 변경 사유 명시 필수 |
|------|------|------------|------------------------|
| **Frozen** | 0 ~ DTF (30일) | **변경 절대 불가** | (Mini-S&OP Cycle 발동만 예외) |
| **Slushy** | DTF ~ PTF (30-60일) | Supply Planning Owner + 재무 협의 | 비용 영향 산출 |
| **Liquid** | PTF 이후 (60일+) | Demand Manager | 분기 confirmation 영향 검토 |

#### 조항 5 — Decision Authority Matrix (RACI)

| 의사결정 | Process Owner | Demand Mgr | Supply Mgr | VP Sales | VP Mktg | VP Ops | VP Fin | CEO |
|------------|------------------|---------------|---------------|----------|----------|---------|---------|------|
| 통계 baseline 변경 | A | R | C | I | I | I | I | I |
| Marketing 인풋 변경 | C | C | I | I | R/A | I | I | I |
| Sales 인풋 변경 (글로벌) | C | C | I | R/A | I | I | I | I |
| NPI 일정·물량 | C | C | C | C | C | I | I | R/A → 위양 가능 |
| 컬러군 신규 추가 | C | C | C | I | C | I | I | R/A |
| Operations Plan 변경 (Slushy) | A | I | R | C | C | C | C | I |
| Operations Plan 변경 (Frozen) | A | I | R | I | I | C | C | **R/A** |
| ODM dual sourcing 결정 | A | I | R | I | I | C | C | R/A |
| 캠페인 일정 변경 | C | C | C | C | R/A | I | I | I |
| 환율 시나리오 release | I | I | I | I | I | I | R/A | I |
| Master Data 변경 | A | C | C | I | I | I | I | I |
| Mini-S&OP Cycle 발동 | R | C | C | C | C | A | C | I |

(R = Responsible, A = Accountable, C = Consulted, I = Informed)

#### 조항 6 — Meeting Cadence

| 회의 | 주기 | 시간 | 참석 |
|------|------|------|------|
| Data Gathering 마감 | 매월 working day 3 | — | Process Owner |
| Demand Consensus | 매월 working day 7 | 60-90분 | VP Marketing·Sales(2)·Product Development + Demand Manager |
| Supply sign-off | 매월 working day 10 | 30분 | VP Operations + Supply Planning Owner |
| **Pre-meeting** | 매월 working day 13 | 90분 | Process Owner + Demand Manager + Supply Planning Owner + Finance 1 + VP Marketing 1 + VP Sales 1 |
| **Exec Meeting** | 매월 working day 15 | 60-90분 | **CEO + 6 essential VP (전원)** |
| Mini-S&OP | ad-hoc (trigger 발생 시) | 60-90분 | 영향 받는 부서만 |
| 분기 review | 분기 마지막 working day -3 | 90분 | CEO + 전 VP |
| 연간 maturity 진단 | 연 1회 | 반나절 | CEO + 전 VP + 외부 facilitator |

→ Exec Meeting은 **1년치 일정 사전 잡기** (Wallace 권장 — 이사회·trade show 충돌 회피).

#### 조항 7 — Override & Escalation

- Frozen zone 안에서 변경이 필요한 경우 → **반드시 CEO 승인** + Mini-S&OP Cycle 발동
- DTF 위반 발생 시 → 다음 Pre-meeting에 root cause + 재발 방지 보고
- 분기 review에서 Broken Process 7 신호 3개 이상 ✓ → 즉시 Re-implementation 검토

---

## 5. Phase 2 — Live Pilot 90일 (3 Monthly Cycle)

### 5.1 Pilot Scope 정량

| 항목 | 범위 |
|------|------|
| **Family** | F01 (립글로스 컬러군 A, 베스트셀러) + F08 (글로벌 전용 SKU FTO) |
| **Channel** | CH-US-SEPH (세포라 미국) + CH-JP-Q10 (Qoo10 일본) + CH-KR-OL (한국 온라인) |
| **ODM** | 한국콜마 (F01 100% + F08 50%) + 코스맥스 (F08 50% dual sourcing) |
| **호라이즌** | 18개월 forecast (2026-07 ~ 2028-01) |
| **사용 도구** | 샘플 워크북 v0 확장 — F01 + F08 시트 2개 |

### 5.2 90일 일정 (3 Cycle)

```
Cycle 1   (Month 1, 7월)   ──────────────────────────
Day 1-3   Step 1 Data Gathering (초도 — 마스터 데이터 정착)
Day 4-7   Step 2 Demand Planning + Consensus
Day 4-10  Step 3 Supply Planning + sign-off
Day 13    Pre-meeting (Step 4)
Day 15    Exec Meeting (Step 5) ★ CEO 참여 첫 사례

Cycle 2   (Month 2, 8월)   ──────────────────────────
Day 1-3   Step 1 (Cycle 1 학습 반영)
Day 4-7   Step 2 (FVA 측정 첫 누적)
Day 4-10  Step 3 (ODM dual sourcing 검토)
Day 13    Pre-meeting
Day 15    Exec Meeting

Cycle 3   (Month 3, 9월)   ──────────────────────────
Day 1-3   Step 1 (자동화 일부 시도)
Day 4-7   Step 2 (3-mo MAPE·Bias 첫 측정)
Day 4-10  Step 3 (Capacity Headroom 추세 분석)
Day 13    Pre-meeting
Day 15    Exec Meeting

Day 16-20 Phase 2 회고 + Go/No-Go #2 결정
```

### 5.3 Cycle별 학습 목표

| Cycle | 학습 목표 | 측정 |
|--------|------------|------|
| Cycle 1 | 5-step 운영 가능성 자체 검증 | Process KPI 22개 중 50% 측정 가능? |
| Cycle 2 | FVA·Bias 첫 의미 있는 데이터 | layer별 FVA 산출 |
| Cycle 3 | Cadence·Cross-functional 정착 | Exec Meeting Attendance 100%? + Soft Benefit 정성 평가 |

### 5.4 Pilot 동안 발견 가능한 문제 (사전 예측)

| 문제 | 예상 발생 시점 | 대응 |
|------|------------------|------|
| Master Data drift (Family·SKU·Channel 부서별 다른 ID) | Cycle 1 | Master Data Steward 즉시 정비 |
| ODM 입고 데이터 latency (5-10일) | Cycle 1 | 한국콜마·코스맥스와 batch 자동화 협의 |
| Sales(글로벌·국내) baseline·campaign 통합 인풋 | Cycle 1-2 | Marketing Adjustment 양식 강제 |
| Statistical baseline 신뢰 부족 | Cycle 1-2 | FVA 3-mo 누적 후 evidence 제시 |
| Pre-meeting 결정 안 됨 (Conflict aversion) | Cycle 2 | Moose Rule 도입 |
| Exec Meeting attendance 결석 | Cycle 2-3 | CEO 직접 escalation |
| DTF 위반 (Frozen zone 변경 요청) | Cycle 2-3 | 단호한 거부 + Mini-S&OP 발동 룰 |
| NPI 인풋 지연 (프로덕트 부문) | Cycle 1-3 | 매월 working day 6 cutoff 강제 |

---

## 6. Step 4 — Pre-meeting 운영 매뉴얼 (90분)

지금까지 W3·W4에서 언급만 됨. 본 페이지에서 상세 운영 매뉴얼.

### 6.1 참석자 (6-8명)

| 역할 | 인물 | 기여 |
|------|------|------|
| **Process Owner** (운영) | SCM SC기획팀장 | 어젠다 운영·자료 사전 배포 |
| **Demand Manager** | 마케팅 BM/PM 파트장 | Demand 측 인풋 통합 보고 |
| **Supply Planning Owner** | SCM 본부장 | Supply 측 인풋·constraint 보고 |
| **Finance representative** | 재무 부문 1명 (CFO 위임) | 환율·KRW 환산·재무 영향 |
| **Marketing representative** | 마케팅 부문 1명 | 캠페인 일정·NPI 일정 |
| **Sales representative** | 글로벌사업 또는 국내사업 1명 | 채널 인풋 |

→ Mid-management 회의. VP는 참석 안 함.

### 6.2 어젠다 (90분)

| Time | Section | 활동 |
|------|----------|------|
| 0-10 | Process KPI 22개 review (전월) | Process Owner |
| 10-25 | F01 family review — Sally Smith Sheet | Demand Mgr + Supply Mgr |
| 25-40 | F08 family review — Sally Smith Sheet | Demand Mgr + Supply Mgr |
| 40-55 | NPI status — 진행 중 launch curve 모니터링 | Marketing rep + Product Dev (콜인) |
| 55-70 | Constraint Identification — Capacity Headroom·Stockout 위험 | Supply Planning Owner |
| 70-80 | **Top 3 Moose** — 갈등 표면화 | 전원 |
| 80-90 | Exec Meeting 어젠다 확정 + Recommendations | Process Owner |

### 6.3 출력 (Exec Meeting 자료 패키지)

| 자료 | 형식 |
|------|------|
| 1 페이지 Macro $$$ Review | family 합계 chart |
| Customer Service Performance | Order Fill Rate 표 (채널별) |
| New Product Issues | NPI 진행 상황 + Forecast Accuracy |
| Family-by-family Recommendations | F01·F08 각 1 slide |
| **Major Constraints / Decisions Needed** | escalated issue별 alternative 양식 |
| Collective Impact on Business Plan | 재무 영향 요약 |
| Top 3 Moose | 갈등 issue별 권고 |

---

## 7. Step 5 — Exec Meeting 운영 매뉴얼 (60-90분)

### 7.1 참석자 (Wallace [[src_wallace_executive_sop_workshop|워크샵]] p48 기준)

**Essential**:
- 이지철 CEO (President / Process Owner)
- 김중찬 SCM 본부장 (VP Operations)
- 안일홍 마케팅 본부장
- 손여진 글로벌사업 본부장
- 이정미 프로덕트 본부장
- 이종영 CFO

**Probable**:
- Process Owner (SCM SC기획팀장)
- Pre-meeting Facilitator
- Demand Manager

**Possible** (issue별):
- Controller·Customer Service Manager·Forecast Analyst·HR Manager·Master Scheduler·Plant Manager·Product Development Manager·Product Manager·Purchasing Manager

### 7.2 어젠다 (Wallace 표준 8항목)

| Min | Item | 메시지 |
|-----|------|---------|
| 0-10 | **Macro $$$ Review** — 전 family 합계 | "이번 달 비즈니스 plan vs actual" |
| 10-20 | **Customer Service Performance** — Order Fill Rate | "고객 약속 지켰는가" |
| 20-30 | **New Product Issues** | "혁신 속도" |
| 30-55 | **Family-by-family Review and Decisions** — F01, F08 | "각 family 의사결정" |
| 55-65 | **Production / Procurement Rate Changes** | Operations 변경 승인 |
| 65-75 | **Collective Impact on Business Plan** | 재무 영향 |
| 75-85 | **Recap of Decisions Made** | 다음 cycle 마치 명령 |
| 85-90 | **Critique of Meeting** | "오늘 회의의 잘된 점·개선점" |

### 7.3 의사결정 4 유형 ([[demand_planning|2.]] §0 인용)

각 family당 다음 4 중 하나:
1. **Change the Sales Plan** (forecast 조정)
2. **Change the Operations Plan** (production rate·MOQ·dual sourcing)
3. **Change the inventory/backlog projection** (safety stock 변경)
4. **None of the above — 현행 plan OK**

### 7.4 회의 후 24시간 액션

| 시간 | 액션 | 책임 |
|------|------|------|
| 회의 종료 즉시 | 의사결정 사항 chat 공유 | Process Owner |
| +2 working day | 정식 minutes + 업데이트된 Sally Smith Sheet 배포 | Process Owner |
| +5 working day | 다음 cycle 일정·자료 준비 시작 | Process Owner |

---

## 8. Phase 2 회고 + Go/No-Go #2 (Day 76-90)

### 8.1 90일 회고 양식

| 항목 | 평가 (0-3) | 증거 | 개선 액션 |
|------|---------------|------|------------|
| Process KPI Stage 진화 | | 22개 KPI 중 측정 가능 비율 | |
| Cadence 정착 | | 9 회의 (Demand Consensus 3 + Pre-meeting 3 + Exec Meeting 3) on-time 비율 | |
| Master Data drift | | 부서간 ID 불일치 건수 | |
| FVA layer별 결과 | | layer 1~4 각 FVA 값 | |
| Order Fill Rate (3 채널) | | 채널별 측정 | |
| Capacity Headroom 추세 | | F01·F08 ODM 슬롯 utilization | |
| **Wallace Broken Process 7 신호** | ✓/✗ × 7 | Pre-meeting·Exec Meeting 진행 양상 | |
| **Soft Benefit 첫 정성 평가** | | 6 essential VP 인터뷰 | |

### 8.2 Go/No-Go #2 — Expansion 결정

| 조건 | YES 임계 |
|------|----------|
| Process KPI 50%+ 측정 가능 | Y |
| Exec Meeting Attendance 100% (3/3 cycle) | Y |
| Cycle 3 FVA layer 양수 (baseline·marketing) | Y |
| Sally Smith Sheet 자동화 안정 | Y |
| Soft Benefit 정성 평균 3.0+ (5점) | Y |
| Broken Process 7 신호 중 ≤2 ✓ | Y |
| CEO commitment 지속 (월 1.5h 실제 invest) | Y |

→ 5/7 이상 YES면 Phase 3 진행. 3-4 YES면 Pilot 1 cycle 연장 후 재평가. 2 이하 NO면 W6 Re-implementation 경로.

---

## 9. Phase 3 — Expansion & Replication (4개월)

### 9.1 Expansion 단계

| Month | Family 추가 | 누적 family |
|--------|---------------|---------------|
| Month 4 | F02 (립글로스 시즌 한정) + F03 (립 틴트) | 4 |
| Month 5 | F04 (아이섀도) + F05 (베이스) | 6 |
| Month 6 | F06 (선케어) + F07 (스킨케어) | 8 |
| Month 7 | 정착 + 자동화 강화 | 8 |

→ **2-4개 family / month 추가** (Wallace 권장 페이스).

### 9.2 Channel 확장

| Month | Channel 추가 |
|--------|-----------------|
| Month 4 | CH-UK-BOOTS (Boots 영국) |
| Month 5 | CH-JP-LOFT (LOFT 일본) + CH-US-AMZ (아마존 미국) |
| Month 6 | CH-KR-RT (국내 리테일 — 올리브영) |
| Month 7 | 정착 |

### 9.3 운영 부담 증가 대응

| 영역 | Pilot (2 family) | Phase 3 끝 (8 family) | 대응 |
|------|---------------------|-------------------------|------|
| Demand Manager 시간 | 5h/cycle | 15h/cycle | 추가 인력 1명? 또는 자동화 |
| Pre-meeting 시간 | 90분 | 120-150분 | family당 시간 단축 강제 |
| Exec Meeting 시간 | 60-90분 | 90-120분 | family 묶음 review |
| Sally Smith Sheet 운영 | 1 master file | 8 family × file | 통합 워크북 또는 BI 도구 |

→ Phase 3 후반 자동화 / 도구 도입 검토 (ToolsGroup·o9 평가 시작).

---

## 10. Phase 4 — Integration of Financials (2개월)

### 10.1 통합 영역

| 영역 | 활동 |
|------|------|
| Volume → $ 환산 | 환율 시나리오 3개 자동 적용 + 분기 budget과 monthly forecast 정합성 |
| 분기 budget review와 S&OP 통합 | 분기말 Exec Meeting에 budget vs S&OP 비교 |
| What-if 시뮬레이션 도입 | family×channel×환율 시나리오 3×3×3 = 27 시나리오 |
| CFO 어젠다 통합 | Adam Szczepanski 인용 — "매월 strategic process에 life" |
| 분기 보고서 자동화 | KPI dashboard from Sally Smith Sheets |

### 10.2 Wallace 미래 비전 단계 진입 (선택)

| 미래 자산 | 도입 시점 |
|------------|------------|
| Top Management War Room | Phase 4 끝 (12개월) — 시뮬레이션 SW 도입 후 |
| Running Delta | Phase 4 중 (Excel 수식으로 구현 가능) |
| Red Zone | LAKA 비상장이지만 분기 review 활용 |
| Audit Trail of Decisions | Phase 4 중 (Decision Log 도입) |

---

## 11. KPI 목표 — Phase 2 vs Phase 3 vs Phase 4

[[sop_kpis|W5]] §8 Progression의 Live Pilot 적용:

| KPI | Phase 2 끝 (90일) | Phase 3 끝 (7개월) | Phase 4 끝 (9-12개월) |
|-----|----------------------|----------------------|--------------------------|
| MAPE (F01) | < 25% | < 18% | **< 15%** |
| Bias (F01) | ±10% | ±7% | **±5%** |
| Order Fill Rate (CH-US-SEPH) | > 92% | > 94% | **> 95%** |
| Production Plan Adherence | 90-110% | 92-108% | **95-105%** |
| Time-fence Discipline | 월 5건 미만 | 월 2건 | **0건 (Mini-S&OP 제외)** |
| Exec Meeting Attendance | 100% | 100% | **100%** |
| Soft Benefit 평균 | 3.0 | 3.5 | **3.8** |

→ **Stage 2 → Stage 3 진입** 18개월 목표.

---

## 12. v1 → v2 진화 계획

90일 + 추가 6-9개월 운영 후 v2 작성. v1 대비 변경 후보:

| 영역 | v1 | v2 변경 후보 |
|------|----|----------------|
| Family 수 | 2 → 8 (단계 확장) | 12-15 (sub-family 분리) |
| Channel 분해 | Pilot 3 채널만 | 모든 채널 + DC 단위 |
| Mix forecasting | Mix는 S&OP 외부 | Master Schedule 정식 도입 (W4 후속) |
| 도구 | Excel만 | ToolsGroup / o9 / Logility 평가·도입 |
| 시뮬레이션 | What-if 수식 | Top Management War Room (Wallace 미래 비전) |
| 재무 통합 | Volume → $ 단순 환산 | 분기 budget·Wall Street guidance 통합 |
| 거버넌스 | LAKA 단일 entity | (글로벌 entity 분리 시 검토) |

→ v2는 사실상 **Stage 3 → Stage 4 진입** 단계 자료.

---

## 13. Risk Register — Pilot 중 위험과 대응

| Risk | 확률 | Impact | 대응 |
|------|------|----------|------|
| CEO 회의 결석 (다른 우선순위) | 중 | 매우 큼 | 1년치 일정 사전 잡기·alternate 사전 합의 |
| 국내사업 본부장 임명 지연 | 高 | 큼 | CEO 임시 owner 지속, 임명 일정 추적 |
| 한국콜마 데이터 협조 거부 | 낮 | 큼 | LAKA 5% 지분 leverage + 분기 confirmation 데이터부터 |
| 마스터 데이터 정착 실패 | 중 | 매우 큼 | Master Data Steward 100% 시간 투입 |
| Demand Manager 핵심 인력 이직 | 낮 | 큼 | 문서화 + 후임 1명 사전 식별 |
| Sales 단기 과대예측 패턴 정착 | 高 | 중 | FVA 측정 강제·교육 |
| Pre-meeting facilitator 운영 미숙 | 중 | 중 | 외부 facilitator 1-2 cycle 활용 |
| 환율 급변 (지정학·관세 등) | 중 | 큼 | 시나리오 3개·Mini-S&OP 발동 |
| 글로벌 채널 갑작스러운 PO 변동 | 高 | 큼 | DTF 30일 + 채널과 사전 alignment |

---

## 14. 시뮬레이션의 한계 (자기 평가)

본 v1 작성 후 가장 명확한 갭:

| 영역 | 갭 |
|------|-----|
| Family 정의 | F01~F08 정의가 실제 LAKA의 운영 분류와 일치하는지 미확인 |
| ODM 운영 cadence | 한국콜마·코스맥스의 Annual·Quarterly·Monthly PO 실제 흐름이 추정과 다를 수 있음 |
| 단가·MOQ·Lead Time | 마스터 데이터 모두 추정 |
| 8부문 본부장 실제 commitment | 인터뷰 안 함 |
| 국내사업 본부장 공석 영향 | 추정만 |
| 마스터 데이터 현행 상태 | Family·SKU·Channel·UoM 거버넌스 미파악 |
| 시스템 통합 갭 | 자체 ERP·창고·세포라/Boots/Qoo10 시스템 실제 갭 미파악 |
| ODM 데이터 공유 협조 의향 | 한국콜마·코스맥스와 협의 안 함 |
| 환율 단일 release 정착 가능성 | 재무 부문 실제 의향 미확인 |
| 분기 budget 사이클과 통합 가능성 | 분기 review 실제 운영 방식 미파악 |

→ **실제 적용 시 위 10개 갭 모두 보정 필수**. 본 v1은 "이런 모양이 될 것"의 가설일 뿐.

---

## 관련 페이지

- [[sop_overview]] — W1 (Phase 1 Executive Briefing 자료 base)
- [[sop_glossary]] — W2 (모든 용어 정의)
- [[data_gathering]] — 1. (Step 1 운영)
- [[demand_planning]] — 2. (Step 2 운영)
- [[supply_planning_odm]] — 3. (Step 3 운영)
- [[sop_kpis]] — W5 (Pilot KPI 22개·Outcome KPI 측정)
- [[sop_failure_patterns]] — W6 (Pilot 중 위험 패턴 대응)
- 📎 [laka_sop_template_v0.xlsx](./laka_sop_template_v0.xlsx) — Pilot 운영 도구 (v0, Pilot 시 F08 시트 추가)
- [[LAKA]] — LAKA 기업 entity
- [[ODM]] / [[ODM_발주_프로세스]] — LAKA SCM 현행 base
- [[K-뷰티_ODM_비교]] / [[한국콜마_vs_코스맥스_ODM_비교]] — ODM 협상 base
- [[src_wallace_executive_guide_book]] — Implementation Path·Master Scheduling Policy·Exec Meeting Agenda 원천
- [[src_wallace_executive_sop_workshop]] — Pre-meeting·Exec Meeting 운영 원천
- [[src_implement_sop_handbook]] — Pilot scope·Operations Plan 원천
- [[src_supply_chain_insights_sop_guide]] — Stage progression·CFO 가치 원천
