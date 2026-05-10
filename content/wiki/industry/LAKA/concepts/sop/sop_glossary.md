---
title: "S&OP 용어집 — Glossary"
type: concept
axis: work
tags: [work/sop, s&op, glossary, terminology, laka]
created: 2026-05-11
updated: 2026-05-11
status: draft
publish: false
---

# S&OP 용어집 (Glossary)

> **본 페이지의 역할**: W2. Wallace 책 [[src_wallace_executive_guide_book|*Executive's Guide*]] Glossary 70+ 용어 + Implement·SCI 보충 용어를 한국어로 번역하고 LAKA 적용 시 의미를 명시. W3~W7에서 인용되는 용어의 표준 정의.
>
> **연관 Linear 이슈**: [COM-21](https://linear.app/luneneuf) W2

---

## 사용 안내

- 용어는 카테고리별로 묶음. 카테고리 안에서는 중요도순.
- 각 항목: **원어** — 한국어 — 정의 — *LAKA 적용*(있을 때) — `출처`
- `W`=Wallace 책/워크샵, `I`=Implement 핸드북, `S`=SCI 가이드
- **굵게** 표기된 용어는 W1~W7에서 빈번히 인용되는 핵심 용어

---

## 1. Core S&OP Frameworks

### **Sales & Operations Planning (S&OP)**
**판매·운영 계획.** demand와 supply를 균형 맞추는 비즈니스 프로세스 집합. **Executive S&OP** + Demand Planning + Supply Planning + Master Scheduling + 기타 detail-level 도구. 단독 사용 시 보통 큰 entity 전체를 가리킴. `W·I·S`

### **Executive S&OP**
**임원 S&OP.** S&OP 중 **aggregate volume** 수준에서 demand와 supply를 균형 맞추는 **임원 의사결정 프로세스**. 매월 1회, family 단위, units AND $$$ 동시. *Wallace: "Executive S&OP is the heart of Sales & Operations Planning."* — S&OP의 핵심 엔진. `W`

### **Integrated Business Planning (IBP)**
**통합 사업 계획.** Oliver Wight 진영(2005~)이 도입한 용어. 일부는 "Sales + Finance + SCM의 데이터 연결", 일부는 "S&OP의 성숙 형태"로 해석. **SCI 입장: IBP = Maturity Stage 3** (S&OP의 진화 형태). `S`

### **One Set of Numbers**
**하나의 숫자.** Executive S&OP의 결과물 원칙 — 영업·운영·재무가 같은 forecast/plan을 공유. 단, 상장사는 internal stretch goals + external 보수적 숫자 두 set 운영 가능. `W`

---

## 2. Volume vs Mix (The Four Fundamentals)

### **Volume**
**볼륨.** "얼마나(How much)?" — aggregate 수준의 판매·생산 rate. **Product Family** 단위, monthly 18-36개월 호라이즌, **Top Management** 책임. Executive S&OP의 다루는 차원. `W`

### **Mix**
**믹스.** "어떤 것을(Which ones)?" — 개별 product·SKU·고객 주문 단위 details. Weekly/Daily, 1-3개월 호라이즌, **Middle Management** 책임. Master Scheduling의 다루는 차원. `W`

### **Product Family**
**제품군.** Executive S&OP의 **기본 계획 단위**. 분류 기준: 고객·시장·application·사용 방식. **Sales/Marketing 관점**에 적합. *LAKA: 립 글로스 컬러군, 틴트, 아이섀도, 선케어 등으로 분류 예정 (W3에서 확정).* `W`

### **Product Subfamily**
**제품 하위군.** Family와 SKU 사이 중간 단위. Family A 안에 A1·A2·A3 등. *LAKA: 립 글로스 → 베스트셀러 vs 시즌 한정 등 하위 그룹화 가능.* `W`

### **Aligned Resources vs Matrix Resources**
**정렬 자원 vs 매트릭스 자원.** Aligned = 한 family 전용 (예: Family A는 Department 1에서만 생산). Matrix = 여러 family 공유 (Department 1이 A·C·D·G 생산). 매트릭스가 capacity 계획 더 복잡. *LAKA: 한국콜마·코스맥스 ODM 라인은 모두 matrix (여러 K뷰티 브랜드 공유). 슬롯 경쟁 관리가 핵심.* `W`

---

## 3. 시간 호라이즌 (Time Horizons)

### **Strategic Planning**
**전략 계획.** 3-5년 호라이즌, 네트워크 디자인·M&A·신사업·CapEx. S&OP의 인풋. `W·I·S`

### **Business Plan / Business Planning**
**사업 계획 / 사업 계획 수립.** 연간 dollar 단위 예산, 3-5 회계연도까지 확장. 첫 1년이 annual budget, 이후는 less detail. Top management의 corporate office·이사회·금융계 공약. `W`

### **Tactical Horizon**
**전술 호라이즌.** 주~월 단위, order/inventory matching ~ aggregate 자재계약 수준. **Executive S&OP가 여기에 거주**. `S`

### **Operational Time Horizon / Slush Period**
**운영 호라이즌 / 슬러시 기간.** 일~주 단위, order duration 다음·tactical 직전. S&OP 실행이 일어나는 기간 — 이전 plan을 실행 결과로 변환. `S`

### **Executional Period / Order Duration**
**실행 기간 / 주문 지속 기간.** 주문 확정 후 출하까지. 산업별: consumer electronics 1일, consumer products 2.7일, discrete 수주~수개월. `S`

---

## 4. Time Fences (시간 경계)

### **Demand Time Fence (DTF)**
**수요 시간 경계.** Master Schedule에서 **미판매 예측을 무시**하는 근시점 구간. 보통 finishing lead time 근처. 이 안에서는 confirmed orders만 반영. *LAKA: 한국콜마 finishing lead time 30-45일 → DTF는 약 30일.* `W`

### **Planning Time Fence (PTF) / Critical Time Fence**
**계획 시간 경계.** Master Schedule에서 detailed planning이 반드시 존재해야 하는 구간. 보통 cumulative lead time × 1.25~1.5. 이 안에서는 시스템이 자동 변경 안 함. *LAKA: ODM cumulative lead time ~75일 → PTF 약 90-110일.* `W`

### **Time Fence (일반)**
미래 시점 중 하나의 time zone과 다른 time zone을 구분하는 지점. `W`

---

## 5. Demand-Side 용어

### **Demand Plan**
**수요 계획.** forecast + 확정 customer orders + 기타 anticipated demand (interplant, export, samples). = Sales Plan의 양적 표현. `W`

### **Sales Forecast / Forecast**
**판매 예측.** 미래 수요의 추정. `W`

### **Sales Plan**
**판매 계획.** Sales/Marketing 경영진이 forecast된 수준의 실제 customer orders를 달성하기 위해 취하는 모든 합당한 조치에 대한 commitment. = Demand Plan의 의도 표현. `W`

### **Mix Forecast / Detailed Forecast**
**믹스 예측 / 세부 예측.** 개별 product 단위 forecast. 단기 plant·supplier scheduling용. `W`

### **Volume Forecast / Aggregate Forecast / Product Group Forecast**
**볼륨 예측.** Family/group 단위 forecast. Sales planning·capacity planning·재무 분석·재무 projection 사용. `W`

### **Forecast Error**
**예측 오차.** forecast가 actual sales와 deviate한 양. MAD, SOD로 측정. `W`

### **MAD (Mean Absolute Deviation)**
**평균 절대 편차.** forecast 오차의 절댓값 평균. *LAKA: 컬러군별·채널별로 MAD 추적, W5 KPI 후보.* `W`

### **Bias / SOD (Sum of Deviations) / RSFE (Running Sum of Forecast Error)**
**편향.** 오차의 누적 합(±). 일관된 과대/과소 예측 측정. Sales가 단기 과대·장기 과소예측하는 패턴이 흔함(Implement). `W·I`

### **Forecast Consumption**
**예측 소비.** 불확실한 미래 demand(forecast)를 known future demand(주로 customer orders)로 대체하는 프로세스. `W`

### **Forecast Frequency**
**예측 빈도.** forecast를 full review·update하는 빈도. 보통 월간. `W`

### **Forecast Horizon**
**예측 호라이즌.** forecast가 커버하는 미래 시간 길이. *LAKA Executive S&OP: 18-36개월 권장.* `W`

### **Forecast Interval**
**예측 간격.** 예측 시간 구간의 폭. 보통 weekly 또는 monthly. *LAKA Executive S&OP: monthly.* `W`

### **Forecast Value Added (FVA)**
**예측 부가가치.** 각 단계(통계 baseline → marketing 조정 → sales 조정 등)가 예측 정확도를 개선하는 정도. 음수면 그 단계가 정확도를 떨어뜨림. `S`

### **Demand Sensing**
**수요 감지.** 시장 판매 신호를 **zero-latency·no-bullwhip**으로 부서 간 전달. 룰 기반이 아닌 consumption 데이터 기반. SCI Pandemic Shift의 핵심. `S`

### **Demand Management**
**수요 관리.** Sales forecasting + customer order entry + order promising + DC requirements + interplant orders + service/spare. ATP·Abnormal Demand 관리 포함. `W`

### **Demand Manager**
**수요 관리자.** Demand Management 프로세스 조율 직무. 통계 forecasting 시스템 운영 + marketing/sales와 협업. *LAKA: 마케팅 부문 BM/PM 파트가 후보, W7에서 지정.* `W`

### **Abnormal Demand**
**비정상 수요.** forecast에 없던 비정상적으로 큰 수요 (보통 신규·비전형 고객). ATP·Master Schedule이 별도 처리. *LAKA: 신규 글로벌 채널 진입 시점 적용.* `W`

### **Bullwhip Effect**
**채찍 효과.** demand 신호가 supply chain의 functional silo를 통과할 때 증폭·왜곡되는 현상. S&OP·Demand Sensing이 완화. `S`

---

## 6. Supply-Side 용어

### **Operations Plan / Production Plan**
**운영 계획 / 생산 계획.** Sales Plan을 지원하고 재고/backlog 목표를 달성하기 위한 합의된 생산·조달 rate·volume. Exec Meeting 승인 후 Master Scheduler의 "marching orders". `W`

### **Supply Planning**
**공급 계획.** Demand Plan을 만족하고 재고·backlog 목표를 위한 production rate 설정 (in-house + outsourced). RCCP가 보통 지원. `W`

### **Capacity Planning**
**용량 계획.** 미래 production에 필요한 capacity 결정. Aggregate level (RCCP) 또는 detail level (CRP). `W`

### **Rough-Cut Capacity Planning (RCCP)**
**대략적 용량 계획.** Operations Plan 또는 MPS를 미래 capacity requirements로 변환. demand가 aggregate units → 표준 hours 변환. **Departmental level** 검증. *LAKA: ODM 라인 일별 슬롯 → 월간 LAKA 가용 슬롯 매핑.* `W`

### **Capacity Requirements Planning (CRP)**
**용량 요구 계획.** Detailed level capacity. open production orders + planned orders를 work center별·time period별 hours로 변환. 복잡 job shop용. `W`

### **Material Requirements Planning (MRP)**
**자재 요구 계획.** BOM·재고·MPS 데이터로 자재 requirements 계산. Replenishment 주문 권고 + 재일정 권고. `W`

### **Distribution Requirements Planning (DRP)**
**배송 요구 계획.** MRP 로직을 원격 위치(DC·consignment·고객 창고) 재보충에 적용. Planned orders가 Master Schedule의 input이 됨. *LAKA: 미국·영국·일본 창고 보유 후 적용 가능.* `W`

### **Master Schedule / Master Production Schedule (MPS)**
**기준 일정 / 기준 생산 일정.** **Product 단위** demand/supply 균형. Executive S&OP의 family-level 균형을 mix-level로 변환. ATP의 source. `W`

### **Master Scheduling Policy**
**기준 일정 정책.** Top management 승인 문서. demand/supply 양쪽의 역할·책임·decision rights·time zone별 권한을 명시. *LAKA: W7 거버넌스 문서의 핵심.* `W`

### **Available-to-Promise (ATP)**
**약속 가능 재고.** 현재 재고 + 미래 재고(MPS) 중 customer orders로 commit되지 않은 부분. Customer order promising의 핵심 도구. *LAKA: 채널별 배분 시 ATP 분리 필요.* `W`

### **Capable-to-Promise (CTP)**
**약속 가능 능력.** ATP의 발전형. 정식 스케줄에 없지만 available material·capacity로 생산 가능한 부분까지 포함. 보통 APS에 탑재. `W`

### **Projected Available Balance**
**투영 가용 잔고.** 미래 재고 잔고. On-hand 재고 − requirements + scheduled receipts + planned orders의 running sum. `W`

### **Resource**
**자원.** Production·delivery에 가치를 더하는 것들. Plant·department·supplier·equipment·skilled labor. `W`

---

## 7. Order Fulfillment Strategies

### **Make-to-Stock (MTS)**
**재고생산.** 주문 받기 전에 완제품을 미리 만들어 finished goods inventory에 보관. *LAKA: 베스트셀러 컬러군 (예: 207 모브) 후보.* `W`

### **Make-to-Order (MTO)**
**주문생산.** 주문 받은 후 제조. 표준 + 고객 specific 변형 결합. *LAKA: 시즌 한정 컬러, 글로벌 채널 한정 라벨.* `W`

### **Finish-to-Order (FTO) / Assemble-to-Order (ATO) / Build-to-Order (BTO)**
**완성생산 / 조립생산.** Subcomponents·bulk product를 sales forecast로 미리 만들고, 주문 받은 후 finishing. Dell Computer가 대표. *LAKA: 다국가 라벨링 변형 (bulk는 미리, 채널별 finishing은 주문 후).* `W`

### **Design-to-Order (DTO)**
**설계생산.** 주문 받은 후 detailed design 시작. 복잡 customized one-of-a-kind. *LAKA 직접 적용 X.* `W`

### **Demand/Supply Strategies**
**수요·공급 전략.** Family별 "Meet the Customer" 정의 statement. 예: "Family A는 MTS, target line fill 99.5%, target finished inventory 10일치." *LAKA: W7에서 컬러군별 명시 (W1의 Volume Family 후보 표 참조).* `W`

### **Target Fill Rates · Target Finished Goods Inv · Target Customer Order Backlog**
**목표 충족률 · 목표 완제품 재고 · 목표 주문 백로그.** Demand/Supply Strategy 안의 정량 목표. 보통 days on hand로 표현. `W`

---

## 8. Service Metrics

### **Order Fill Rate**
**주문 충족률.** 전체 customer orders 대비 정시·완전 출하된 주문 비율. Line fill보다 엄격. 한 주문에 20개 라인 중 1개라도 빠지면 그 주문은 0. *LAKA W5 KPI 1순위.* `W`

### **Line Fill Rate**
**라인 충족률.** 주문 라인 단위 정시·완전 출하 비율. *LAKA W5 KPI 보조 — [[OTD]] 확장.* `W`

---

## 9. The 5-Step Process & Meetings

### **Five-Step Executive S&OP Process**
**5단계 임원 S&OP 프로세스.** Step 1 Data Gathering → Step 2 Demand Planning → Step 3 Supply Planning → Step 4 Pre-meeting (Heavy Lifting) → Step 5 Executive Meeting. `W`

### **Pre-meeting**
**사전 회의.** Step 4. Executive Meeting 앞 cross-functional 의사결정 회의 — 권한 내 사항 자체 결정, 권한 밖은 recommendations + scenarios 준비. **"이게 우리 회사라면 무엇을 결정할까?"** 사고방식. Middle manager의 임원 ranks 진입 훈련장. `W`

### **Exec Meeting / Executive Meeting**
**임원 회의.** Step 5. 월간 S&OP의 culminating event. President + staff + key individuals 참석. 1-2시간. Family-by-family 의사결정 + business plan 영향 검토. `W`

### **Demand Consensus Meeting**
**수요 합의 회의.** Step 2 마무리. Senior Sales/Marketing 인원이 forecast 검토·challenge·승인 → "management-authorized forecast" 도출. Exec Meeting의 surprises 방지. `W`

### **Compromise Meeting** (Eli Lilly 용어)
Pre-meeting의 별칭. 모든 참가자가 일부 양보하여 전체 비즈니스에 가장 좋은 plan으로 수렴. `W`

### **Mini-S&OP Cycle**
**미니 S&OP 사이클.** 중대 disruption (supply crash/spike, demand crash/spike) 발생 시 정규 monthly cycle 외에 가동되는 abbreviated process. **같은 사람·포맷·프로세스 사용**, 영향받은 부분만 focus. `W`

### **Sally Smith's Spreadsheet**
**샐리 스미스 스프레드시트.** Wallace의 표준 1페이지 표. 3개 블록(Forecast·Production·Inventory) × Forecast/Actual/Difference/Cum Difference 행 × 월 컬럼. *LAKA W7 MVP 시트 직접 차용.* `W`

---

## 10. Organizational / Behavioral 용어

### **Stewardship**
**수탁 책임.** 임원이 corporate office·이사회·주주·금융계·직원·공급사·지역사회에 대해 갖는 책임. S&OP는 임원의 이 책임 수행 도구. `W`

### **Hold the High Ground**
**고지 점거.** Wallace 군사 비유. S&OP 도입 시 처음부터·끝까지 top management(특히 President)를 hands-on으로 끌어들이는 원칙. `W`

### **Build It and They Will Come** (경고)
"기술·프로세스 먼저 만들고 top mgmt 사후 설득" 접근법. **낮은 성공 확률**. Hold the High Ground와 정반대. `W`

### **The Moose on the Table**
**책상 위의 무스.** NCR CEO 유래 비유. 모든 회사에 의제에 안 오르는 큰 문제(=무스)가 있음. 무스 노출 = 해결 첫 단계. Bob Stahl은 컨설팅 시 literal stuffed moose 제공 — 갈등 표면화 안전 보장 ("shoot the messenger" 회피). *LAKA: Pre-meeting에 도입 가능.* `W`

### **Conflict Aversion**
**갈등 회피.** Wallace 책 Ch7 Impediment #3. S&OP 성공의 주요 장애. 해결: Moose on the Table + Energy Alignment. `W`

### **Energy Alignment**
**에너지 정렬.** 조직 에너지가 무방향 → 한 방향 정렬. 갈등 표면화 후 해소의 결과. Figure 7-1. `W`

### **Behavior Change vs Fact Transfer**
**행동 변화 vs 사실 전달.** Wallace의 다이어트 비유: "적게 먹어라/잘 먹어라/운동해라"는 fact transfer. 실제 살빼기는 behavior change. **두 개는 별개**, fact transfer만으로는 부족. `W`

### **ABC of Implementation**
**구현의 ABC.** A = People (가장 중요, 영향의 2/3+) → B = Data → C = Computer (가장 후순위). Wallace + Oliver Wight 원칙. `W`

---

## 11. Maturity & Failure Patterns

### **5-Stage Maturity Model (SCI)**
**5단계 성숙도 모델.** Stage 1 React (기능 사일로) → Stage 2 Sales-Driven (S 또는 OP 편중) → Stage 3 IBP (부분 정렬) → Stage 4 Demand-Driven (다단위 feasible plan) → Stage 5 Market-Driven (시장-시장 oscillator). 6차원 평가: Alignment/Goal/Capability/Measurement/Execution/Reporting. *LAKA 현재 Stage 1-2, 18개월 목표 Stage 3.* `S`

### **Gartner 5-Stage Maturity (Implement 인용)**
React → Anticipate → Integrate → Collaborate → Orchestrate. SCI 모델과 단계 명칭 다르나 진화 방향 동일. `I`

### **Pothole vs Pitfall**
**구덩이 vs 함정.** SCI 구분. Pothole = 점진적 열화 (계획 엔진·교육·마스터데이터·프로세스 명확성·리더십). Pitfall = 구조적 함정 (전략 정렬·예산 역할·거버넌스·프로세스 규율·측정 시스템). 분기 회고 체크리스트. `S`

### **Broken Process — 7 Signals**
**고장난 프로세스 7 신호.** Wallace: ①top mgmt 불참 ②teamwork 개선 안 됨 ③회의 attendance 저조 ④mix·단기 focus ⑤conflict 미해결 ⑥finger-pointing not "off limits" ⑦decisions not made. 분기 self-audit. *LAKA: W6 체크리스트 base.* `W`

### **3 Impediments to Behavior Change**
**행동 변화의 3대 장애물.** Wallace 책 Ch7: ① Lack of Discipline/Self-discipline ② Fuzzy Accountability ③ Conflict Aversion. `W`

### **Suicide Quadrant**
**자살 사분면.** Implement Ch3. 장기 호라이즌 × SKU 세부 단위 조합 — 정확도 개선 없이 공수만 낭비. `I`

---

## 12. Cross-Cutting Concepts (SCI 6 정의)

### **Harmonization**
**조화.** Sales/Finance/SCM 데이터를 단위·SKU·위치 차원에서 부서 간 변환. 통합(integration)이 아닌 변환 가능 상태. `S`

### **Synchronization**
**동기화.** 다른 cycle·horizon의 시스템·프로세스를 한 자리에 통합. `S`

### **Orchestration**
**오케스트레이션.** 기능별 대안의 양방향 trade-off로 최적안 도출. Maturity Stage 4-5의 핵심 역량. `S`

### **Planning Master Data**
**계획 마스터 데이터.** 대체 소싱·사이클 타임·환산율·원가·리드타임. 모든 계획의 baseline. *LAKA: ODM 리드타임·환율(USD/KRW)·SKU 변환표·MOQ가 핵심.* `S`

### **Above the Line vs Below the Line**
**선 위 vs 선 아래.** "Line" = Executive S&OP review meeting. Above = Executive S&OP 자체. Below = 자재·자산 중심 실행 계획 (DRP/MRP/MEIO). 지난 10년간 Above는 발전, Below는 더 messy. `S`

### **Outside-In vs Inside-Out**
**외부→내부 vs 내부→외부.** Inside-Out = enterprise 데이터(주문 이력) 기반. Outside-In = 시장 데이터(소비 신호) 기반. Stage 4-5의 전환 방향. `S`

---

## 13. Process Frameworks (병렬 비교)

### **Lean Manufacturing**
**린 제조.** 모든 자원(시간 포함) 사용 최소화 강조. Plant + 직접 suppliers에 강함. Toyota가 대표. `W`

### **Kanban**
**칸반.** Lean의 demand pull 신호 방법. Downstream operation이 upstream에 카드(또는 신호)로 요청. `W`

### **Lean + Executive S&OP — "You Need 'Em Both"**
Wallace Appendix B. Lean = 실행, S&OP = 미래 의사결정. Lean = plants·직접 suppliers, S&OP = customers·suppliers 양방향. 보완 관계. `W`

### **CPFR (Collaborative Planning, Forecasting, and Replenishment)**
**협업 계획·예측·보충.** Supply chain partners 간 jointly managed planning. "Second generation ECR." *LAKA: 한국콜마와의 future state.* `W`

### **ECR (Efficient Consumer Response)**
**효율적 소비자 응답.** Retailer·distributor·supplier가 supply chain의 과잉 비용 제거 위해 협업. `W`

### **VMI (Vendor Managed Inventories)**
**공급사 관리 재고.** Replenishment 의사결정을 공급사가 담당. 공급사가 stockout 방지 + 합의된 재고 수준 유지 책임. `W`

### **APS (Advanced Planning Systems)**
**고급 계획 시스템.** 최적화 알고리즘 기반 단기 scheduling. CTP·what-if 시뮬레이션 탑재 가능. SCI 벤더 카탈로그 33개 중 다수가 APS 계열. `W·S`

### **DDMRP (Demand Driven Material Requirements Planning)**
**수요 기반 자재 요구 계획.** MRP의 발전형. O8SupplyChain·Demand Solutions 강세. `S`

---

## 14. Financial Integration

### **Financial Interface**
**재무 인터페이스.** 재무 정보와 운영 정보를 함께 운영. Operational 데이터가 financial 데이터와 다르지 않게 'one set of numbers' 운영. `W`

### **Financial Planning**
**재무 계획.** Revenues·costs·cash flow·기타 자산 변동에 대한 달러 단위 projection. `W`

### **Running Delta**
**런닝 델타.** Wallace 책 Ch8 미래 비전. (a) Executive S&OP에서 승인된 volume plan ($) vs (b) 현재 운영 중 detailed schedule 합계 ($)의 차이. 실시간 drift 모니터링. `W`

### **Red Zone**
**레드 존.** 분기 말 며칠 — Wall Street earnings call 직전 critical 시기. Running Delta가 red zone calls 정확도 향상. *LAKA가 비상장이지만 동일 규율 가능.* `W`

### **Audit Trail of Decisions**
**의사결정 감사 추적.** 중요 의사결정 누가/언제/왜 했는지 기록. Sarbanes-Oxley 시대 governance 요건. 책임 추궁이 아닌 학습용. `W`

### **Sarbanes-Oxley (SOX)**
미국 2002년 기업 governance 법. 분기 reporting 정확도 강제. Executive S&OP가 분기 예측 신뢰성 향상에 기여 → SCI도 강조. `W·S`

---

## 15. Global S&OP

### **Entity (Global S&OP)**
**엔티티.** Demand와 supply가 정렬되는 지역(region). 5-step 프로세스가 entity 내에서 완전 실행. *LAKA: 일본지사 1개 보유 — 그러나 supply는 한국 단일이므로 entity 1개 운영 가능.* `W`

### **Global Consolidation (Step 6)**
World HQ에서 각 entity의 Exec Meeting 결과 통합. `W`

### **Global Exec Meeting (Step 7)**
주로(배타적이지 않게) 재무 중심의 글로벌 의사결정. `W`

---

## 16. Wallace 라이브러리 (외부 참조)

### **Sales & Operations Planning: The How-To Handbook**
Wallace 책. *Executive's Guide*보다 implementation 상세. **현재 LAKA 보유 X — 입수 우선순위 1**. `W·라이브러리`

### **Sales & Operations Planning: The Self-Audit Workbook**
Wallace 책. **분기 자가진단 체크리스트** — W6 직접 차용. **현재 보유 X — 입수 우선순위 1**. `W·라이브러리`

### **Sales & Operations Planning: Best Practices**
Dougherty & Gray (2006). 13개사 케이스 (Scotts·Cast-Fab·Eli Lilly 포함). `W·라이브러리`

### **Enterprise Sales & Operations Planning** (Palmatier & Crum)
Oliver Wight 진영의 대안 학파. IBP 강조. `W·라이브러리`

---

## 핵심 한국어 번역 정책

LAKA 내부 문서/회의에서 사용할 한국어 번역 통일안:

| 영문 | 권장 한국어 | 비고 |
|------|-------------|------|
| Sales & Operations Planning (S&OP) | **S&OP** (영문 유지) | 약어가 표준 |
| Executive S&OP | **임원 S&OP** | 또는 영문 유지 |
| Volume / Mix | **볼륨 / 믹스** | 영문 음역 |
| Product Family | **제품군** | 컬러군·카테고리 등 LAKA 맥락 추가 |
| Demand Plan / Supply Plan | **수요 계획 / 공급 계획** | — |
| Pre-meeting | **사전 회의** | 또는 Pre-meeting |
| Executive Meeting | **임원 회의** | 또는 Exec Meeting |
| Sally Smith Spreadsheet | **표준 S&OP 시트** | 비유 제거 |
| Hold the High Ground | **CEO 직접 참여 원칙** | 비유 의역 |
| Moose on the Table | **무스 룰 / 어려운 이슈 명시 룰** | 비유 유지 + 설명 |
| Bullwhip Effect | **채찍 효과** | 표준 번역 |
| Pothole / Pitfall | **구덩이 / 함정** | 분기 회고 항목명 |

---

## 관련 페이지

- [[sop_overview]] — W1 (이 용어집의 framing)
- [[demand_planning]] — W3 (예정), Forecast 용어 심화
- [[supply_planning_odm]] — W4 (예정), Capacity·Time Fences 심화
- [[sop_kpis]] — W5 (예정), MAD·SOD·Fill Rate 운영
- [[sop_failure_patterns]] — W6 (예정), Pothole/Pitfall·3 Impediments·Broken Process 7 신호
- [[laka_sop_v1]] — W7 (예정), 모든 용어의 LAKA 적용 통합
- [[ODM]] / [[ODM_발주_프로세스]] — Demand Time Fence·Planning Time Fence LAKA 현행 매핑
- [[OTD]] — Order Fill Rate / Line Fill Rate 확장 base
- [[src_wallace_executive_guide_book]] — 본 용어집의 70+ 용어 원천
- [[src_wallace_executive_sop_workshop]] — Mini-S&OP Cycle·Sally Smith·Hold the High Ground 원천
- [[src_implement_sop_handbook]] — Suicide Quadrant·Gartner 5단계 원천
- [[src_supply_chain_insights_sop_guide]] — Maturity 5단계·6 정의·Pothole/Pitfall 원천
