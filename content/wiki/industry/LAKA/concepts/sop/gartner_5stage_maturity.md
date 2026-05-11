---
title: "Gartner 5-Stage Maturity Model — 두 모델 + 5 Ps"
type: concept
axis: work
tags: [work/sop, s&op, maturity, gartner, 5-ps, ibp, laka]
created: 2026-05-12
updated: 2026-05-12
status: draft
publish: false
---

# Gartner 5-Stage Maturity Model — 두 모델 + 5 Ps

> **본 페이지의 역할**: Gartner의 5-stage maturity 프레임워크 두 가지 (**Process** vs **Technology**) + **My Supply Chain Group의 5 Ps** 통합 정리. 기존 [[sop_glossary|용어집]] §11 "5-Stage Maturity Model (SCI)" 보강. SCI·Wallace 모델과의 비교, LAKA 5 Ps 진단.
>
> **핵심 통찰 (이 페이지의 발견)**:
> 1. Gartner는 같은 5-stage 프레임을 **여러 도메인**에 적용 — Process / Technology / Demand-Driven / PLM / Logistics 다섯 가지 별개 모델 존재
> 2. "Gartner S&OP Maturity"라 하면 **Process** 모델 (React → Anticipate → Integrate → Collaborate → Orchestrate)
> 3. **Gartner와 SCI는 IBP 정의가 정반대** — Gartner: IBP = Stage 4-5 (성숙) / SCI: IBP = Stage 3 (중간)
> 4. 5 Ps (People·Processes·Platforms·Policies·Performance) 각각이 다른 단계에 머무는 게 일반적 — LAKA 진단에 활용

---

## 1. Gartner의 5-stage 프레임 — 5 개 도메인 (분류 정리)

| # | 도메인 | 5 Stage | 출처 |
|---|---------|----------|------|
| 1 | **S&OP Process Maturity** | React → Anticipate → Integrate → Collaborate → Orchestrate | Gartner ID 2587021 (paywalled) |
| 2 | **Supply Chain Planning Technology** | Spreadsheets → Demand SW → Planning SoR → MEIO & SoD → Algorithmic | Tim Payne, 2017 — ToolsGroup blog |
| 3 | **Demand-Driven Maturity** | (구체 단계 별도) | Gartner ID 2389615 (paywalled) |
| 4 | **PLM Excellence** | (구체 단계 별도) | Gartner ID 3823184 (paywalled) |
| 5 | **Logistics Maturity** | (구체 단계 별도) | gartner.com/smarterwithgartner |

→ **"Gartner 5-stage maturity"**라는 표현 사용 시 **어느 도메인인지 명시** 필수. 같은 회사가 5 도메인에 다른 모델 적용.

---

## 2. Gartner S&OP Process Maturity Model — 5 Stage

### 2.1 5 Stage 정의

| Stage | 명칭 | 핵심 특성 |
|--------|------|------------|
| 1 | **React** | 사후 대응, 기능 사일로, 단기 focus |
| 2 | **Anticipate** | demand 예측 시작, 부분 forecast 운영 |
| 3 | **Integrate** | 내부 integration (★ 신규 추가 단계) |
| 4 | **Collaborate** | 외부 협업 + IBP 전환 시점 |
| 5 | **Orchestrate** | 시장-시장 오케스트레이션, trading partner 통합 |

### 2.2 왜 5-stage가 되었나 — 4→5 진화 이유

**원본**: 4-stage (React → Anticipate → Collaborate → Orchestrate)

**문제**: WebSearch 결과 — *"two-thirds of companies find it difficult to move from the Anticipate stage to the Collaborate stage"*

→ Anticipate(2)에서 Collaborate(4 구버전)으로 점프하는 갭이 너무 큼. **2/3의 기업이 막힘**.

**해결**: 그 사이에 **"Integrate"** 단계 신설. 내부 integration이 외부 협업의 전제 조건임을 명시.

### 2.3 IBP 전환 시점

> *"Higher stages (Collaborate & Orchestrate)에서 S&OP가 IBP (Integrated Business Planning)로 transformed."*

→ **Gartner 입장: IBP = Stage 4-5** (성숙 단계의 결과)

---

## 3. Tim Payne Technology Maturity (다른 모델, 같은 5-stage 형식)

ToolsGroup blog (Tim Payne 인용, 2017 Supply Chain Management Executive Conference).

| Stage | 기술 | 비유 | 초점 |
|--------|------|------|------|
| 1 | **Spreadsheets** | 스카치 테이프 | 부서별 임시 계획 |
| 2 | **Demand Planning Software** | 망치 | 단일 기능 표준화 |
| 3 | **Planning System of Record (SoR)** | 스위스 아미 나이프 | 통합·시나리오·종단간 |
| 4 | **MEIO & Systems of Differentiation (SoD)** | 자동화 장비 | 다층 재고 최적화·트레이드오프 |
| 5 | **Algorithmic Planning** | 로봇 | E2E 알고리즘·AI·복원력 |

**핵심 인용**:
- Stage 3는 *"이정표이지 목적지가 아니다"* — 경쟁 우위가 아닌 필수 요건
- Stage 5의 비유: *"의식은 초당 4가지 자극 처리, 무의식은 2천만 가지 모니터링"* — 자동화의 필연성

### 3.1 다음 단계 진화 어려움 5 원인

1. 문화적 저항
2. 투자 규모
3. 통합 복잡성
4. 인력 개발
5. 변화 관리

→ **Wallace ABC of Implementation (A=People, B=Data, C=Computer)와 정합**.

### 3.2 LAKA 매핑 (현행 추정)

| 영역 | LAKA 현재 | 18개월 목표 |
|------|-------------|---------------|
| 기술 성숙도 | **Stage 1** (Excel만) | Stage 2 (수요계획 SW 평가) |
| 프로세스 성숙도 | **Stage 1 (React)** ~ 일부 Anticipate | **Stage 3 (Integrate)** 진입 |

→ Process와 Technology가 다른 속도로 진화. **Wallace 가르침: A→B→C 순서 — Process(People) 먼저, Technology 나중**.

---

## 4. 5 Ps of S&OP Maturity (My Supply Chain Group)

[[src_supply_chain_insights_sop_guide|SCI]]와 별개의 컨설팅 분석 (Gartner 5-stage 인용).

### 4.1 5 Ps 정의

| P | 정의 |
|---|------|
| **People** | 내부 및 외부 전문성 — 인력·역량·교육 |
| **Processes** | S&OP 기능을 반복적으로 계획·실행·협업하는 절차 |
| **Platforms** | S&OP 기능을 촉진하는 기술 인프라 |
| **Policies/Practices** | S&OP가 상황에 대응하는 방식의 비즈니스 룰 |
| **Performance** | 목표 설정·결과 추적 KPI |

### 4.2 5 Ps × 5 Stages 매트릭스 — 진화 패턴

| | Stage 1 React | Stage 2 Anticipate | Stage 3 Integrate | Stage 4 Collaborate | Stage 5 Orchestrate |
|---|--------|----------|--------|--------|--------|
| **People** | 기능 사일로, 부서별 인원 | demand planner 등장 | cross-functional team | 외부 협업 인력 | 글로벌 네트워크 인재 |
| **Processes** | ad-hoc | 단발 forecast 사이클 | 5-step 정착 | 공급사·고객 통합 | 자동 orchestration |
| **Platforms** | Excel | Demand SW (단일) | Planning SoR | MEIO·SoD | Algorithmic Planning |
| **Policies** | 부재 | 부서별 자율 | Master Scheduling Policy | trading partner 합의 | 시장-시장 룰 |
| **Performance** | 기능 KPI | 부분 측정 | 통합 KPI | Hard Benefits | 균형 스코어카드 |

→ **My Supply Chain Group 핵심 인사이트**: *"대부분 조직에서 5 Ps가 서로 다른 성숙도 단계에 있음."* 균형 진화 못 함.

### 4.3 5 Ps 균형 부재 사례 5개 (My Supply Chain Group 인용)

| Case | 산업 | 영역 | 갭 |
|------|------|------|----|
| 1 | CPG | People | 15명 기획자 교육 부재 → 주간 세션·Jeopardy 게임 도입 후 3-6개월 만에 개선 |
| 2 | 하이테크 | Processes | 안전재고 가정 근거 부재 → 기획자 개별 편견에 따라 다양한 접근 |
| 3 | 중기계 | Platforms | 과도한 커스터마이제이션 → 표준 기능 활용 방해 |
| 4 | 산업 유통 | Policies | 벤더 협업 정책 부재 → 가격 협상 기회 손실 |
| 5 | 다중 기능 | Performance | "서비스 수준 ↑ vs 재고 ↑" KPI 충돌 관리 메커니즘 부재 |

---

## 5. SCI 5-Stage vs Gartner 5-Stage 비교

[[src_supply_chain_insights_sop_guide|SCI Maturity]]와 Gartner Process Maturity는 같은 5-stage이나 단계 명칭·정의 다름.

### 5.1 단계 비교 표

| Stage | **SCI (2020)** | **Gartner (Process)** |
|--------|---------------------|--------------------------|
| 1 | (Stage 1, 명칭 없음) — 기능 focus | **React** |
| 2 | **Sales-Driven** — S 또는 OP 편중 | **Anticipate** |
| 3 | **IBP** — 부분 정렬 | **Integrate** |
| 4 | **Demand-Driven** — 전략 기반 trade-off | **Collaborate** + IBP 전환 |
| 5 | **Market-Driven** — 시장-시장 통합 | **Orchestrate** |

### 5.2 IBP 정의 정반대

| 영역 | SCI 입장 | Gartner 입장 |
|------|----------|----------------|
| IBP 위치 | **Stage 3** (중간) | **Stage 4-5** (성숙) |
| IBP 정의 | "S&OP의 더 성숙한 형태" 단순 단계 | S&OP가 cross-functional·외부 협업으로 transformed된 결과 |
| LAKA 18개월 목표 | Stage 3 IBP 진입 | Stage 3 Integrate (내부 통합) — Gartner 명칭은 IBP가 아닌 Integrate |

→ **두 학파의 IBP 정의 차이 명시 필요**. 본 wiki는 SCI 기준 채택 (Stage 3 = IBP) — 단, Gartner Process 모델에서는 "Stage 3 = Integrate, IBP는 Stage 4-5" 별도 표기.

### 5.3 단계별 LAKA 자가 진단 가이드 (3 모델 통합)

| 차원 | SCI 명칭 | Gartner Process 명칭 | LAKA 현재 | LAKA 18개월 목표 |
|------|------------|------------------------|---------------|---------------------|
| Stage 1 | (Reactive) | React | ✓ 현재 (일부 Anticipate) | — |
| Stage 2 | Sales-Driven | Anticipate | 일부 | — |
| Stage 3 | **IBP** | **Integrate** | — | ✓ **18개월 목표** |
| Stage 4 | Demand-Driven | Collaborate (+ IBP 전환) | — | (24-36개월) |
| Stage 5 | Market-Driven | Orchestrate | — | (장기) |

---

## 6. Wallace의 Maturity 입장 (비교)

Wallace ([[src_wallace_executive_guide_book|책]] / [[src_wallace_executive_sop_workshop|워크샵]])는 **명시적 5-stage 모델 없음**. 대신:

- **"Better decision-making processes lead to better decisions"** — KPI 진화 시간 따라
- **Implementation Path 4 Phase** (Executive Briefing → Live Pilot → Expansion → Financial Integration) — 진화 경로 자체
- **Soft Benefits 7개** (Teamwork → Decisions → Window into the Future) — 진화 결과

→ Wallace는 **stage 분류 X, 본질·실행 강조**. SCI·Gartner의 stage 모델과 보완적.

---

## 7. LAKA 5 Ps 자가 진단 (시뮬레이션 — 실제 인터뷰로 보정 필수)

| P | LAKA 추정 단계 | 증거 |
|---|------------------|------|
| **People** | Stage 1-2 | SCM 10명·마케팅 15명 보유, 단 Demand Manager 직책 미정립 |
| **Processes** | Stage 1 (React) | S&OP 미구축, 분기 budget 사이클만. [[laka_sop_v1\|W7 Pilot 후 Stage 3 진입 목표]] |
| **Platforms** | Stage 1 (Spreadsheets) | Excel 기반 가정. ERP·창고·채널 통합 갭 추정 |
| **Policies** | Stage 1 | Master Scheduling Policy 부재 (W7에서 Draft 제시) |
| **Performance** | Stage 1 | [[OTD]] 정도 존재. 통합 KPI 22개 모두 신규 |

**5 Ps 불균형**:
- 가장 진보된 P: **People** (SCM·마케팅 인력 보유)
- 가장 낙후된 P: **Policies** + **Performance** (정립 부재)

**18개월 목표**: 5 Ps 모두 **Stage 3 Integrate** 균형 진입 — [[laka_sop_v1|W7 v1]] Phase 1-4가 이 목표 달성 path.

---

## 8. 통합 인용 가이드 — wiki 내 사용 시

W1~W8 wiki에서 maturity 언급 시:

| 언급 | 의도 | 명시 표기 |
|-------|------|------------|
| "Stage 3 진입" | SCI IBP 기준 | "(SCI Stage 3 = IBP)" |
| "IBP" 단어 사용 | SCI vs Gartner 정의 다름 — 본 wiki는 SCI 기준 | "(SCI 기준 — Gartner는 Stage 4-5에서 IBP 전환)" |
| "Maturity Stage 1-2" | 일반 진단 | 추가 명시 불필요 |
| "Gartner 5-stage" | 명시적 Gartner 참조 | "**Process** vs **Technology** 어느 도메인인지 명시" |
| "5 Ps" | My Supply Chain Group 프레임 | "(People·Processes·Platforms·Policies·Performance)" |
| "Tim Payne" | Technology Maturity 인용 | "(2017, Supply Chain Planning Tech)" |

---

## 9. 비평 — Simon Eagle "Gartner DDVN is misleading" (2017)

**LinkedIn 글**: "What do Gartner say about Demand-Driven SCM?" — Simon Eagle (CAMELOT Management Consultants)의 Gartner Demand-Driven Value Network(DDVN) Maturity 비평.

### 9.1 Eagle의 Gartner DDVN 비판 3가지

| # | 비판 | Eagle 입장 |
|----|------|-----------|
| 1 | **Pull-based replenishment를 Stage 5에 배치** | "이 핵심 속성은 Stage 3부터 시작되어야" |
| 2 | **Stage 4에서 협업적 forecast 기반 재고 관리 추천** | *"예측-주도형 시스템은 계획되지 않은 비용 생성 버퍼(과도한 대기시간·불균형 재고)를 만든다"* |
| 3 | **협업 SCM을 Stage 4에 배치한 순서 오류** | "내부 demand-driven 시스템 구현이 협업 단계 전제 조건" |

### 9.2 Eagle의 Demand-Driven SCM 정의 (대안)

> *"여러 개의 신중하게 규모가 정해진 재고 위치를 수요에 맞춰 안정적이고 예측 가능한 순서로 보충하는 pull-based 메커니즘"*

**핵심 특징**:
- 안정적·예측 가능한 재고 보충 순서
- 고급 안전재고 (extreme/exceptional events용)
- **예측 정확도 의존성 제거** ← Forecast-Driven과 정반대

### 9.3 Demand-Driven SCM 도입 효과 (Eagle 인용)

| 지표 | 개선 수준 |
|------|------------|
| 재고 | **−30~50%** |
| 리드타임 | **−50% 이상** |
| 서비스 수준 | 계획 수준 달성 |
| 필요 용량 | 현저히 감소 |
| 긴급 대응 | 불필요 |

**사례 기업 (Eagle 인용 early adopter)**: Unilever · Nestlé · Sandoz-Novartis · Shell Lubricants · P&G · BT · AG Barr · Michelin

### 9.4 Eagle 대안 4-Stage 모델 (Eagle & Barratt 2017)

| Stage | 명칭 | 비율 |
|--------|------|------|
| 1 | Misaligned | **99%** 기업 현재 위치 |
| 2 | Internally Aligned | 소수 |
| 3 | Extended & Aligned | 매우 드뭄 |
| 4 | Extended & Aligned with Dominant Player | 극소수 |

→ Gartner 5-stage보다 단순하나, "99% 기업이 Stage 1에 머문다"는 도발적 진단.

### 9.5 CPFR 실패 — Eagle 핵심 통찰

> *"높은 예측 정확도를 요구하는 'forecast push' 모델은 필연적으로 실패한다. 문제는 forecast-driven 접근 자체에 있다."*

→ Wallace의 *"Better decision-making processes"* (Forecast Accuracy 회의주의 아님)와 비교 흥미. Eagle은 더 강하게 **forecast 의존도 자체 거부**.

### 9.6 LAKA 적용 시사점 (Eagle 시각)

| 영역 | LAKA 현재 | Eagle 시각의 보강 |
|------|-------------|----------------------|
| Demand 측 | Forecast layering (4-layer) — [[demand_planning\|2.]] | Eagle: forecast 정확도 의존 줄이고 pull-based 보충 강화 |
| Supply 측 | DTF 30/PTF 60 — [[supply_planning_odm\|3.]] | Eagle: Demand Time Fence 안의 자동 pull 메커니즘 (Kanban-like) 검토 |
| Safety Stock | family·channel별 days-supply 목표 | Eagle: "advanced safety stock" — extreme event 대비, 평소엔 작게 |
| 핵심 패러다임 | Forecast-Driven (Wallace·SCI·Implement 모두 동의) | Eagle은 정반대 — Demand-Driven (Pull) |

→ **LAKA 입장**: 본 wiki는 Forecast-Driven (Wallace 3 학파) 패러다임 채택. Eagle 시각은 보충 reference로 유지. Stage 4+ 진입 시 demand-driven 요소 일부 도입 검토 (예: 베스트셀러 컬러에 pull-based 보충).

---

## 10. 출처

| 자료 | 접근성 |
|------|---------|
| Gartner ID 2587021 — "Introducing the Five-Stage S&OP Maturity Model for Supply Chain Leaders" | **Paywalled** (Gartner 클라이언트만) |
| Tim Payne, 2017 Supply Chain Management Executive Conference | 발표 자료 (ToolsGroup 인용) |
| ToolsGroup blog — "Gartner's Five Stages of Supply Chain Planning Technology Maturity" | **무료 공개** |
| My Supply Chain Group — "Road Map of IBP Part II — The 5 Ps of S&OP Maturity" | **무료 공개** |
| Gartner ID 2389615 — "Five-Stage Demand-Driven Maturity Model" | Paywalled |
| Gartner ID 3823184 — "Five-Stage PLM Maturity Model" | Paywalled |
| Gartner ID 3913817 — "Reference Model for S&OP System of Differentiation" | Paywalled |
| Gartner Smarter With Gartner — "5 Stages of Logistics Maturity" | **무료 공개** (단, 본 fetch 시 403 — bot protection. 직접 접근 권장) |
| **Simon Eagle / CAMELOT — "Gartner's DDVN Maturity Model is misleading"** (2017, LinkedIn) | **무료 공개** |

---

## 관련 페이지

- [[sop_overview]] — W1 (LAKA Stage 1-2 진단·18개월 목표)
- [[sop_glossary]] — W2 §11 Maturity Stages 정의 (본 페이지가 보강)
- [[sop_kpis]] — W5 §8 KPI Progression Stage 1→5 (SCI 기준)
- [[laka_sop_v1]] — W7 (Implementation Path 4 Phase = Wallace의 진화 모델)
- [[src_supply_chain_insights_sop_guide]] — SCI 5-stage 원천 (Sales-Driven → Market-Driven)
- [[src_implement_sop_handbook]] — Gartner 5-stage 인용 (Ch10)
- [[src_wallace_executive_guide_book]] — Wallace는 stage 모델 X, 본질 강조
- [[src_wallace_executive_sop_workshop]] — Implementation Path 4 Phase
