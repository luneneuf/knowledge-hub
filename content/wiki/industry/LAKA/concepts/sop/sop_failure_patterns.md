---
title: "S&OP Failure Patterns — 실패 패턴과 복구"
type: concept
axis: work
tags: [work/sop, s&op, failure, impediment, pothole, pitfall, moose-on-the-table, mini-sop, broken-process, laka]
created: 2026-05-11
updated: 2026-05-11
status: draft
publish: false
---

# S&OP Failure Patterns — 실패 패턴과 복구

> **본 페이지의 역할**: W6. S&OP 도입·운영의 실패 유형 통합. **Wallace 3 Impediments + Broken Process 7 신호 + SCI Pothole/Pitfall + Implement Suicide Quadrant** 를 한자리에 정리. LAKA 8부문별 위험 진단, Mini-S&OP Cycle 발동 trigger, 분기 회고 체크리스트, Re-implementation 경로.
>
> **연관 Linear 이슈**: [COM-25](https://linear.app/luneneuf) W6
>
> **선행**: 모든 이전 페이지 — 각 step 운영의 실패 패턴이 이 페이지에 통합

---

## 0. 분류 프레임워크 — 3 Type of Failure

S&OP 실패는 **본질·진화·단발** 3가지 type:

```
┌─────────────────────────────────────────────────────────┐
│ Type A — Behavior Change 실패 (도입 차원, 본질)         │
│   "S&OP 자체가 작동 안 함"                              │
│   Wallace 3 Impediments + Broken Process 7 신호         │
│   → 해결: Behavior Change 자체 (몇 개월)                │
├─────────────────────────────────────────────────────────┤
│ Type B — Process 열화 (운영 진화, 점진적)               │
│   "잘 작동했는데 점차 효력 잃음"                        │
│   SCI Pothole 5 + Pitfall 6 + Capability Gap Top 5      │
│   → 해결: 분기 회고 + KPI Stage progression             │
├─────────────────────────────────────────────────────────┤
│ Type C — Disruption 대응 실패 (단발, 외부 충격)         │
│   "한 사건이 plan을 깨뜨림"                             │
│   Sales 과대예측 / Suicide Quadrant / Stockout 6 원인   │
│   → 해결: Mini-S&OP Cycle 발동                          │
└─────────────────────────────────────────────────────────┘
```

→ 같은 증상도 type에 따라 처방이 다름. **진단이 잘못되면 잘못된 대응**.

---

## 1. Type A — Behavior Change 실패 (Wallace)

### 1.1 3 Impediments to Behavior Change ([[src_wallace_executive_guide_book|책]] Ch7)

#### Impediment #1 — Lack of Discipline / Self-Discipline

**원형**: Emil's Engineers 케이스 (100년 된 동부 제조사)

> *"You can't schedule creativity."* — Emil
>
> *"Meetings are considered optional; if they have nothing better to do, they may show up. Or they may not. This behavior exists up and down the line. That's our culture."*

**증상**:
- Pre-meeting·Exec Meeting attendance 비정형 (필수 참석자 빠짐)
- Forecast·Operations Plan 마감 working day 7 (Step 2 Consensus) 빈번 지연
- "I don't know when it'll be done" 답변 정상화
- Disciplined cadence보다 ad-hoc 의사결정 선호

**LAKA 적용 위험**:
- 크리에이티브 부문 (9명, CEO 겸임) — 마케팅 캠페인·신제품 컨셉 일정 cycle에 잘 안 맞춰질 위험
- 신생 조직 (LAKA) 일반 — 룰 정착 전 자유로운 운영 문화 잔존

**대응**:
- CEO·Process Owner 명시적 cadence 보호 (working day 7 절대 마감)
- 1년치 Exec Meeting 일정 사전 잡기 (Wallace 권장)
- 다른 회의·trade show·이사회와 충돌 회피
- "Cadence는 협상 안 됨, 단 콘텐츠는 협상 가능" 룰

#### Impediment #2 — Fuzzy Accountability

**원형**: Aerospace 케이스 (Boeing·Lockheed·NASA 거래사, "Best to work for" 명단)

> *"Touchy-feely culture, accountability was very muted and opaque."*

**증상**:
- Forecast 빗나가도 누가 책임인지 불명
- Production Plan Adherence 95% 미달인데 후속 액션 없음
- 같은 family 매월 다른 사람이 인풋, drift 추적 안 됨
- "그건 우리 영역 아니다" 답변 빈번

**LAKA 적용 위험**:
- 8부문 분리 + 글로벌·국내 사업 분리 → demand 인풋 책임 모호
- ODM 슬롯 부족 시 SCM vs 마케팅 vs 글로벌사업 책임 finger-pointing

**대응**:
- Family·KPI별 single owner 명시 (Demand Manager·Supply Planning Owner 등)
- 매월 Variance Analysis (Bias·MAPE·Adherence) 정량 추적
- Pre-meeting에 "지난달 빗나간 이유 + 다음달 보정" 어젠다 고정

#### Impediment #3 — Conflict Aversion + "Moose on the Table"

**원형**: NCR CEO 발언 — *"At our company, we try hard to get the moose on the table."*

**증상**:
- 회의실에 "큰 문제(무스)"가 있는데 아무도 안 꺼냄
- "Shoot the messenger" 회피 본능 — 문제 raise한 사람이 비난받음
- 갈등이 표면화 안 되니 결정 안 됨 → 상태 유지(status quo)
- Pre-meeting이 "리뷰만 하고 결정 안 하는" 회의로 변질

**LAKA 적용 위험**:
- 한국 조직 문화 일반 — 갈등 회피 경향
- 글로벌사업·국내사업·마케팅 사이 채널 우선순위 갈등 (글로벌 채널 vs 국내 trade-off)
- CEO 앞 임원 간 의견 충돌 회피

**대응**:
- **"Moose Rule"** — Pre-meeting·Exec Meeting에 누구든 어려운 이슈 raise 가능, retaliation 금지
- Bob Stahl 도구 차용: stuffed moose 인형 (또는 LAKA 버전 마스코트) — 어려운 이슈 raise 시 책상 위에 올림
- Pre-meeting에 "Top 3 Moose" 어젠다 고정 — 명시적 갈등 표면화 시간

### 1.2 Behavior Change vs Fact Transfer

Wallace 다이어트 비유:
- "적게 먹어라 / 잘 먹어라 / 운동해라" = fact transfer (정보 전달)
- 실제 살빼기 = behavior change (행동 변화)
- **두 개는 별개**. 정보만 전달해도 행동 변화 X.

**LAKA 적용**:
- 본 wiki의 모든 페이지 = fact transfer
- 실제 도입 = CEO·8부문 본부장 워크샵 + Live Pilot (W7) — behavior change 진행
- Wallace 권장 Implementation Path Phase 1·2 가 이 차원

### 1.3 Energy Alignment

```
Random energy → Aligned arrows
Accomplishment ↗   →   ACCOMPLISHMENT ▶▶▶▶▶
```

→ 조직 에너지가 무방향에서 한 방향 정렬. 갈등 표면화 후 해소의 결과.

**측정 가능 신호**:
- 8부문 KPI가 같은 방향 (예: 마케팅 매출 목표 ↔ SCM 재고 목표 정렬)
- 의사결정 후 부문 간 협업 속도
- 분기 회고에서 "이번 분기 가장 잘된 것" 답변의 일관성

---

## 2. Broken Process 7 신호 ([[src_wallace_executive_guide_book|Wallace]] p87)

S&OP가 "broken"이라는 진단 체크리스트. **이 중 3개 이상 ✓면 즉시 개입**.

| # | 신호 | 측정 | LAKA 분기 진단 (Y/N) |
|----|------|------|------------------------|
| B1 | Top management is not involved | CEO·6 본부장 attendance | TBD |
| B2 | Teamwork has not visibly improved | 8부문 협업 만족도 서베이 (Soft S1) | TBD |
| B3 | Meeting attendance is poor | Exec Meeting Attendance KPI | TBD |
| B4 | Focus is on mix and the short term | Pre-meeting 어젠다의 Volume vs Mix 비율 | TBD |
| B5 | Conflict is not resolved | "Top 3 Moose" 해결률 | TBD |
| B6 | Finger-pointing is not "off limits" | Variance Analysis의 finger-pointing 회수 | TBD |
| B7 | Decisions are not made | Exec Meeting "결정 안 됨"으로 끝난 이슈 % | TBD |

→ 분기 자가진단 시 7개 각각 ✓/✗ 평가.

### 2.1 신호별 즉시 개입 액션

| 신호 ✓ | 즉시 액션 |
|---------|------------|
| B1 | CEO 직접 대화 + Exec Meeting 일정 재확인 (Hold the High Ground) |
| B2 | 부문 간 사일로 진단 + Energy Alignment 워크샵 |
| B3 | Attendance 6 essential 100% 룰 강제 + alternate 지정 |
| B4 | Mix 안건은 Operational S&OP로 이관, Volume·Long-term 회복 |
| B5 | Moose Rule 재공유 + Pre-meeting facilitator 교체 검토 |
| B6 | KPI Governance — Single Source of Truth + 정량 evidence 우선 |
| B7 | Decision Authority 매트릭스 명시화 (W7) |

---

## 3. Type B — Process 열화 (SCI)

### 3.1 SCI Pothole 5종 (점진적 열화)

[[src_supply_chain_insights_sop_guide|SCI 가이드]] p13. "기술·일상 차원의 함정".

| # | Pothole | 의미 | LAKA 위험 |
|----|----------|------|------------|
| PH1 | Degradation of Planning Engine Effectiveness | 통계 baseline·forecast tool 점차 정확도 하락 | Stage 1 — Excel만 운영, 도구 미정착 |
| PH2 | Training and Skill Dilution | 핵심 인력 이직·신규 인력 교육 부족 | Demand Manager(가칭) 1명 의존 위험 |
| PH3 | Management of Planning Master Data | Family·SKU·Channel·Lead Time 마스터 데이터 drift | **[[data_gathering|1.]]에서 명시 — LAKA 가장 큰 갭** |
| PH4 | Clarity of Process Definitions | Step별 운영 룰의 점차 모호화 | 초기 합의 후 분기별 review 부재 위험 |
| PH5 | Shifts in Leadership | CEO·CFO·SCM 본부장 교체 시 commitment 약화 | LAKA 임원 교체 가능성 (특히 국내사업 본부장 공석) |

### 3.2 SCI Pitfall 6종 (구조적 함정)

"전략·거버넌스 차원의 함정".

| # | Pitfall | 의미 | LAKA 위험 |
|----|----------|------|------------|
| PF1 | Strategy Alignment | 회사 전략과 S&OP 의사결정의 분리 | CEO 전략 vs 부문 KPI 불일치 |
| PF2 | The Role of the Budget | 예산이 plan input vs plan output 혼동 | 분기 budget review와 monthly S&OP 분리 미흡 |
| PF3 | Organizational Governance | 의사결정 권한·책임 매트릭스 부재 | 8부문 분리 + 글로벌·국내 분리 — governance 복잡 |
| PF4 | Process Discipline and Clarity of Roles | 역할·룰의 점진적 변형 | 초기 정착 부재 시 fast erosion |
| PF5 | Measurement Systems | KPI gaming·잘못된 인센티브 | [[sop_kpis|W5]] §10 참조 |
| PF6 | Executive S&OP의 reporting line | Profit center에 reporting 못 함 | LAKA에서는 SCM 본부장→CEO 직보 ★ Wallace 권장 충족 |

### 3.3 LAKA 분기 회고 시 Pothole·Pitfall 체크리스트

| Pothole/Pitfall | Y/N | 증거 (KPI 또는 사건) | 보정 액션 |
|------------------|-----|----------------------|------------|
| PH1 통계 baseline 효력 하락 | | FVA layer 1 점진적 음수 | 통계 알고리즘 재검토·교육 |
| PH2 인력 skill 희석 | | 핵심 인력 turnover | 후임 교육·문서화 |
| PH3 마스터 데이터 drift | | Master Data Drift KPI > 0 | Master Data Steward 1명 임명 |
| PH4 프로세스 정의 모호 | | Pre-meeting facilitator 매번 다른 운영 | 분기 1회 룰 재확인 |
| PH5 리더십 교체 영향 | | 새 본부장 임명 사건 | Onboarding briefing 워크샵 |
| PF1 전략 정렬 | | CEO 전략 vs S&OP 결정 갭 | 분기 strategy review |
| PF2 예산 vs S&OP 혼동 | | budget input/output 명확 X | Process Owner가 룰 재정의 |
| PF3 거버넌스 | | 의사결정 finger-pointing | Decision Authority Matrix |
| PF4 역할·룰 변형 | | 같은 step을 부서별 다르게 운영 | 룰 재공표 |
| PF5 측정 시스템 | | KPI gaming 의심 | 다중 KPI 교차 검증 |
| PF6 reporting line | | S&OP가 profit center 못 들어옴 | 조직 구조 검토 |

### 3.4 SCI Capability Gap Top 5 ([[src_supply_chain_insights_sop_guide|SCI]] p19)

107개사 정량 서베이 — "중요도 vs 실제 수행" 갭. LAKA가 피해야 할 함정:

| 순위 | Capability | Importance | Performance | Gap |
|------|--------------|---------------|---------------|-----|
| 1 | What-if 분석으로 대안 도출 | 70% | 31% | **−39%** |
| 2 | 기회·리스크 관리 분석 | 85% | 49% | **−36%** |
| 3 | Sales-Operations 협업 | 88% | 55% | **−33%** |
| 4 | 최수익 계획 도출 기술 | 49% | 22% | **−27%** |
| 5 | 프로세스 흐름 관리 | 72% | 47% | **−25%** |

→ **상위 2개 모두 "분석 역량"** — 정량 시뮬레이션 도구 없이 토론 프로세스에 머무는 게 본질적 문제.

**LAKA 대응**:
- Sheets MVP에 **시나리오 컬럼 (best/base/worst) 필수** ([[demand_planning|2.]] §5.3)
- Stage 3 진입 후 What-if 도구 도입 검토 (ToolsGroup·o9 등)

---

## 4. Type C — Disruption 대응 (단발)

### 4.1 Sales 단기 과대·장기 과소예측 ([[src_implement_sop_handbook|Implement]] Ch4)

**원형 패턴**:
- 단기 1-3개월 forecast: Personal targets 반영 → 과대
- 4-12개월 forecast: Conservative bias → 과소
- 결과: 단기 stockout + 장기 overstock 동시 발생

**LAKA 적용 위험**:
- 글로벌사업 17명 + 국내사업 14명 = 31명의 Sales 인력
- 각자 다른 인센티브·target → bias 누적

**대응**:
- Baseline · Campaign · NPI 분리 인풋 강제 ([[demand_planning|2.]] §6.4)
- Layer별 FVA 측정 — Sales adjustment가 음수 FVA 지속 시 가중치 조정
- Sales target vs Forecast 분리 — target은 motivational, forecast는 best estimate

### 4.2 Suicide Quadrant ([[src_implement_sop_handbook|Implement]] Ch3)

**정의**: 장기 호라이즌 × SKU 세부 단위 조합 — 정확도 개선 없이 공수만 낭비.

```
              호라이즌
              단기      장기
       SKU  │  ✓       ❌ ← Suicide Quadrant
            │ (Mix)    (낭비)
       단위 │
       Family│ ◐       ✓ 
            │ (보조)   (Volume = Executive S&OP)
```

**LAKA 적용 위험**:
- 영업·마케팅이 18개월 forecast을 SKU 단위로 요구
- 결과: 분석 공수만 늘고 정확도 안 오름

**대응**:
- 15-36개월은 Family 단위만 ([[demand_planning|2.]] §4)
- SKU 단위는 0-3개월만 (Master Schedule 영역)

### 4.3 Stockout 6 원인 분류 ([[sop_kpis|W5]] §4.3 재인용)

| 원인 | 책임 step | 대응 |
|------|------------|------|
| Forecast 과소예측 | Step 2 | Demand consensus 개선 + FVA |
| ODM 슬롯 부족 | Step 3 | Capacity headroom·dual sourcing |
| ODM 정시 납품 실패 | 외부 | OTD 모니터링·협력사 다변화 |
| 운송 지연 | 외부 | Freight forwarder 다변화 |
| 라벨링·finishing 부족 | Step 3 | Finishing capacity 별도 추적 |
| 마스터 데이터 오류 | Step 1 | Master Data Drift KPI 0 |

---

## 5. Mini-S&OP Cycle 발동 Trigger (긴급 대응)

[[sop_glossary|용어집]] Mini-S&OP Cycle: 중대 disruption 시 같은 사람·포맷·프로세스로 부분 재실행.

### 5.1 발동 Trigger 매트릭스

| Trigger | 발동 여부 | 발동 시점 |
|---------|-------------|------------|
| Stockout 발생 (베스트셀러) | ★ 즉시 | 발견 working day +1 |
| Demand spike (>20% surge, 5일 이상 지속) | ★ 즉시 | 5일째 |
| Demand crash (>20% drop, 5일 이상 지속) | ★ 즉시 | 5일째 |
| Supply crash — ODM 라인 사고 | ★ 즉시 | 통보 받은 즉시 |
| Supply spike — 갑작스러운 추가 슬롯 확보 | 검토 | 다음 정기 cycle 가능 |
| 신규 채널 진입 결정 (NPI 외) | 검토 | 1주일 내 |
| Capacity Headroom < 0% (다음 3개월) | ★ 즉시 | 발견 즉시 |
| Major customer (예: 세포라) PO 변동 ±30%+ | ★ 즉시 | PO 도착 즉시 |
| 환율 급변 (±10% 주간) | 검토 | 1주일 누적 |
| ODM 정시 납품 실패 (OTD < 80%) | 검토 | 발생 시 |
| 4 Disruption (Demand spike/crash, Supply spike/crash) 본격화 | ★ 즉시 | Wallace 4가지 표준 |

### 5.2 Mini-S&OP Cycle 운영 룰

| 룰 | 내용 |
|----|------|
| 같은 사람 | Step 2 Consensus + Pre-meeting + Exec Meeting과 동일 |
| 같은 포맷 | Sally Smith Sheet 사용, 영향받은 family만 |
| 같은 프로세스 | Step 2→3→4→5 압축 실행 |
| 시간 압축 | 보통 3-5 working days (정규 7-10일의 50%) |
| Focus | 영향받은 family 1-3개만 |
| 출력 | "Updated Game Plan" + 다음 정규 cycle에 통합 |

### 5.3 Mini-S&OP 남용 위험

- 모든 사건에 Mini-S&OP 발동 → 정규 cycle 약화
- "DTF discipline" KPI 위반 정상화
- 임원 시간 burnout

→ **분기 1회 Mini-S&OP 발동 회수 review**. 6회/분기 이상이면 정규 cycle 자체 재점검 필요.

---

## 6. LAKA 8부문별 특화 위험 진단

VER. '26.03.04 조직 기반. 부문별 자주 발생할 위험 패턴 + 모니터링 KPI:

| 부문 | 인력 | 본부장 | 위험 패턴 | 모니터링 KPI |
|------|------|--------|------------|------------------|
| **프로덕트** | 8명 | 이정미 | NPI launch 일정 cycle 미준수 → Step 2 인풋 지연 | NPI 인풋 on-time, Cannibalization 추정 정확도 |
| **크리에이티브** | 9명 | CEO 겸임 | "스케줄링 못 함" (Emil 패턴) → 캠페인 일정 변동 | Campaign 인풋 on-time |
| **국내사업** | 14명 | **공석** | 본부장 부재 → demand 인풋 책임자 모호 | 국내 sell-through coverage |
| **마케팅** | 15명 | 안일홍 | Sales target vs Forecast 혼동, Baseline·Campaign 통합 인풋 | Marketing Adjustment FVA, Baseline 분리 준수 |
| **글로벌사업** | 17명 | 손여진 | 17명 4개 채널 분산 — channel별 다른 인풋 표준 | Channel별 sell-through coverage, Order Fill Rate by channel |
| **SCM** | 10명 | 김중찬 | ODM 슬롯 over-confirm, DTF 위반 빈발 | ODM Slot Utilization, Time-fence Discipline |
| **재무** | 4명 | 이종영 CFO | 환율 단일 release 미정착, KRW 환산 부서 간 불일치 | KRW Single Source of Truth |
| **경영지원** | 4명 | 안일홍 | (S&OP 직접 인풋 없음) — 그러나 CEO 비서 역할 시 Exec Meeting 운영 책임 | Exec Meeting attendance·Decision On-time |

### 6.1 가장 큰 위험 3개 (LAKA 특화)

1. **국내사업 본부장 공석** — Step 2 인풋 책임 owner 부재. CEO가 임시로 owner 담당 필요.
2. **마스터 데이터 drift** ([[data_gathering|1.]] §5 진단) — 6개 갭 모두 W7 전 해결 필수.
3. **ODM 슬롯 경쟁** ([[supply_planning_odm|3.]] §4.2) — 거의 모든 critical resource가 Matrix. 한국콜마·코스맥스 협상력 보강.

---

## 7. 분기 회고 체크리스트 (자가진단)

### 7.1 분기 회고 Agenda (90분 권장)

| Section | 시간 | 활동 |
|----------|------|------|
| 1. Process KPI Review | 15분 | 22개 Process KPI Stage 진화 |
| 2. Outcome KPI Review | 15분 | Hard 8 + Soft 7 |
| 3. **Broken Process 7 신호 진단** | 10분 | 각 ✓/✗ |
| 4. **Pothole·Pitfall 체크** | 15분 | 11개 항목 |
| 5. Mini-S&OP 발동 회수 review | 5분 | 회수·trigger·해결 시간 |
| 6. **Capability Gap Top 5 진단** | 10분 | LAKA 현재 수준 자가 평가 |
| 7. Stage Maturity 자가 진단 | 10분 | SCI 5단계 어디 |
| 8. **Top 3 Moose** | 10분 | 갈등 표면화 |

### 7.2 자가진단 점수표

매 항목 4점 척도 (0=문제 심각, 1=문제 있음, 2=정상, 3=우수):

| 영역 | 점수 (0-3) | 액션 |
|------|---------------|------|
| Broken Process 7 신호 (✗ 개수 ÷ 7 점수) | | |
| Pothole 5 (정상 운영 비율) | | |
| Pitfall 6 (정상 운영 비율) | | |
| Capability Gap Top 5 (LAKA 자체 평가) | | |
| Stage Maturity 자가 평가 | | |

→ 종합 점수가 떨어지면 Re-implementation 경로 검토.

---

## 8. Re-implementation 경로 ([[src_wallace_executive_guide_book|Wallace]] p87-89)

S&OP가 broken 진단 시 복구 매뉴얼:

### 8.1 결정 트리

```
Step 1: Broken Process 7 신호 중 3개 이상 ✓?
   YES → Step 2
   NO  → 분기 회고에서 개선 액션 (Type B 대응)

Step 2: President·staff 매월 참여하는가?
   YES → self-audit 결과대로 문제 해결
   NO  → Step 3 (Re-implementation 필요)

Step 3: President가 Executive Briefing 동의?
   YES → Wallace Implementation Path 처음부터 (Live Pilot부터)
   NO  → Step 4

Step 4: President가 "Outsider Audit" 동의?
   YES → 외부 컨설턴트(또는 Wallace 책 기반 자가 audit) → mini Executive Briefing → 1 product family 재시작
   NO  → 살려두기 — 점진 개선, executive staff 멤버 참여 유지, 다음 분기 재진단
```

### 8.2 Re-implementation 위험 신호

- President 회의 결석이 6개월 누적 50%+
- Pre-meeting이 "리뷰만 하고 결정 안 되는" 회의로 변질 6개월+
- Soft Benefit 서베이 평균 2.5점 미만
- Process KPI 22개 중 50%+ 목표 미달

→ 한 가지라도 해당 시 즉시 CEO 직접 대화.

---

## 9. 출력 (분기 회고 + 연간 maturity 진단)

| 출력 | 받는 곳 | 빈도 |
|------|----------|------|
| 분기 회고 보고서 (체크리스트 + Top 3 Moose) | Exec Meeting | 분기 |
| Mini-S&OP 발동 log | Process Owner | 분기 |
| Capability Gap 자가 평가 | 임원진 + 분기 review | 분기 |
| Stage Maturity 진단 (SCI 5단계) | CEO·이사회 | 연간 |
| Re-implementation 결정 (필요 시) | CEO·이사회 | ad-hoc |

---

## 관련 페이지

- [[sop_overview]] — W1 (Hard/Soft Benefits 프레임워크)
- [[sop_glossary]] — W2 (Moose on the Table·Mini-S&OP Cycle·Energy Alignment·Suicide Quadrant 용어)
- [[data_gathering]] — 1. (Master Data Drift 진단)
- [[demand_planning]] — 2. (Sales 과대예측 패턴 + FVA layer)
- [[supply_planning_odm]] — 3. (Time-fence Discipline 위반 패턴)
- [[sop_kpis]] — W5 (KPI Gaming 함정·Single Source of Truth)
- [[laka_sop_v1]] — W7 (예정), Wallace Implementation Path 적용
- [[K뷰티_ODM_QA_실패_8유형]] — 외부 공급 disruption 사례 (Mini-S&OP 발동 trigger 참조)
- [[ODM_발주_프로세스]] — Time Fence·DTF 위반 시 대응 base
- 📎 [laka_sop_template_v0.xlsx](./laka_sop_template_v0.xlsx) — FVA_Tracking 시트에 Sales 음수 FVA 패턴 시연
- [[src_wallace_executive_guide_book]] — Ch7 3 Impediments + Broken Process 7 + Re-implementation 원천
- [[src_wallace_executive_sop_workshop]] — Identifying·Fixing Broken Process 원천
- [[src_implement_sop_handbook]] — Sales 과대예측 + Suicide Quadrant 원천
- [[src_supply_chain_insights_sop_guide]] — Pothole/Pitfall + Capability Gap + Maturity 원천
