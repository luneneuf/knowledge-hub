---
title: "S&OP Handbook — Implement Consulting Group (2014)"
type: summary
axis: work
tags: [work/sop, s&op, implement, supply-chain, demand-planning]
created: 2026-05-10
updated: 2026-05-10
status: active
publish: false
---

# S&OP Handbook — Implement Consulting Group

**출처:** Implement Consulting Group P/S (덴마크 기반 경영컨설팅)
**판:** 4th edition, 2014 (Light Version — 축약본. 전체판은 별도 문의)
**파일:** `raw/sop/implement_sop_handbook_2014.pdf` (31p)
**연관 이슈:** [[COM-20]] W1 sop_overview.md 생성 시 주요 참고 소스

---

## 소스 개요

Tom Wallace(S&OP 개념 창시자 중 한 명)와 협업하는 컨설팅 펌이 만든 실무 핸드북.
이론이 아닌 "현장 구현 관점"에서 S&OP를 설명하며, 11개 챕터로 구성된다.

**이 핸드북의 핵심 주장:**
> *"S&OP 구현은 People 65%, Process 25%, System 10%의 문제다. 그러나 실제 프로젝트에서는 System에 80%를 쏟는다."*

---

## 챕터별 핵심 내용

### Ch1. What is S&OP (p4~5)
- 용어 혼란: IBP, S&OP, Executive S&OP, SIOP, MIOE 등은 사실상 동일 개념 (Tom Wallace 견해)
- APICS 정의: "수요·공급 균형, 재무·운영 계획 통합, 전략과 일상 운영 연결을 위한 의사결정 프로세스 집합"
- 3개 기능의 본질적 이해충돌: Sales(재고↑), Operations(안정적 생산), Finance(비용↓)
- S&OP = 이 충돌을 하나의 균형 잡힌 의사결정으로 해소하는 메커니즘

### Ch2. Why S&OP (p6~8)
- **타이밍 실패의 연쇄**: 용량 확대 늦음→납기 실패, 용량 삭감 늦음→과잉비용, 재고 확대 늦음→매출 손실
- **진단 질문 9가지**: 용량·공급 가시성, 크로스펑셔널 의사결정 존재 여부, 과거 놓친 기회 등
- **임팩트 수치** (Tom Wallace, 2009, 미검증 평균치):
  - 납기 정시 +25%, 재고 수준 -41%, 생산 다운타임 -35%, 공장 효율 +17%, 운송비 -17%
- **4개 차원 균형**: Focus(목표)·Process(설계)·People(행동)·System(데이터)

### Ch3. S&OP 프로세스 구조 (p9~11)
- **4개 계획 레이어**:
  | 레이어 | 호라이즌 |
  |--------|---------|
  | Strategic planning | 5년 |
  | **S&OP** | **2~18개월** |
  | Tactical planning | 1~3개월 |
  | Operational planning | 0~6주 |
- **"Suicide Quadrant"**: 장기 호라이즌에서 SKU 단위 세부 계획 = 정확도 개선 없이 공수만 낭비
- **월간 4주 사이클**:
  - W1: Demand Planning (통계 예측 + Sales 인풋 + 수요계획 승인) + Product Review
  - W2: Supply Planning (크리티컬 자원 검토, 공급망 계획, 수요 갭 파악) + Inventory Planning
  - W3: Balancing & Decisions (시나리오 분석, Pre-meeting, Executive 의사결정 회의, 재무 업데이트)
  - W4: Execution (핸드오버, Latest Estimate 업데이트, 의사결정 커뮤니케이션)

### Ch4. Demand Forecasting (p12~13)
- **7개 관점**:
  1. Sales·Finance·Operations 공유 합의 수량 예측
  2. 예측 집계 수준은 의사결정 수준에 맞춰야
  3. Sales is from Venus, Operations is from Mars → 예측은 Operations가 생성, Sales가 검토
  4. 통계 예측은 단순·투명해야
  5. 베이스라인과 캠페인/입찰 물량 분리
  6. SKU당 투입 시간은 임팩트에 비례 배분
  7. KPI는 호라이즌별로 다르게 설정
- **Sales 편향 패턴**: 단기 과대예측, 장기 과소예측

### Ch5. New Product Introduction (p14)
- 신제품 출시 = 가장 큰 수요 불확실성 원천이자 Demand Shaping 수단
- 반드시 S&OP에 통합: 순증분 물량 + 카니발리제이션 동시 추적
- 개발 단계별로 S&OP 통합 방식이 달라야

### Ch6. Capacity & Inventory Planning (p15~16)
- **5개 관점**:
  1. 공급망 스케일러빌리티를 모든 엔티티별로 파악
  2. 예측 정확도로 안전 여유 설정
  3. 호라이즌별 의사결정 주체 명확화 (Sales vs Operations)
  4. 각 레이어는 하위 레이어가 설정한 제약 내에서 계획
  5. 계획 세부도 ≤ 예측 분산 (세부 계획이 정확도보다 세밀하면 의미 없음)
- **공급망 스케일러빌리티**: 각 공급망 엔티티(생산·창고·운송·공급사)마다 탄력성 범위가 다름
  - 예: 초과근무로 +5%, 추가 교대로 +8~12%, 외주로 +15~25%
  - 탄력성 범위와 반응 시간을 호라이즌과 매핑해야

### Ch7. One Common Language (p17~19)
- Sales(€/브랜드·채널) ↔ Finance(€/사업부) ↔ Operations(수량·kg/생산사이트) = 각각 다른 언어
- "Google Translate" 필요: 시장 전망 → 재무 전망, 공급망 요건으로 변환
- 설계 핵심:
  1. 제품 계층구조 + 고객 그룹핑 계층구조 정의
  2. 예측 집계 수준 = 의사결정 수준과 일치

### Ch8. Scenario Planning & Decision-Making (p20~21)
- S&OP = 토론 프로세스가 아니라 **의사결정 프로세스**
- 시나리오 분석 → 의사결정 추천안 → KPI 대시보드 순서로 임원에게 제시
- 불확실성 高일 때 (신제품, 포트폴리오 전환, 빅 성장, 장기 계획): 단일 예측 → 시나리오 범위(best~worst)로 전환
- 정의: "가능한 미래 사건을 대안적 결과로 분석하는 과정"

### Ch9. Finance in S&OP (p22~23)
- Finance의 6개 역할: 시나리오 계획·비즈니스 케이스, 분산 분석, 재무 조정, 예측 공동 소유, 정기 재무 전망(RE/YTG), 성과관리
- 핵심: 판매·운영 계획을 재무 언어로 변환해야 전사 비즈니스 플랜과 비교 가능
- Finance는 S&OP에서 핵심 파트너 — 후방 지원이 아닌 공동 의사결정자

### Ch10. Key Principles for Implementation (p24~25)
- **4가지 원칙**:
  1. **Create impact**: Business case 기반 목적 정의, KPI 성공 기준 연결
  2. **Executive commitment**: Sales·Operations·Finance 임원 참여, 워크숍 기반
  3. **Get started**: 병행 구현 (프로젝트와 동시에 S&OP 사이클 시작), 프로토타입 우선
  4. **S&OP methodology**: 표준 방법론 활용, 성숙도 자가진단으로 목표 수준 설정
- **Gartner 5단계 성숙도**:
  - Stage 1 React → Stage 2 Anticipate → Stage 3 Integrate → Stage 4 Collaborate → Stage 5 Orchestrate

### Ch11. IT-Supported S&OP (p26~28)
- S&OP 성공 투자 비중 권장: **Mindset/People 65%, Process 25%, System 10%**
- 실제 프로젝트 현실: System 80%, Process 15%, People 5% → 역전된 우선순위
- 시스템 필요도 결정 인자: 복잡도(공급망 티어 수, 제품 수) + 애자일성(시장 변동성, 예측 품질)
- 단순 프로세스: Excel로 충분 / 고도화 단계: 시나리오 계산 가능한 APS 필요

---

## LAKA 적용 시 핵심 시사점

**LAKA 조직 개요 (VER. '26.03.04 기준):**
전체 83명, 1지사(일본), 8부문, 17팀, 10파트

| 부문 | 인원 | 본부장 | S&OP 역할 |
|------|------|--------|-----------|
| 프로덕트 | 8명 | 이정미 | NPI 인풋 |
| 크리에이티브 | 9명 | CEO 겸임 | — |
| 국내사업 | 14명 | 공석 | 국내 수요 인풋 |
| 마케팅 | 15명 | 안일홍 | 수요 계획 주도 |
| 글로벌사업 | 17명 | 손여진 | 채널별 수요 인풋 |
| SCM | 10명 | 김중찬 | **S&OP 주관** (SC기획팀 내 S&OP파트) |
| 재무 | 4명 | 이종영 CFO | 재무 조정 |
| 경영지원 | 4명 | 안일홍 | — |

| 챕터 | LAKA 현황 | 시사점 |
|------|-----------|--------|
| Ch3 프로세스 | 월간 S&OP 미구축 | W1~W2 학습 후 4주 사이클 설계 |
| Ch4 수요예측 | ODM 의존, 신제품 비중 高 | 베이스라인과 런치 물량 분리가 우선 |
| Ch5 NPI | 신규 컬러·SKU 빈번 출시 | S&OP에 NPI 검토 항목 명시적 포함 |
| Ch6 공급계획 | ODM 슬롯 제약이 병목 | ODM 슬롯 = 핵심 스케일러빌리티 지점 |
| Ch7 공통언어 | 세포라(USD) ↔ ODM(개수) ↔ 재무(KRW) | 환율·단위 변환 규칙 사전 합의 필요 |
| Ch10 구현 원칙 | CEO 스폰서십 확보 여부 미정 | Stage 1~2 수준에서 병행 구현 시작 |
| Ch11 IT | SCM 부문 10명이 주관, 전사 참여 크로스펑셔널 | Sheets 기반 MVP로 시작, 시스템 투자 후순위 |

---

## 파생 페이지

- (예정) [[sop_overview]] — W1 작업 시 이 소스 주요 인용
- (예정) [[demand_planning]] — Ch4 기반
- (예정) [[supply_planning_odm]] — Ch6 기반
- (예정) [[sop_failure_patterns]] — Ch10·11 기반
