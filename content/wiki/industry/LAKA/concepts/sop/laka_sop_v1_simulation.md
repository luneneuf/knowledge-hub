---
title: "LAKA S&OP v1 — Pilot 90일 운영 시뮬레이션 + 회고"
type: concept
axis: work
tags: [work/sop, s&op, laka, simulation, pilot, retrospective, v1-to-v2]
created: 2026-05-11
updated: 2026-05-11
status: draft
publish: false
---

# LAKA S&OP v1 — Pilot 90일 운영 시뮬레이션

> ⚠️ **시뮬레이션 — Wallace "Bad Day at Acme Widget" 양식 차용**
>
> 본 페이지는 [[laka_sop_v1|W7 Playbook]]을 base로 **Pilot 90일을 가상 운영**한 시뮬레이션 narrative입니다. Cycle별 발견·issue·의사결정·학습을 storytelling 형식으로 정리. 실제 LAKA에서 발생할 만한 패턴 예측 + v1 보정안 도출.
>
> **사용 모든 인물·사건은 시뮬레이션**. 실제 LAKA 임원의 발언·행동·의사결정 아님. 본 페이지가 W7 + 실제 데이터의 갭을 식별하는 사고 실험 가치.
>
> **연관 Linear 이슈**: [COM-27](https://linear.app/luneneuf) W8

---

## 0. 시뮬레이션 타임라인

```
2026-07-01   Phase 1 Executive Briefing (60분)
2026-07-15   Kickoff Session (반나절) — Master Scheduling Policy sign-off
2026-08-01   Cycle 1 Step 1 시작 ★
2026-08-15   Cycle 1 Exec Meeting
2026-09-01   Cycle 2 Step 1
2026-09-15   Cycle 2 Exec Meeting
2026-10-01   Cycle 3 Step 1
2026-10-15   Cycle 3 Exec Meeting
2026-10-20   Phase 2 회고
2026-10-25   Go/No-Go #2 결정
```

→ Phase 2 = 8월·9월·10월 3개월. 11월부터 Phase 3 Expansion 시작 (시뮬레이션 YES 시나리오).

---

## 1. Cycle 1 — 2026년 8월 (Discovery)

### 1.1 시작 상태

- Master Data 거버넌스 6 영역 사전 정의 — 단, 부서간 ID drift 미확인
- 통계 baseline 처음 산출 — F01·F08 둘 다 24개월 과거 데이터 활용
- 6 essential VP 처음 cadence 노출 — 모두 처음 경험
- Demand Manager (마케팅 BM/PM 파트장 김OO) + Process Owner (SCM SC기획팀장 박OO) — 둘 다 운영 첫 cycle

### 1.2 Cycle 1 Step별 발견

#### Step 1 (Day 1-3) — Master Data 첫 충돌

**Day 1 09:00** — SCM SC기획팀장 박OO이 7월 ERP 출하 batch 산출. F01 출하 14,200개. 그런데 마케팅이 ERP에서 다운로드한 F01 출하는 13,800개. **400개 차이**.

원인 추적 — 한 SKU(LK-LG-207, 207 모브)가 SCM ERP에는 "F01" Family로, 마케팅 다운로드에는 "립글로스_핵심"으로 분류되어 있음. 다른 부서가 다른 alias 사용.

**Day 1 14:00** — 박OO이 Master Data Steward(SCM SC기획팀 임OO) 호출. 즉시 정비:
- Family ID 표준화 결정 — F01 ~ F08 ID만 사용. "립글로스_핵심" 같은 alias 금지.
- 모든 부서 ERP·BI 대시보드의 Family 컬럼 통일 작업 시작 (1주일 예상)

→ **첫 발견 — [[sop_failure_patterns|W6]] Pothole #3 (Planning Master Data) LAKA 실제 사례**.

**Day 2** — ODM 입고 데이터 한국콜마에서 도착. 그런데 7월 셋째 주 입고 데이터가 빠짐. SCM이 한국콜마 SCM 담당자에게 문의 → "월말 batch만 보내드린다고 했는데요" — **이 정보 자체가 LAKA 측 SCM에 사전 합의 안 된 사실**.

**Day 2 16:00** — SCM 본부장 김중찬이 한국콜마에 weekly batch 협조 요청 공문. 답변 D+5 (한국콜마 내부 ERP 작업 필요).

**Day 3** — 통계 baseline 첫 산출. F01 8월: 12,000개. F08 8월: 7,500개. Demand Manager 김OO이 24개월 과거 데이터로 지수평활 (α=0.3) + 시즌 계수 적용. F01은 합리적, F08은 launch 후 12개월만 데이터 있어 변동성 큼.

#### Step 2 (Day 4-7) — Sales 첫 baseline·campaign 통합 인풋

**Day 4 10:00** — Marketing Adjustment 양식 배포. 다음 18개월 Campaign 일정 + Promotion 추정.

**Day 5 11:00** — 글로벌사업 본부장 손여진의 인풋 도착. F01 세포라 US 8월: **18,000개**.

Demand Manager 김OO이 baseline 12,000 + Marketing campaign +1,000 + Sales +5,000 = 18,000? 그런데 손여진은 "그냥 18,000 forecast"라고만 적었음. **Baseline·campaign 분리 안 함**. → 모든 layer가 합쳐서 들어옴.

**Day 5 14:00** — 김OO이 손여진에게 전화. "본부장님, 이번 회의 양식이 layer별 분리거든요. 어디까지가 평소 patterns이고 어디부터가 추가 캠페인인지..." 손여진: *"평소 그렇게 안 봐요. 그냥 8월 18K이면 18K지."*

→ 첫 cycle은 통합 인풋 그대로 받고, Pre-meeting에서 Sales adjustment 가중치 평가는 보류. Cycle 2부터 양식 강제 학습.

**Day 7 15:00** — Demand Consensus Meeting. 마케팅·국내·글로벌·프로덕트·CFO 위임 1명 참석. 60분 예정이 90분 초과. 이유: F08 (글로벌 전용 SKU) launch curve 시나리오 base/opt/pess 합의 안 됨.
- 프로덕트 이정미: "base = 7,500개"
- 마케팅 안일홍: "조금 conservative한 듯, base는 9,000 가능"
- 글로벌사업 손여진: "**세포라 매장 80개 확장 결정 받았어요. 12,000 가능**."

**손여진 발언이 polite bomb**. 매장 80개 확장 정보는 본 회의 전에 SCM이나 마케팅에 공유되지 않았음. → Step 3 ODM 슬롯 재계산 필요. CEO 의사결정 사항이 될 수 있음.

#### Step 3 (Day 4-10) — ODM 슬롯 첫 위기

**Day 8 09:00** — Supply Planning Owner (SCM 본부장 김중찬)이 손여진 정보로 RCCP 재계산. F08 base scenario 7,500 → 12,000 변경 시 한국콜마 립글로스 라인 8월 슬롯 부족.

기존 confirm:
- F01: 11일 (=11,000개)
- F02 (시즌 한정, Pilot 외 family): 2.5일
- F08: 4.2일 (=5,000개 dual sourcing 50% + 한국콜마 50% = 7,500 가정)
- **Total: 17.7일 / 가용 18일 → Headroom 0.3일 (1.7%)** ✗

F08 base 12,000 변경 시 한국콜마 측 8.4일 필요 → Total 22.1일 → **−4.1일 deficit**.

**Day 9** — 김중찬이 한국콜마에 슬롯 +4.1일 추가 요청. 답변: "다른 브랜드와 조정 필요. 1주일 시간 주세요" (이미 슬롯 경쟁 — Matrix Resources의 현실).

Alternative 3개 도출:
- A. 코스맥스 dual sourcing F08 50% → 100%로 증가 — cost +12%, 단 cycle 1 안에 onboarding 어려움
- B. F01 한국콜마 슬롯 1일 양보 (재고 활용 — 현재 17,000개 = 1.5개월 supply) — F01 단기 부족 위험
- C. F08 base scenario를 9,000으로 합의 (손여진 12,000과 SCM 7,500의 중간) — 매출 기회 일부 포기

→ **Pre-meeting 어젠다 1순위**.

#### Step 4 Pre-meeting (Day 13)

**Day 13 14:00** — 90분 예정. 참석 8명. 진행:

| Min | Section | 발견 |
|------|----------|--------|
| 0-10 | Process KPI review | 22개 중 14개 측정 가능. Data On-time Rate 67% (ODM 데이터 latency 영향) |
| 10-25 | F01 review | Difference Cum -3K (7월 actual sales 13.5K vs forecast 14K). 트래픽 라이트 노랑 |
| 25-40 | F08 review | base scenario 합의 안 됨. 3 alternative 보고 |
| 40-55 | NPI status | (Cycle 1은 NPI 없음, skip) |
| 55-70 | Constraints | F08 ODM 슬롯 deficit -4.1일 |
| 70-80 | **Moose Top 3** | ①Sales layer별 분리 안 함 ②ODM 슬롯 정보 공유 부재 ③글로벌·SCM 간 정보 비대칭 |
| 80-95 | Exec Meeting 어젠다 | F08 base 합의·ODM alternative C 추천 |

**90분 → 95분 초과**. Moose Top 3 raise는 의미 있었으나 해결 시간 부족. 다음 cycle 90분 엄수 결정.

#### Step 5 Exec Meeting (Day 15)

**Day 15 14:00** — 90분. CEO 이지철 + 6 essential VP. 첫 Exec Meeting.

**의사결정 1** (F08 base scenario):
- 손여진 12,000 vs 김중찬 7,500 → 안일홍이 "8월은 9,000으로 시작, 9월 sell-through 보고 재조정" 제안. CEO 승인. 
- → **Sales Plan 변경** (Wallace 의사결정 4 유형 #1)

**의사결정 2** (ODM 슬롯):
- Alt C 채택 (F08 9,000개) → 한국콜마 추가 슬롯 필요 없음. 코스맥스 dual sourcing은 9월에 onboarding 시작.
- → **Operations Plan 유지** (#4 None of the above)

**의사결정 3** (정보 흐름):
- CEO: *"오늘 회의에서 본 데이터, 그동안 보지 못한 것 많네. 매월 이거 보자고."*
- Soft 결과 — CEO commitment 강화.

**Critique of Meeting** (마지막 5분):
- 김중찬: "Pre-meeting에 ODM 정보 더 일찍 알았어야"
- 이종영 CFO: "F08 9,000개 KRW 환산은 어떻게 됐는지 자료 봐도 안 보임" — **재무 인풋 미흡**

### 1.3 Cycle 1 학습 (5개)

1. **Master Data ID drift 즉시 발견** → Master Data Steward 임명·정비 시작
2. **ODM 데이터 latency 5-10일 → 1-3일 협조** 필요. 한국콜마와 합의 진행
3. **Sales layer별 분리 인풋** 합의 어려움 — Cycle 2부터 양식 강제
4. **정보 흐름 비대칭** — 글로벌사업 → SCM 정보 공유 룰 필요
5. **재무 환산 시점** — Pre-meeting까지 KRW 환산 미흡. 재무 인풋 cadence 보강

---

## 2. Cycle 2 — 2026년 9월 (Discipline)

### 2.1 시작 상태

- Master Data ID 정비 1주일 만에 완료
- 한국콜마 weekly batch 협조 시작 (월말 batch + weekly summary)
- Layer별 분리 인풋 양식 강제 시작
- F08 코스맥스 dual sourcing onboarding (9월 첫 PO)

### 2.2 Cycle 2 발견

#### Step 1 (Day 1-3)

**Day 1** — Master Data ID 통일 후 ERP·BI 데이터 일치 확인. 부서간 drift = 0.

**Day 2** — 한국콜마 weekly batch 첫 도착. ODM Data Latency 1.5일로 단축.

→ Process KPI 개선: Data On-time Rate 67% → 92%.

#### Step 2 (Day 4-7)

**Day 5 14:00** — 손여진의 글로벌 인풋 도착. 이번에는 **Baseline · Campaign · NPI 분리 양식**으로:

| F01 9월 | base | campaign | NPI | total |
|---------|------|----------|-----|-------|
| 세포라 US | 8,000 | +2,000 (백투스쿨) | 0 | 10,000 |
| Qoo10 JP | 3,500 | 0 | 0 | 3,500 |
| 한국 OL | 4,500 | +500 (가정의 달) | 0 | 5,000 |

→ **Cycle 1 학습 #3 성공**. 양식 강제 효력. 김OO Demand Manager가 손여진에게 *"본부장님, 이번 양식 보기 좋아요. 감사해요"*.

**FVA 첫 측정**:
- Layer 1 (Baseline): 8월 actual 13.5K vs forecast 14K → APE 3.6%
- Layer 2 (+Marketing): 14K → 같은 (Cycle 1 통합 인풋이었음, FVA 측정 불가)
- Layer 3 (+Sales): 18K → APE 33% — **Sales 단기 과대예측 패턴 첫 확인**
- Layer 4 (Consensus): 14K → APE 3.6% (Consensus가 Sales를 보정함)

→ Cycle 2 인풋부터는 분리 추적 가능. Cycle 3에 3-mo MAPE·FVA 첫 의미 있는 데이터.

#### Step 3 (Day 4-10)

**Day 6** — F08 코스맥스 dual sourcing 첫 PO 발행. 4,000개 (50%). 한국콜마 5,000개 (50%). Total 9,000개.

**Day 8** — RCCP 재계산. 한국콜마 슬롯 정상. 단, F08 코스맥스 측 처음 PO라 품질·납기 위험 있음 → Stockout Risk Note 별도 작성.

#### Step 4 Pre-meeting (Day 13)

**Day 13 14:00** — 90분 엄수. Cycle 1 95분의 학습.

진행:
- Process KPI 22개 중 18개 측정 가능 (전월 14개)
- F01 트래픽 라이트 흰색 (Difference Cum 안정)
- F08 트래픽 라이트 노랑 (8월 actual 8,000 vs Consensus 9,000 → -1K)
- Constraint 없음 (한국콜마 슬롯 정상)
- **Moose Top 3** — ①코스맥스 dual sourcing 품질 위험 (첫 PO) ②글로벌사업 17명의 채널별 인풋 표준 부재 ③국내사업 본부장 공석 — CEO 임시 owner의 시간 부담

#### Step 5 Exec Meeting (Day 15)

**60분 단축 완료**. Wallace Sample Agenda 8 항목 sequential 진행. 의사결정 3건:

1. F08 base scenario 9월 actual 추세 따라 10월 7,500 → 8,500으로 상향
2. 코스맥스 첫 PO 품질 모니터링 — 9월말 입고 시 QA 결과 review (Mini-S&OP 발동 가능성)
3. 국내사업 본부장 임명 일정 — CEO 자체 deadline 12월 1일

**Critique**:
- 이정미 (프로덕트): "60분으로 단축됐는데 가져갈 게 더 명확해짐"
- 이종영 CFO: "KRW 환산 자료 이번에 좋았어요. F01·F08 합계 8월 35억원 → 9월 38억원, 분기 누적 추세 ±3%."

### 2.3 Cycle 2 학습 (4개)

1. **Layer 분리 양식 효력 확인** — Sales 33% APE 첫 정량 발견
2. **Master Data 정비 후 KPI 즉시 개선** — Data On-time 67→92%
3. **F08 첫 발견 → Consensus 보정 작동** — 9,000개 합의가 적절했음
4. **90분 엄수 가능** — 사전 자료 준비 + facilitator 진행 강화

---

## 3. Cycle 3 — 2026년 10월 (Stabilization)

### 3.1 시작 상태

- 9월 actual: F01 14,500개 (Consensus 14,000 → +500), F08 7,800개 (Consensus 9,000 → -1,200)
- **3-mo MAPE 첫 산출 가능** (Aug/Sep/Oct)
- 코스맥스 첫 PO 입고 — QA 결과: 1,200개 중 28개 불량 (2.3% 불량률, 한국콜마 평균 0.8% 대비 高)

### 3.2 Cycle 3 발견

#### Step 1 — 자동화 시도

박OO Process Owner이 ERP·창고 데이터 통합 Excel macro 작성. Day 1 데이터 수집 시간 4시간 → 1시간 단축. → **Process Owner skill 가치**.

#### Step 2 — 3-mo FVA 첫 의미 있는 데이터

| Family | Layer | 8월 APE | 9월 APE | 10월 APE | **3-mo MAPE** | **FVA vs Baseline** |
|---------|-------|----------|----------|-----------|------------------|------------------------|
| F01 | 1. Baseline | 3.6% | 3.4% | 3.7% | 3.6% | (base) |
| F01 | 3. + Sales | 33% | 6.7% | 5.5% | **15.1%** | **−11.5%p** (악화) |
| F01 | 4. Consensus | 3.6% | 3.6% | 3.4% | 3.5% | +0.1%p (개선) |

→ **Sales layer가 일관 음수 FVA**. [[sop_failure_patterns|W6]] Type C — Sales 단기 과대예측 패턴 정량 확인. Cycle 4부터:
- Sales layer 가중치 0.3 → 0.15
- 분기 회고에 Sales 교육 항목 포함

#### Step 3 — 코스맥스 품질 issue

**Day 7** — QA 결과 보고. F08 코스맥스 1,200개 중 28개 불량. 김중찬: *"품질 SLA 합의 필요. 2% 임계로 정하고 초과 시 재검사 룰."*

→ **Mini-S&OP 발동 trigger** — Supply quality crash. 그러나 발동 안 함 — 영향 family·channel 1개씩으로 한정, 정규 Pre-meeting에서 처리 가능.

#### Step 4 Pre-meeting (Day 13)

**Process KPI 22개 중 20개 측정 가능**. 첫 의미 있는 분기 추세 보임:

| KPI | 8월 | 9월 | 10월 | 추세 |
|-----|-----|-----|------|------|
| Data On-time Rate | 67% | 92% | 95% | ★ |
| Production Plan Adherence (F01) | 95% | 98% | 97% | 안정 |
| ODM Slot Utilization (한국콜마) | 88% | 92% | 90% | 안정 |
| Order Fill Rate (세포라 US, F01) | 94% | 96% | 97% | ↑ |
| Exec Meeting Attendance | 100% | 100% | 100% | ★ |

**Moose Top 3**:
- ①Sales FVA 음수 → 교육 필요 (위 정량 발견)
- ②코스맥스 품질 SLA → 정식 협상 필요
- ③Phase 3 Expansion 시 family 6개 추가 → Demand Manager 1명으로 가능한지

#### Step 5 Exec Meeting — Phase 2 마지막 회의

**의사결정**:
1. Sales 교육 — 11월 워크샵 (글로벌·국내사업 + 마케팅) — *"forecast는 target이 아니다"* 메시지
2. 코스맥스 품질 SLA — 김중찬 + CFO 협상 권한
3. Phase 3 Expansion **YES** — 다음 4개월 family 6개 추가 + Demand Manager 1명 추가 인력 검토

**CEO 발언 (Soft Benefit)**:
*"3개월 전에는 매월 이 정도 정보를 1시간에 보지 못했어요. 옛날에는 부서별 부분 데이터 받아서 큰 그림 못 그렸는데. 이게 'window into the future'네요."*

→ Wallace Soft Benefit S7 (Window into the Future) 실현 첫 사례.

### 3.3 Cycle 3 학습 (5개)

1. **3-mo FVA가 Sales 패턴 확실히 드러냄** — 정성 의심이 정량 evidence로
2. **Process Owner 자동화 skill** — Data On-time KPI 95%까지 도달
3. **Mini-S&OP 발동 안 함이 정상** — 정규 cycle이 흡수 가능한 issue는 routing
4. **CEO commitment 확신** — Window into the Future 실현
5. **Phase 3 진입 준비** — Demand Manager 인력 확장 검토 필요

---

## 4. Phase 2 회고 (Day 76-90, 2026년 10월 셋째 주)

### 4.1 W7 회고 양식 평가 결과

[[laka_sop_v1|W7]] §8.1 회고 양식 8개 항목 — 4점 척도 (0=문제·1=문제 있음·2=정상·3=우수):

| 항목 | 점수 | 증거 |
|------|------|------|
| Process KPI Stage 진화 | **3** | 22개 중 20개 측정 가능, 8개 안정 |
| Cadence 정착 | **3** | 9 회의 모두 on-time, 모든 회의 attendance 100% |
| Master Data drift | **3** | Cycle 1 정비 후 drift 0 유지 |
| FVA layer별 결과 | **2** | Baseline·Consensus 양수, Sales 음수 (의도된 발견) |
| Order Fill Rate (3 채널) | **2** | F01 세포라 94→97%, Qoo10 정상, 한국 정상 |
| Capacity Headroom 추세 | **3** | 한국콜마 88→92%·90%, 안정 zone |
| Broken Process 7 신호 | **3** | ✓ 0개 (모두 ✗) |
| Soft Benefit 정성 | **2** | CEO·CFO·SCM 본부장 명시 인용. 다른 VP 정성 평가 미수집 |

**평균: 2.6 / 3.0** = 우수 zone (2.0+).

### 4.2 Go/No-Go #2 결정

[[laka_sop_v1|W7]] §8.2 7개 YES 조건:

| 조건 | 결과 |
|------|------|
| Process KPI 50%+ 측정 가능 | ✓ (91%, 20/22) |
| Exec Meeting Attendance 100% (3/3) | ✓ |
| Cycle 3 FVA layer 양수 (baseline·marketing) | ✓ (3.5% MAPE) |
| Sally Smith Sheet 자동화 안정 | ✓ (Cycle 3 자동화 시작) |
| Soft Benefit 정성 평균 3.0+ | △ (정량 미수집, CEO·CFO 인용은 4.0+ 수준) |
| Broken Process 7 신호 ≤2 ✓ | ✓ (0개) |
| CEO commitment 지속 | ✓ |

→ **6/7 YES, 1/7 △** (Soft Benefit 정량 미수집은 다음 사이클에 서베이 도입). **Phase 3 진행 결정**.

### 4.3 시뮬레이션 Pilot의 가장 큰 발견

| Top | 발견 | Type |
|------|------|------|
| 1 | **Master Data ID drift는 즉시 발견·해결 가능** — Cycle 1 1주 만에 정비 | Type B (Pothole) → 해결 |
| 2 | **Sales 단기 과대예측 패턴은 3-mo FVA로만 확실히 드러남** — 1 cycle 데이터로는 noise vs signal 구분 어려움 | Type C |
| 3 | **글로벌사업 → SCM 정보 흐름 비대칭** — 세포라 매장 80개 확장 정보 사례 | Type A (Conflict Aversion 미흡) |
| 4 | **ODM 데이터 latency 협조 가능** — 한국콜마는 협조적, 코스맥스는 미정 | Type C |
| 5 | **CEO Window into the Future 실현** — Wallace Soft Benefit 가장 큰 가치 | Type A 해결 |
| 6 | **Process Owner skill의 중요성** — Excel macro 작성 능력 = Data on-time KPI | Type B (Pothole) → 자동화 진화 |
| 7 | **Pre-meeting Moose Top 3 효력** — 매 cycle 의미 있는 갈등 표면화 | Type A 해결 |

---

## 5. v1 → v2 보정안

90일 시뮬레이션에서 발견된 v1 한계 + v2 보정안:

### 5.1 W7 자기 평가 갭 10개 점검 결과

| W7 §14 갭 | Pilot에서 확인 결과 | v2 보정안 |
|-------------|------------------------|------------|
| Family 정의 일치성 | F01·F08 운영 가능. 단 마케팅 alias "립글로스_핵심"이 ID 충돌 발견 | ID 표준 단일 강제 룰 명시 |
| ODM 운영 cadence | Annual·Quarterly·Monthly PO 모두 실제 작동. 코스맥스 처음 onboarding 1.5개월 소요 | 코스맥스 dual sourcing 1.5개월 lead time 명시 |
| 단가·MOQ·Lead Time | 추정값 대체로 정확. F08 코스맥스 50% dual은 비용 +12% (시뮬레이션 추정) | 정확한 비용 표 추가 |
| 8부문 본부장 commitment | 시뮬레이션상 모두 100% 참석. 단 Soft Benefit 서베이 미수집 | 반기 서베이 cadence 추가 |
| 국내사업 본부장 공석 | CEO 임시 owner 부담 큼. 12월 임명 deadline 시뮬레이션 | 공석 시 명시 운영 룰 추가 |
| 마스터 데이터 현행 | Cycle 1에 ID drift 발견 → 1주 정비. 가능성 검증 | Phase 1 직후 즉시 Master Data audit 단계 추가 |
| 시스템 통합 갭 | 매뉴얼 Excel·BI 가능. 자동화 Cycle 3에 Process Owner이 자체 macro | Phase 3에 ETL·RPA 정식 도입 plan |
| ODM 데이터 협조 | 한국콜마 협조적·코스맥스 미정 | 코스맥스와의 합의 step 추가 |
| 환율 단일 release | CFO 협조 검증 — Cycle 2 Pre-meeting부터 정상 | (변경 없음) |
| 분기 budget 통합 | Phase 2 종료 시점이 LAKA 분기말 아님. 통합 검증 미흡 | Phase 4에 분기 budget·S&OP 통합 매뉴얼 추가 |

### 5.2 v1 추가 보강 사항 (Phase 3 진입 전 추가 필요)

| 추가 | 이유 |
|------|------|
| Sales 교육 워크샵 매뉴얼 | "forecast는 target이 아니다" 메시지 — Cycle 3 발견 |
| 코스맥스 품질 SLA 양식 | 첫 PO 2.3% 불량률 (한국콜마 0.8% 대비) — Cycle 3 발견 |
| 글로벌사업 → SCM 정보 공유 룰 | 세포라 매장 확장 사례 — Cycle 1 발견 |
| Process Owner skill 진화 path | Excel macro → ETL → APS — Phase 3-4 |
| 분기 회고 서베이 양식 | Soft Benefit 정량 측정 — Phase 2 회고에서 미수집 |

### 5.3 Pilot에서 발견된 위험 → v2 Risk Register 추가

| 신규 Risk | 확률 | Impact | 대응 |
|------------|------|----------|------|
| 코스맥스 품질 변동성 (vs 한국콜마) | 高 | 중 | 품질 SLA·재검사 룰·dual sourcing 비율 동적 조정 |
| Sales 단기 과대예측 패턴 정착 | 高 | 중-高 | 교육·FVA 측정·가중치 조정 |
| Process Owner 1명 의존 | 중 | 큼 | 후임 1명 사전 식별·문서화 |
| Soft Benefit 서베이 정착 어려움 | 중 | 낮 | 단순 5점 척도 5문항으로 시작 |

---

## 6. 시뮬레이션 학습 — 책상머리의 가치와 한계

본 시뮬레이션을 통해 학습한 본질적 깨달음:

### 6.1 책상머리 시뮬레이션의 가치

| 가치 | 구체 |
|------|------|
| **사고 실험 도구** | Wallace 책의 추상 개념(Moose·Bullwhip·Behavior Change)이 LAKA 맥락에서 어떻게 발현될지 narrative로 그려봄 |
| **갭 식별** | W7 §14 자기 평가 갭 10개가 시뮬레이션에서 실제로 8개 검증·2개 새 발견 |
| **운영 자료 양식 검증** | Sally Smith Sheet·Master Scheduling Policy·Pre-meeting 어젠다가 sequentially 작동하는지 검증 |
| **위험 사전 식별** | 9개 W7 Risk + 4개 새 위험 식별 |
| **임원 교육 자료** | Pilot 시뮬레이션 narrative 자체가 Phase 1 Executive Briefing의 일부로 활용 가능 ("이런 사건이 발생할 것입니다") |

### 6.2 책상머리의 한계

| 한계 | 본질 |
|------|------|
| **사람의 반응 예측 못 함** | 손여진 본부장의 "그냥 18K이면 18K지" 발언은 합리적 추정이지만, 실제는 다른 반응 가능성 多 |
| **Master Data 현황의 실제 복잡도 모름** | 실제 LAKA의 ERP·BI·창고 시스템 통합 갭은 더 클 수도, 작을 수도 |
| **ODM 협상력 모름** | 한국콜마 weekly batch 협조는 시뮬레이션상 5일 만에 합의. 실제는 분기 협상일 수도 |
| **Soft Benefit 시뮬레이션 어려움** | CEO "Window into the Future" 발언은 본 시뮬레이션의 가장 큰 가정. 실제 시작은 더 회의적일 수도 |
| **Outcome KPI 미반영** | Hard Benefit 8개 (Inventory ↓·Obsolescence ↓ 등)는 시뮬레이션 길이 90일로 불충분 — 6-12개월 호라이즌 |

### 6.3 결론 — Wallace 가르침 재확인

> *"Behavior Change ≠ Fact Transfer. 다이어트 책 읽는다고 살 빠지지 않는다."*

본 W8 시뮬레이션은 **고도화된 fact transfer**. behavior change는 실제 LAKA에서만 가능. 단, fact transfer의 완성도가 높을수록 behavior change 진입 후 첫 30일이 부드러움.

---

## 7. 다음 단계 (실제 적용 시)

만약 천승범 본부장(또는 다른 사용자)이 LAKA 또는 유사 회사에 본 wiki를 들고 가서 적용한다면:

### 7.1 W7 + W8 활용 방법

| 자료 | 활용 |
|------|------|
| [[sop_overview\|W1]] | Phase 1 Executive Briefing 60분 발표 자료 |
| [[sop_failure_patterns\|W6]] | 8부문 워크샵 토론 자료 (위험 진단) |
| [[laka_sop_v1\|W7]] §2.4 예상 반론 6개 | Briefing 동안 사용 |
| [[laka_sop_v1\|W7]] §4 Master Scheduling Policy 양식 | Kickoff Session에서 LAKA-customized 후 sign-off |
| 📎 laka_sop_template_v0.xlsx | Briefing 시연 + Phase 2 Pilot 도구 |
| **W8 본 페이지** | "이런 시뮬레이션 결과가 있다 — 실제는 어떻게 다를지 확인하자" 자료 |

### 7.2 Phase 1 실행 직전 체크리스트

| 항목 | YES면 진행 |
|------|--------------|
| CEO와 직접 60분 미팅 가능? | |
| 8부문 본부장 명단·현황 정확? | |
| 한국콜마·코스맥스와의 관계 baseline 이해? | |
| 현행 Family 정의 (또는 그 부재) 확인? | |
| ERP·창고·채널 시스템 통합 갭 진단 가능? | |
| Master Data Steward 후보 1명 식별 가능? | |
| Demand Manager 후보 1명 식별 가능? | |

→ 7/7 YES면 Phase 1 진행. 부족하면 사전 작업 (data audit 등) 1-2주.

### 7.3 1년 후 v3 작성 계획

| 시점 | 산출물 |
|--------|---------|
| T+12개월 | LAKA S&OP v3 — Stage 3 진입 후 운영 매뉴얼 |
| T+18개월 | LAKA S&OP v4 — Stage 4 진입 시도 (Outside-In·Demand Sensing) |
| T+24개월 | LAKA S&OP Best Practice Case Study — 외부 공유 가능 |

---

## 8. W1~W8 시리즈 마무리

본 W8을 마지막으로 LAKA S&OP 학습 시리즈 완성:

| W | 산출물 | 성격 |
|---|---------|------|
| W1 | sop_overview | Fact Transfer — 프레임워크 |
| W2 | sop_glossary | Fact Transfer — 용어 |
| W3 | (2.) demand_planning | Fact Transfer — Step 2 |
| W3.5 | (1.) data_gathering | Fact Transfer — Step 1 |
| W4 | (3.) supply_planning_odm | Fact Transfer — Step 3 |
| W5 | sop_kpis | Fact Transfer — 측정 |
| W6 | sop_failure_patterns | Fact Transfer — 실패 |
| W7 | laka_sop_v1 | Simulation — Playbook |
| **W8** | laka_sop_v1_simulation | Simulation — 90일 narrative |

→ **8개 페이지 + 1개 워크북 + 4개 source 페이지 = 13개 문서**. LAKA S&OP 시리즈 완성.

Wallace 가르침의 마지막 인용:

> *"S&OP is fiercely efficient. Of all the things I do, it's the most highly leveraged use of my time."* — group VP ([[src_wallace_executive_guide_book|책]] p69)

→ Pilot 시뮬레이션이 이 약속을 확인. 90일 30시간 투자로 — 데이터 정비·정보 흐름·CEO commitment·Soft Benefit S7 (Window into the Future) 모두 첫 단추.

---

## 관련 페이지

- [[sop_overview]] — W1
- [[sop_glossary]] — W2
- [[data_gathering]] — 1.
- [[demand_planning]] — 2.
- [[supply_planning_odm]] — 3.
- [[sop_kpis]] — W5
- [[sop_failure_patterns]] — W6
- [[laka_sop_v1]] — W7 (본 시뮬레이션의 base)
- 📎 [laka_sop_template_v0.xlsx](./laka_sop_template_v0.xlsx) — Pilot 운영 도구
- [[LAKA]] — LAKA 기업 entity
- [[ODM_발주_프로세스]]
- [[K뷰티_ODM_QA_실패_8유형]] — 코스맥스 품질 issue 사례 참조
- [[src_wallace_executive_guide_book]] — "Bad Day at Acme Widget" Ch3 narrative 양식 차용
- [[src_wallace_executive_sop_workshop]]
- [[src_implement_sop_handbook]]
- [[src_supply_chain_insights_sop_guide]]
