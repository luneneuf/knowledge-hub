---
title: "S&OP KPIs — Process · Outcome 통합"
type: concept
axis: work
tags: [work/sop, s&op, kpi, hard-benefits, soft-benefits, otd, fill-rate, laka]
created: 2026-05-11
updated: 2026-05-11
status: draft
publish: false
---

# S&OP KPIs — Process · Outcome 통합

> **본 페이지의 역할**: W5. S&OP 운영의 측정. **Process KPI** (Step 1·2·3 운영 품질) + **Outcome KPI** (Wallace Hard/Soft Benefits) 통합 + LAKA 기존 [[OTD]] 확장. Pre-meeting·Exec Meeting 대시보드 설계. Stage 1→3→4 진화에 따른 KPI 목표 progression.
>
> **연관 Linear 이슈**: [COM-24](https://linear.app/luneneuf) W5
>
> **선행**: [[data_gathering]] (1.) — 6 Process KPI / [[demand_planning]] (2.) — 6 Process KPI / [[supply_planning_odm]] (3.) — 8 Process KPI / [[sop_overview]] — Hard/Soft Benefits 프레임워크 / [[sop_glossary]] — Order Fill Rate·Line Fill Rate·MAPE·Bias·FVA 등 용어

---

## 0. KPI 분류 프레임워크

S&OP는 **2층 KPI 체계**로 측정:

```
┌──────────────────────────────────────────────────────┐
│ Layer 1 — Outcome KPIs (비즈니스 성과)              │
│   "S&OP를 잘 하면 비즈니스가 어떻게 좋아지나"        │
│   = Wallace Hard Benefits (정량) + Soft Benefits (정성) │
└──────────────────────────────────────────────────────┘
                          ▲
                          │ 영향
                          │
┌──────────────────────────────────────────────────────┐
│ Layer 2 — Process KPIs (S&OP 자체의 운영 품질)       │
│   Step 1 Data → Step 2 Demand → Step 3 Supply →      │
│   Step 4 Pre-meeting → Step 5 Exec Meeting           │
└──────────────────────────────────────────────────────┘
```

**원칙**:
- **Outcome KPIs는 천천히 움직임** — 6-12개월 단위 변화. Stage 진화의 척도.
- **Process KPIs는 빠르게 움직임** — 월간 측정. 운영 품질 즉시 진단.
- Process KPI를 잘 운영하면 → Outcome KPI가 따라옴 (Wallace: "Better decision-making processes lead to better decisions").

---

## 1. Process KPIs — Step 1·2·3 통합 (20개)

### 1.1 Step 1 Data Gathering — 6개 ([[data_gathering|상세]])

| # | KPI | 정의 | Stage 2-3 목표 | 측정 빈도 | 책임 |
|----|-----|------|------------------|------------|------|
| P1-1 | **Data On-time Rate** | 각 데이터 소스가 working day 3 cutoff 안에 도착한 비율 | > 95% | 월간 | Process Owner (SCM S&OP파트) |
| P1-2 | **Data Completeness** | 필수 필드(Family·SKU·Channel·UoM·Qty·Date) 채워진 row 비율 | > 99% | 월간 | Process Owner |
| P1-3 | **Master Data Drift** | 부서간 SKU·Family·Channel ID 불일치 건수 | 0 | 월간 | Master Data Steward |
| P1-4 | **Statistical Baseline FVA** | baseline이 naive forecast(last month = next month) 대비 정확도 개선% | > +10%p | 분기 | Demand Manager |
| P1-5 | **ODM Data Latency** | ODM 입고 데이터 도착까지 working days | ≤ 2일 | 월간 | SCM |
| P1-6 | **Channel Coverage** | 운영 채널 中 전월 sell-through 확보된 채널 % | > 95% | 월간 | 글로벌·국내사업 |

### 1.2 Step 2 Demand Planning — 6개 ([[demand_planning|상세]])

| # | KPI | 정의 | Stage 2-3 목표 | 측정 빈도 | 책임 |
|----|-----|------|------------------|------------|------|
| P2-1 | **MAPE (Family)** | Family 평균 절대 백분율 오차 | < 15% (베스트셀러) / < 25% (시즌·신규) | 월간 | Demand Manager |
| P2-2 | **MAPE (SKU)** | SKU 평균 절대 백분율 오차 | < 30% (베스트셀러 핵심 SKU) | 월간 | Demand Manager |
| P2-3 | **Bias (SOD)** | 누적 forecast − actual 합 | ±5% 이내 | 월간 (3-mo rolling) | Demand Manager |
| P2-4 | **FVA (Layer별)** | 각 layer baseline 대비 개선% | 모든 layer 양수 | 분기 | Demand Manager |
| P2-5 | **Consensus On-time** | 매월 working day 7까지 완료 비율 | 100% | 월간 | Demand Manager |
| P2-6 | **NPI Forecast Accuracy** | 신규 launch 첫 90일 actual vs base 시나리오 | ±50% | 신제품별 | Demand Manager + 프로덕트 |

### 1.3 Step 3 Supply Planning — 8개 ([[supply_planning_odm|상세]])

| # | KPI | 정의 | Stage 2-3 목표 | 측정 빈도 | 책임 |
|----|-----|------|------------------|------------|------|
| P3-1 | **Production Plan Adherence** | 월간 actual / planned | 95-105% | 월간 | Supply Planning Owner |
| P3-2 | **Operations Plan Stability** | 직전 월 plan vs 이번 월 plan 차이율 (Slushy zone) | < 10% | 월간 | Supply Planning Owner |
| P3-3 | **ODM Slot Utilization** | 확보 슬롯의 실제 사용률 | 90-95% | 월간 | SCM |
| P3-4 | **Inventory Days of Supply** | 재고 ÷ 평균 일일 demand | Safety Stock ±20% | 월간 | SCM |
| P3-5 | **Stockout Rate** | family·channel별 stockout 발생 빈도 | < 1% (베스트셀러) | 월간 | SCM + 글로벌·국내사업 |
| P3-6 | **Capacity Headroom** | (가용 − 요구) / 가용 (Critical Resource별) | > 5% | 월간 | SCM |
| P3-7 | **Constraint Resolution Rate** | Pre-meeting raise된 constraint 중 해결률 | > 80% | 분기 | Supply Planning Owner |
| P3-8 | **Time-fence Discipline** | DTF 안에서 PO 변경 발생 건수 | 0 (Mini-S&OP 제외) | 월간 | SCM |

### 1.4 Step 4·5 — 1개 (W7에서 상세)

| # | KPI | 정의 | Stage 2-3 목표 | 측정 빈도 | 책임 |
|----|-----|------|------------------|------------|------|
| P4-1 | **Exec Meeting Attendance** | 6 essential 참석자 중 실참 비율 | 100% (CEO 100% 또는 reschedule) | 월간 | CEO 비서·Process Owner |
| P5-1 | **Decision On-time Rate** | Exec Meeting 의사결정의 working day +2 안에 communicate되는 비율 | 100% | 월간 | Process Owner |

→ **총 Process KPIs 22개**. 모두 매월 또는 분기 단위 측정. Wallace 권장: 한 meeting에서 보는 KPI는 5-7개로 제한.

---

## 2. Outcome KPIs — Hard Benefits (정량)

Wallace 7개 표준 + LAKA 적용 ([[sop_overview|W1]] 인용):

| # | Hard Benefit | 측정 정의 | LAKA 측정 방법 | 6개월 baseline | 18개월 목표 |
|----|---------------|--------------|------------------|-------------------|----------------|
| O1 | **Customer Service ↑** | Order Fill Rate · Line Fill Rate | 채널 PO 충족률 (전체 채널 가중평균) | TBD (현행 측정) | +5-10%p |
| O2 | **Inventory ↓** | Inventory Days of Supply 또는 재고 turnover | 평균 재고 / 평균 일일 cost of goods | [[LAKA_재고_200억_구조분석\|현재]] | -15-25% |
| O3 | **Obsolescence ↓** | 폐기·할인처분 비율 (시즌 한정 컬러·EOL SKU) | 분기 폐기 KRW / 평균 재고 KRW | TBD | -30-50% |
| O4 | **Freight Costs ↓** | 출하당 운송비 (단위: KRW/unit shipped) | 월간 운송비 총액 / 출하 units | TBD | -5-10% (가급적 premium freight 회피) |
| O5 | **Order Lead Times ↓** | 주문 수령 → 출하 완료 days (채널·국가별) | 채널별 lead time 평균 | TBD | -10-20% |
| O6 | **Supplier Lead Times ↓** | ODM 발주 → 입고 days | 한국콜마 평균 lead time | 45-60일 | 30-50일 |
| O7 | **Time to Launch New Products ↓** | NPI 결정 → 전 채널 launch days | Eli Lilly 사례 비교: 11년 vs 산업 14년+ | TBD | -20-30% |
| O8 | **Plant Productivity ↑** | LAKA에서는 "ODM 슬롯 효율" = output / confirmed slot | 한국콜마 슬롯 utilization | TBD | +10-15% |

### 2.1 LAKA 우선순위 (자원 제약 고려)

| 우선순위 | Outcome KPI | 이유 |
|------------|---------------|------|
| **★★★** | O1 Customer Service, O2 Inventory | Designer/Distributor 핵심 — 채널 신뢰·운전자본 동시 영향 |
| **★★★** | O3 Obsolescence | 시즌 한정 컬러 빈번 — LAKA 특화 위험 |
| **★★** | O7 NPI Speed | K-뷰티 트렌드 사이클 빠름 — 경쟁 우위 |
| **★** | O4 Freight, O5/O6 Lead Times | 글로벌 채널 확장 시 중요해짐 |
| **○** | O8 Plant Productivity | LAKA 직접 운영 X, ODM 영향 |

---

## 3. Outcome KPIs — Soft Benefits (정성)

Wallace 7개 + 측정 방법 (대부분 서베이 또는 정성 진단):

| # | Soft Benefit | LAKA 측정 방법 | 빈도 |
|----|---------------|------------------|------|
| S1 | **Enhanced Teamwork** | 8부문 cross-functional 협업 만족도 서베이 (5점 척도) | 반기 |
| S2 | **Improved Communications (Institutionalized)** | "양 사이드 정보 비대칭이 줄었나?" 임원 평가 | 반기 |
| S3 | **Better Decisions, Less Effort/Time** | 의사결정 회의 수·시간 추이 (S&OP 도입 전후 비교) | 반기 |
| S4 | **Better $$$ Plans, Less Effort/Time** | 분기 예산 사이클 소요 시간 + 정확도 | 분기 |
| S5 | **Greater Accountability** | "각 부문의 plan 실행에 대한 책임이 명확한가?" | 반기 |
| S6 | **Greater Control** | "Bad surprises 발생 빈도" (예: 갑작스러운 stockout) | 분기 |
| S7 | **Window into the Future** | "임원진의 18개월 view 명확성" 자가 평가 | 반기 |

→ Wallace: *"Top management's handle on the business"* (가장 큰 Soft Benefit).

**측정 도구 권장**: 8부문 본부장 + 임원 대상 단일 페이지 서베이 (10문항, Likert 5점). 반기 1회.

---

## 4. OTD 확장 — Fill Rate 체계 ([[OTD|기존 페이지]] 연계)

기존 [[OTD]] = 공급업체→LAKA 측 KPI. S&OP 도입 후 **LAKA→채널 측 KPI** 추가 필요.

### 4.1 4-단계 Fill Rate Hierarchy

| Level | KPI | 정의 | 측정 |
|--------|-----|------|------|
| Supplier→LAKA | [[OTD]] (Order-based 또는 Quantity-based) | ODM·자재 협력사가 정시 납품한 비율 | 기존 운영 — 한국콜마·코스맥스 OTD |
| LAKA→Channel | **Line Fill Rate** | LAKA가 채널 PO의 line(SKU)별 정시·완전 출하 비율 | 신규 — channel별 |
| LAKA→Channel | **Order Fill Rate** | LAKA가 채널 PO의 order 단위 정시·완전 출하 비율 (line 중 1개라도 빠지면 0) | 신규 — 더 엄격 |
| LAKA→End Customer | **Perfect Order Rate** | 정시 + 완전 + 정확 + 손상 없음 + 정확한 invoice 모두 만족 | Stage 4+ |

### 4.2 LAKA Fill Rate 목표 (Stage 2-3 진입 시점)

| Family · Channel | Line Fill Target | Order Fill Target |
|--------------------|-----------------------|---------------------|
| 베스트셀러 (F01) · 세포라 US | > 98% | > 95% |
| 베스트셀러 (F01) · Boots UK | > 97% | > 93% |
| 시즌 한정 (F02) · 모든 채널 | > 90% (시즌 내) | > 85% |
| 글로벌 전용 (F08) · 채널별 | > 95% | > 90% |
| 국내 채널 모든 family | > 95% | > 92% |

→ Wallace Demand/Supply Strategy 양식 ([[sop_glossary|용어집]]): family별로 명시.

### 4.3 Stockout 분석 — 원인 분류

| 원인 | 책임 step | 대응 |
|------|------------|------|
| Forecast 과소예측 → 재고 부족 | Step 2 | Demand consensus 개선, FVA 측정 |
| ODM 슬롯 부족 → 생산 부족 | Step 3 | Capacity headroom 확보, dual sourcing |
| ODM 정시 납품 실패 (OTD↓) | 외부 | 협력사 다변화, OTD 모니터링 |
| 운송 지연 | 외부 | Freight forwarder 다변화, premium 옵션 hedge |
| 라벨링·finishing capacity 부족 | Step 3 | Finishing capacity 별도 추적 |
| 마스터 데이터 오류 → 잘못된 발주 | Step 1 | Master Data Drift KPI 0 유지 |

---

## 5. Sally Smith Sheet에서 자동 측정되는 KPI

샘플 워크북 [F01_Sally_Smith] 시트에서 직접 도출 가능:

| KPI | Sally Smith Sheet 위치 | 계산 방법 |
|-----|---------------------------|------------|
| Forecast Accuracy (Family) | Forecast 블록의 Cum Difference | 1 − \|Cum Diff\| / Cum Total Forecast |
| Production Plan Adherence | Production 블록의 Difference | Actual / Planned |
| Inventory Days of Supply | Inventory 블록의 Actual Inventory ÷ 평균 일일 demand | 별도 계산 |
| Bias (SOD) | Forecast 블록의 Cum Difference (3-mo) | 누적 합 |

→ **트래픽 라이트 색상**이 곧 KPI 시각화. 임원 5초 진단 가능.

### 5.1 워크북 KPI 자동화 확장 (v0 → v1)

| 현재 v0 | v1 추가 |
|----------|----------|
| Difference·Cum Diff 자동 계산 | MAPE_3mo 자동 계산 행 추가 |
| 트래픽 라이트 (Difference 행) | Cumulative Bias 차트 |
| KRW 환산 | Days of Supply 행 자동 계산 |
| FVA Tracking 시트 (12 row 예시) | FVA 자동 누적 + chart |
| — | Outcome KPIs 대시보드 시트 (Hard Benefits 7개) |

---

## 6. KPI 측정 cadence + 책임 매트릭스

| Cadence | KPI | 책임 | 보고처 |
|----------|------|------|---------|
| **매월** | Process KPI 22개 (Step 1·2·3·4·5) | 각 step owner | Pre-meeting (Step 4) |
| **매월** | Outcome KPI O1·O2·O3 (현행 측정 가능한 3개) | SCM | Exec Meeting (Step 5) |
| **분기** | Outcome KPI O4~O8 + FVA·Constraint Resolution | SCM + 재무 | 분기 임원 review |
| **반기** | Soft Benefit 서베이 (S1~S7) | CEO 비서 (서베이 운영) | CEO·이사회 |
| **연간** | Stage Maturity 진단 (SCI 5단계) | Process Owner | 연간 S&OP review |

---

## 7. Pre-meeting / Exec Meeting 대시보드 설계

Wallace 권장 **"한 meeting에 KPI 5-7개로 제한"**.

### 7.1 Pre-meeting (Step 4, mid-mgmt) — 7개 KPI

| # | KPI | 형식 |
|----|------|------|
| 1 | MAPE (Family, 전월) — Demand 정확도 | 표 (전 family) |
| 2 | Bias 3-mo rolling — Demand 편향 | 추이 chart |
| 3 | Production Plan Adherence (전월) | 표 |
| 4 | ODM Slot Utilization (전월) | 표 |
| 5 | Inventory Days of Supply by Family | 표 (트래픽 라이트) |
| 6 | Stockout Rate (전월) | 표 (event별) |
| 7 | Capacity Headroom (다음 3개월) | 표 |

### 7.2 Exec Meeting (Step 5, top mgmt) — 5개 KPI

| # | KPI | 형식 | 메시지 |
|----|------|------|---------|
| 1 | Macro $$$ Review — 전 family 합계 (units + KRW) | 1 slide | "이번 달 비즈니스 plan vs actual" |
| 2 | Customer Service Performance — Order Fill Rate (전 채널) | 1 slide | "고객 약속 지켰는가" |
| 3 | Inventory $$$ vs Target | 1 slide | "재고 자본 효율" |
| 4 | New Product Issues — NPI Forecast Accuracy + launch status | 1 slide | "혁신 속도" |
| 5 | Major Constraints (unresolved from Pre-meeting) | 1-2 slide | "결정 필요 이슈" |

---

## 8. KPI 목표 Progression — Stage 1 → 5

SCI 5단계 Maturity Model ([[sop_glossary|용어집]] §11) 진화에 따른 KPI 목표:

| KPI | Stage 1 (현재) | Stage 2 | **Stage 3** (18개월 목표) | Stage 4 | Stage 5 |
|-----|-----------------|----------|-----------------------------|----------|----------|
| MAPE (Family 베스트셀러) | 측정 안 함 | < 25% | **< 15%** | < 10% | < 8% |
| Bias (SOD) | 측정 안 함 | ±10% | **±5%** | ±3% | ±2% |
| Order Fill Rate (베스트셀러·세포라) | 측정 안 함 | > 92% | **> 95%** | > 97% | > 99% |
| Inventory Days of Supply | drift 없는 통제 부재 | Safety stock ±30% | **±20%** | ±10% | ±5% |
| Obsolescence rate | 측정 안 함 | 분기 측정 | **−30% vs baseline** | −50% | −70% |
| Time-fence Discipline | 빈번한 DTF 위반 | 월 5건 | **0건 (Mini-S&OP 제외)** | 0건 | 0건 |
| Exec Meeting Attendance | (회의 없음) | 80% | **100%** | 100% | 100% |
| Soft Benefit 평균 (5점 척도) | 측정 안 함 | 3.0 | **3.8** | 4.3 | 4.7 |

---

## 9. KPI Governance — 데이터 소스 일관성

### 9.1 KPI 출처 단일화 룰

| 영역 | Single Source of Truth | Owner |
|------|---------------------------|-------|
| Sales actual | ERP (월말 cutoff) | SCM |
| Forecast (모든 layer) | Sally Smith Sheet master file | Demand Manager |
| Production actual | ODM 입고 데이터 통합 | SCM |
| Inventory | 4개국 창고 시스템 통합 | SCM |
| 환율 | 재무 release | 재무 |
| ODM lead time·MOQ | Master_Data 시트 | SCM |

→ **하나의 KPI는 하나의 source만 사용**. 부서별 다른 source 사용 절대 금지.

### 9.2 KPI 변경 룰

| KPI 변경 유형 | 승인 |
|----------------|------|
| 목표값 (target) 조정 | CEO + SCM 본부장 |
| 측정 방법 (산식) 변경 | Process Owner + 영향 부문 |
| 신규 KPI 추가 | Exec Meeting 결정 |
| KPI 폐기 | CEO 결정 |

→ KPI 자체가 자주 바뀌면 추세 분석 불가. **분기 1회 review, 연 1회 정식 개정**.

---

## 10. 흔한 실패 패턴 (KPI 측면, W6에서 심화)

| 패턴 | 원인 | 대응 |
|------|------|------|
| KPI 너무 많아서 임원이 보지 않음 | "모든 걸 측정하자" 마인드 | Wallace 5-7개 룰 강제 |
| Process KPI만 측정·Outcome 무시 | 운영 부서 단독 운영 | Hard/Soft Benefits를 Exec Meeting에 명시 |
| KPI Gaming (수치 맞추기) | 인센티브 misalignment | KPI 자체보다 추세·맥락 강조, 다중 KPI 교차 검증 |
| Forecast Accuracy만 보고 Bias 무시 | 단순 MAPE 의존 | Bias·FVA·Layer별 분석 병행 |
| Soft Benefit 측정 안 함 | "정성은 측정 어렵다" | 단순 서베이 5점 척도로 시작 |
| Stockout 발생 시 책임 finger-pointing | 원인 분류 부재 | 원인 6 category 명시 (섹션 4.3) |
| KPI 목표값을 한 번 정하고 진화 안 시킴 | Stage 인식 부족 | Stage 1→5 progression 표 사용 |
| 측정 가능한 것만 측정, 중요한 건 측정 안 함 | 도구 한계 | 분기 KPI review에서 gap 평가 |

---

## 11. 출력 (S&OP 운영의 산출)

| 출력 | 받는 곳 | 빈도 |
|------|----------|------|
| Process KPI 22개 표 | Pre-meeting 어젠다 | 월간 |
| Outcome KPI 대시보드 (Hard 3개) | Exec Meeting | 월간 |
| Outcome KPI 전체 + Soft 서베이 | 분기 임원 review | 분기 |
| Stage Maturity 진단 + KPI progression | 연간 S&OP review | 연간 |
| KPI Variance + Root Cause Analysis | 다음 사이클 개선 | 분기 |

---

## 관련 페이지

- [[sop_overview]] — W1 (Hard/Soft Benefits 프레임워크)
- [[sop_glossary]] — W2 (Order Fill Rate·Line Fill Rate·MAPE·Bias·FVA·Demand/Supply Strategies 정의)
- [[data_gathering]] — 1. (Step 1 KPI 6개 상세)
- [[demand_planning]] — 2. (Step 2 KPI 6개 상세)
- [[supply_planning_odm]] — 3. (Step 3 KPI 8개 상세)
- [[sop_failure_patterns]] — W6 (예정), KPI Gaming·측정 함정 심화
- [[laka_sop_v1]] — W7 (예정), Pre-meeting·Exec Meeting 대시보드 구체 디자인
- [[OTD]] — 기존 KPI 페이지 (supplier→LAKA 측). 본 페이지에서 LAKA→channel 측 KPI 보강
- [[공급망_KPI]] — 보충 자료
- [[LAKA_재고_200억_구조분석]] — Inventory baseline
- [[K뷰티_립_CS_벤치마크]] — Customer Service 비교 reference
- 📎 [laka_sop_template_v0.xlsx](./laka_sop_template_v0.xlsx) — Sally Smith Sheet의 KPI 자동 측정 데모
- [[src_wallace_executive_guide_book]] — Ch1 Hard/Soft Benefits 원천
- [[src_wallace_executive_sop_workshop]] — Hard/Soft Benefits 워크샵 버전
- [[src_implement_sop_handbook]] — Ch9 Finance in S&OP + KPI 호라이즌별 설정
- [[src_supply_chain_insights_sop_guide]] — Maturity Model 단계별 KPI progression
