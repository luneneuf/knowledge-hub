---
title: "1. Data Gathering"
type: concept
axis: work
tags: [work/sop, s&op, data-gathering, master-data, planning-master-data, laka]
created: 2026-05-11
updated: 2026-05-11
status: draft
publish: false
---

# 1. Data Gathering

> **본 페이지의 역할**: [[sop_overview|5-step 프로세스]]의 **Step 1 — Data Gathering** 운영 매뉴얼 + LAKA 마스터 데이터 거버넌스. 매월 1-3일 working day 동안 전월 actual 수집·통계 forecast 생성·다음 step에 disseminate.
>
> **연관 Linear 이슈**: COM 프로젝트 신규 (W3.5)
>
> **왜 별도 페이지인가**: SCI 2020 정량 서베이 결과 **"적시에 올바른 데이터에 접근하는 어려움" = 구현 갭 1위 (58%)**. LAKA Designer/Distributor 특성 (ODM·다채널·다국가) 때문에 Step 1이 가장 큰 진입 장벽. 마스터 데이터 거버넌스가 W3(Demand)·W4(Supply) 작동의 전제 조건.
>
> **선행**: [[sop_overview]] (W1) — 프레임워크 / [[sop_glossary]] (W2) — Planning Master Data·Aligned vs Matrix Resources·Demand Manager 등 용어

---

## 0. 위치와 책임

5-step에서 Step 1:

```
End of Month → ★ Step 1 Data Gathering ★ → Step 2 Demand Planning → Step 3 Supply Planning → Step 4 Pre-meeting → Step 5 Exec Meeting
```

**Wallace 정의** ([[src_wallace_executive_guide_book|책]] Ch4 p39):

> *"Step 1의 활동은 월말 직후에 일어난다. 세 가지 요소로 구성된다 — ①전월 actual 데이터로 파일 update, ②Sales/Marketing이 새 forecast를 만들 때 사용할 정보 생성 (volume·필요 시 mix 단위 — sales analysis·통계 forecast·field salespeople worksheets 등), ③이 정보를 적절한 사람들에게 disseminate."*

> *"S&OP를 timely process로 만들려면 이 step은 월말 후 1-2일 안에 완료되어야 한다."*

**LAKA 책임 매핑** (VER. '26.03.04):

| 역할 | LAKA 부문/인력 | Step 1에서 할 일 |
|------|------------------|---------------------|
| **Process Owner** (운영 owner) | SCM 부문 SC기획팀 내 S&OP파트 (신설 예정) | 7개 데이터 소스 수집·통합·disseminate 책임 |
| ERP 출하 데이터 | SCM 부문 | 전월 actual sales by Family·SKU·채널·국가 |
| ODM 입고 데이터 | SCM 부문 (한국콜마·코스맥스와 협업) | 전월 actual production·입고 |
| 채널 sell-through | 글로벌사업·국내사업 (협조) | 세포라·Boots·Qoo10·국내몰 데이터 dump |
| 재고 데이터 | SCM 부문 (창고 시스템 통합) | 국내·일본·미국·영국 창고 잔고 |
| 환율 | 재무 부문 | 전월말 spot rate + 향후 18개월 시나리오 3개 (base/opt/pess) |
| 시장 인텔리전스 | 마케팅 부문 (큐레이션) | @cosme·LIPS·트레이드 리뷰 핵심 트렌드 |
| 통계 baseline forecast | Demand Manager (마케팅 BM/PM) — Step 2 시작 직전 | Family·SKU 통계 산출 (시즌·이동평균·지수평활) |

→ **현실적 운영**: Step 1은 SCM 부문 S&OP파트가 **데이터 통합 owner**, 각 부문이 자신의 데이터 정시 제출 책임.

---

## 1. Step 1의 4가지 결과물

| # | 결과물 | 형식 | 받는 곳 |
|---|---------|------|----------|
| 1 | 전월 actual update — Sales / Production / Inventory | Sally Smith Sheet의 actual 행 채움 | Step 2 (Demand Manager) |
| 2 | Statistical baseline forecast | Family·SKU 통계 산출 표 | Step 2 (Marketing/Sales adjustment 출발점) |
| 3 | 시장 인텔리전스 노트 | 큐레이션 노트 + 첨부 | Step 2 (Marketing adjustment 인풋) |
| 4 | Data quality report | 누락·이상치·갭 표 | Process Owner + 책임 부문 (다음 사이클 개선) |

---

## 2. LAKA 데이터 소스 인벤토리 (7개 소스)

### 2.1 데이터 소스 × LAKA 시스템 매핑

| # | 데이터 | 출처 시스템 | 빈도 | 통합 난이도 | 책임 |
|----|---------|---------------|------|---------------|------|
| 1 | 전월 actual sales (Family·SKU·채널·국가) | 자체 ERP | 월말 batch | 중 | SCM |
| 2 | 전월 actual production·입고 | 한국콜마·코스맥스 외부 시스템 + LAKA 수령 ERP | 월말 batch | **상** (외부 협조) | SCM + ODM 커뮤니케이션 |
| 3 | 채널 sell-through (PO·sell-out) — 세포라 US | 세포라 SDK / Vendor Portal | weekly | **상** | 글로벌사업·SCM |
| 4 | 채널 sell-through — Boots UK | Boots Vendor Portal | weekly | **상** | 글로벌사업·SCM |
| 5 | 채널 sell-through — Qoo10 JP | Qoo10 셀러센터 API | daily 가능 | 중 | 글로벌사업·SCM |
| 6 | 채널 sell-through — 국내 (대리점·온라인몰) | 자체 ERP + 외부 몰 API | weekly-monthly | 중 | 국내사업·SCM |
| 7 | 재고 — 국내·일본·미국·영국 창고 | 창고별 시스템 (보통 3PL) | monthly batch (가능 시 weekly) | 중 | SCM |

**별도 인풋**:

| # | 데이터 | 출처 | 빈도 | 책임 |
|----|---------|------|------|------|
| A | 환율 (USD/JPY/GBP→KRW) | 한국은행·Bloomberg·은행 | monthly | 재무 |
| B | 시장 인텔리전스 | @cosme·LIPS·트레이드 publication·경쟁사 모니터링 | 상시 큐레이션 | 마케팅 |
| C | 신제품 launch schedule | 프로덕트 부문 ROADMAP | monthly update | 프로덕트 |
| D | 캠페인·프로모션 일정 | 마케팅 부문 calendar | monthly update | 마케팅 |
| E | ODM 슬롯 확정 일정 | 한국콜마·코스맥스 발주 시스템 | monthly | SCM |

### 2.2 데이터 빈도와 latency 목표

| 데이터 | 현재 빈도 | Step 1 latency 목표 |
|---------|-------------|------------------------|
| ERP 출하 | 일일 → 월말 cutoff | 월말 +1 working day |
| ODM 입고 | ODM별 다름 | 월말 +2 working day |
| 채널 sell-through | 채널별 다름 (weekly가 표준) | 월말 +1 working day (전월 마지막 주 데이터까지) |
| 재고 | 월말 batch | 월말 +1 working day |
| 환율 | 매일 | 월말 +1 working day |

→ **Wallace 권장 = Step 1 총 1-2 working days 안에 완료**. LAKA 초기에는 3일 허용, 6개월 후 2일 단축 목표.

---

## 3. 마스터 데이터 거버넌스 (LAKA 핵심 갭)

SCI 정의 **Planning Master Data** ([[sop_glossary|용어집]]): "대체 소싱·사이클 타임·환산율·원가·리드타임 — 모든 계획의 baseline".

→ Step 1의 **본질은 단순 데이터 수집이 아니라 마스터 데이터 거버넌스**. 6개 영역.

### 3.1 Family Hierarchy (Volume 계획 단위)

**원칙** ([[sop_glossary|용어집]] Product Family): 5-10개 family로 시작. Marketing 관점(고객·사용·시장)에 맞춤.

**LAKA Family 후보 (W3 demand_planning에서도 인용)**:

| Family ID | 명칭 | 구성 SKU 수 (추정) | 단위 | 비고 |
|------------|------|----------------------|------|------|
| F01 | 립 글로스 컬러군 A (베스트셀러) | 5-7 | units | 207 모브 등 핵심 |
| F02 | 립 글로스 컬러군 B (시즌 한정) | 분기 신규 | units | 출시/단종 사이클 高 |
| F03 | 립 틴트 | 10-15 | units | |
| F04 | 아이섀도 | 10-15 | units | |
| F05 | 베이스 (파데·쿠션) | 5-10 | units | |
| F06 | 선케어 | 3-5 | units | 한국콜마 차별화 |
| F07 | 스킨케어 | 5-10 | units | 글로벌 확장 |
| F08 | 글로벌 전용 SKU (세포라·Boots 라벨) | 시즌별 | units | 라벨링 변형 |

→ **확정 시점**: W7 laka_sop_v1 또는 그 이전 별도 합의 필요. 본 페이지에서는 후보로만 제시.

**Family 정의 변경 규칙**:
- 분기당 1회만 family 정의 변경 허용 (forecast 연속성 위해)
- 신제품 launch 시 어느 family에 속하는지 사전 결정 + 통계 baseline reseed
- Family 변경 시 과거 데이터 backfit (최소 12개월) 필수

### 3.2 SKU 매핑 (Mix 단위)

각 SKU는 다음 속성 보유:

| 속성 | 예시 | 유지 책임 |
|------|------|-----------|
| SKU ID | LK-LG-207 | 프로덕트 |
| Family | F01 (베스트셀러) | 프로덕트 + Demand Manager |
| 컬러·variant | 207 모브 | 프로덕트 |
| 채널 variant | 세포라 US 라벨 vs Boots UK 라벨 vs 국내 | 프로덕트 + 글로벌사업 |
| GTIN/UPC/EAN | 채널별 다를 수 있음 | 프로덕트 |
| Status | active·EOL·NPI·hold | 프로덕트 |
| Launch date | 채널별 | 프로덕트 |
| EOL date | 채널별 | 프로덕트 |

→ **글로벌 라벨 변형 추적이 LAKA의 고유 복잡성**. 동일 bulk(한국 ODM 생산) → 세포라 US 라벨링·Boots UK 라벨링·Qoo10 JP 라벨링이 모두 다른 SKU. **Finish-to-Order(FTO) 전략**의 mix 정의 핵심.

### 3.3 Channel 코드 표준화

| Channel ID | 명칭 | 국가 | type |
|-------------|------|------|------|
| CH-KR-RT | 한국 리테일 (CJ올리브영·롭스·랄라블라) | KR | retail |
| CH-KR-OL | 한국 온라인 (자체몰·쿠팡·11번가·SSG) | KR | online |
| CH-JP-Q10 | Qoo10 일본 | JP | online (마켓플레이스) |
| CH-JP-LOFT | 일본 LOFT·로프트·도큐핸즈 | JP | retail (버라이어티샵) |
| CH-US-SEPH | 세포라 미국 | US | retail (specialty beauty) |
| CH-US-AMZ | 아마존 미국 | US | online |
| CH-UK-BOOTS | Boots 영국 | UK | retail (drugstore) |
| (기타) | … | … | … |

→ **Channel 코드는 ERP·창고·forecast·시장 보고서 전반에 동일 코드 사용**. 부서별 다른 약어 금지.

### 3.4 단위 환산 (Units of Measure)

| 단위 | 사용처 | 환산 규칙 |
|------|---------|-------------|
| Each (개) | 모든 baseline | 기본 |
| Case (박스) | ODM 발주·창고 출하 | SKU별 case pack 정의 (예: 24개/박스) |
| KRW | 재무 plan·국내 매출 | 단가 × 수량 |
| USD | 세포라·아마존 매출 | 환율 적용 (재무 시나리오 일관) |
| GBP | Boots 매출 | 상동 |
| JPY | Qoo10·LOFT 매출 | 상동 |

→ **환율 일관성**: 재무가 base/opt/pess 3개 시나리오 단일 배포. **부서별 다른 환율 사용 절대 금지** ([[demand_planning|W3]] 실패 패턴 #3 상동).

### 3.5 Lead Time·MOQ·Pack 정보 (Planning Master Data 핵심)

각 SKU/Family에 대해:

| 속성 | 예시 (한국콜마 립 글로스) | 비고 |
|------|----------------------------|------|
| Bulk lead time | 30-45일 | 한국콜마 |
| Finishing lead time | 7-14일 | 라벨링·포장 |
| Total cumulative lead time | 45-60일 | Bulk + Finishing |
| **Demand Time Fence (DTF)** | 30일 | 이 안 미판매 forecast 무시 |
| **Planning Time Fence (PTF)** | 60일 | 이 안 detailed plan 필수 |
| MOQ (minimum order quantity) | ODM·SKU별 | 한국콜마 SKU당 5,000-10,000개 가정 |
| Pack size | 24개/박스, 12박스/팔레트 등 | 채널 출하 단위 |
| Safety stock | 채널·family별 day-supply 목표 | 베스트셀러 30일, 시즌 한정 15일 |

→ **이 표가 LAKA의 Planning Master Data 핵심**. W4 supply_planning_odm에서 이 데이터로 capacity 계산.

### 3.6 작동하는 마스터 데이터 샘플 📎

**다운로드**: [laka_sop_template_v0.xlsx](./laka_sop_template_v0.xlsx) — `Master_Data` 시트

샘플 시트가 담고 있는 마스터 데이터:
- **Family 8개** (F01~F08) — Family ID · 명칭 · 단가 · Lead Time · MOQ · Safety Stock
- **환율 시나리오 3개** — USD/GBP/JPY → KRW · base/optimistic/pessimistic
- **Channel 코드 8개** — CH-KR-RT/CH-KR-OL/CH-JP-Q10/CH-JP-LOFT/CH-US-SEPH/CH-US-AMZ/CH-UK-BOOTS/CH-XX-OTHER

→ 모든 family 시트(`F01_Sally_Smith` 등)는 Master_Data를 cross-sheet 참조 (예: 단가 = `Master_Data!$D$4`). Master에서만 수정하면 전 시트 자동 반영.

### 3.7 마스터 데이터 update cycle

| 마스터 데이터 | update 빈도 | 책임 |
|----------------|---------------|------|
| Family 정의 | 분기 1회 (필요 시) | Demand Manager + 프로덕트 |
| SKU master | 신규 launch / EOL 시마다 | 프로덕트 |
| Channel master | 신규 채널 진입 시 | 글로벌사업/국내사업 |
| UoM·환산표 | 신규 SKU 시 | SCM |
| Lead time·MOQ·Pack | 분기 1회 review (ODM 변경 시 즉시) | SCM |
| Safety stock | 분기 1회 review | SCM + Demand Manager |
| 환율 시나리오 | 월간 | 재무 |

---

## 4. 통계 baseline forecast 도구 선정

Wallace ([[src_wallace_executive_sop_workshop|워크샵]] p77-82): "When in doubt, pick **option 3** (Hybrid — start with spreadsheet, switch to specific later)."

### 4.1 LAKA 단계별 도구

| 단계 | 도구 | 기간 |
|------|------|------|
| MVP (현재 ~ 12개월) | **Excel + 통계 함수** (지수평활·이동평균·시즌 분해) | 1년 |
| 성숙 (Stage 3 진입 후) | S&OP-specific SW 검토 — SCI 벤더 카탈로그 中 LAKA 핏: **ToolsGroup (SO99+) / o9 Solutions / Logility** | 12-24개월 |
| 미래 (Stage 4+) | Demand sensing + Digital Twin (Aera·BlueCrux 등) | 24개월+ |

### 4.2 Excel 통계 baseline 권장 알고리즘

| Family 특성 | 권장 알고리즘 |
|--------------|------------------|
| 베스트셀러 (안정적 demand) | 지수평활 (α=0.2-0.3) + 시즌 계수 |
| 시즌 의존 高 (홀리데이·발렌타인) | Holt-Winters (level+trend+seasonal) |
| 시즌 한정·신규 launch | 별도 처리 — NPI 시나리오 ([[demand_planning|W3]] 섹션 5) |
| 글로벌 다채널 | 채널별 baseline 산출 → 합산, 채널별 환율 적용 |

### 4.3 Statistical Forecast Output 양식

Sally Smith 시트의 "FORECAST" 행에 들어가는 값:

```
Family F01 (립글로스 컬러군 A) — Statistical Baseline
            Nov-25 Dec-25 Jan-26 Feb-26 Mar-26 ... Aug-27
Level         10     10     10     10     10           10
Trend          0      0      0      0      0            0
Seasonal     ×1.5   ×1.4   ×0.9   ×1.4   ×1.0          ×1.0
─────────────────────────────────────────────────────────
Baseline      15     14      9     14     10           10
```

→ Step 2 Marketing/Sales adjustment의 시작점.

---

## 5. LAKA 데이터 현행 갭 진단

SCI 정량 갭 1위 (58%, "적시 데이터 접근")가 LAKA에 어떻게 나타나는지:

| 갭 영역 | 현재 상태 추정 | 위험 | W7 도입 전 해결 필요? |
|----------|------------------|------|------------------------|
| Family 정의 부재 | SKU 단위로만 운영 추정 | Volume forecast 불가 → S&OP 작동 안 함 | **YES** (반드시) |
| SKU master 다부서 동기화 미흡 | 프로덕트·마케팅·SCM 각각 다른 ID 사용 가능 | Forecast vs Production 정합성 깨짐 | **YES** |
| 채널 코드 비표준 | 부서별 약어 (예: "Sephora" vs "SEPH" vs "세포라 US") | 데이터 통합 시 매핑 작업 매월 반복 | **YES** |
| ODM 입고 데이터 latency | 월말 후 5-10일 추정 | Step 1이 2일 안에 못 끝남 | YES (한국콜마·코스맥스 협조) |
| 채널 sell-through 자동화 | 세포라/Boots/Qoo10 각각 manual 다운로드 | weekly 운영 비용 高 | 부분 (MVP는 monthly batch로 시작) |
| 환율 단일 시나리오 부재 | 부서별 다른 환율 사용 가능 | Volume → $ 환산 시 부서 간 불일치 | **YES** (재무가 release) |
| 시장 인텔리전스 큐레이션 | 마케팅·글로벌사업 각자 모니터링, 통합 안 됨 | Marketing adjustment 인풋 일관성 결여 | 부분 (큐레이션 룰만 정의해도 OK) |

→ **YES 표시 6개는 W7 전 반드시 해결**. W4(Supply Planning)·W7(LAKA SOP v1) 작동의 전제 조건.

---

## 6. LAKA Step 1 매월 Cadence

| Working Day | 활동 | 책임 |
|--------------|------|------|
| 월말 마지막 영업일 | 전월 cutoff — 모든 시스템 closing | 각 부문 |
| 1 (오전) | 전월 ERP 출하·재고·환율 batch 산출 | SCM + 재무 |
| 1 (오후) | 채널 sell-through 다운로드 (세포라·Boots·Qoo10·국내) | 글로벌사업 + 국내사업 |
| 2 | ODM 입고 데이터 통합 (한국콜마·코스맥스) | SCM |
| 2 | 시장 인텔리전스 큐레이션 노트 | 마케팅 |
| 2 (오후) | Sally Smith Sheet의 actual 행 update | Process Owner (SCM S&OP파트) |
| 3 (오전) | 통계 baseline forecast 산출 | Demand Manager (마케팅) |
| 3 (오후) | Data quality report 산출 + Step 2 disseminate | Process Owner |

→ Step 1 총 3 working days. 매월 1-3일 안에 완료. Step 2 (Day 4-7)로 매끄럽게 연결.

---

## 7. Step 1 KPI (W5에서 상세)

| KPI | 정의 | 목표 (Stage 2-3 진입 시점) |
|-----|------|------------------------------|
| **Data On-time Rate** | 각 데이터 소스가 day 3 cutoff 안에 도착한 비율 | > 95% |
| **Data Completeness** | 필수 필드(Family·SKU·Channel·UoM·Qty·Date) 채워진 row 비율 | > 99% |
| **Master Data Drift** | 부서간 SKU·Family·Channel ID 불일치 건수 | 0 |
| **Statistical Baseline FVA** | baseline이 naive forecast(last month = next month) 대비 정확도 개선% | > +10%p |
| **ODM Data Latency** | ODM 입고 데이터 도착까지 working days | ≤ 2일 |
| **Channel Coverage** | 운영 채널 中 전월 sell-through 데이터 확보된 채널 % | > 95% |

---

## 8. 흔한 실패 패턴 (W6에서 심화)

| 패턴 | 원인 | 대응 |
|------|------|------|
| 부서별 다른 SKU·Family·Channel ID 사용 | 마스터 데이터 owner 미정 + 부서별 약어 관행 | Master Data Steward 1명 임명 (SCM 부문) + ID 표준 강제 |
| ODM 입고 데이터 지연 (월말 후 5-10일) | ODM과의 데이터 공유 합의 부재 | 한국콜마·코스맥스와 monthly batch 자동화 협의 (SCI CPFR 단계) |
| 채널 sell-through 수집 manual 의존 | 각 채널 시스템 다름·API 미연동 | MVP는 manual 허용, 6개월 후 RPA 또는 ETL 도구 도입 |
| 환율 부서별 다름 | 재무 release 미정착 | 재무가 매월 1일 환율 시나리오 3개 단일 release |
| Statistical baseline 무시되고 매월 manual override | 통계 도구 신뢰 부족 + FVA 미측정 | FVA 3개월 누적 후 객관 evidence 제시·교육 |
| 시장 인텔리전스 노트가 비대해짐 (모든 트렌드 다 적음) | 큐레이션 룰 부재 | "Top 3 actionable" 룰 강제 — 3개 이상 적지 말 것 |
| Data quality report가 작성되나 아무도 안 봄 | feedback loop 부재 | Process Owner가 매월 Pre-meeting에서 1 slide 보고 |

---

## 9. 출력 (→ Step 2)

| 출력 | 형식 | 받는 곳 |
|------|------|---------|
| 전월 actual update (Family·SKU·Channel) | Sally Smith Sheet actual 행 채움 | Demand Manager |
| Statistical baseline forecast (Family·SKU) | Sally Smith Sheet의 baseline 행 | Demand Manager (Marketing/Sales adjustment 출발) |
| 시장 인텔리전스 큐레이션 노트 (Top 3) | 1 페이지 노트 | Marketing 부문 (Marketing adj 인풋) |
| 환율 시나리오 3개 (base/opt/pess) | 표 | 재무 + 글로벌사업 |
| Data quality report | 표 | Process Owner + 책임 부문 |
| 마스터 데이터 변경 사항 (있을 시) | 표 | 전 부문 distribution |

---

## 10. 도입 로드맵 (data 측면)

| 단계 | 시점 | 활동 |
|------|------|------|
| **Phase 0** (지금부터 W7 전까지) | 0-2개월 | 마스터 데이터 거버넌스 6 영역 정의 — Family·SKU·Channel·UoM·Lead Time·Update Cycle |
| **Phase 1** (W7 Live Pilot 시작 시) | 2-5개월 | Sally Smith Sheet 운영 시작 (1-2 family) — manual 데이터 수집 OK |
| **Phase 2** (Wallace Expansion 단계) | 5-9개월 | 전 family 확장 + ODM·채널 데이터 자동화 일부 |
| **Phase 3** (Stage 3 진입 시) | 12-18개월 | ETL·RPA 도입 + 통계 도구 평가 (Excel → ToolsGroup·o9 검토) |

→ **Wallace 원칙**: ABC of Implementation — A(People) > B(Data) > C(Computer). Data(B)는 People 다음. 도구 도입 서둘지 말고 Step 1 manual 운영부터.

---

## 관련 페이지

- [[sop_overview]] — W1 (Step 1 위치)
- [[sop_glossary]] — W2 (Planning Master Data·Aligned vs Matrix Resources·Demand Manager·DTF·PTF 용어)
- [[demand_planning]] — 2. Demand Planning — Step 1 출력을 받는 곳
- [[supply_planning_odm]] — 3. Supply Planning (예정), Lead time·MOQ 활용
- [[sop_kpis]] — W5 (예정), Data on-time·Completeness 운영
- [[sop_failure_patterns]] — W6 (예정), 마스터 데이터 drift·ODM 지연 등 심화
- [[laka_sop_v1]] — W7 (예정), Phase 0-3 도입 로드맵 통합
- [[ODM]] / [[ODM_발주_프로세스]] — LAKA 현행 supply 측 — Lead time 매핑 source
- [[src_wallace_executive_guide_book]] — Ch4 Step 1 원천
- [[src_supply_chain_insights_sop_guide]] — Planning Master Data·58% 데이터 갭 통계 원천
- [[src_implement_sop_handbook]] — Ch11 IT-Supported S&OP·CPFR 단계 원천
