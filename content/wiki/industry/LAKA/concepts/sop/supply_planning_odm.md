---
title: "3. Supply Planning (ODM)"
type: concept
axis: work
tags: [work/sop, s&op, supply-planning, odm, capacity, scalability, time-fence, laka]
created: 2026-05-11
updated: 2026-05-11
status: draft
publish: false
---

# 3. Supply Planning (ODM)

> **본 페이지의 역할**: [[sop_overview|5-step 프로세스]]의 **Step 3 — Supply (Capacity) Planning** 운영 매뉴얼. [[demand_planning|2. Demand Planning]]에서 받은 management-authorized forecast를 한국콜마·코스맥스 ODM 슬롯·재고·자재 capacity로 변환하고, **constraint를 식별해 Pre-meeting(Step 4)으로 escalation**. LAKA Designer/Distributor 특성상 supply의 본질이 "공장 운영"이 아닌 **ODM 슬롯 확보 + 자재·라벨 인풋 조율**.
>
> **연관 Linear 이슈**: [COM-23](https://linear.app/luneneuf) W4
>
> **선행**: [[sop_overview]] (W1) — 프레임워크 / [[sop_glossary]] (W2) — RCCP·DTF/PTF·Aligned vs Matrix Resources·Demand·Supply Strategies 용어 / [[data_gathering]] (1.) — Lead Time·MOQ 마스터 데이터 / [[demand_planning]] (2.) — Step 2 산출 인풋

---

## 0. 위치와 책임

5-step에서 Step 3:

```
Step 1 Data Gathering → Step 2 Demand Planning → ★ Step 3 Supply Planning ★ → Step 4 Pre-meeting → Step 5 Exec Meeting
```

**Wallace 정의** ([[src_wallace_executive_guide_book|책]] Ch4 p43):

> *"Step 3의 첫 단계는 변경이 필요한 family·subfamily의 Operations Plan을 수정하는 것이다. … 그다음 key resources에 대한 **capacity check**가 필요하다. 이는 volume forecasts를 적절한 단위(보통 hours)로 변환하는 것을 요구한다. … 출력은 갱신된 Operations Plan + Capacity Planning report + 해결 불가능한 supply 문제 list (Pre-meeting으로 escalation)."*

**LAKA 책임 매핑** (VER. '26.03.04):

| 역할 | LAKA 부문/인력 | Step 3에서 할 일 |
|------|------------------|---------------------|
| **Supply Planning Owner** | SCM 부문 (10명, 김중찬 본부장) — SC기획팀 내 S&OP파트 | 인풋·출력 통합, ODM 커뮤니케이션 owner |
| ODM 슬롯·발주 plan | SCM (한국콜마·코스맥스 SCM 담당자와 협업) | 가용 슬롯 vs 요구 비교 |
| 자재 BOM·인풋 capacity | SCM + 프로덕트 부문 (8명, 이정미) | 패키지·튜브·라벨·실리콘 등 critical 인풋 가용성 |
| Finishing capacity (라벨링·포장) | SCM (한국콜마 finishing 라인 또는 별도 협력사) | 글로벌 라벨 변형 SKU의 finishing 슬롯 |
| Financial impact (단가·CapEx·운송비) | 재무 부문 (4명, 이종영 CFO) | Operations Plan 변경의 dollar 영향 산출 |
| Senior Operations sign-off | SCM 본부장 (김중찬) | Step 3 산출의 commitment |
| Constraint escalation → Pre-meeting | Supply Planning Owner | 해결 불가 issue를 Step 4 어젠다로 |

---

## 1. Step 3의 인풋과 출력

### 1.1 인풋 (Step 2에서 받음)

| 인풋 | 형식 | 사용처 |
|------|------|---------|
| Management-authorized Volume Forecast | Family 단위, units + KRW, 15-18개월 | Operations Plan 산출 base |
| NPI demand 시나리오 3개 (base/opt/pess) | Family·launch별 | base는 발주, worst는 hedge 재고 검토 |
| Marketing assumption 문서 | 프로모션·캠페인·가격 변동 일정 | Capacity peak 식별 |
| Sales channel breakdown | 채널·국가별 mix ratio | Finishing(라벨링) capacity 분배 |
| 마스터 데이터 변경 사항 | Family·SKU·Lead Time·MOQ 변경 | Operations Plan 재계산 트리거 |

### 1.2 출력 (→ Step 4 Pre-meeting)

| 출력 | 형식 | 받는 곳 |
|------|------|---------|
| Updated Operations Plan | Family 단위 18개월 production rate | Pre-meeting + Sally Smith Sheet의 Planned Production 행 |
| Capacity check report (RCCP) | Critical resource별 demand vs supply | Pre-meeting (constraint 시각화) |
| Inventory projection | Family 단위 18개월 재고 trajectory | Pre-meeting + Sally Smith Sheet의 Planned Inventory 행 |
| Unresolved supply issues list | Issue별 alternatives + cost | **Pre-meeting 어젠다 핵심** |
| Major resource change recommendations | 신규 ODM 라인 추가·외주 전환·EOL 검토 등 | Exec Meeting까지 escalation |
| Financial impact summary | Operations Plan 변경의 KRW 영향 | Finance + Pre-meeting |

---

## 2. Operations Plan 업데이트

### 2.1 무엇을 update하나

Wallace 원칙: **전월과 비교해 변경이 필요한 family·subfamily만** update.

변경 trigger 조건:
- Demand Forecast 변동 > Family safety stock의 50%
- NPI launch 일정·물량 변동
- 재고 수준이 target inventory 대비 ±25% 이상 차이
- ODM 슬롯 availability 변동 (한국콜마·코스맥스 capacity 조정 통보)
- 환율 시나리오 변경에 따른 channel-specific 수요 영향
- 자재 (패키지·튜브·라벨) supply 변동

### 2.2 Operations Plan = "Planned Production" 산출

기본 공식 (Family 단위, monthly):

```
Planned Production[t] 
  = max(
      MOQ,
      Target Inventory[t] − Inventory[t-1] + Demand Forecast[t]
    )
```

**LAKA 적용 — F01 립글로스 컬러군 A 예시** (샘플 워크북 [F01_Sally_Smith] 시트 참조):

```
Month       Demand FCST   Target Inv (30d)   Inventory(t-1)   Planned Prod
Feb-26      14            14                 12               16
Mar-26      11            11                 14               8 → MOQ 5
Apr-26      12            12                 11               13
```

→ Planned Production이 MOQ(5,000개) 미만이면 ODM에 발주 불가. 다음 달에 합치거나 다른 family와 동시 ordering. **MOQ 제약은 LAKA에 매우 중요** — 시즌 한정 컬러는 한 번의 발주로 시즌 전체 cover하는 패턴.

### 2.3 Production Lot Sizing 룰

| 룰 | LAKA 적용 |
|----|------------|
| Fixed Lot Size (FLS) | MOQ 5,000 단위로만 발주 — 한국콜마 립글로스 룰 |
| Lot-for-Lot (LFL) | 필요량 그대로 — 충분한 volume의 베스트셀러만 |
| Period Order Quantity (POQ) | N개월치 묶어 발주 — 시즌 한정 컬러에 적용 (예: 3개월치 한 번에) |
| Min-Max | 재고 min·max bound 사이에서 자동 발주 — Stage 3+ 도입 검토 |

---

## 3. Capacity Check — Rough-Cut Capacity Planning (RCCP)

### 3.1 RCCP의 의미

[[sop_glossary|용어집]]: RCCP = Operations Plan 또는 MPS를 **미래 capacity requirements로 변환**. demand가 aggregate units → 표준 hours / 슬롯으로 변환.

LAKA의 경우 "공장 hours"가 아니라 **ODM 슬롯 + finishing capacity + 자재 가용성** 3 영역.

### 3.2 LAKA Critical Resources 인벤토리

| Resource ID | 명칭 | 단위 | Owner | Aligned vs Matrix |
|--------------|------|------|-------|-----------------------|
| R-KK-LG | 한국콜마 립글로스 라인 | day·units/day | 한국콜마 | **Matrix** (다 브랜드 공유) |
| R-KK-SC | 한국콜마 선케어 라인 | day·units/day | 한국콜마 | **Matrix** |
| R-KK-SK | 한국콜마 스킨케어 라인 | day·units/day | 한국콜마 | **Matrix** |
| R-CM-LG | 코스맥스 립글로스 라인 (이중 발주 시) | day·units/day | 코스맥스 | **Matrix** |
| R-FN-LBL | 글로벌 라벨링·finishing | day·SKU/day | 한국콜마 또는 별도 협력사 | **Matrix** |
| R-PKG-TUBE | 립 글로스 튜브 (패키지) | units/month | 패키지 협력사 | **Matrix** |
| R-PKG-BOX | 외박스·sleeve | units/month | 인쇄 협력사 | **Matrix** |
| R-WH-KR | 국내 창고 (3PL) | pallet·m³ | 3PL | Aligned |
| R-WH-JP | 일본 창고 | pallet·m³ | 3PL | Aligned |
| R-WH-US | 미국 창고 | pallet·m³ | 3PL | Aligned |
| R-WH-UK | 영국 창고 | pallet·m³ | 3PL | Aligned |

→ **거의 모든 ODM·자재 자원이 Matrix** = LAKA만 사용하는 dedicated 자원 없음. 즉 **다른 K뷰티 브랜드와 슬롯 경쟁**. 이게 LAKA capacity 계획의 본질.

### 3.3 RCCP 변환 — Family Forecast → Critical Resource Load

Wallace 표준 공식:

```
Critical Resource Load[t]
  = Σ (Family[f] Planned Production[t] × Resource Coefficient[f, resource])
```

**Resource Coefficient 예시 (한국콜마 립글로스 라인)**:

| Family | Production rate (units/day) | Coefficient (days/천개) |
|---------|------------------------------|----------------------------|
| F01 (베스트셀러) | 1,000 units/day (단순 컬러군 가정) | 1.0 day per 1,000 units |
| F02 (시즌 한정) | 800 units/day (소량 다품종) | 1.25 day per 1,000 units |
| F08 (글로벌 전용 FTO) | 1,200 units/day | 0.83 day per 1,000 units |

**RCCP 출력 — Resource 가용 vs 요구 비교**:

```
한국콜마 립글로스 라인 (R-KK-LG) — 26-Mar 가용 슬롯 = 18일 (전체 22일 중)

Family   Production (천)   Load (days)
F01      11                11.0
F02       2                 2.5
F08       5                 4.2
────────────────────────────────
Total                      17.7 days  vs  18.0 days 가용
                           Headroom: 0.3 days (1.7%)  ← 위험!
```

→ Headroom < 5%면 yellow flag, < 0%면 red flag → constraint 식별, Pre-meeting escalation.

### 3.4 Inventory Projection — Sally Smith의 Inventory 블록

Planned Inventory[t] = Inventory[t-1] + Planned Production[t] − Demand Forecast[t]

→ 매월 trajectory 산출. Target inventory (Safety stock × Demand)와 비교.

| 상태 | 의미 | 대응 |
|------|------|------|
| Inventory > Target × 1.5 | 과잉 재고 위험 | Production 삭감 검토 |
| Target × 0.7 < Inv < Target × 1.5 | 정상 zone | 변경 없음 |
| Inventory < Target × 0.7 | 부족 위험 | Production 증가 검토 |
| Inventory < Safety Stock | **재고 부족 임박** | Mini-S&OP Cycle 검토 |

---

## 4. ODM 슬롯 매핑 (LAKA 핵심 갭)

LAKA의 공급 측 본질은 한국콜마·코스맥스 슬롯 확보. 일반 제조사의 "plant scheduling"과 다른 운영.

### 4.1 ODM 슬롯 확보 메커니즘 (한국 K뷰티 표준)

| 단계 | 활동 | 리드타임 |
|------|------|----------|
| 1. Annual Forecast | LAKA가 ODM에 연간 추정 물량 제공 | T−12개월 |
| 2. Quarterly Confirmation | LAKA·ODM 분기별 slot 확약 | T−3개월 |
| 3. Monthly PO Issue | 월간 PO 발행 (구속력 있음) | T−1.5개월 (DTF) |
| 4. Bulk Production | ODM 라인에서 bulk 생산 | T−1개월 |
| 5. Finishing (라벨·포장) | 채널별 라벨링·포장 | T−0.5개월 |
| 6. Inbound to Warehouse | LAKA 창고 입고 | T |

→ **Demand Time Fence (DTF) = 30일** (Monthly PO 시점). 이 안에서는 forecast 변경해도 PO 변경 불가.
→ **Planning Time Fence (PTF) = 60일** (Quarterly Confirmation 시점). 이 안에서는 slot이 사실상 고정.

### 4.2 슬롯 경쟁 (Matrix Resources의 현실)

한국콜마 립글로스 라인 한 달 가용 슬롯이 22일이면, 이를 K뷰티 브랜드 다수가 공유:
- LAKA: 10일 (예시)
- 다른 K뷰티 브랜드 A: 5일
- 브랜드 B: 4일
- 브랜드 C: 3일

→ LAKA가 갑작스레 +20% demand 증가 → 한국콜마 가용 슬롯 부족 → **alternative**:
1. 코스맥스로 일부 이중 발주
2. 한국콜마와 슬롯 확장 협상 (정기 슬롯 외 추가)
3. 외부 협력사 (소형 ODM) 일시 활용
4. Demand 우선순위 조정 (글로벌 채널 vs 국내 trade-off)

→ Pre-meeting에서 임원 의사결정 필요.

### 4.3 Aligned vs Matrix Resource 진단 (Implement Ch6 + Wallace)

| 차원 | Aligned (전용) | Matrix (공유) |
|------|------------------|------------------|
| 정의 | 1 family ↔ 1 resource | N family ↔ 1 resource |
| Capacity 계산 | 단순 (volume × coefficient) | 복잡 (다 family 합산 vs 가용) |
| LAKA 예시 | 창고 (R-WH-*) | ODM 라인 모두, 자재 모두 |
| 변동 대응 | 자체 조정 가능 | 외부 협상 필요 |
| Wallace 가이드 | 단순 RCCP로 충분 | scenario simulation 필요 |

→ LAKA의 거의 모든 critical resource가 Matrix. **Step 3의 핵심은 단순 capacity 계산이 아니라 ODM 협상·alternative 시나리오 도출**.

---

## 5. Time Fences — DTF / PTF / Demand Visibility

### 5.1 LAKA Time Fence 구조

```
T-3개월 ──┬── PTF (Planning Time Fence) 60일
         │   이 안: detailed planning 필수, slot 확약
         │
T-1개월 ──┼── DTF (Demand Time Fence) 30일
         │   이 안: forecast 무시, PO 기준만 운영
         │
T (출하)─┘
```

### 5.2 Time Zone별 운영 룰

| Zone | 기간 | 운영 룰 | 변경 권한 |
|------|------|---------|------------|
| **Frozen zone** | 0 ~ DTF (30일) | 변경 절대 불가 | 없음 (Mini-S&OP만) |
| **Slushy zone** | DTF ~ PTF (30-60일) | 변경 시 cost 발생 | Supply Planning Owner (재무 협의) |
| **Liquid zone** | PTF 이후 (60일+) | 자유 변경 | Demand Manager (단, 분기별 quarterly confirmation 영향 검토) |

### 5.3 Demand Visibility 요구

ODM에 제공해야 할 forecast의 정밀도:

| 호라이즌 | LAKA → ODM 제공 정밀도 | 변경 시 협의 강도 |
|----------|----------------------------|----------------------|
| 0-30일 (DTF 내) | 확정 PO | 변경 불가 |
| 1-3개월 (PTF 내) | Family 단위 ±10% | 분기 confirmation 갱신 |
| 3-12개월 | Family 단위 ±25% | 분기별 review |
| 12-18개월 | Annual forecast 수준 | Annual cycle |

→ LAKA가 ODM에 더 정확한 forecast 제공 = ODM이 더 안정적 슬롯 배정. **Bullwhip effect 감소의 핵심**.

---

## 6. Scalability 분석 (Implement Ch6 + LAKA 특화)

[[src_implement_sop_handbook|Implement Ch6]] 핵심: **공급망 스케일러빌리티는 각 엔티티마다 다른 범위·반응 시간을 갖는다**.

### 6.1 LAKA 공급 측 Scalability Range

| 영역 | 단기 (1주 내) | 중기 (1-4주) | 장기 (1-6개월) |
|------|------------------|------------------|-------------------|
| 한국콜마 립글로스 라인 | +0~5% (overtime) | +5~15% (추가 shift) | +20~50% (라인 증설·신규 ODM 추가) |
| 자재 (튜브·박스) | +5~10% (안전재고 활용) | +15~30% (협력사 추가 주문) | +50~100% (신규 협력사 onboarding) |
| 글로벌 라벨링 | +0~5% (overtime) | +15~25% (외주) | +50~100% (자동화 도입) |
| 창고 (4개국) | +10~20% (외부 임대) | +30~50% (3PL 추가 계약) | +100%+ (신규 권역 진입) |

### 6.2 반응 시간 vs 호라이즌 매핑

→ Volume forecast 변동이 어느 호라이즌에서 발생하느냐에 따라 활용 가능한 elasticity가 다름.

**예시**: 26-Aug에 베스트셀러 +30% 갑작스러운 demand 발생 (현재 26-Jul, 1개월 전 감지)

| 대응 옵션 | 효과 | 한계 | 권장 |
|-----------|------|------|------|
| 한국콜마 슬롯 +30% 추가 | +5~15% 가능 | 다른 브랜드 슬롯 빼앗기 어려움 | △ |
| 코스맥스 이중 발주 | +10~20% 가능 | 처음 발주 시 onboarding 1-2개월 | × (이미 1개월 전) |
| 안전재고 활용 | 30일치 = +100% 가능 (한 달) | 다음 달 재고 0 | ○ (단기 해결) |
| Demand 우선순위 조정 | 글로벌 채널만 만족, 국내 일부 hold | 매출 손실 | △ |
| Mini-S&OP Cycle | 위 옵션 통합 검토 | 의사결정 시간 필요 | ★ 권장 |

---

## 7. Constraint Identification & Escalation

### 7.1 Constraint 분류

| Type | 정의 | 대응 |
|------|------|------|
| **Hard constraint** | 일정 안에 해결 불가 (예: ODM 슬롯 max 도달) | Demand 조정 필요 |
| **Soft constraint** | 추가 비용·시간으로 해결 가능 | 비용·trade-off 분석 |
| **Material constraint** | 자재 lead time이 demand horizon보다 김 | 단기 대안: 안전재고 / 장기: 협력사 다변화 |
| **Capacity constraint** | 라인 가용 capacity vs 요구 | RCCP에서 식별, alternatives 도출 |
| **Inventory constraint** | 창고 capacity vs 재고 trajectory | 권역별 redeployment |

### 7.2 Escalation Framework

각 constraint에 대해 Pre-meeting 어젠다 양식:

| 항목 | 내용 |
|------|------|
| Issue ID | UNIQ ID |
| Family·Resource | 예: F01 ↔ 한국콜마 립글로스 라인 (R-KK-LG) |
| Time horizon | 예: 26-Aug |
| Gap | demand vs capacity 차이 (수치) |
| Root cause | NPI 출시 + 발렌타인 캠페인 동시 |
| Alternative A | 코스맥스 이중 발주 (cost +5% / lead time 2개월) |
| Alternative B | 안전재고 활용 (재고 30→5일) |
| Alternative C | 글로벌 우선·국내 hold (매출 손실 -3%) |
| Recommendation | Alt B + Alt A 병행 |
| Decision needed | CEO·CFO·SCM·마케팅 본부장 |

→ Pre-meeting (Step 4)에서 mid-mgmt가 권한 내는 자체 결정, 외는 Exec Meeting (Step 5)에 escalation.

---

## 8. Sally Smith Spreadsheet — Production·Inventory 블록 운영

### 8.1 Step 3가 채우는 행 (샘플 워크북 F01 시트 기준)

| 블록 | 행 | Step 3 책임 |
|------|----|-------------|
| Production | Planned Production | **Step 3 산출** ← Operations Plan |
| Production | Actual Production | Step 1에서 입력 (전월 actual) |
| Production | Difference, Cum Diff | 수식 자동 |
| Inventory | Planned Inventory | **Step 3 산출** ← Inventory projection |
| Inventory | Actual Inventory | Step 1에서 입력 |
| Inventory | Difference | 수식 자동 |

### 8.2 트래픽 라이트 의미 (Production·Inventory 측면)

| Production Difference | 의미 |
|-------------------------|------|
| 흰색 (±5%) | ODM 슬롯 정상 |
| 노란색 (±5-10%) | ODM 슬롯 미세 미달/초과 — 일회성 |
| 빨간색 (±10%+) | 구조적 capacity 이슈 — Pre-meeting 어젠다 후보 |

| Inventory Difference | 의미 |
|------------------------|------|
| 흰색 (±5%) | 재고 trajectory 정상 |
| 노란색 (±5-10%) | 재고 drift 주의 — 다음 사이클 보정 |
| 빨간색 (±10%+) | 과잉 또는 부족 위험 — production rate 조정 검토 |

---

## 9. LAKA Step 3 매월 Cadence

| Working Day | 활동 | 책임 |
|--------------|------|------|
| 4-5 | Step 2 인풋 받음 시작 (병행) | Supply Planning Owner |
| 4-5 | 한국콜마·코스맥스에 분기 slot 재확인 | SCM |
| 5-7 | Operations Plan 재계산 (Family별) | SCM (S&OP파트) |
| 7-8 | RCCP — Critical Resource Load 계산 | SCM |
| 8-9 | Inventory projection 산출 | SCM |
| 9 | Constraint identification + alternatives 도출 | SCM + 협력 부문 |
| 10 | Financial impact (재무 협업) | 재무 |
| 10 | **Senior Operations sign-off** | SCM 본부장 (김중찬) |
| 10 (저녁) | Pre-meeting 어젠다·자료 배포 | Supply Planning Owner |

→ Step 3 총 6-7 working days. Day 4-10 운영. Step 2와 4-7일 병행.

---

## 10. Supply-side KPI (W5에서 상세)

| KPI | 정의 | 목표 (Stage 2-3 진입 시점) |
|-----|------|------------------------------|
| **Production Plan Adherence** | 월간 actual production / planned production | 95-105% (±5%) |
| **Operations Plan Stability** | 직전 월 plan과 이번 월 plan의 차이율 (Slushy zone) | < 10% |
| **ODM Slot Utilization** | LAKA가 확보한 슬롯의 실제 사용률 | 90-95% (낮으면 over-confirmed) |
| **Inventory Days of Supply** | 재고 ÷ 평균 일일 demand | Safety Stock 목표값 ±20% |
| **Stockout Rate** | family·channel별 stockout 발생 빈도 | < 1% (베스트셀러) |
| **Capacity Headroom** | Critical Resource별 (가용 − 요구) / 가용 | > 5% (긴급 대응 여력) |
| **Constraint Resolution Rate** | Pre-meeting에서 raise된 constraint 중 해결률 | > 80% |
| **Time-fence Discipline** | DTF 안에서 PO 변경 발생 건수 | 0 (Mini-S&OP 제외) |

→ W5 sop_kpis에서 Demand-side KPI ([[demand_planning|2.]] 섹션 8)와 통합.

---

## 11. 흔한 실패 패턴 (W6에서 심화)

| 패턴 | 원인 | 대응 |
|------|------|------|
| ODM 슬롯 over-confirm 후 utilization 70%대 | "혹시 모를" 안전 confirm | utilization 추적·90% 미만 시 분기 조정 |
| DTF 안에서 PO 변경 빈발 | Demand 측 후행 인풋 | 단호한 DTF 규율 + Mini-S&OP만 예외 |
| 한국콜마·코스맥스 이중 발주의 무계획적 사용 | "양쪽 보험" 마인드 | 명시적 dual sourcing 룰 (예: 베스트셀러만 dual) |
| 자재 협력사 다변화 부재 | 단기 cost 최저 우선 | critical 자재 별 2nd source 확보 (Bullwhip 완화) |
| Inventory projection이 family 단위만, channel 분해 X | Master Schedule 영역 미구축 | W4 이후 Master Schedule 도입 검토 |
| Pre-meeting에 capacity 자료만, 재무 영향 없음 | 재무 협업 부재 | Step 3 cadence에 재무 sign-off 포함 |
| 모든 family에 동일 lot sizing 룰 | 단순화 | family별 룰 분리 (FLS·POQ·LFL) |
| Aligned vs Matrix 구분 없이 모두 RCCP 단순 적용 | 인식 부족 | Critical Resource 인벤토리 표 명시 + Matrix 슬롯 경쟁 시뮬레이션 |

---

## 12. 출력 (→ Step 4 Pre-meeting)

매월 Day 10 저녁까지 Pre-meeting 자료 패키지:

| 자료 | 형식 |
|------|------|
| 1. Updated Sally Smith Sheet (전 family) | Excel — Step 1·2·3 모두 채워진 상태 |
| 2. Capacity Check Report (RCCP) | Critical Resource × month, demand vs capacity 시각화 |
| 3. Inventory Projection by Family | 18개월 trajectory chart |
| 4. Unresolved Issues List | issue별 alternatives + recommendations 양식 |
| 5. Financial Impact Summary | KRW 영향 (Operations Plan 변경분) |
| 6. Major Resource Change Recommendations | 신규 ODM·외주·EOL 등 (Exec Meeting 검토) |
| 7. Customer Service Risk Note | Stockout 위험 family·channel·timing |

→ Pre-meeting (Step 4)이 받는 인풋. Step 4에서 cross-functional 의사결정 → Step 5 Exec Meeting 어젠다 확정.

---

## 관련 페이지

- [[sop_overview]] — W1 (Step 3 위치)
- [[sop_glossary]] — W2 (RCCP·DTF/PTF·Aligned vs Matrix·MTS/MTO/FTO·MOQ·Lot Sizing 용어 정의)
- [[data_gathering]] — 1. Data Gathering (Lead Time·MOQ 마스터 데이터 source)
- [[demand_planning]] — 2. Demand Planning (Step 2 산출 인풋)
- [[sop_kpis]] — W5 (예정), Supply-side KPI 운영
- [[sop_failure_patterns]] — W6 (예정), ODM over-confirm·dual sourcing 등 심화
- [[laka_sop_v1]] — W7 (예정), Step 1-3-4-5 통합 운영 매뉴얼
- [[ODM]] / [[ODM_발주_프로세스]] — LAKA 현행 supply 측 — Step 3가 여기로 이어짐
- [[한국콜마]] / [[코스맥스]] / [[K-뷰티_ODM_비교]] / [[한국콜마_vs_코스맥스_ODM_비교]] — 자세한 ODM 정보
- [[K뷰티_ODM_QA_실패_8유형]] — 공급 disruption 사례 (Mini-S&OP Cycle 학습 자료)
- [[OTD]] — Supply-side KPI base
- 📎 [laka_sop_template_v0.xlsx](./laka_sop_template_v0.xlsx) — F01_Sally_Smith 시트의 Production·Inventory 블록 데모
- [[src_wallace_executive_guide_book]] — Ch4 Step 3 원천
- [[src_wallace_executive_sop_workshop]] — RCCP·Alternative Scenarios 원천
- [[src_implement_sop_handbook]] — Ch6 Capacity & Inventory + 5 관점·Scalability 원천
- [[src_supply_chain_insights_sop_guide]] — Time Fences·Matrix Resources·Bullwhip 원천
