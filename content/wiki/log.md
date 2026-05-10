---
title: "Log"
updated: 2026-05-10
---

# 변경 이력

## [2026-05-11] W3 | demand_planning — Step 2 운영 매뉴얼 (COM-22)

**신규 생성**: `wiki/industry/LAKA/concepts/sop/demand_planning.md` — concept 페이지, W3 산출물

**구성 (10개 섹션)**:
1. 위치·책임 매핑 — Demand Manager(마케팅 BM/PM)·Marketing(15)·국내사업(14)·글로벌사업(17)·프로덕트(8)·재무(4)·승인 라인
2. Step 2 인풋 — Step 1 데이터 + LAKA 추가 인풋 (채널별 sell-through·ODM 슬롯·환율 시나리오·시즌 캠페인)
3. **4-Layer Forecast Layering** — Statistical baseline → Marketing adj → Sales adj → Senior Consensus
4. **FVA (Forecast Value Added)** 측정 — 각 layer가 정확도 개선/악화에 기여한 정도. Sales 단기 과대예측 패턴 경고
5. Volume vs Mix 분리 — Volume은 Step 2 (Family), Mix는 후속 Master Schedule (SKU)
6. **NPI(신제품) 4 차원** — Incremental·Cannibalization·Pipeline fill·Sample. LAKA 컬러 launch curve 양식
7. **Sally Smith Spreadsheet LAKA 템플릿** — 3 블록(Forecast/Production/Inventory) × 립 글로스 컬러군 A 예시 + 시즌·캠페인·NPI 행 분리 양식
8. LAKA Step 2 매월 cadence — Working day 1-7
9. Demand-side KPI 6개 사전 정의 (MAPE·Bias·FVA·Consensus On-time·NPI Accuracy)
10. 흔한 실패 패턴 6개 + 출력(→Step 3) 5종

**LAKA 특화 결정사항**:
- 매월 working day 7까지 management-authorized forecast 확정
- NPI 시나리오 3개(base/opt/pess) 모두 Supply Planning에 전달 → ODM 발주는 base·재고 hedge는 worst
- Forecast Update 후 Cum Difference 색상 ±5%/±10%/±15% 트래픽 라이트
- Volume→$ 환산 시 재무 단일 환율 시나리오 사용 (부서별 다른 환율 금지)

**index.md 업데이트**: demand_planning 등재. 페이지 카운트 150 → 151.

**다음**: W4 supply_planning_odm — Step 3 상세 + ODM 슬롯·Capacity 매핑 + Demand/Planning Time Fences

## [2026-05-11] W2 | sop_glossary — S&OP 용어집 (COM-21)

**신규 생성**: `wiki/industry/LAKA/concepts/sop/sop_glossary.md` — concept 페이지, W2 산출물

**구성** (16개 카테고리, 100+ 용어):
1. Core S&OP Frameworks — S&OP / Executive S&OP / IBP / One Set of Numbers
2. Volume vs Mix — Product Family / Subfamily / Aligned vs Matrix Resources
3. 시간 호라이즌 — Strategic / Business / Tactical / Operational / Executional
4. Time Fences — DTF / PTF
5. Demand-side — Forecast / MAD / SOD / FVA / Demand Sensing / Bullwhip 등 14개
6. Supply-side — Operations Plan / RCCP / CRP / MRP / DRP / MPS / ATP / CTP 등 11개
7. Order Fulfillment Strategies — MTS / MTO / FTO / DTO / Demand·Supply Strategies
8. Service Metrics — Order Fill Rate / Line Fill Rate
9. 5-Step Process & Meetings — Pre-meeting / Exec Meeting / Mini-S&OP Cycle / Sally Smith Spreadsheet
10. Organizational/Behavioral — Stewardship / Hold the High Ground / Moose on the Table / ABC
11. Maturity & Failure — 5-Stage Maturity / Pothole vs Pitfall / Broken Process 7 신호 / 3 Impediments
12. Cross-Cutting (SCI 6) — Harmonization / Synchronization / Orchestration / Above-Below the Line / Outside-In
13. Process Frameworks 병렬 — Lean / Kanban / CPFR / VMI / APS / DDMRP
14. Financial Integration — Running Delta / Red Zone / Audit Trail / SOX
15. Global S&OP — Entity / Global Consolidation
16. Wallace 라이브러리 — How-To Handbook / Self-Audit Workbook 등 입수 우선순위

**한국어 번역 통일안 표** 포함 — LAKA 내부 문서/회의 표준화 base.

**LAKA 매핑 명시 용어** (W3-W7에서 인용 예정): Product Family (컬러군), Demand Time Fence (한국콜마 finishing 30-45일), Planning Time Fence (~90-110일), Matrix Resources (ODM 슬롯 경쟁), MTS/MTO/FTO (베스트셀러/시즌한정/채널라벨변형), Order Fill Rate (W5 1순위), Demand Manager (마케팅 BM/PM 파트 후보), Master Scheduling Policy (W7 거버넌스 핵심).

**index.md 업데이트**: sop_glossary 등재. 페이지 카운트 149 → 150.

**다음**: W3 demand_planning — Step 2 상세 + Sally Smith Spreadsheet 템플릿 + Forecast Value Added (FVA) 적용

## [2026-05-11] W1 | sop_overview — LAKA S&OP 도입 개요 (COM-20)

**신규 생성**: `wiki/industry/LAKA/concepts/sop/sop_overview.md` — concept 페이지, S&OP 학습 W1 산출물

**구성**:
- LAKA = Wallace가 명시한 Designer/Distributor 카테고리 (Microsoft X-Box 매핑)
- 현재 격차 진단 (분기 budget만 vs 매월 rolling, ODM 슬롯 사후 매칭 등)
- The Four Fundamentals — Volume × Mix / Demand × Supply
- 시간 호라이즌 4-tier (Strategic / Business / **Executive S&OP** / Detailed)
- 5-Step Monthly Process + LAKA 초기 cadence 제안
- 4개 인풋 → President 1.5h/월
- LAKA 조직 매핑 (8부문, Process Owner = SCM 부문 S&OP파트)
- Hard/Soft Benefits + CFO 어젠다 (Adam Szczepanski 인용)
- SCI Maturity Model 적용 — LAKA 현재 Stage 1-2, 18개월 목표 Stage 3
- W1~W7 로드맵 + Wallace 4-phase Implementation Path

**핵심 인용 5개 (임원 브리핑용)**: Wallace Designer/Distributor 정당성, President 1.5h, Hold the high ground, CFO 어젠다, SCI 60/30/10

**index.md 업데이트**: LAKA — S&OP (concepts/sop/) 섹션 신설, sop_overview 등재. 페이지 카운트 148 → 149.

**다음**: W2 sop_glossary — Wallace 책 Glossary 70+ 용어 한국어 + LAKA 매핑

## [2026-05-10] ingest | Wallace & Stahl — Sales & Operations Planning: The Executive's Guide (2006, 책)

**소스**: `raw/study/sop/wallace_executive_guide_book_2006.pdf` (144p, T.F. Wallace & Company, 2006 1쇄→2014 7쇄, ISBN 978-0-9978877-9-2, Internet Archive 2022 디지털화)

- **신규 생성**: `wiki/industry/LAKA/sources/src_wallace_executive_guide_book.md` — Wallace+Stahl 책 본문 정리. 워크샵 슬라이드와 같은 프레임워크 + **신규 자산 4개 집중**:
  - Ch5 비제조업 적용 (Retail/Designer-Distributor/Process Design/Banks) + Best Practice 3개사 (Scotts·Cast-Fab·Eli Lilly)
  - Ch7 3 Impediments to Behavior Change (Lack of Discipline/Fuzzy Accountability/Conflict Aversion + "Get the Moose on the Table") + Energy Alignment + 4-step Implementation Path
  - Ch8 Future Vision: Top Management War Room / Running Delta / Red Zone / Audit Trail (Sarbanes-Oxley governance)
  - Appendix A Terminology Shift + Appendix B Lean+S&OP + Glossary 70+ 표준 용어 (W2 sop_glossary 직접 차용 가능)
- **index.md 업데이트**: src_wallace_executive_guide_book 추가, 총 페이지 147 → 148

**왜 별도 src로 작성했나 (워크샵 src와 분리)**:
- 같은 저자·같은 프레임워크지만 매체 다름 (워크샵 슬라이드 vs 출판물 144p)
- 책에만 있는 신규 자산 4개가 LAKA에 직접 적용 가능
- 워크샵은 5-step process diagram·Sally Smith·Mini-S&OP의 1차 자료, 책은 Designer/Distributor 카테고리·Glossary·Future Vision의 1차 자료 — 상호 보완

**LAKA 적용 결정적 인용 (책 Ch5)**:
> "공장 소유 여부는 중요하지 않다 — demand/supply는 여전히 균형 필요하다." (Designer/Distributor 카테고리, Microsoft X-Box 사례)

→ **LAKA의 ODM 의존 구조 = Wallace가 명시적으로 적용 가능하다고 한 카테고리**. W1 sop_overview 첫 문단 핵심 정당성.

**CFO 직접 차용 인용 (Adam Szczepanski, V&M Star CFO, p93)**:
> "Executive S&OP는 보통 1년에 1-2번만 일어나는 strategic process에 매월 life를 가져온다."

→ LAKA CFO 이종영 대상 어젠다 협상 한 줄.

**Wallace 라이브러리 입수 우선순위 (책 Appendix C에서 확인)**:
1. Wallace, *Self-Audit Workbook* (2005) — W6 체크리스트
2. Wallace+Stahl, *How-To Handbook* (3rd Ed) — W7 implementation 상세 (현재 raw에는 웹 리서치 요약만)
3. Dougherty & Gray, *S&OP: Best Practices* (2006) — 13개사 케이스
4. Crum & Palmatier, *Demand Management Best Practices* (2003) — 마케팅 부문 어젠다

## [2026-05-10] ingest | Tom Wallace — Sales & Operations Planning Workshop (2010)

**소스**: `raw/study/sop/wallace_executive_sop_workshop_2010.pdf` (91p, 슬라이드 deck, OMTEC Chicago 2010-06-16, www.tfwallace.com)

- **신규 생성**: `wiki/industry/LAKA/sources/src_wallace_executive_sop_workshop.md` — Wallace 워크샵 전문 정리. 12개 Part(Volume/Mix Fundamentals → 5-step Process → Sally Smith Spreadsheet → Risk/Mini-S&OP → Global 7-step → ABC Implementation → Broken Process Diagnosis → Future) + 3개 소스(Implement/SCI/Wallace) 종합 비교 표 + LAKA 조직 매핑 + 시사점 표
- **index.md 업데이트**: src_wallace_executive_sop_workshop 추가, 총 페이지 146 → 147

**왜 1차 권위인가**:
- Implement(2014) 핸드북에서 Wallace 협업 명시
- SCI(2020) 가이드에서 Wallace 프레임워크 인용
- 두 보조 소스가 모두 가리키는 본인 자료가 이 PDF
- 기존 raw `wallace_sop_handbook_summary.md` (책 요약, 웹 리서치 기반)와 동일 저자·동일 프레임워크지만 매체가 다름(book vs workshop slides) — 이 슬라이드가 1차 자료

**Wallace 고유 자산 (다른 두 소스에 없음)**:
- Volume vs Mix 분리 (Executive S&OP=Volume, Operational S&OP=Mix) — 전체 프레임워크의 출발점
- Sally Smith's Spreadsheet 1페이지 표준 표 (Forecast/Actual/Diff/Cum Diff × 수요/공급/재고 3블록) → **W7 MVP 시트 템플릿 직접 차용**
- 5-step Process (Data → Demand → Supply → Pre-Meeting "Heavy Lifting" → Exec Meeting)
- Mini-S&OP Cycle (긴급 대응 매커니즘, 같은 사람·포맷·프로세스로 부분 재실행)
- Global Executive S&OP 7-step (Entity 기반)
- ABC of Implementation (A=People, B=Data, C=Computer)
- Hybrid software 권장 ("When in doubt, pick 3")
- 정량 가이드라인: 8-12개월, <$100K, President 1.5h/월
- "Hold the high ground" vs "Build it and they will come" 경고
- Broken Process 7 신호 + Re-implementation 경로

**LAKA 적용 핵심**: W1·W7에서 Wallace를 1차 인용으로 채택, Implement·SCI는 보조. CEO 월 1.5h commitment 어젠다 협상이 진입 장벽 가장 낮은 출발점.

## [2026-05-10] ingest | Supply Chain Insights — S&OP: A Guide for the Supply Chain Leader (2020)

**소스**: `raw/study/sop/supply_chain_insights_sop_guide_2020.pdf` (39p, Lora Cecere & Regina Denman, Supply Chain Insights LLC, Open Content)

- **신규 생성**: `wiki/industry/LAKA/sources/src_supply_chain_insights_sop_guide.md` — SCI 가이드 전문 요약. Executive Overview·정의·Pre-Pandemic State·Pandemic Shifts·Maturity Model 5단계·Capability Gap·33개 벤더 카탈로그·Implement 핸드북 비교·LAKA 적용 시사점 표
- **index.md 업데이트**: src_implement_sop_handbook + src_supply_chain_insights_sop_guide 두 줄 추가, 총 페이지 144 → 146

**핵심 자산 (LAKA 적용)**:
- 5단계 Maturity Model 표 (Stage 1 Reactive → Stage 5 Market-Driven, 6차원 평가)
- 정량 갭 데이터: 데이터 접근 58%, 신제품-운영 정렬 −38%, Sales-Ops −36%, What-if 분석 −39%
- 변화관리 60% / 프로세스 30% / 기술 10% 투자 비중 (Implement 65/25/10과 정합)
- 33개 벤더 LAKA 적합도 평가 — 1순위 후보군: ToolsGroup·o9 (단, Stage 3 진입 후 검토)

**연관 이슈**: COM-20 (W1 sop_overview), COM-25 (W5 sop_kpis), COM-26 (W6 sop_failure_patterns) 보조 인용 소스. concepts/sop/ 페이지는 W1~W7 진행 시 생성 예정.

## [2026-04-21] ingest | 캡틴 차이나 리단, 안사이(휘), 그리고 정씨 해상제국

**소스**: 대화 중 제공된 심층 리서치 (이단·정지룡·정성공 3세대 동아시아 해상 패권사)

- **신규 생성**: `wiki/history/uwo/people/이단.md` — 이단(李旦/Andrea Dittis) 전기. 마닐라→히라도, 1624년 팽호 협상 중재, 캡틴 휘 네트워크 구조, 정지룡과의 관계
- **신규 생성**: `wiki/history/uwo/people/정지룡.md` — 정지룡(鄭芝龍/Nicholas Iquan) 전기. 이단 상단 VOC 통역사→시바즈히 18인 연맹→명 제독→요라오만 해전→청 처형
- **신규 생성**: `wiki/history/uwo/people/정성공.md` — 정성공(鄭成功/Koxinga) 전기. 히라도 출생→1659 남경 공략 실패→1661 대만 침공→VOC 축출→동녕국 건국→1662 급사
- **업데이트**: `wiki/history/uwo/people/하마다_야효에.md` — "리단(李旦)" 언급에 [[이단]] 위키링크 추가

## [2026-04-21] ingest | 쿠로호로슈와 오다 노부나가 직속 무장 — 역할·실전·후대 왜곡

**소스**: `raw/uwo/쿠로호로슈_오다노부나가_직속무장.md`

- **신규 생성**: `wiki/history/uwo/themes/호로슈.md` — 쿠로호로슈·아카호로슈 제도 상세 (호로의 기원·편성·인원 사료 불일치·역할·구성원·후대 왜곡)
- **신규 생성**: `wiki/history/uwo/people/삿사_나리마사.md` — 쿠로호로슈 필두, 나가시노 철포 봉행, 사라사라고에, 1588년 할복
- **업데이트**: `wiki/history/uwo/people/마에다_도시이에.md` — 아카호로슈 필두 정보 추가, 호로슈·삿사_나리마사 링크 추가

## [2026-04-19] ingest | 나사우 함대 항해 보고서 + 심층 리서치

**소스**:
- `Downloads/나사우 함대 (Nassausche Vloot) 항해 보고서.md`
- `obsidian-vaults/uwo/raw/perplexity/2026-04-14_나사우함대_심층리서치.md`

- **신규 생성**: `wiki/history/나사우_함대.md` — 함대 구성·지휘관·항해 경로·전투 결과·역사적 의의 종합
- **신규 생성**: `wiki/history/후안_페르난데스_제도.md` — 지리·나사우 함대 기착·셀커크 연결·섬 이름 변천
- **신규 생성 (entity ×7)**: 자크_르_에르미트, 헨_스하펜함, 율리우스_페르스호르, 비터_더윗, 아돌프_데커, 요하네스_판발베크, 야코프_베헤르

## [2026-04-19] ingest | 알렉산더 셀커크 리서치 노트

**소스**: 대화 중 제공된 UWO History 트위터 스레드용 원재료 리서치 노트

- **신규 생성**: `wiki/history/알렉산더_셀커크.md` — 생애 연표, 무인도 생존 기록, 핵심 아이러니 5개, 로빈슨 크루소 연계, UWO 소재 정리

## [2026-04-16] ingest | 가나자와성 소실의 역사와 전성기의 위용

**소스**: `raw/uwo/2026-04-16_가나자와성_소실의역사.md` (Perplexity 리서치)

**신규 생성 페이지** (11개):

*places/*
- `wiki/history/uwo/places/가나자와성.md` (entity) — 가가 백만 석 거성, 6차 화재 연표 포함
- `wiki/history/uwo/places/이시카와몬.md` (entity) — 현존 성문, 납 기와·나마코 벽 원형 보존
- `wiki/history/uwo/places/다쓰미용수.md` (entity) — 1631년 구축 11km 방화 수로

*events/*
- `wiki/history/uwo/events/가나자와성_화재연대기.md` (summary) — 1602~1881, 6차 화재 전체 연대기
- `wiki/history/uwo/events/호레키_대화재.md` (summary) — 1759년 10,508호 소실, 사상 최대

*people/*
- `wiki/history/uwo/people/마에다_도시이에.md` (entity) — 초대 번주, 1583년 입성
- `wiki/history/uwo/people/마에다_도시쓰네.md` (entity) — 3대 번주, 소가마에·다쓰미용수 구축

*themes/*
- `wiki/history/uwo/themes/납_기와.md` (concept) — 납 지붕 기와, 가나자와성 고유 건축재
- `wiki/history/uwo/themes/파괴_소방법.md` (concept) — 에도 소방 방식, 인근 건물 파괴로 방화선 구축
- `wiki/history/uwo/themes/소가마에.md` (concept) — 성+성하 이중 해자 방어 체계
- `wiki/history/uwo/themes/푄_현상_가나자와.md` (concept) — 봄 대화재 반복의 자연 원인

**업데이트 페이지**:
- `index.md` — 11개 페이지 추가, 총 81페이지

## [2026-04-16] ingest | 스에쓰구 헤이조 인물 카드 (UWO-30, UWO-15 파생)

**소스**: `raw/uwo/하마다야효에_나위츠사건_전면개정.md` (기존 소스 재활용)

**신규 생성 페이지**:
- `raw/uwo/suetsugu-heizo.md` (소스 요약)
- `wiki/history/uwo/people/스에쓰구_헤이조.md` (entity) — 나가사키 대관, 하마다 야효에 직속 상관, 타이오완 사건 막후 조종자, 1630년 사망

**업데이트 페이지**:
- `wiki/history/uwo/people/하마다_야효에.md` — 관련 인물에 [[스에쓰구_헤이조]] 추가
- `wiki/history/uwo/events/타이오완_사건.md` — 본문·연표·관련 페이지에 [[스에쓰구_헤이조]] 링크 추가

## [2026-04-15] ingest | 하마다 야효에 생애와 나위츠 사건 (전면개정)

**소스**: `raw/uwo/하마다야효에_나위츠사건_전면개정.md` (이미지 2장 포함)

**신규 생성 페이지**:
- `wiki/history/uwo/people/하마다_야효에.md` (entity) — 에도 초기 주인선 선장, 1628년 납치 사건 주인공
- `wiki/history/uwo/events/타이오완_사건.md` (summary) — 1628년 나위츠 납치 사건 전모 + 외교 후폭풍 연표

**이미지 등록**:
- `raw/uwo/assets/hamada_fort_zeelandia.jpg`
- `raw/uwo/assets/hamada_nuyts_ukiyoe.jpg`

**업데이트 페이지**:
- `wiki/history/uwo/events/마카오_전투.md` — 타이오완_사건, 하마다_야효에 크로스링크 추가

## [2026-04-11] infra | Asana MCP 연동 완료
- Asana 프로젝트 3개 생성: 회사 업무 / 산업 공부 / 역사+콘텐츠
- 각 프로젝트에 섹션 4개 생성: 📥 백로그 / 🔄 진행 중 / 👀 검토 중 / ✅ 완료
- `scripts/asana_task.py` 스크립트 작성 및 동작 확인
- `CLAUDE.md`에 Asana 연동 규칙 + 모든 GID 기록
- `~/.zshrc`에 ASANA_ACCESS_TOKEN 환경변수 추가
- 전체 워크플로 통합 테스트 통과 (태스크 생성 → 완료 흐름 확인)

## [2026-04-11] infra | Quartz 웹 퍼블리싱 파이프라인 구축
- 모든 vault 페이지에 `publish` frontmatter 필드 추가 (기본값: false)
- CLAUDE.md frontmatter 표준에 `publish` 필드 설명 추가
- Quartz v4.5.2 설치 및 설정 (`~/quartz`)
- GitHub 레포 생성: https://github.com/luneneuf/knowledge-hub
- Vercel 프로젝트 연결: knowledge-hub (GitHub 자동 배포)
- `~/quartz/deploy.sh` 생성 — vault 동기화 + push 원스텝 스크립트
- 배포 후 배포 URL: https://knowledge-hub-tau-one.vercel.app

## [2026-04-10] migration | 스키마 교체 및 3축 구조 이관
- 기존 CLAUDE.md → CLAUDE.md.bak 보존
- 62개 페이지 3축 구조로 이관 (history/work/industry)
  - history/uwo/ : 16페이지 (people 6, events 5, themes 3, moc/publish_log 2)
  - work/labor/ : 1페이지
  - industry/LAKA/ : 45페이지 (entities 14, analysis 12, sources 9, career 5, concepts 4, overview 1)
- frontmatter: title/type/axis 필드 62개 파일 전체 추가
- 태그 체계 교체 (history/work/industry 3축)
- 위키링크: 케이스 A (`[[파일명]]`) — 경로 수정 불필요
- index.md 3축 테이블 구조로 전면 재작성

## 2026-04-05
- **init** — 위키 초기화. CLAUDE.md, index.md, log.md 생성.
- **ingest** `raw/research/라플라타강-은의강.md` — wiki 페이지 3건 생성: 라플라타강, 포토시 은광, 부에노스아이레스. index.md 갱신.

## 2026-04-08
- wiki/uwo/ 폴더 구조 생성 (people, events, themes)
- moc.md, publish_log.md 초기 파일 생성
- 라플라타강.md, 포토시_은광.md, 부에노스아이레스.md → wiki/uwo/events/ 이관
- 파일명 컨벤션 적용 (포토시-은광 → 포토시_은광)

## 2026-04-08 (2)
- LAKA wiki 페이지 frontmatter 일괄 점검
- 대상: overview.md + analysis/ career/ concepts/ entities/ sources/ (총 37개)
- 수정: 30개 / 정상: 7개
- 주요 작업: tags에 cosmetics + 폴더 태그 prepend, updated 2026-04-08 갱신
- 파일명 변경: src_리서치_결과_보고서_RQ-2026-04-01.md → src_리서치_결과_보고서_RQ_2026_04_01.md (하이픈 제거)
- 링크 업데이트: index.md, analysis/경쟁사_비교.md, analysis/글로벌_채널_전략.md, concepts/K뷰티_일본시장.md, concepts/젠더뉴트럴_뷰티.md
- 미승인 태그(LAKA, 일본시장, 성과관리 등)는 제거하지 않고 보존

## 2026-04-08 (3)
- LAKA 태그 정리: 미승인 ~70종 → 승인 태그로 재매핑 또는 제거
- 재매핑: 43건 (예: 일본시장→market/japan, 성과관리→hr 등)
- 단순 제거: 78건 (브랜드/회사명/인물명 태그)
- 모호 태그 1건 처리 완료: entities/세포라.md `유럽` → `market/eu` (CLAUDE.md에 market/eu 신규 승인)

## 2026-04-08 (4)
- index.md 전면 갱신: vault 실제 구조 기준 재작성
- UWO 5페이지 + LAKA 37페이지 + 노무 1페이지 + 미분류 1페이지 = 총 44개 등록
- category 비표준 필드 31개 파일에서 일괄 제거
- CLAUDE.md LAKA 태그 목록 갱신 (신규 12개 추가)
- 대상: wiki/ 하위 LAKA 페이지 37개 전체

## 2026-04-08 (5)
- 중복 wiki/index.md, wiki/log.md 제거
- 빈 legacy 폴더 6개 제거 (content, history, navigators, ports, production, trade-goods)
- 다마스쿠스_강철.md → wiki/uwo/themes/ 이관 + 파일명·frontmatter 정비 (하이픈 제거, tags=[uwo, theme])
- 노무wiki_파이프라인_셋업.md 날짜 접두사 제거 + frontmatter 정비
- index.md 재생성 (LAKA 31개 페이지에 한 줄 설명 머지)

## 2026-04-08 (6)
- **ingest** `raw/cosmetics/한국콜마_vs_코스맥스_ODM_심층분석.md`
- analysis/ 1개 생성: [[한국콜마_vs_코스맥스_ODM_비교]] — ODM 양대산맥 재무·기술·전략·고객사·지역확장 비교
- entities/ 1개 생성: [[코스맥스]] — 글로벌 화장품 ODM 1위 기업 프로필
- entities/ 1개 업데이트: [[한국콜마]] — 설립 역사, 2025 실적, 선케어 강점, 북미 전략, 연우 리스크 보강
- index.md 갱신 (analysis 1건, entities 1건 추가)

### 머지된 이력 (구 wiki/wiki/log.md에서 흡수)

**[2026-04-05] LAKA 초기 ingest** (raw/cosmetics/ 12개 파일 처리)
- 처리 소스 (MD 8개): 리서치 결과 보고서 RQ-2026-04-01.md, LAKA_성과관리_케이스별_제도설계_20260405.md, 달바글로벌 전략 리스크 분석 — LAKA 관점.md, 중소기업 성과관리·인사평가 시스템 변화 리서치 의뢰서.md, LAKA 성과관리·인사평가 제도 설계 리서치 의뢰서.md, 성과관리 리서치 결과 보고서 20260405-1.md, 에이피알_COO_보고서_최종본_20260407.md, 달바글로벌_COO_보고서_최종본_20260407.md
- 참조 PDF 3개: [에이피알]사업보고서_2025년.pdf, [달바글로벌]사업보고서(2025.03.18).pdf, 달바 (유진증권).pdf
- 결과: sources 8개 + entities 11개 (LAKA, 에이피알, 달바글로벌, 이지철, 이민미, 롬앤, 구다이글로벌, 한국콜마, 세포라, 부츠, Qoo10_일본) + concepts 3개 (성과관리_시스템, K뷰티_일본시장, 젠더뉴트럴_뷰티) + analysis 5개 (글로벌_채널_전략, 경쟁사_비교, 에이피알_벤치마크, 달바글로벌_벤치마크, LAKA_성과관리_제도설계) + career 4개 (역량_매핑, 면접_예상질문, 지원_전략, 리스크_요인) = **총 31개 페이지 생성**

**[2026-04-08] LAKA 종합 리서치 리포트 ingest**
- 처리 소스: compass_artifact_wf-091c61f3-...md (현재 LAKA_코스메틱스_종합_리서치_리포트로 rename됨)
- sources/ 1개 생성: src_LAKA_종합_리서치_리포트
- entities/ 1개 업데이트: LAKA (경영진 상세, 제품 라인 확장, 채널 현황 보강)

## 2026-04-08 (6)
- [LAKA] raw 추가: 한국콜마 vs 코스맥스 ODM 심층분석 (`raw/cosmetics/한국콜마_vs_코스맥스_ODM_심층분석.md`)
- [LAKA] wiki 신규: `concepts/ODM.md`, `analysis/K-뷰티_ODM_비교.md`, `entities/코스맥스.md`
- [LAKA] wiki 업데이트: `entities/한국콜마.md` — 연혁·사업구조·글로벌 거점·고객사 보강
- index.md 갱신: Analysis에 K-뷰티_ODM_비교, Concepts에 ODM 등록

## 2026-04-08 (8)
- [UWO] 프로젝트 범위 확장: 트위터 전용 → 역사 콘텐츠 허브로 재정의 (CLAUDE.md 갱신)
- [UWO] 승인 태그 추가: `topic/renaissance`, `topic/art`
- [UWO] raw 추가: `raw/uwo/research/미켈란젤로_vs_다빈치_르네상스_디스전.md` (변경 이력 블록 포함, 본문 원본 보존)
- [UWO] wiki 신규 4건: `people/미켈란젤로.md`, `people/레오나르도_다빈치.md`, `themes/미켈란젤로_vs_다빈치.md`, `themes/파라고네.md`
- [UWO] 자동 ingest 잔여물 제거: `themes/르네상스_파라고네_논쟁.md` (themes/미켈란젤로_vs_다빈치 + themes/파라고네로 분리·재작성됨)
- [UWO] `wiki/uwo/people/레오나르도_다빈치.md` 자동 ingest 본 → 수동 지시서 기준 재작성 (잘못된 `period/dutch-golden-age` 태그 제거, 1999 그란 카발로 복원 fact는 머지)
- moc.md, index.md 갱신

## 2026-04-09
- [UWO] raw 추가: `raw/uwo/research/솔리스_탐험과_죽음.md` — 후안 디아스 데 솔리스 인물 리서치, 1-트윗 단일 포스트 컨셉 포함
- [UWO] wiki 신규: `wiki/uwo/people/솔리스.md` (3-1~3-7 구조, draft) — 라플라타강 발견자, 1516년 사망
- index.md 갱신: People에 솔리스 등록

## 2026-04-09 (3)
- [UWO] raw 보강: `raw/uwo/research/시티_완_켐방_리서치.md` — 3-1~3-10 리서치 섹션 추가 (즉위 배경, 푸트리 사둥 후일담, 키장 금화, 연대 논쟁, UWO 게임 데이터 등)
- [UWO] wiki 재작성: `wiki/uwo/people/시티_완_켐방.md` — raw 기반 전면 재작성. 기본 정보·역사 요약·핵심 포인트·푸트리 사둥 후일담·역사적 맥락·게임 연계·콘텐츠 현황 구성

## 2026-04-09 (2)
- [UWO] raw 추가: `raw/uwo/research/시티_완_켐방_리서치.md` — 인수인계서 원문 보존, 변경 이력 블록 포함
- [UWO] wiki 신규: `wiki/uwo/people/시티_완_켐방.md` (3-1~3-7 구조, published) — 켈란탄 전설적 여왕, 말레이시아 중앙은행 키장 금화 기원, 실존 불확실
- index.md 갱신: People에 시티_완_켐방 등록 (44→45개)

## 2026-04-10
- [공통] CLAUDE.md `## 환경 / 팁` 섹션 신규 생성 — symlink 팁 추가 (`ln -s ~/obsidian-vaults/wiki/CLAUDE.md ~/.claude/CLAUDE.md`)

## 2026-04-08 (7)
- [LAKA] raw 추가: K-뷰티 브랜드 IPO 동향 2024-2026 (`raw/cosmetics/K-뷰티_브랜드_IPO_동향_2024_2026.md`)
- [LAKA] wiki 신규: `analysis/K-뷰티_IPO_동향.md`
- [LAKA] wiki 신규 (자동 ingest 생성 → 크로스링크만 수동 보정): `entities/비나우.md`, `entities/아로마티카.md`
- [LAKA] wiki 업데이트 (IPO 섹션 보강): `entities/에이피알.md`(창업자·미국 얼타·B2B 피부과), `entities/달바글로벌.md`(2E 전략·FI 오버행·코스트코·얼타), `entities/구다이글로벌.md`(브랜드 포트폴리오·2026 IPO 주관사·한성USA)
- [LAKA] `entities/한국콜마.md`: 구다이글로벌·달바글로벌 크로스링크 추가
- index.md 갱신: Analysis에 K-뷰티_IPO_동향, Entities에 비나우·아로마티카 추가

## [2026-04-10] ingest | 이사벨라 데스테 (UWO A급 항해사)

- raw 등록: raw/uwo/research/ 3개 파일 (기본 노트, 5개 축 심층 패키지, Q&A 추가 리서치)
- wiki 생성: wiki/uwo/people/이사벨라_데스테.md (draft)
- index.md: uwo 섹션 1개 항목 추가 (48→49개)

## [2026-04-10] ingest | VOC의 마카오 두 번의 패전 (1601, 1622)

- raw 저장: raw/uwo/research/VOC의_마카오_두_번의_패전__1601년과_1622년.md
- wiki 신규: events/마카오_전투.md, people/빌럼_본테쿠.md
- wiki 갱신: moc.md (Events·People 추가, 미완료 섹션 신설), index.md (51개)
- 비고: 빌럼 본테쿠-박연 크로스링크 후속 필요
## [2026-04-11 08:57] auto-ingest | fswatch_test.md
- 파일: /Users/al02471021/obsidian-vaults/wiki/raw/uwo/fswatch_test.md
- Notion 카드 자동 생성 완료

## [2026-04-11 08:58] auto-ingest | fswatch_test.md
- 파일: /Users/al02471021/obsidian-vaults/wiki/raw/uwo/fswatch_test.md
- Notion 카드 자동 생성 완료

## [2026-04-11 08:58] auto-ingest | fswatch_test2.md
- 파일: /Users/al02471021/obsidian-vaults/wiki/raw/uwo/fswatch_test2.md
- Notion 카드 자동 생성 완료

## [2026-04-11 08:58] auto-ingest | fswatch_test2.md
- 파일: /Users/al02471021/obsidian-vaults/wiki/raw/uwo/fswatch_test2.md
- Notion 카드 자동 생성 완료

## [2026-04-11 08:58] auto-ingest | fswatch_test2.md
- 파일: /Users/al02471021/obsidian-vaults/wiki/raw/uwo/fswatch_test2.md
- Notion 카드 자동 생성 완료


## [2026-04-11] setup | Notion 칸반 자동화 연동 완료
- notion_card.py 스크립트 작성 (scripts/)
- watch_raw.sh 업데이트 — fswatch → Notion 카드 자동 생성
- launchd 등록 (com.vault.watchraw) — 부팅 시 자동 실행
- CLAUDE.md Notion 연동 규칙으로 교체
- 테스트 완료: raw/uwo/ 파일 저장 시 Notion "시작 안 함" 컬럼에 자동 카드 생성 확인
## [2026-04-11 09:28] auto-ingest | 대항해시대_오리진_통합참고자료.md
- 파일: /Users/al02471021/obsidian-vaults/wiki/raw/uwo/대항해시대_오리진_통합참고자료.md
- Notion 카드 자동 생성 완료

## [2026-04-11 09:28] auto-ingest | 대항해시대_오리진_통합참고자료.md
- 파일: /Users/al02471021/obsidian-vaults/wiki/raw/uwo/대항해시대_오리진_통합참고자료.md
- Notion 카드 자동 생성 완료


## [2026-04-11] maintenance | CLAUDE.md 개편 — Notion→Linear, 인제스트 워크플로 재설계
- Notion 칸반 연동 규칙 섹션 삭제 → Linear 이슈 관리 섹션으로 교체
- scripts/notion_card.py, scripts/watch_raw.sh 삭제
- 인제스트 워크플로: 1:1 요약 생성 → 기존 페이지 업데이트 우선 방식으로 재설계

## [2026-04-11] ingest | UWO 참고 데이터 파일 이관
- 대항해시대_오리진_통합참고자료.md (Downloads → raw/uwo/)
- frontmatter 추가 완료
- index.md sources 섹션 업데이트
- 비고: 원본 지시서의 CSV 파일 2종(항해사_통합_데이터.csv, UWO_항해사_관련_최우선_참고자료.csv)은 미발견 → 별도 이관 대기

## [2026-04-11] maintenance | CLAUDE.md 개편 — Notion→Linear, 인제스트 워크플로 재설계
- Notion 칸반 연동 섹션 삭제 → Linear 이슈 관리 섹션으로 교체
- 인제스트 워크플로: 소스 1:1 요약 방식 → 기존 페이지 통합 우선 방식으로 재설계
- scripts/notion_card.py 삭제
- scripts/watch_raw.sh 삭제 (fswatch 연동 불필요)

## [2026-04-16] ingest | 하마다 야효에 / 타이오완 사건 (UWO-15)
- raw 등록: `raw/uwo/hamada-yahyoe-taiowan-incident.md` (전문 수록)
- wiki 신규 3건:
  - `people/pieter-nuyts.md` — VOC 대만 총독·일본 대사, 납치 피해자, 1655년 사망
  - `people/francois-caron.md` — 위그노 출신 VOC 총지배인, 1636년 닛코 등롱 외교
  - `concepts/shuinsen.md` — 주인선 제도 개요, 1634년 종언, 쇄국 연결
- wiki 기존 업데이트 2건 (크로스링크 보강):
  - `people/하마다_야효에.md` — pieter-nuyts, francois-caron, shuinsen 링크 추가
  - `events/타이오완_사건.md` — pieter-nuyts, francois-caron, shuinsen 링크 추가
- 비고: `하마다_야효에.md`, `타이오완_사건.md`는 2026-04-15 기존 생성본 유지 (중복 영문 파일 제거)
- index.md 갱신 (67→70페이지)

## [2026-04-25] ingest | LAKA 입사 전 학습 자료 1주차 — 규제 (14개 파일)
- raw 등록: `raw/study/week1/` (day1~day6, 14개 md)
  - 한국 화장품법(법률 제20901호), 미국 MoCRA, ODM 납품 서류, 세포라·부츠 공급자 요건, 제품 리뷰, 일본 PMD법
- `day1_화장품법_조문.md` PDF 원문(법률 제20901호, 2026.4.2 시행) 기준으로 전면 교정
  - 법률 번호 수정, 삭제조항(14조의2~5) 반영, 과태료 정정(1천만→100만원)
- wiki 신규 5건 (`wiki/industry/LAKA/regulations/`):
  - `한국_화장품법.md`, `미국_MoCRA.md`, `영국_화장품규제.md`, `일본_화장품규제.md`, `이상사례_보고_비교.md`

## [2026-04-25] ingest | LAKA 입사 전 학습 자료 2주차 — SCM·CS (21개 파일)
- raw 등록: `raw/study/week2/` (day8~day13, 21개 md + index)
  - 화장품 SCM(ODM발주·수출통관), 세포라·Boots·일본 운영구조, CS 유입경로, 경쟁사 리뷰 벤치마크
- wiki 신규 9건:
  - SCM (`wiki/industry/LAKA/scm/`): `ODM_발주_프로세스.md`, `수출_채널별_라벨링_SKU.md`, `수출_통관_절차.md`, `일본_유통_구조.md`
  - 채널 (`channels/`): `세포라_운영구조.md`, `Boots_UK_운영구조.md`
  - 비교 (`comparisons/`): `K뷰티_립_CS_벤치마크.md`, `K뷰티_일본_리뷰_트렌드.md`
  - 리서치 (`research/`): `LAKA_글로벌_채널_리뷰.md`
- index.md 갱신 (110페이지)

## [2026-05-10] ingest | LAKA 글로벌 전용 스킨케어 3종 신규 생성

**소스**: `raw/scrape/laka_products_global_20260501.json`

- **신규 생성** `products/skin-active-serum.md` — Glutathione·PDRN 세럼, Amazon US 단독 (\$18.40, ASIN: B0G1M6NR83)
- **신규 생성** `products/active-booster.md` — Peptides·Hyaluronic Acid 부스터, Amazon US 단독 (\$20.00, ASIN: B0G1LRY8DJ)
- **신규 생성** `products/scaling-toner.md` — AHA·PHA 스케일링 토너, Amazon US 단독 (\$16.00, ASIN: B0G1LYY37P)
- 3종 모두 laka.co.kr 미출시, the-laka.com은 WordPress 어필리에이트(Amazon 연동)

## [2026-05-10] update | LAKA 프루티 글램 틴트 — 컬러 데이터 완성 (COM-19)

**작업**: 프루티 글램 틴트 + 관련 제품 위키 데이터 보강 (COM-19 완결)

- **업데이트** `products/프루티-글램-틴트.md`
  - 컬러 라인업 60종 헥스코드 전체 추가 (`aOptionColorchip` JS 추출, swatch_mapping_180.json)
  - 영문 컬러명 60종 전체 기입 (Sephora 확인 10종 + KR 음역 기반 50종)
  - Sephora US 취급 10색 구체 목록 확인 및 별도 섹션 추가 (#101/#102/#103/#104/#108/#120/#121/#122/#123/#124)
  - 단종 추정 주석 추가 (laka.co.kr 2026-05 기준 삭제 확인)
- **업데이트** `products/프루티-립-글로셔너.md` — Sephora 5색 섹션 추가 (#701/#705/#706/#707/#709), 영문명 10종 기입
- **업데이트** `products/본딩-글로우-립스틱.md` — Sephora 5색 섹션 추가 (#213/#216/#217/#218/#220), 영문명 24종 기입
- **USD 가격 추가** (Amazon 실시간 조회): 드림빔-하이라이터 \$17, 러브-실크-블러쉬 \$12, 모노-아이섀도우 \$8, 멜티-딥-클렌징-팩투폼 \$12.75, 프루티-글램-틴트-미니 \$10
- **미수집 항목** (후속 과제): 글로벌 단독 스킨케어 3종 (Skin Active Serum/\$18.40, Active Booster/\$20, Scaling Toner/\$16) wiki 페이지 미생성

## [2026-04-25] maintenance | Vercel 배포 — 사이드바 정리 완료
- ignorePatterns 최종 정리: 게임정책·로블록스 glob 수정(괄호→와일드카드), wiki/ 구버전 파일 전체 제외
- 옵시디언 vault 정리 반영: business/·uwo/ 삭제, old/ 아카이브 폴더로 이전
- ignorePatterns에 `"old"`, `".claude"` 추가
- 공개 사이드바: Stanford CS146S, Wiki Index, Claude Skill 가이드만 노출
