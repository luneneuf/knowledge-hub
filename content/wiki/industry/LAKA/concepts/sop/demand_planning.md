---
title: "2. Demand Planning"
type: concept
axis: work
tags: [work/sop, s&op, demand-planning, forecast, fva, npi, laka]
created: 2026-05-11
updated: 2026-05-11
status: draft
publish: false
---

# 2. Demand Planning

> **본 페이지의 역할**: [[sop_overview|5-step 프로세스]]의 **Step 2 — Demand Planning** 운영 매뉴얼. [[data_gathering|1. Data Gathering]]에서 받은 데이터로 Sally Smith Spreadsheet 템플릿 LAKA 컬러군 적용, 통계 baseline → consensus까지 layering, FVA(Forecast Value Added) 측정, 신제품(NPI) 통합, 매월 cadence.
>
> **연관 Linear 이슈**: [COM-22](https://linear.app/luneneuf) W3
>
> **선행**: [[sop_overview]] (W1) — 프레임워크 / [[sop_glossary]] (W2) — Forecast·MAD·SOD·FVA·Demand Sensing 용어

---

## 0. 위치와 책임

5-step에서 Step 2:

```
Step 1 Data Gathering → ★ Step 2 Demand Planning ★ → Step 3 Supply Planning → Step 4 Pre-meeting → Step 5 Exec Meeting
```

**Wallace 정의** ([[src_wallace_executive_guide_book|책]] Ch4 p40):

> *"Step 2는 Sales와 Marketing 인원이 Step 1에서 받은 정보를 분석·논의하여 향후 15개월 이상의 새 management volume forecast를 생성하는 단계다. **이 forecast는 기존 제품과 신제품 모두 포함**해야 한다."*

**LAKA 책임 매핑** (VER. '26.03.04):

| 역할 | LAKA 부문/인력 | Step 2에서 할 일 |
|------|------------------|---------------------|
| **Demand Manager** (운영 owner) | 마케팅 부문 BM/PM 파트 (가칭) | 통계 baseline + layering 운영 + Consensus 회의 진행 |
| Marketing 인풋 | 마케팅 부문 (15명, 안일홍) | 프로모션·신제품·캠페인·가격 변동·트렌드 |
| 국내 Sales 인풋 | 국내사업 (14명, 본부장 공석) | 한국 채널·대리점·온라인몰 단위 mix 인풋 |
| 글로벌 Sales 인풋 | 글로벌사업 (17명, 손여진) | 세포라·Boots·Qoo10·일본지사 인풋 (channel별 분리) |
| Product 인풋 | 프로덕트 (8명, 이정미) | 신규 컬러·라인 launch 시점·order quantity·런인 곡선 |
| Finance 인풋 | 재무 (4명, 이종영 CFO) | 단가·환율(USD/JPY/GBP→KRW)·revenue conversion |
| **승인** (Demand Consensus) | Senior Sales/Marketing 합의 → 마케팅·국내·글로벌 본부장 sign-off | "management-authorized forecast" 확정 |

---

## 1. Step 2의 인풋 (Step 1에서 받음)

매월 1-3일 (Step 1) 수집 후 Step 2로 전달:

| 인풋 | 출처 | 형식 |
|------|------|------|
| 전월 actual sales | ERP/주문 시스템 (Family·SKU·채널·국가별) | 표 |
| 전월 actual production | ODM 입고 데이터 (한국콜마·코스맥스) | 표 |
| 전월 actual inventory | 창고 시스템 (국내·일본·미국·영국 창고) | 표 |
| Statistical forecast | 통계 도구 산출 baseline (Excel·통계 SW) | 표 |
| 전월 forecast vs actual gap | Step 1 산출 — Family·SKU별 difference·cum difference | 표 (Sally Smith 형식) |
| 시장 인텔리전스 | 트레이드 publication, @cosme/LIPS 리뷰 트렌드, 경쟁사 launch | 노트 |
| 신제품 plans | 프로덕트 부문의 launch schedule | 노트 + 표 |

→ **LAKA 추가 인풋 (Designer/Distributor 특성)**:

| 추가 인풋 | 출처 | 비고 |
|-----------|------|------|
| 채널별 PO·sell-through 데이터 | 세포라·Boots SDK / Qoo10 API / 국내 대리점 | weekly 빈도 가능 |
| ODM 슬롯 확정 schedule | SCM 부문 → Step 3에 전달, Step 2에 reference | 동일 |
| 환율 (USD/JPY/GBP/KRW) | 재무 — 전월말 시점 + 향후 18개월 시나리오 | base·optimistic·pessimistic 3개 |
| 시즌 캠페인 일정 | 마케팅 (홀리데이·발렌타인·여름 등) | 12개월 + 신규 |

---

## 2. Forecast Layering — 통계 baseline → Consensus

Wallace Demand Planning의 표준 layering ([[src_wallace_executive_guide_book|책]] p40-43):

```
Layer 1: Statistical Baseline      ← 과거 데이터 + 통계 알고리즘
   ↓ (FVA 측정)
Layer 2: Marketing Adjustment      ← 프로모션·신제품·트렌드 반영
   ↓ (FVA 측정)
Layer 3: Sales Adjustment          ← 채널·고객·field 인텔리전스
   ↓ (FVA 측정)
Layer 4: Senior Consensus          ← Demand Consensus Meeting → "management-authorized"
```

### 2.1 Layer 1: Statistical Baseline

- **Family 단위 통계 forecast** — 과거 12-36개월 sales 데이터 + 시즌·트렌드 분해 + 통계 알고리즘 (지수평활법·ARIMA 등)
- LAKA 초기에는 **Excel 시즌·이동평균** 충분 (Wallace: "Software for S&OP — pick spreadsheet first")
- **주의**: 통계 baseline은 baseline일 뿐. 신제품·prom·외부 변화는 반영 못 함 → 다음 레이어가 보완

**LAKA 적용 — 베스트셀러 컬러군 (예시)**:

```
립 글로스 컬러군 A (베스트셀러 5-7개)
- 과거 24개월 출하 데이터 → 지수평활법 (α=0.3)
- 시즌 계수: 발렌타인(2월) ×1.4, 어머니날(5월) ×1.2, 홀리데이(11-12월) ×1.5
- Baseline 1월 forecast: 10,000 units
```

### 2.2 Layer 2: Marketing Adjustment

마케팅 부문(15명)이 baseline에 다음을 반영:

- **Promotional plans** — 프로모션·할인·번들·증정 일정
- **Price changes** — 가격 인상·인하·환율 영향 (글로벌 채널)
- **New product launches** — 신규 컬러 출시 (NPI는 별도 섹션 참조)
- **Cannibalization** — 신제품이 기존 SKU 잠식하는 부분
- **Competitive activity** — 경쟁사 launch·promotion 정보 (롬앤·달바·APR)
- **Industry dynamics** — K-뷰티 전반 (@cosme 트렌드·세포라 입점 변동 등)
- **Economic conditions** — 환율·소비 심리

**Marketing Adjustment 결과**: Layer 1에 ±N% 또는 ±units 형태로 반영.

### 2.3 Layer 3: Sales Adjustment

국내사업(14명) + 글로벌사업(17명)이 추가:

- **Field intelligence** — 대리점·바이어 미팅·트레이드쇼에서 얻은 정보
- **Large customers** — 세포라 미국 신규 도어 확장, Boots 영국 promotion request, Qoo10 일본 빅세일 참여 등
- **Channel-specific demand** — 채널별 sell-through rate 변화

**주의 사항 (Implement Ch4)**:
- "Sales is from Venus, Operations is from Mars" — Sales 본능적으로 **단기 과대예측·장기 과소예측** 경향
- 해결: forecast는 Operations(Demand Manager)가 생성·Sales가 review
- Sales는 baseline·캠페인 물량 분리하여 인풋 (Implement Ch4 7개 관점 #5)

### 2.4 Layer 4: Senior Consensus (Demand Consensus Meeting)

**Wallace Step 2 마무리** ([[src_wallace_executive_guide_book|책]] p43):

> *"The last step in the Demand Planning phase is to 'finalize' the numbers through a senior level demand consensus meeting."*

**목적**:
1. Senior Sales/Marketing이 ask·challenge·필요 시 수정
2. **Executive Meeting의 surprises 방지**
3. "management-authorized forecast" 도출 — 모든 key player sign-off

**LAKA Consensus 참석자**:
- 마케팅 본부장 (안일홍)
- 국내사업 본부장 (공석 — 임시 CEO)
- 글로벌사업 본부장 (손여진)
- 프로덕트 본부장 (이정미)
- 재무 1명 (CFO 위임)
- Demand Manager (마케팅 BM/PM 파트)

**Time-box**: 60-90분 (Wallace: "short meeting"). 매월 Step 2 마지막 working day 권장.

---

## 3. Forecast Value Added (FVA) — 각 레이어의 정확도 기여 측정

SCI 차용 ([[src_supply_chain_insights_sop_guide|가이드]] p14).

### 3.1 FVA란

각 forecast layer가 baseline 대비 정확도를 **얼마나 개선했는지 정량 측정**.

```
Layer 1 (Statistical baseline)   → MAPE 25%
Layer 2 (Marketing adj 후)        → MAPE 20%  (FVA = +5%p, 개선)
Layer 3 (Sales adj 후)            → MAPE 22%  (FVA = -2%p, 악화!)
Layer 4 (Consensus 후)            → MAPE 18%  (FVA = +4%p, 개선)
```

→ **Layer 3가 FVA 음수면** = Sales adj가 정확도를 떨어뜨림. 그 다음 사이클부터 Sales 인풋 가중치 조정·교육 필요.

### 3.2 LAKA 초기 FVA 측정 권장

- **3개월 데이터 누적 후 첫 측정** — 첫 사이클은 보정 데이터 없음
- **Family·채널 cross-tab** — 어느 family·어느 채널이 어느 layer에서 가치 잃는지
- **MAPE (Mean Absolute Percentage Error)** 사용 — 단위 무관, 비교 용이

### 3.3 Sales 단기 과대예측 패턴 (Implement 경고)

자주 발생하는 FVA 음수 케이스:
- Sales가 단기 1-3개월 forecast에 personal targets 반영 → 과대
- 4-12개월 forecast는 conservative bias → 과소
- 해결: baseline + **분리된** campaign volumes로 ask (commit·stretch·confidence band)

---

## 4. Volume Forecast vs Mix Forecast 분리

[[sop_overview|W1]] 원칙: Executive S&OP는 Volume, Master Schedule은 Mix.

| 차원 | Volume Forecast | Mix Forecast |
|------|------------------|---------------|
| 단위 | Product Family (컬러군·카테고리) | 개별 SKU·컬러·채널 |
| 호라이즌 | 15-36개월 | 1-3개월 |
| 빈도 | 월간 | 주간 |
| 정확도 기대 | Family 수준 ±10-15% | SKU 수준 ±25-40% (어차피 변동 큼) |
| 사용처 | Executive S&OP·재무 plan·capacity 계획 | Master Schedule·ODM 발주·창고 출하 |
| LAKA 책임 | Step 2 — Demand Manager | Step 2 후 SCM 부문 [[ODM_발주_프로세스]]에서 활용 |

**핵심 원칙 (Wallace)**: Mix forecast는 short-term scheduling용. **15-36개월 horizon에서 mix를 forecast하지 마라** — 정확도 없음, 공수 낭비 (Implement: "Suicide Quadrant").

**LAKA Volume → Mix 변환 비율**:
- Volume forecast (Family) → **historical mix ratio**로 SKU 단위 분해 (예: 컬러군 A 안에서 207 모브 35%, 다른 컬러 N%…)
- Mix ratio는 monthly로 update

---

## 5. 신제품 통합 (New Product Introduction, NPI)

Wallace + Implement Ch5 + LAKA 특화 (컬러 launch 빈도 高).

### 5.1 NPI Demand 4 차원

1. **Incremental volume** — 신제품 출시로 인한 순증분 수요
2. **Cannibalization** — 기존 SKU 잠식분 (반드시 추정 + 추적)
3. **Pipeline fill** — 채널 입점 시 초도 물량 (one-time, 보통 2-4주차)
4. **Sample / pre-production** — 마케팅 샘플·테스트 unit (mass production 전)

→ Volume forecast에 **4개 모두 별도 컬럼**으로 추적, 합산이 최종 family forecast.

### 5.2 NPI Curve 패턴 (LAKA 컬러)

K-뷰티 컬러 launch 일반 패턴 (관찰 기반):

```
주차 1-2 (초도 입점)    : 채널 fill, 평소 4-6주분 일시 출하
주차 3-8 (런인)         : 실제 sell-through 형성, 마케팅 집중
주차 9-12 (피크)        : 최고 출하량 (성공 시)
주차 13-26 (정상화)     : 베이스라인 형성 — 기존 컬러군 평균 대비 ±%
주차 27+               : 일반 baseline (장기 forecast의 일부)
```

**Step 2 NPI 인풋 양식 (LAKA 권장)**:

| 항목 | 내용 |
|------|------|
| 신제품 ID·이름 | 예: 립 글로스 #208 코랄 |
| Family | 립 글로스 컬러군 A (베스트셀러 그룹 합류) 또는 B (시즌 한정) |
| Launch 일자 | 채널별 (한국·세포라·Boots·Qoo10 모두 다를 수 있음) |
| Pipeline fill (units, 일회성) | 채널별 합계 |
| Run-in curve (주차 3-26) | base·optimistic·pessimistic 3개 시나리오 |
| Long-tail baseline (주차 27+) | family 평균 대비 % |
| Cannibalization 추정 | 잠식 대상 family 컬러 + 잠식률 % |

### 5.3 NPI 정확도 (Wallace 경고)

> *"신제품 출시는 수요 불확실성의 가장 큰 원천이자 동시에 demand shaping 수단이다."* (Implement Ch5)

→ NPI forecast 정확도는 본질적으로 낮음 (±50-100% 흔함). 대응:
- 시나리오 3개 (best/base/worst) 모두 Supply Planning에 전달 → ODM 발주는 base·재고 hedge는 worst 기준
- 첫 90일 후 실제 sell-through로 신속 보정 — Mini-S&OP Cycle 발동 trigger

---

## 6. Sally Smith Spreadsheet — LAKA 템플릿

Wallace 표준 1페이지 시트 ([[src_wallace_executive_sop_workshop|워크샵]] p32-38).

### 6.1 시트 구조 (3 블록 × 4 행)

```
            T+1   T+2   T+3   T+4   T+5   ... T+15  T+16  T+17  T+18
─────────── FORECAST 블록 ─────────────────────────────────────────
FORECAST     X     X     X     X     X         X     X     X     X
ACTUAL SALES x     x     x
DIFFERENCE   d     d     d
CUM DIFF     d     d     d

─────────── PRODUCTION 블록 ──────────────────────────────────────
PLANNED PROD X     X     X     X     X         X     X     X     X
ACTUAL PROD  x     x     x
DIFFERENCE   d     d     d
CUM DIFF     d     d     d

─────────── INVENTORY 블록 ───────────────────────────────────────
PLANNED INV  X     X     X     X     X         X     X     X     X
ACTUAL INV   x     x     x
DIFFERENCE   d     d     d
```

- T = 현재월. 과거 3개월 actual 노출, 미래 15-18개월 plan 노출
- **Forecast - Production - Inventory** 3개 블록이 한 페이지에 동시 보임 → 임원이 family 1개당 5-10초 내 진단 가능

### 6.2 LAKA 적용 — 립 글로스 컬러군 A (베스트셀러) 예시

```
              25-Nov 25-Dec 26-Jan 26-Feb 26-Mar 26-Apr 26-May ... 26-Dec 27-Jan ... 27-Aug
              (actual) (actual) (actual)  ─── 통계 baseline + Marketing/Sales adj ───
─────── FORECAST 블록 (units, 천개) ─────────────────────────────────────────────────
FORECAST       12     15     10     14     11     12     13          16     11          12
ACTUAL SALES   11     14     9
DIFFERENCE    -1     -1    -1
CUM DIFF      -1     -2    -3

─────── PRODUCTION 블록 (한국콜마 입고 units, 천개) ───────────────────────────────
PLANNED PROD   10     12     12     12     12     12     12          15     12          12
ACTUAL PROD    10     13     11
DIFFERENCE     0     +1    -1
CUM DIFF       0     +1     0

─────── INVENTORY 블록 (units, 천개, 1 month supply 목표) ─────────────────────────
PLANNED INV    12     12     12     14     11     12     13          16     11          12
ACTUAL INV     14     13     15
DIFFERENCE    +2     +1    +3                                                                  
```

→ 위 예시는 forecast 대비 actual sales 누적 -3, 그러나 actual inventory는 +3 (현재 15)으로 **3개월치 demand에 못 미치는 forecast인데 inventory는 1.5개월 과잉** = 다음 step에서 production rate 조정 검토.

### 6.3 시트 운영 규칙 (LAKA 초기)

| 규칙 | 내용 |
|------|------|
| 1 family = 1 sheet | 컬러군별 별도 탭, 총 7-10개 family로 시작 |
| Units AND $ | 두 번째 시트 탭에 동일 구조의 dollar 환산 (환율은 base 시나리오) |
| 시즌·신제품 분리 | baseline·campaign·NPI 3개 행 분리하여 합산 표시 |
| Cum Difference 색상 | ±5% 이내 흰색, ±10% 노란색, ±15% 빨간색 (트래픽 라이트) |
| Update 빈도 | 월간 (Step 1 데이터 입수 후 1-2일 내) |

### 6.4 작동하는 워크북 샘플 📎

**다운로드**: [laka_sop_template_v0.xlsx](./laka_sop_template_v0.xlsx)

5 시트 구성 (16KB, 수식 51개):

| 시트 | 내용 |
|------|------|
| README | 사용법 + 가정 + 컬러 코드 의미 |
| Master_Data | Family 8개·환율 시나리오 3개·Channel 코드 8개 |
| **F01_Sally_Smith** | 립글로스 컬러군 A 18개월 view — 3 블록(Forecast·Production·Inventory) × 4 row(Baseline·Campaign·NPI·Total) |
| NPI_Tracker | 컬러 #208 코랄 launch curve 예시 (4 채널·3 시나리오·잠식률) |
| FVA_Tracking | 12 row 예시 (F01 × 3 month × 4 layer) + 양수/음수 자동 색상 |

**핵심 특징**:
- 파란 글씨 = 수동 입력 셀 / 검은 글씨 = 수식 셀 / 녹색 글씨 = Master_Data cross-sheet 참조
- Difference 행에 트래픽 라이트 자동 적용 (±5% 이내 흰색 / ±5-10% 노란색 / ±10% 초과 빨간색)
- F01 시트의 단가는 Master_Data!$D$4 참조 → Master에서만 수정하면 자동 반영
- KRW 환산 = Total Forecast(천 units) × 단가(KRW) ÷ 1,000 = 백만 KRW 단위

**v0 한계**:
- 1 family만 (F01). family당 시트 복제 필요
- 채널 분해 미포함 (W7 이후 확장)
- 자동화 없음 — manual Excel만

### 6.5 시즌·캠페인 분리 양식

```
FORECAST 블록 (3 행 분리)
                Nov   Dec   Jan   Feb  ...
Baseline        10    11    9     10
Campaign        +1    +3    +1    +3  ← 발렌타인·홀리데이 등
NPI             0     0     0     +1   ← 신규 출시 컬러
────────────────────────────────────
TOTAL FCST      11    14    10    14
```

→ Baseline·Campaign·NPI 분리하면 각각의 FVA 측정 가능 + 사후 어느 layer가 빗나갔는지 진단.

---

## 7. LAKA Step 2 매월 Cadence

| Working Day | 활동 | 책임 |
|--------------|------|------|
| 1-3 | Step 1 Data Gathering 완료 | SCM 부문 (S&OP파트) |
| 4 | Statistical baseline 생성·배포 | Demand Manager |
| 4-5 | Marketing Adjustment 인풋 | 마케팅 부문 |
| 5-6 | National Sales Adjustment 인풋 | 국내사업 부문 |
| 5-6 | Global Sales Adjustment 인풋 (병렬) | 글로벌사업 부문 |
| 6 | NPI 인풋 추가 | 프로덕트 부문 |
| 6 | Volume→$ 환산 | 재무 부문 |
| 7 | **Demand Consensus Meeting** (60-90분) | 마케팅·국내·글로벌·프로덕트 본부장 + Demand Manager |
| 7 (저녁) | management-authorized forecast 확정 → Step 3로 전달 | Demand Manager |

→ Step 2 총 소요 = 약 4 working days. 매월 1-7일 안에 완료.

**병행 활동**: SCM 부문은 Step 1 직후 곧장 Step 3 Supply Planning 사전작업 시작 (특히 ODM 슬롯 확정 schedule 재정렬).

---

## 8. Demand-side KPI (W5에서 상세)

Step 2 운영 품질 측정을 위해 사전 정의:

| KPI | 정의 | 목표 (Stage 2-3 진입 시점) |
|-----|------|------------------------------|
| **MAPE (Family)** | Family 단위 평균 절대 백분율 오차 | < 15% (베스트셀러) / < 25% (시즌·신규) |
| **MAPE (SKU)** | SKU 단위 평균 절대 백분율 오차 | < 30% (베스트셀러 핵심 SKU) |
| **Bias (SOD)** | 누적 forecast - actual 합 | ±5% 이내 (장기 과대/과소 방지) |
| **FVA (Layer별)** | 각 layer baseline 대비 개선% | 모든 layer 양수 |
| **Consensus On-time** | 매월 working day 7까지 완료 비율 | 100% |
| **NPI Forecast Accuracy** | 신규 launch 첫 90일 actual vs base 시나리오 | ±50% 이내 (현실적 목표) |

→ W5 sop_kpis에서 [[OTD]] 확장 + supply-side KPI와 통합.

---

## 9. 흔한 실패 패턴 (W6에서 상세)

Step 2 운영 초기 자주 발생:

| 패턴 | 원인 | 대응 |
|------|------|------|
| Sales가 baseline·campaign 통합 인풋 | "한 숫자가 편함" 인식 | 분리 양식 강제, FVA 측정 시 layer별 추적 |
| Marketing이 일관 과대예측 (희망사항 반영) | KPI가 매출 목표 | Consensus 회의에서 challenge 메커니즘 |
| 글로벌 채널 forecast의 환율 일관성 결여 | 부서별 다른 환율 사용 | 재무 환율 시나리오 단일 배포 |
| NPI cannibalization 무시 | 잠식 추정 어려움 | 보수적 잠식률 default + 90일 후 보정 |
| Demand Consensus 시간 부족·tactical mix 빠짐 | 임원 일정 어려움 | time-box 90분 엄수, 1 family 5분 |
| 통계 baseline 신뢰 부족 → 매월 manual override | 통계 도구 학습 부족 | FVA 음수 데이터 누적·교육 |

---

## 10. 다음 단계와 연결

| 출력 (Step 2 → Step 3) | 형식 |
|-------------------------|------|
| Management-authorized Volume Forecast | Family 단위, units + $, 15-18개월 |
| NPI demand (시나리오 3개) | Family·launch별, base/optimistic/pessimistic |
| Marketing assumption 문서 | 프로모션·캠페인·가격 변동 일정 |
| Sales channel breakdown | 채널·국가별 mix ratio (참고용) |
| FVA report (3개월 누적 후) | Family·Layer cross-tab |

→ Step 3 [[supply_planning_odm|Supply Planning]]은 이 인풋으로 한국콜마·코스맥스 슬롯·재고 trajectory·재무 영향 계산.

---

## 관련 페이지

- [[sop_overview]] — W1 (Step 2 위치)
- [[sop_glossary]] — W2 (Forecast·MAD·SOD·FVA·NPI·Demand Sensing·Bullwhip 용어 정의)
- [[supply_planning_odm]] — W4 (예정), Step 2 산출이 Step 3로 어떻게 흐르나
- [[sop_kpis]] — W5 (예정), Demand-side KPI 운영
- [[sop_failure_patterns]] — W6 (예정), Sales 편향·FVA 음수 등 실패 패턴 심화
- [[laka_sop_v1]] — W7 (예정), Step 2 운영 매뉴얼 통합
- [[ODM]] / [[ODM_발주_프로세스]] — LAKA 현행 supply 측 — Step 2 산출이 여기로 흐름
- [[OTD]] — W5 KPI 확장 base
- [[K뷰티_일본_리뷰_트렌드]] — Field intelligence 인풋 source
- [[K뷰티_립_CS_벤치마크]] — Sales adjustment 시 참고
- [[src_wallace_executive_guide_book]] — Ch4 Step 2 원천
- [[src_wallace_executive_sop_workshop]] — Sally Smith Spreadsheet 원천
- [[src_implement_sop_handbook]] — Ch4 Demand Forecasting 7 관점 + Ch5 NPI 원천
- [[src_supply_chain_insights_sop_guide]] — FVA·Demand Sensing 원천
