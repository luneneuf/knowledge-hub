---
title: "Log"
updated: 2026-05-18
---

## [2026-05-18] 보완 | 날짜 필터 추가 (>= 2026-04-01)

**작업**: 사용자 결정 — 4-5월 항목만 보기로 함. 수집 후·저장 전 단계에서 날짜 필터 적용.

- **`collect-inline.ps1` 보완**
  - `$StartDate = [datetime]'2026-04-01'` 변수 추가 (필터 컷오프)
  - `Try-ParseDate` 함수 추가 — RFC822 (Google News), ISO 8601 (Atom·JSON), `YYYY-MM-DD` (KCIA), `YYYY MMM [DD]` (PubMed) 등 다양한 형식 처리
  - 컷오프 미만 또는 날짜 불명 항목은 `excluded.json`에 별도 보관 (디버깅·재검토용)
  - 다이제스트 헤더에 필터 정보 명시 ("필터: 게시일 >= 2026-04-01")
- **3차 실행 결과**: 514건 수집 → **77건 유지** / 제외 437건 (기간 외 434 + 날짜 불명 3)
- **핵심 시그널 (4-5월 한정)**:
  - FDA 네일 폴리시 리무버 메틸렌 클로라이드 회수 4건 연속 (4/14·16·22·24)
  - 2026-05-08 FDA Warning Letter to IBeautyStore (K-뷰티 미국)
  - 2026-04-30 EU Safety Gate 등록 화장품 회수 분석
  - 2026-04-03 Skincare 브랜드 선스크린 회수 (Allure)
  - K-뷰티 1분기 수출 사상 최고 + 중동 충격 대응
- **업데이트** `wiki/industry/LAKA/analysis/안전관리정보_자동수집_기술검증.md` — 필터 적용 결과 분포 추가

## [2026-05-18] 보완 | KCIA 스크래퍼 추가 + 운영 주기 확정 (월 1회)

**작업**: KCIA 게시판 HTML 구조 재확인 후 정규식 보완, 본부장 결정 사항 반영

- **KCIA 스크래퍼 보완** (`collect-inline.ps1`)
  - 행 단위(`<tr>`) split → 각 행에서 카테고리·제목·날짜·공지여부·번호 추출
  - 2차 실행 결과: **10건/회 안정 수집** (notice.php 첫 페이지 전체)
  - 잡힌 LAKA 직접 관련 시그널: 식약처 자외선차단지수 협조 요청, 화장품 안전기준 일부개정고시, 책판 법정교육 일정 등
- **정기 실행 주기 확정**: **월 1회** (R&R 15번과 정합). 현재는 1주 수동 운영(테스트) 중
- **2차 실행 누적**: 총 513건 수집 (1차 503 + KCIA 10)
- **업데이트** `content/tools/safety_signals/README.md` — 운영 계획 섹션 추가 (월 1회, 테스트 모드)
- **업데이트** `wiki/industry/LAKA/analysis/안전관리정보_자동수집_기술검증.md` — KCIA 보완 결과, 본부장 결정 반영, KCIA 내 LAKA 직접 관련 항목 6개 발췌

## [2026-05-18] 구현·검증 | 안전관리 정보 자동수집 1단계 기술 PoC

**작업**: 본부장 방향 전환 — Slack/인력 운영 통합 보류, 기술적 수집 기능 개발·검증 우선

- **신규 코드 폴더** `content/tools/safety_signals/`
  - `sources.json` — 수집 후보 출처 정의
  - `verify-sources.ps1` — 출처 동작 검증 스크립트
  - `collect-inline.ps1` — 수집 본체 (PowerShell + .NET XML, Invoke-Expression 패턴으로 실행 정책 우회)
  - `output/verify_results_latest.md` — 검증 보고서
  - `output/daily/20260518/items.json` + `digest.md` — **503건 자동 수집 성공**
  - `README.md` — 도구 안내
- **검증 결과**: 9개 RSS·JSON 출처 작동 + 1개 HTML 스크래퍼 보완 필요. 추가 비용·설치 없이 PowerShell만으로 동작
  - 작동: Google News RSS 6개 (KR·EN·UK 키워드별), GOV.UK OPSS Atom, GOV.UK Search JSON, PubMed eutils 2-step
  - 우회: FDA·EU Safety Gate·MFDS 회수 페이지 → Google News로 우회 (직접 RSS 미제공 또는 동적 렌더링)
  - 미완: KCIA `notice.php` 스크래퍼 (정규식 보완 필요)
- **콘텐츠 품질 확인**: 첫 실행에서 LAKA Tier A 시그널 다수 — 스칼렛레드 색소 회수, K-뷰티 회수 3.2배 급증, 에이피알 메디큐브 FDA 부작용 접수, MoCRA 강제 회수 가이드라인, Neutrogena 회수 등
- **신규 위키** `wiki/industry/LAKA/analysis/안전관리정보_자동수집_기술검증.md` — 기술 PoC 결과 보고서
- **기존 페이지 보류 표시** `안전관리정보_자동수집_1단계_스펙.md` status: draft → on-hold, 상단에 보류 사유 명시
- **업데이트** `wiki/index.md` — 189페이지

## [2026-05-18] 작성 | 안전관리 정보 자동수집 1단계 구현 스펙

**작업**: 본부장(사용자) 승인으로 1단계 진행 결정. 실행 가능 수준 스펙 작성.

- **신규 위키** `wiki/industry/LAKA/analysis/안전관리정보_자동수집_1단계_스펙.md`
  - 채널 명세 (`#qa-시그널-피드` Public, 핀고정 메시지 포함)
  - 8개 RSS 소스 — 4개 RSS 직접 제공 (FDA·EU Safety Gate·PubMed·식약처 보도자료) + 4개 IFTTT/수동 (식약처 회수공고·KCIA·UK OPSS·일본 PMDA)
  - Slack RSS 앱 `/feed subscribe` 셋업 단계
  - 메시지 포맷 표준 — 🔴/🟡/🟢/✅ 이모지 라벨링, Tier A 이관 템플릿
  - 운영 룰 — 일일 검수 10분(김건), 주간 회고 15분(금), Tier A 에스컬레이션 5개 조건
  - 4주 일정 — Week 1 셋업, Week 2 IFTTT 보강, Week 3 조정, Week 4 종합 회고·2단계 결정
  - 검수 기준 5개, 리스크 5개·완화책
  - 부록: URL 검증 체크리스트, IFTTT 셋업 가이드, 실행 명령 참조
- **업데이트** `wiki/index.md` — 188페이지

## [2026-05-18] 작성 | 안전관리 정보 수집 자동화 제안 보고서

**작업**: [[품질관리_RR_2026-05]] 15번 안전관리 정보 수집(월 1회) 자동화 보고 초안 작성

- **신규 위키** `wiki/industry/LAKA/analysis/안전관리정보_자동수집_제안.md`
  - 수집 대상 5개 카테고리 정리 (국내·해외 관 공식 / 미디어 / SNS / 학술)
  - 키워드 매트릭스 Tier A/B/C 분류
  - 3계층 아키텍처 (수집-필터-배포) + 도구 스택 권장
  - 단계별 실행 계획 — 1단계 Slack RSS (2주, 비용 0원) → 2단계 GitHub Actions + Claude API (3개월, 월 5만원) → 3단계 SNS·서식 자동화 (6개월)
  - Slack 채널 별도 신설 `#qa-시그널-피드` 권고
  - Tier A 즉시 알림 트리거 5개 조건
  - 리스크 5개 (정보 누락·AI 분류 오류·알림 피로·식약처 보고 자동화 한계·보안)
  - 의사결정 5건 + 권고안
  - 4주 실행 일정
- **업데이트** `wiki/index.md` — 187페이지

## [2026-05-18] ingest | 화장품 향료 중 알레르기 유발성분 표시 지침 (식약처, 2020.1.1 시행)

**작업**: HWP 파일 (HWP 자동 추출 불가 → 사용자 본문 직접 붙여넣기) 인제스트. LAKA 립 카테고리(95%+ leave-on)에 직접 영향.

- **소스**: `C:\Users\laka\Downloads\붙임_화장품 착향제 중 알레르기 유발물질 표시 지침.hwp`
- **raw 보존**: `wiki/raw/cosmetics/착향제_알레르기유발물질_표시지침_식약처.hwp` (원본)
- **텍스트 보존**: `wiki/raw/cosmetics/착향제_알레르기유발물질_표시지침_식약처_텍스트.md` (사용자 붙여넣기 + 표 정리)
- **신규 위키** `wiki/industry/LAKA/regulations/향료_알레르기유발성분_표시.md`
  - 25종 성분표 + CAS 번호 + LAKA 노출 가능성 점수 (리모넨·리날룰·시트로넬올·제라니올·쿠마린·시트랄·벤질알코올·시트랄 8종 "상")
  - 표시 방법 5안 중 1·2·3안 가능, 4·5안 불가 ([[품질관리_RR_2026-05]] #4 표시문안 검토 운영 룰)
  - LAKA 영향 매핑: 사6 립스틱·립라이너, 사7 립글로스·립밤, 라3 아이섀도 등 leave-on 0.001% 엄격 적용
  - 비건/식물 추출 라인 (수딩비건립오일·소울비건립밤·헬시세럼밤) — 지침 ⑥ 직접 적용
  - UK SI 2024/1334 80종과의 관계 (25종은 80종의 부분집합)
  - 원료목록보고와의 연결 (변경보고 트리거)
  - 실행 체크리스트(즉시·중기·장기)
- **업데이트** `wiki/index.md` — 186페이지

## [2026-05-18] ingest | 원료목록 사전보고 FAQ (KCA 2019.11.26)

**작업**: 본 매뉴얼과 같은 사이트 게시 FAQ PDF 인제스트. 30개 Q&A 중 LAKA 적용 시그널 7개 추출.

- **소스**: `C:\Users\laka\Downloads\[붙임] 원료목록 사전보고 관련 FAQ_191126.pdf` (560KB)
- **raw 보존**: `wiki/raw/cosmetics/원료목록_사전보고_FAQ_KCA_20191126.pdf`
- **텍스트 추출**: `wiki/raw/cosmetics/원료목록_사전보고_FAQ_KCA_20191126_텍스트추출.md` — pdftotext
- **신규 위키** `wiki/industry/LAKA/regulations/원료목록_사전보고_FAQ_책임판매업자.md`
  - LAKA 핵심 FAQ 7개 분석: Q9(사전보고 = 최초 1회+변경), Q12(샘플도 보고 필수), Q16(**다중 ODM = ODM별 각각 보고** — 프루티글램틴트 콜마/코스맥스 이원화 직접 적용), Q22 vs Q23(단서조항 vs 순수 배합금지), Q23(행정처분 단계: 3개월→6개월→12개월→등록취소), Q26(변경보고 트리거), Q27(함량 변경은 보고 불요)
  - SCM 1~5월 보고서의 변경보고 트리거 매핑(콜마/코스맥스 이원화·수딩프렙립마스크 토출구·세포라용 신제품 등)
  - LAKA 운영 체크리스트(월정기·신제품 사이클 게이트·변경보고 흐름)
- **본 매뉴얼 페이지에 FAQ 양방향 링크 추가**
- **업데이트** `wiki/index.md` — 185페이지

## [2026-05-18] ingest | 화장품 원료목록 사전보고 시스템 안내 (KCA 2019.11.26, 책임판매업자용)

**작업**: 대한화장품협회 발행 책임판매업자 원료목록보고 매뉴얼 PDF 인제스트. (사용자가 맞춤형판매업자 버전을 잘못 받았다가 책임판매업자용으로 정정 요청)

- **소스**: `C:\Users\laka\Downloads\화장품 원료목록 사전보고 시스템 안내_20191126.pdf` (3.8MB, PDF 1.5)
- **raw 보존**: `wiki/raw/cosmetics/원료목록_사전보고_시스템안내_KCA_20191126.pdf`
- **텍스트 추출**: `wiki/raw/cosmetics/원료목록_사전보고_시스템안내_KCA_20191126_텍스트추출.md` — pdftotext (Git for Windows 동봉판) `-layout -enc UTF-8`. 일부 표 레이아웃 깨짐, 핵심 내용 보존
- **신규 위키** `wiki/industry/LAKA/regulations/원료목록_사전보고_책임판매업자.md`
  - 책임판매업자 vs 맞춤형 차이 명시(유통·판매 전 보고 / 별지 제6호 / 변경·단종보고 체계)
  - 보고 양식 8 컬럼 + 기능성 F1~F14 + 품목기준코드
  - 혼합물 작성 규칙(`/` 사용 예외: 단일성분 간주 복수원료)
  - **LAKA 제품 카테고리 유형 코드 매핑**: 프루티글램틴트·맥시글레이어틴트·립스틱·립틴트 → 사6, 립글로스·립밤 → 사7, 본딩커버쿠션 → 사3, 선실드글로이치크 → 사1+F3 등
  - 실제 보고 트리거 사례 SCM 1~5월 보고서와 크로스링크 (변경보고: [[2026-01-W4]] 콜마→코스맥스 이원화 / 단종보고: [[2026-03-W1]] C등급 4종 / 최초보고: [[2026-04-W5]] 세포라용 립라이너 4종 등)
- **업데이트** `wiki/index.md` — 184페이지

## [2026-05-18] 작성 | 품질팀 Slack 운영 초안 보고서

**작업**: 5/17 라카 Slack 임시 운영기준 공지에 맞춰 품질팀 채널 개설 + 운영 규칙 + 에스컬레이션 룰 보고 초안 작성

- **신규 생성** `wiki/industry/LAKA/analysis/품질팀_슬랙운영_초안_2026-05.md`
  - 채널 5개 (`#qa-팀내`·`#qa-신제품-출시검증`·`#qa-클레임-품질이슈`·`#qa-제조업체-audit`·`#qa-인허가-법규`)
  - 정형 보고 템플릿 3종 (QC 결과 / 클레임 접수 / 위해정보 시그널)
  - 에스컬레이션 룰 7개 사안 × 게시 채널 × @멘션 대상
  - 채널 Owner 지정([[품질관리_RR_2026-05]] R&R 매핑)
  - 5/19~22 실행 일정 + 6월 첫 주 운영 회고
  - 향후 확장: 글로벌 컴플라이언스 채널 6월 내 신설 권장, 식약처/KCA 자동 알림 연동, SCM 채널 구조와의 정렬
- **업데이트** `wiki/index.md` — 183페이지

## [2026-05-18] ingest | SCM 주간업무보고 시리즈 완료 — 2월 2주차 ~ 5월 3주차 (6건)

**작업**: 남은 6개 PPTX 일괄 처리 → raw 텍스트 추출 + MD 정리

- **인제스트 완료**:
  - `2026-02-W2_SCM주간업무보고.md` (8슬라이드)
  - `2026-03-W1_SCM주간업무보고.md` (10슬라이드) — 부진재고 운영방안 대표 승인, 대만 회수 비용
  - `2026-03-W4_SCM주간업무보고.md` (8슬라이드) — 화성코스메틱 A등급 Audit, 김포물류센터 수입검사
  - `2026-04-W3_SCM주간업무보고.md` (11슬라이드) — 퍼펙트트윈립 단상자 혼입 클레임 발생
  - `2026-04-W5_SCM주간업무보고.md` (6슬라이드) — 트윈립 클레임 무상 보상, 립라이너 세포라/부츠 B2B 발주
  - `2026-05-W3_SCM주간업무보고.md` (6슬라이드) — ⚠️ 텍스트가 4월 5주차와 100% 동일 (재게재 가능성)
- **추적 인덱스 업데이트**: `wiki/raw/cosmetics/scm_weekly/_index.md` — 8건 전부 요약 행 추가
- **다음 단계**: 8건 종합한 SCM 현황 분석 페이지 `wiki/industry/LAKA/analysis/`에 작성 예정

## [2026-05-18] ingest | SCM 주간업무보고 시리즈 시작 — 1월 2주차

**작업**: 2026년 1~5월 SCM 부문 주간업무보고 PPTX 8건 인제스트 시작 (2~3주 간격). 종합 현황 분석은 전체 인제스트 후 별도 작성.

- **소스 경로**: `C:\Users\laka\OneDrive - 라카코스메틱스\문서\품질관리\업무 보고\` (8개 파일 확인됨)
- **raw 폴더 신설**: `wiki/raw/cosmetics/scm_weekly/`
- **추적 인덱스**: `wiki/raw/cosmetics/scm_weekly/_index.md` (8주차 처리 현황표 + 종합 보고서 계획)
- **첫 인제스트**: `2026-01-W2_SCM주간업무보고.pptx` (47MB, 7슬라이드) → text 추출
  - Slide 1 구매팀: 12월 매입 분석 ([[한국콜마]] 26.6억, 화성코스메틱·코스메카·씨앤씨 신제품 등 총 +4.7억 vs 11월)
  - Slide 2 구매팀: 긴급 대응 (수딩프렙립마스크·워시풀틴트리무버)
  - Slide 3 S&OP파트: 1/5 기준 재고 **국문 82억 + 일문 30억 + 영문 4.8억 = 총 118억**
  - Slide 4 물류파트: HDL 김포물류센터 회계실사 완료
  - Slide 5~6 품질팀: 신제품 QC 3건 (모두 적합) — 프루티글램틴트미니듀오 리뉴얼, 프루티글램틴트 컬러추가, 플러쉬 퍼펙트 립프렙 트리오
  - Slide 7 구매팀: 신제품 입고 일정 8건 (1~3월 런칭)
- **개별 위키 페이지 미생성** — 8건 전체 처리 후 [[LAKA_조직도_2026-05]]·[[품질관리_RR_2026-05]]와 묶어 종합 현황 보고서 작성 예정

## [2026-05-18] ingest | LAKA 품질관리팀 R&R PPTX (차승호 팀장 작성)

**작업**: 사내 공유 PPTX(16슬라이드, 차승호 팀장 / 김건 책임)를 raw 보존 + 텍스트 추출 + 위키 정리본 3단 처리

- **소스**: `C:\Users\laka\OneDrive - 라카코스메틱스\문서\품질관리\문서\품질관리 시스템 체계확립_260518(최종).pptx`
- **raw 보존**: `wiki/raw/cosmetics/품질관리_시스템_체계확립_260518.pptx` (원본 복사)
- **텍스트 추출**: `wiki/raw/cosmetics/품질관리_시스템_체계확립_260518_텍스트추출.md` — PowerShell + System.IO.Compression.ZipFile로 16슬라이드 a:t 노드 전부 추출 (다이어그램 손실, 텍스트는 보존)
- **신규 생성** `wiki/industry/LAKA/analysis/품질관리_RR_2026-05.md`
  - R&R 분배표(17개 업무) 정리 — 차승호 단독 5건·김건 단독 7건·공동 5건(차승호 정/김건 부)
  - 22개 별첨 프로세스 그룹 7개로 분류(클레임·QC / 문안검토 / 인허가·보고 / 서류 / 자재·포장 / 업체평가 / 교육)
  - 갭 분석: 한국 책임판매업자 의무 충실 / **글로벌(MoCRA·UKCR·Clean@Sephora·Drug Claim) 명시 없음** — [[가상_QA리드_4주플랜_시뮬레이션]] 진단과 정합
  - [[LAKA_조직도_2026-05]] 부서간 협업 인터페이스 매핑(영업·상품개발·디자인·구매·물류) — "상품개발팀" 명칭이 현 조직도와 불일치 발견
- **업데이트** `wiki/index.md` — LAKA 섹션 추가, 총 182페이지

## [2026-05-18] ingest | 가상 QA 리드 4주 플랜 시뮬레이션 (Claude Web 문답 v2)

**작업**: Claude Web과의 가상 시뮬레이션 문답 결과물(2026-04-26 v2) 인제스트

- **소스 보존**: `wiki/raw/cosmetics/LAKA_QA리드_가상_4주플랜_v2_20260426.md` — 원문 전체
- **신규 생성** `wiki/industry/LAKA/analysis/가상_QA리드_4주플랜_시뮬레이션.md`
  - 시뮬레이션 성격 명시(가상 인물 = 삼성전자 QA 조직장 출신, 가정 직무 = LAKA 품질·운영 시니어 리드)
  - [[K뷰티_ODM_QA_실패_8유형]](같은 날짜 작성)과의 관계 명시 — 진단 프레임 ↔ 실행 시퀀스 페어
  - Week 1~4 핵심 산출물·Quick Win 3건·90일 로드맵 요약
  - 사용자(현 LINE GAMES, LAKA 글로벌/해외사업 + 경영지원 관심) 관점 함의 정리
  - [[LAKA_조직도_2026-05]]의 품질전략 부문(천승범 외 3명) 현 인력과의 갭 명시
- **업데이트** `wiki/index.md` — LAKA 섹션 추가, 총 181페이지

## [2026-05-18] ingest | 라카 사내 조직도 CSV → MD 전환

**작업**: 사내 공유 조직도 CSV(2026-05-18 기준)를 위키 페이지로 변환

- **소스**: `C:\Users\laka\OneDrive - 라카코스메틱스\문서\조직도.csv` (raw/ 외부 — 사내 공유 원본 직접 참조)
- **신규 생성** `wiki/industry/LAKA/analysis/LAKA_조직도_2026-05.md`
  - 8개 부문 × 23개 팀 × 약 93명 전수 정리 (부문/팀/파트/조직장/조직원 표 형식)
  - 부문별 분석 메모: 마케팅 부문 27명(글로벌PR 단일팀 16명) 최대, 부문장 공석 2곳(국내사업·크리에이티브), 인턴 비중 ~10%, SCM 슬림(7명)
  - [[LAKA]], [[이지철]], [[LAKA_채용공고_현황분석]], [[한국콜마]] 등 위키링크 연결
- **업데이트** `wiki/index.md` — LAKA 섹션에 추가, 총 180페이지

## [2026-05-17] ingest | COM-40 립 제품 소셜 트렌드 — Grok X(Twitter)

**작업**: COM-31~39 Perplexity·웹 기반 리서치의 검증·보완 목적으로 Grok에 X(Twitter) 전용 리서치 의뢰. 한·영·일 3개 언어 × 8개 카테고리 = 24세트 raw 데이터 + 비교 분석 인제스트.

- **Linear 이슈**: COM-40
- **의뢰서**: `RESEARCH/lip_social_grok_20260517/BRIEF.md`
- **raw 보존**: `content/raw/grok/lip_products/lip_social_trends_grok_raw_20260515.md` (약 9,800자)
- **신규 위키** `wiki/industry/LAKA/concepts/립_제품_카테고리/립_소셜_트렌드_X.md`
  - 한·영·일 패러독스: 한국=K뷰티 신상·아이돌, 영어=셀럽·2000s nostalgia, 일본=팝업·한정판
  - **🚨 LAKA 퍼펙트 트윈 립 JP/KR 동시 바이럴** (4/24 JP 런칭 → 5월 한국 예약 폭주) — Perplexity는 못 잡은 6~18개월 leading 신호
  - 신조어: "야르함", "3D입술", "맥시샷", "뽀용립", "탕후루립", "粘膜カラー"
  - Perplexity vs Grok 차이 매트릭스 + LAKA 시사점 5건(#LAKAPerfectTwin 미사용·"샤넬 르 루쥬 듀오 듀프" 드립 대응 등)
- **업데이트** `wiki/industry/LAKA/concepts/립_제품_카테고리/index.md` 허브에 COM-40 행 추가

## [2026-05-17] ingest | COM-39 립버터·립마스크·립패치 — LAKA Sephora US 진입 SKU

**작업**: 립 카테고리 8번째 — 케어 세그먼트 중 립버터/슬리핑 마스크/하이드로겔 패치 통합 인제스트. **2026-05-14 LAKA Soothing Prep Lip Mask Sephora US 온라인 런칭** 정보 위키화.

- **Linear 이슈**: COM-39
- **raw 보존**:
  - `RESEARCH/lipmask_20260516/outputs/lip_lipmask_raw_20260515.md`
  - `RESEARCH/lipmask_20260516/artifacts/agent_results/` agentA·agentB 2건
- **신규 위키** `wiki/industry/LAKA/concepts/립_제품_카테고리/립버터_립마스크_카테고리.md`
  - 시장: 립케어 \$4.12B / 립 마스크 세그먼트 CAGR **7.5%** (2026~33)
  - 카테고리 정의자 2축: Laneige Lip Sleeping Mask(2015, 야간) / Summer Fridays Lip Butter Balm(2020, 데이)
  - **2026-05-14 LAKA Soothing Prep Lip Mask Sephora 미국 온라인 런칭** 명시 — 케어 카테고리 첫 글로벌 메이저 진입
  - SKU 화이트스페이스 3건: 야간 슬리핑 마스크 단독·립버터 단독·하이드로겔 듀오 부재 → 권고 명시
  - 2026.7.31 EU 알레르겐 80종 라벨링 영향 분석
- **업데이트** 허브 [[립_제품_카테고리]] index.md — COM-39 카테고리 행 추가

## [2026-05-16] ingest | 립 카테고리 8종 위키화 + COM-36~38 리서치 (립스틱·립틴트·립글로스·립오일·립라이너·립밤·립플럼퍼)

**작업**: COM-30 시리즈(립 제품 8개 카테고리) 딥리서치 결과를 카테고리별 위키 페이지로 일괄 전환. 신규 폴더 `립_제품_카테고리/` 신설.

- **Linear 이슈**: COM-31(립스틱A)·COM-32(립스틱B)·COM-33(립틴트)·COM-34(립글로스)·COM-35(립오일)·COM-36(립라이너)·COM-37(립밤)·COM-38(립플럼퍼)
- **raw 보존**: 각 카테고리 `RESEARCH/<카테고리>_20260516/outputs/lip_<카테고리>_raw_20260515.md` + 일부 agentA/agentB 분리
- **신규 폴더** `wiki/industry/LAKA/concepts/립_제품_카테고리/`
- **신규 위키 9개**:
  - `index.md` — 허브 (시장 규모 비교 차트·공통 규제 캘린더·LAKA 종합 시사점·관련 컨셉)
  - `립스틱_카테고리.md` — \$9.9~18.1B, APAC CAGR 8%, 럭셔리 리필 시스템, LAKA 본딩-글로우·벌키-매트·라카-데빌립
  - `립틴트_카테고리.md` — \$1.6B, K뷰티=립틴트 글로벌 정의, LAKA 맥시-글레이어 LIPS Japan 4.35점 최고
  - `립글로스_카테고리.md` — \$3.77~4.20B, Fenty 10초당 1개, LAKA 젤링-누드 / 프루티-립-글로셔너
  - `립오일_카테고리.md` — \$573M → \$1,141M (2035), Dior 1.9억 뷰, Rhode \$1B 인수
  - `립라이너_카테고리.md` — 미국 +60% (2022→24), Lip combo +97.5% YoY, LAKA Stain Lip Liner 8컬러(K뷰티 첫 젠더뉴트럴 2018)
  - `립밤_립케어_카테고리.md` — \$4.12B, Burt's Bees 글로벌 1위(8.5%), Rhode \$1B (2025.5), DHC 누적 2억 본, 컬러 립밤 +150%
  - `립플럼퍼_카테고리.md` — 세럼 \$4.31B / 디바이스 \$1.2B, 자극파/자연파 양극화, 펩타이드 이동
- **2026-05-16 폴더 구조 리팩토링 커밋**: 기존 6개 페이지를 `립_제품_카테고리/` 하위로 이동 + index.md 메인 링크 경로 수정(uwo/moc·business/overview → wiki/history/moc·wiki/industry/LAKA/overview)
- **공통 트렌드**: TikTok 주도 카테고리 부활 / K뷰티 글로벌 표준화 / 펩타이드 트리트먼트 시대 / 점막 누디 톤 한·일·미 공통
- **공통 규제**: 🚨 **2026.7.31 EU 향료 알레르겐 80종 라벨링 발효** — 전 카테고리 leave-on 0.001% 초과 라벨 의무

## [2026-05-16] ingest | 대항해시대 동남아시아에서 기독교는 왜 실패했는가

**작업**: 딥리서치 결과물을 history/themes/ 위키 페이지로 전환

- **신규 생성** `wiki/history/themes/동남아시아_기독교_실패.md`
  - 왕권 정당성 관점에서 불교·이슬람·기독교의 동남아 확산 성패 분석
  - 핵심 논제: 통치자의 생존 여부가 기독교 성패를 결정했다는 구조적 법칙
  - 불교(데바라자·담마라자), 이슬람("알라의 그림자"), 기독교(교황 권위·식민주의 결합·혼합주의 거부) 3자 비교표 포함
  - [[아체_믈라카_오스만_역사]], [[메카의_베란다_아체]] 위키링크 연결
- **업데이트** `wiki/history/moc.md` — Pure History 섹션에 추가
- **업데이트** `wiki/index.md` — 총 179페이지

# 변경 이력

## [2026-05-15] ingest | 쓰가루 다메노부·히로사키번 — history/쓰가루 신설

**소스**: 리서치 리포트 (챗 인제스트, raw/ 없음). 쓰가루 다메노부(1550–1607)의 생애부터 히로사키번 에도시대 번정사, 보신전쟁, 메이지 화족~현대까지 전범위 커버.

**신규 생성 페이지 (4개)**:

| 페이지 | 타입 | 설명 |
|--------|------|------|
| `history/쓰가루/쓰가루_다메노부.md` | entity | 번조(藩祖) 다메노부 인물지 — 통일 과정·히데요시 관계·후지와라 자칭의 정치학·사망 |
| `history/쓰가루/히로사키번.md` | entity | 히로사키번 에도시대 전체사 — 12대 번주·석고 변천·번정 황금기·기근·소마 대작 사건 |
| `history/쓰가루/보신전쟁_히로사키번.md` | concept | 보신전쟁 당시 이중적 행동 — 동맹 가맹→이탈, 노헤지 전쟁, 賞典禄 1만 석 결과 |
| `history/쓰가루/쓰가루씨_화족.md` | entity | 메이지 화족 3가(백작·자작·남작)~현대 15대 당주·히타치노미야비 하나코 |

## [2026-05-12] ingest | HBR 7편 위키화 — work/management 신설

**소스**: `Downloads/` 7개 docx (KR-EN bilingual). 추출 후 `raw/hbr/`에 보존.

| raw 파일 | 원문 |
|---|---|
| `HBR_2026_05_better_decisions_structured_empowerment.md` | Sandino, *How Fast-Growing Companies Can Make Better Decisions* (HBR 2026-05-08) |
| `HBR_2026_05_AI_legacy_workflows.md` | Kenny & Pogrebna, *3 Ways AI Can Free Organizations from Legacy Workflows* (HBR 2026-05-07) |
| `HBR_2026_0506_superteams.md` | Friedman, *How to Build a Superteam That Keeps Getting Better* (HBR 2026 May-Jun) |
| `HBR_2025_11_AI_5R_framework.md` | Israeli & Ascarza, *Most AI Initiatives Fail. This 5-Part Framework Can Help.* (HBR 2025-11-20) |
| `HBR_2026_04_burnout_by_level.md` | Auger-Domínguez, *Burnout Looks Different Across the Org Chart* (HBR 2026-04-03) |
| `HBR_2025_0910_now_is_time_for_courage.md` | Gulati, *Now Is the Time for Courage* (HBR 2025 Sep-Oct) |
| `HBR_2025_12_management_tips_top10.md` | HBR Editors, *Our Favorite Management Tips of 2025* (HBR 2025-12-31, digest) |

**신규 폴더**: `wiki/work/management/` — work/ 축의 첫 management 클러스터.

**신규 페이지 (14개)**:

- `wiki/work/management/moc.md` — HBR Management 인덱스 (concept 6 + source 7 + 주제별 클러스터)
- `wiki/work/management/concepts/` (6개)
  - 구조화된_권한_위임 — Sandino, OXXO/School of Rock/IKEA, 5년 스트레스 테스트, Argyris 이중 루프
  - 조직적_망각 — Kenny & Pogrebna, 3대 제약(KPI/정체성/고객 신화), AI 우회 효과
  - 슈퍼팀_7실천 — Friedman, OKC Thunder 닻 사례, 7개 리더 행동 정량
  - 5R_프레임워크 — Israeli & Ascarza, AI 운영 OS (Roles·Responsibilities·Rituals·Resources·Results)
  - 직급별_번아웃 — Auger-Domínguez, 4단계 양상 + 시스템/구조 처방 + 5문항 진단
  - 용기_5전략 — Gulati, VUCA·Knight·Weick·Mandela 토대 + 5전략 실행
- `wiki/work/management/sources/` (7개)
  - src_HBR_structured_empowerment_2026
  - src_HBR_AI_legacy_workflows_2026
  - src_HBR_superteams_2026
  - src_HBR_5R_AI_framework_2025
  - src_HBR_burnout_by_level_2026
  - src_HBR_now_is_time_for_courage_2025
  - src_HBR_management_tips_2025

**index.md 업데이트**: 총 페이지 160 → 174. work/ 섹션에 노무·HBR 매니지먼트 2개 서브섹션 신설.

**크로스컷팅 닻**: 심리적 안전(Edmondson), Microsoft Scrum 데일리 3개 질문, Frank Knight risk vs uncertainty, George Miller 7±2, Karl Weick sensemaking — 6개 개념 페이지가 공통 참조.

## [2026-05-12] 6번째 source 페이지 | src_gartner_demand_driven_2018 — Gartner DDM FOUNDATIONAL research

**배경**: 사용자 결정 — *"Simon Eagle 주장을 받아들이지 않고 주류를 따라갈 것"* → Gartner 본인의 가장 권위 있는 demand-driven maturity model (DDM)을 본 wiki 주류로 채택.

**Scribd URL** (https://www.scribd.com/document/808040386/Gartners-Demand-Driven-Model-for-Supply-Chain-Excellence) — Jina Reader 일시 차단 (이전 Gartner SOP Scribd fetch가 abuse trigger). Wayback Machine 2025-12-14 스냅샷에서 메타데이터·구조·핵심 인용·7 dimension·5 stage 명칭 확보. 각 매트릭스 cell 정의는 SVG 렌더링으로 미확보 — paywall 해제 또는 Jina 차단 풀린 후 (2026-05-12 09:13 KST) 보강.

**신규 생성 (6번째 source 페이지)**: `wiki/industry/LAKA/sources/src_gartner_demand_driven_2018.md`

**원전 메타데이터**:
- 제목: Gartner's Demand-Driven Model for Supply Chain Excellence
- 저자: **Virginia Howard, Paul Lord, Michael Dominy**
- 발행: 2018-11-14, Refreshed 2020-04-02
- ID: **G00372772**
- 등급: **FOUNDATIONAL Gartner research** (master reference for all functional maturity models)
- Base: 100+ clients × 15+ years 연구

**핵심 발견**:
- **5 Stages × 7 Dimensions** 매트릭스 모델 (vs Gartner 2010 = 4 stage × 3 차원)
- 5-stage 명명 "React/Anticipate/**Integrate**/Collaborate/Orchestrate"의 정착 시점 = **2018-11 DDM**
- 7 Dimensions: Strategic Governance · Performance Enablement · Network Design · Supply Operations · Customer Fulfillment · **Demand Management** (★ distinguishing feature) · PLM
- LAKA 8부문 ↔ DDM 7 dimension 거의 1:1 매핑 가능
- 본 DDM은 **모든 functional maturity model (S&OP·Logistics·PLM·Customer Service·Procurement·Talent·Innovation)의 master framework**
- Gartner의 자체 "Demand-Driven Maturity Assessment Tool" 존재

**LAKA 적용 시사점**:
- 본 DDM이 LAKA에 가장 직접 적용 가능한 framework — 8부문 = 7 dimension 1:1
- Demand Management dimension (마케팅 15명)이 LAKA demand-driven 진입의 핵심
- 18개월 목표 = 7 dimension 중 **Strategic Governance + Performance Enablement + Demand Management 3개를 Stage 2→3 진입** (나머지 4개는 Phase 3 이후)
- DSR (Demand Signal Repository) + POS = LAKA Master_Data 시트 MVP의 진화 방향

**구성 (12개 섹션)**:
1. 원전 메타데이터
2. 핵심 주장 ("balance between operating efficiency and innovation")
3. 5 Stages 명명
4. 7 Dimensions × LAKA 매핑 표
5. Gartner Maturity Model Hierarchy (DDM = 마스터 / sub-models = functional)
6. DDM Assessment Tool 명시
7. DDM 평가 원칙 (dimension별 다른 속도 + interactions)
8. Demand Management Dimension "distinguishing feature" 강조
9. 약어 (DSR·POS·CTS·PDM·ROA·GTM·WMS·LSP·FTZ)
10. LAKA 4 영역 적용 (8부문 매핑·자가 진단·18개월 목표·Demand Management 진화)
11. Wallace·Implement·SCI·Gartner 2010 vs DDM 2018 정합성 표
12. Eagle/Barratt 거부 / DDM 채택 정당화

**index.md 업데이트**: src_gartner_demand_driven_2018 등재. 페이지 카운트 159 → 160.

**6 source 페이지 통합 표** (현재 wiki의 source 학파 라이브러리):
1. Wallace Workshop (2010, OMTEC) — Wallace 1차
2. Wallace+Stahl Book (2006) — Wallace 1차
3. Implement Handbook (2014) — 컨설팅 학파
4. SCI Guide (2020, Cecere) — 정량 학파
5. Gartner SOP Maturity (2010, Barrett & Uskert) — Gartner 4-stage origin
6. **Gartner DDM (2018, Howard/Lord/Dominy)** — Gartner 5-stage × 7-dimension FOUNDATIONAL ★ wiki 주류 채택 모델

## [2026-05-12] 5번째 source 페이지 | src_gartner_sop_maturity_2010 — Gartner 원전 1차 자료

**배경**: 사용자 요청 — Scribd URL (https://www.scribd.com/document/474294819) 본문 스캔. Jina Reader 우회로 **5/11 페이지 본문 확보** (paywall 뒤 6-11페이지 미확보).

**중대 발견 — 우리 wiki 정정 필요**:
- Gartner 원본 (Barrett & Uskert 2010, G00207249)은 **4-Stage 모델**: Reacting / Anticipating / **Collaborating** / **Orchestrating**
- **"Integrate" 단계는 후속 진화** (67% 기업이 Stage 1-2에 정체하는 문제 대응)
- 원본 Stage 3 (Collaborating) = "S&OP is no longer supply chain process, but rather aligned business planning process" — **IBP 진입 시점**
- 5-Stage 버전에서 IBP는 Stage 4-5로 이동

**신규 생성 (5번째 source 페이지)**: `wiki/industry/LAKA/sources/src_gartner_sop_maturity_2010.md`

**구성 (12개 섹션)**:
1. 원전 메타데이터 (저자 Jane Barrett·Michael Uskert, G00207249, 2010-11-01)
2. 핵심 주장 — *"two-thirds of businesses do not progress beyond first two stages"*
3. Key Findings 5개 (원문 인용)
4. Recommendations 5개
5. **원본 4-Stage Matrix (3 차원 × 4 단계)** — Goals/Alignment/Process & Tech 원문 표 완전 재현
6. Stage 2 함정 — "Stuck in Neutral" 특징·한계
7. Stage 3 진화 — 3-24mo horizon, multi-tier, "THE forum for decision making"
8. **Translation 8 차원** (SKU·Global Units·Currency·Profit·Customer·Product Category·Plant·Countries/Regions)
9. **Financial Integration S&OP-AOP 6-Step (a-h)** — Demand → Supply → Constraints → Manufacturing → Inventory → Distribution → SG&A → Profit roll-up
10. Profitability 정의 — Stage 3 gross profit / Stage 4 EBIT
11. **Stage 3 Governance Framework** — Sponsor: CEO / Coordinator: SCM / Owner: Line-of-business / KPI focus
12. 미확보 정보 (paywall 뒤 page 6-11) 명시

**우리 wiki 정정**:
- [[gartner_5stage_maturity|gartner_5stage_maturity §2]] 정정 — 원본 2010 4-Stage + 후속 5-Stage 진화 timeline 명시
- 원본 명칭: **Reacting · Anticipating · Collaborating · Orchestrating** (현재 wiki 명칭 React/Anticipate/Integrate/Collaborate/Orchestrate는 5-stage 버전)
- IBP 정의 — Wallace 정확한 부분: *"once moves to Stage 3 it is no longer a supply chain process, but rather aligned business planning process"*

**LAKA 적용 자산** (Gartner 2010 원전 기반 강화):
- **W5 KPI focus** = "demand risk, customer service, profit, cash, market share" (Gartner Stage 3 원전)
- **W7 Governance Framework** = Sponsor/Coordinator/Owner 3-role (Gartner 원전)
- **W2 Translation 8 차원** = SKU·Currency·Profit·Customer 등 (Gartner 원전)
- **Financial Integration 6-step** = LAKA 분기 budget·monthly S&OP 통합 base

**index.md 업데이트**: src_gartner_sop_maturity_2010 등재 (5번째 source). 페이지 카운트 158 → 159.

## [2026-05-12] 보강 | gartner_5stage_maturity — Gartner Maturity 두 모델 + 5 Ps

**배경**: 사용자 요청 — 웹에서 Gartner S&OP Maturity 아티클 검색·통합. 두 무료 공개 자료 fetch:
- ToolsGroup blog (Tim Payne 2017) — Supply Chain Planning Technology Maturity
- My Supply Chain Group — "5 Ps of S&OP Maturity"

**신규 생성**: `wiki/industry/LAKA/concepts/sop/gartner_5stage_maturity.md`

**핵심 발견 4개**:
1. **Gartner는 같은 5-stage 프레임을 5 도메인에 적용** — S&OP Process / Technology / Demand-Driven / PLM / Logistics. "Gartner 5-stage maturity" 표현 시 어느 도메인인지 명시 필수
2. **S&OP Process Model 4→5 stage 진화 이유** — *"two-thirds of companies find it difficult to move from Anticipate to Collaborate"* → Integrate 단계 신설
3. **Gartner vs SCI IBP 정의 정반대** — SCI: IBP = Stage 3 (중간) / Gartner: IBP = Stage 4-5 (성숙). 본 wiki는 SCI 기준 채택, Gartner 인용 시 명시
4. **5 Ps × 5 Stages 매트릭스** — People·Processes·Platforms·Policies·Performance 각각이 다른 단계에 머무는 게 일반적 ("5 Ps 균형 부재")

**구성 (9 섹션)**:
1. Gartner의 5 도메인 분류 표
2. S&OP Process Maturity 5 Stage 정의 + 4→5 진화 이유
3. Tim Payne Technology Maturity 5 Stage + LAKA 매핑 (Process Stage 1-2, Tech Stage 1)
4. **5 Ps × 5 Stages 매트릭스** + My Supply Chain Group 균형 부재 사례 5개 (CPG·하이테크·중기계·산업유통·다중기능)
5. **SCI 5-Stage vs Gartner 5-Stage 비교** + IBP 정의 차이 표
6. Wallace의 maturity 입장 (stage 모델 X, 본질 강조)
7. **LAKA 5 Ps 자가 진단** — People Stage 1-2, Processes Stage 1, Platforms Stage 1, Policies Stage 1, Performance Stage 1
8. 통합 인용 가이드 — wiki 내 maturity 언급 시 명시 표기 표준
9. 출처 8개

**LAKA 적용 결정사항**:
- 본 wiki Stage 표기 = **SCI 기준** (Stage 3 = IBP)
- Gartner 인용 시 명시 표기 추가 (Stage 3 = Integrate, IBP는 Stage 4-5)
- 5 Ps 균형 진단을 분기 회고 또는 [[sop_failure_patterns|W6]] 자가진단에 추가 검토 가능
- LAKA 가장 낙후된 P = Policies + Performance

**index.md 업데이트**: gartner_5stage_maturity 등재. 페이지 카운트 157 → 158.

## [2026-05-11] W8 | laka_sop_v1_simulation — Pilot 90일 운영 + 회고 (COM-27)

**신규 생성**: `wiki/industry/LAKA/concepts/sop/laka_sop_v1_simulation.md` ("LAKA S&OP v1 — Pilot 90일 운영 시뮬레이션 + 회고")

⚠️ **시뮬레이션 명시** — Wallace 책의 "Bad Day at Acme Widget" Ch3 storytelling 양식 차용. 가상 인물·사건 narrative. 사고 실험 가치.

**구성 (8개 섹션)**:
0. 시뮬레이션 타임라인 (2026-07 ~ 2026-10)
1. **Cycle 1 — 8월 Discovery** — Master Data ID drift 즉시 발견(F01 SKU alias 충돌)·ODM 데이터 latency·Sales 통합 인풋·세포라 80개 매장 확장 polite bomb·ODM 슬롯 첫 위기·Pre-meeting 95분(초과)·Exec Meeting CEO "매월 이거 보자고"·학습 5개
2. **Cycle 2 — 9월 Discipline** — Master Data 정비 후 KPI 즉시 개선·Layer별 양식 효력·F08 코스맥스 dual sourcing 첫 PO·FVA 첫 측정 (Sales APE 33% 발견)·90분 엄수·학습 4개
3. **Cycle 3 — 10월 Stabilization** — Process Owner 자동화 시작·**3-mo FVA로 Sales 음수 패턴 정량 확인 (-11.5%p)**·코스맥스 품질 issue (2.3% vs 한국콜마 0.8%)·Mini-S&OP 발동 안 함이 정상·CEO "Window into the Future" 발언 (Wallace Soft Benefit S7 실현 첫 사례)·학습 5개
4. **Phase 2 회고** — 8개 항목 4점 척도 평균 **2.6/3.0** (우수 zone)
5. **Go/No-Go #2** — 6/7 YES, 1/7 △ (Soft Benefit 정량 미수집) → Phase 3 진행 결정. 가장 큰 발견 Top 7
6. **v1 → v2 보정안** — W7 §14 자기 평가 갭 10개 점검 결과 표 + 추가 보강 5개 + 신규 Risk 4개
7. **책상머리 시뮬레이션의 가치와 한계** — 가치 5개 + 한계 5개. Wallace "Behavior Change ≠ Fact Transfer" 재인용
8. **다음 단계 (실제 적용 시)** — Phase 1 직전 7개 체크리스트 + 1년 후 v3 계획

**핵심 storytelling 발견**:
- Cycle 1 Master Data ID 충돌 (F01 vs "립글로스_핵심") — Pothole 즉시 발견·1주 정비
- Cycle 1 글로벌사업 → SCM 정보 비대칭 (세포라 80개 매장 확장) — Conflict Aversion 표면화 시뮬레이션
- Cycle 2 손여진 본부장 "Layer 분리 양식 보기 좋아요" — 양식 강제 효력
- Cycle 3 **3-mo FVA로 Sales 단기 과대예측 패턴 정량 확인** — APE 33% / FVA −11.5%p
- Cycle 3 CEO **"Window into the Future"** 발언 — Wallace Soft Benefit S7 실현 시뮬레이션
- 코스맥스 첫 PO 2.3% 불량률 vs 한국콜마 0.8% — 품질 SLA 협상 필요 시점
- Process Owner Excel macro 자동화 → Data On-time KPI 67%→95%

**시뮬레이션 학습 정리**:
- **사고 실험 도구로서의 가치**: W7 갭 10개 → 8개 검증·2개 새 발견
- **위험 사전 식별**: W7 Risk 9개 + 4개 신규 Risk
- **임원 교육 자료 가치**: Pilot narrative 자체가 Phase 1 Briefing 일부로 활용 가능
- **본질적 한계**: Outcome KPI Hard Benefits (Inventory ↓·Obsolescence ↓ 등) 6-12개월 호라이즌 — 90일로 불충분
- **Wallace 가르침 재확인**: Behavior Change ≠ Fact Transfer. 본 시뮬레이션은 "고도화된 fact transfer"

**시리즈 완성**:
- W1~W8 = 8 페이지
- + 1 워크북 (laka_sop_template_v0.xlsx)
- + 4 source 페이지 (Wallace workshop/book, Implement, SCI)
- = **13개 문서**

**index.md 업데이트**: laka_sop_v1_simulation 등재. 페이지 카운트 156 → 157.

**전체 W1~W8 진행률**: **8/8 완료 (100%)**. LAKA S&OP 학습 시리즈 종료.

## [2026-05-11] W7 | laka_sop_v1 — Live Pilot Playbook 시뮬레이션 (COM-26)

**신규 생성**: `wiki/industry/LAKA/concepts/sop/laka_sop_v1.md` ("LAKA S&OP v1 — Live Pilot Playbook (시뮬레이션)")

⚠️ **시뮬레이션 명시** — 페이지 상단 yellow box로 표기. 실제 LAKA Executive Briefing·인터뷰·현장 데이터 없이 추정 기반 작성. 실제 적용 시 모든 가정 보정 필요.

**구성 (14개 섹션)**:
0. **가정 명시** — 시작 시점 2026-07, Pilot Family F01+F08, Pilot Channel 3개, ODM 한국콜마+코스맥스, 마스터 데이터 사전 정착
1. Wallace 4-Phase Implementation Path LAKA 적용 — 8-12개월, <$100K, Go/No-Go gate 2개
2. **Phase 1 — Executive Briefing 60분 운영 매뉴얼** — 8명 참석자·sequential agenda 60분·5 sound bite·예상 반론 6개·Go/No-Go #1 6 조건
3. Kickoff Session 반나절 agenda
4. **Master Scheduling Policy v1 (Draft) — 7 조항** — Process Definition·Scope·Roles & Responsibilities·Time Zone·**Decision Authority RACI 매트릭스 12 의사결정**·Meeting Cadence (9 회의)·Override & Escalation
5. **Phase 2 — Live Pilot 90일 3 Cycle** — Pilot Scope 정량·Cycle별 학습 목표·발견 가능한 문제 8개 사전 예측
6. **Step 4 Pre-meeting 운영 매뉴얼 90분** — 6-8명 참석자·sequential agenda·출력 자료 7종
7. **Step 5 Exec Meeting 운영 매뉴얼 60-90분** — Essential/Probable/Possible 참석·Wallace 표준 8 agenda·의사결정 4 유형·회의 후 24시간 액션
8. **Phase 2 회고 + Go/No-Go #2** — 8개 평가 항목·7개 YES 조건
9. Phase 3 Expansion 4개월 — Month 4-7 family·channel 확장 schedule + 운영 부담 증가 대응
10. Phase 4 Financial Integration 2개월 — Wallace 미래 비전(War Room·Running Delta·Red Zone·Audit Trail) 도입 시점
11. KPI 목표 Phase 2·3·4 progression 표
12. v1 → v2 진화 계획
13. **Risk Register 9개** — Pilot 중 위험·확률·impact·대응
14. **시뮬레이션 갭 10개 자기 평가** — Family·ODM cadence·단가·MOQ·8부문 commitment·국내사업 공석 영향·마스터 데이터 현행·시스템 통합·ODM 데이터 협조·환율 release·분기 budget 통합 모두 추정

**핵심 자산**:
- **Master Scheduling Policy 7 조항** — LAKA-customized 거버넌스 공식 문서 양식 (CEO·이사회 승인 base)
- **Decision Authority Matrix (RACI)** — 12 의사결정 유형 × 8 부문 R/A/C/I 명시
- **9 회의 cadence** — Data Gathering 마감·Demand Consensus·Supply sign-off·Pre-meeting·Exec Meeting·Mini-S&OP·분기 review·연간 maturity
- **60분 Executive Briefing agenda + 예상 반론 6개** — Phase 1 직접 운영 자료
- **90일 Pilot 3 cycle 일정** — Day 1-20 매 cycle 활동
- **시뮬레이션의 한계 10개 명시** — 실제 적용 시 보정해야 할 갭

**LAKA-customized 결정사항**:
- Pilot family = F01 + F08 (베스트셀러 + 글로벌 FTO)
- Pilot channel = 세포라 US + Qoo10 JP + 한국 온라인
- Pilot ODM = 한국콜마 + 코스맥스 (F08 dual sourcing 시뮬레이션)
- 국내사업 본부장 공석 = CEO 임시 owner
- 시작 시점 = 2026년 7월 (가상)

**index.md 업데이트**: laka_sop_v1 등재. 페이지 카운트 155 → 156.

**전체 W1~W8 진행률**: 7/8 완료 (87.5%). 마지막 W8 = 시뮬레이션 운영 (90일 Pilot 가상 진행) + 회고 + v1 → v2 업데이트.

**다음**: W8 — Pilot 90일 시뮬레이션 진행. 3 cycle 가상 운영 + cycle별 발견·학습 + Phase 2 회고 + v1 보정안.

## [2026-05-11] W6 | sop_failure_patterns — 실패 패턴 통합 (COM-25)

**신규 생성**: `wiki/industry/LAKA/concepts/sop/sop_failure_patterns.md`

**구성 (9개 섹션)**:
0. **3 Type of Failure 분류 프레임워크** — Type A 본질(behavior change)·Type B 진화(pothole/pitfall)·Type C 단발(disruption)
1. **Type A — Wallace 3 Impediments** — Lack of Discipline(Emil's Engineers)·Fuzzy Accountability(Aerospace 케이스)·Conflict Aversion(Moose on the Table) + LAKA 위험·대응
2. **Broken Process 7 신호** — 분기 자가진단 체크리스트 + 신호별 즉시 액션 7개
3. **Type B — SCI Pothole 5 + Pitfall 6 + Capability Gap Top 5** + LAKA 분기 체크리스트
4. **Type C — Sales 단기 과대예측 + Suicide Quadrant + Stockout 6 원인**
5. **Mini-S&OP Cycle 발동 Trigger 매트릭스 11개** + 운영 룰 + 남용 위험
6. **LAKA 8부문 특화 위험 진단 표** — 부문별 위험 패턴·모니터링 KPI + 가장 큰 위험 3개(국내사업 본부장 공석·마스터 데이터 drift·ODM 슬롯 경쟁)
7. **분기 회고 체크리스트** — 90분 agenda + 4점 척도 점수표
8. **Re-implementation 경로** (Wallace) — 결정 트리 4 step + 위험 신호 4개
9. 출력 (분기 회고 + 연간 maturity 진단)

**핵심 통찰**:
- **3 type 분류가 중요** — 같은 증상이라도 type에 따라 처방이 다름. 진단 잘못되면 잘못된 대응
- Wallace "Behavior Change vs Fact Transfer" — 본 wiki는 fact transfer, 실제 도입은 behavior change (W7 Live Pilot)
- LAKA 가장 큰 3개 위험: 국내사업 본부장 공석·마스터 데이터 drift·ODM 슬롯 경쟁
- Mini-S&OP는 강력하지만 남용 시 정규 cycle 약화 — 분기 6회 이상 발동 시 정규 cycle 재점검

**LAKA 8부문 위험 진단 표** 핵심 매핑:
- 크리에이티브(CEO 겸임): Emil 패턴 위험
- 국내사업(공석): 인풋 owner 부재 (CEO 임시 owner)
- 마케팅(15명): Baseline·Campaign 통합 인풋 위험
- 글로벌사업(17명): 4 채널 분산 — channel별 인풋 표준 필요
- SCM(10명): ODM over-confirm·DTF 위반 위험

**Moose Rule**: Pre-meeting·Exec Meeting에 stuffed moose 인형(또는 LAKA 마스코트) — 어려운 이슈 raise 시 책상 위에 올림. Bob Stahl 컨설팅 도구 차용.

**index.md 업데이트**: sop_failure_patterns 등재. 페이지 카운트 154 → 155.

**전체 W1~W8 진행률**: 6/8 완료 (75%). 남은 작업: W7 laka_sop_v1 (Live Pilot Playbook 통합) + W8 시뮬레이션.

**다음**: W7 laka_sop_v1 — 1~6 모두 통합 + Step 4·5 Pre-meeting·Exec Meeting 운영 매뉴얼 + Wallace 4-phase Implementation Path LAKA 적용 + 거버넌스 문서 (Master Scheduling Policy)

## [2026-05-11] W5 | sop_kpis — Process·Outcome KPI 통합 (COM-24)

**신규 생성**: `wiki/industry/LAKA/concepts/sop/sop_kpis.md` ("S&OP KPIs — Process · Outcome 통합")

**구성 (11개 섹션)**:
0. **2층 KPI 프레임워크** — Layer 1 Outcome (Hard/Soft Benefits) ← Layer 2 Process (Step별)
1. **Process KPI 22개** 통합 표 — Step 1(6) + Step 2(6) + Step 3(8) + Step 4-5(2)
2. **Outcome KPI Hard 8개** (Wallace Customer Service ↑·Inventory ↓·Obsolescence ↓·Freight ↓·Lead Times ↓·NPI Speed ↓·Productivity ↑) + LAKA 우선순위
3. **Outcome KPI Soft 7개** (Teamwork·Communications·Decisions·$$$ Plans·Accountability·Control·Window into Future) + 반기 서베이 5점 척도
4. **OTD 확장 — 4단계 Fill Rate Hierarchy** — Supplier→LAKA(OTD)·LAKA→Channel(Line/Order)·LAKA→End(Perfect Order). family·channel별 목표값 표 + Stockout 6 원인 분류
5. Sally Smith Sheet 자동 측정 KPI + v0→v1 확장 plan
6. KPI 측정 cadence + 책임 매트릭스 (Monthly·Quarterly·Semi-annual·Annual)
7. Pre-meeting 대시보드 7개·Exec Meeting 대시보드 5개 (Wallace 5-7개 룰)
8. **KPI 목표 Progression Stage 1→5** — 8개 핵심 KPI의 SCI Maturity Stage별 목표값 진화
9. KPI Governance — Single Source of Truth 룰·KPI 변경 승인 룰
10. 흔한 실패 패턴 8개 (KPI Gaming·Forecast Accuracy 단독 의존·Soft Benefit 무시 등)
11. 출력 (월간 22개 process KPI + 분기 outcome + 연간 maturity 진단)

**핵심 통찰**:
- **Process KPI는 빠르게 움직임 (월간) → Outcome KPI는 천천히 움직임 (6-12개월)**. 운영 부서는 Process, 임원은 Outcome 보는 구분
- Wallace 권장 "한 meeting에 KPI 5-7개" 룰 명시
- 기존 [[OTD]] 페이지는 supplier→LAKA 측 — 본 페이지에서 LAKA→channel 측 (Order/Line Fill Rate) 보강
- Soft Benefit 측정의 어려움을 단순 5점 척도 서베이 (반기)로 해결

**LAKA Stage 1→3 KPI 진화 예시**:
- MAPE: 측정 안 함 → 25% → **15%**
- Order Fill Rate: 측정 안 함 → 92% → **95%** (베스트셀러·세포라)
- Time-fence Discipline: 빈번한 위반 → 월 5건 → **0건**

**index.md 업데이트**: sop_kpis 등재. 페이지 카운트 153 → 154.

**다음**: W6 sop_failure_patterns — Wallace 3 Impediments + Broken Process 7 신호 + SCI Pothole·Pitfall + Sales 단기 과대예측 + Mini-S&OP Cycle 발동 trigger

## [2026-05-11] W4 | supply_planning_odm — Step 3 운영 매뉴얼 (COM-23)

**신규 생성**: `wiki/industry/LAKA/concepts/sop/supply_planning_odm.md` ("3. Supply Planning (ODM)")

**구성 (12개 섹션)**:
0. 위치·책임 매핑 — Supply Planning Owner = SCM 부문 (10명, 김중찬), ODM·자재·finishing·재무·sign-off 6 role
1. Step 3 인풋(5종) · 출력(6종)
2. Operations Plan 업데이트 — 변경 trigger 6개, Planned Production 공식, Lot Sizing 룰 4종(FLS/LFL/POQ/Min-Max)
3. **RCCP (Rough-Cut Capacity Planning)** — Critical Resource Coefficient 변환, Resource Load 계산, Headroom 5% 임계
4. **ODM 슬롯 매핑** — 한국 K뷰티 ODM 슬롯 확보 6단계 (Annual → Quarterly → Monthly PO → Bulk → Finishing → Inbound), 슬롯 경쟁 alternatives 4개, **거의 모든 critical resource가 Matrix** = LAKA만 사용 dedicated 자원 없음
5. **Time Fences** — Frozen(DTF 30일)·Slushy(30-60일)·Liquid(60일+) 3 zone, ODM forecast visibility 정밀도 표
6. **Scalability 분석** (Implement Ch6) — 영역별 단기·중기·장기 elasticity 범위, 30% 갑작스러운 demand 대응 옵션 5개
7. **Constraint Identification & Escalation** — 5 type(Hard/Soft/Material/Capacity/Inventory), Pre-meeting 어젠다 양식
8. Sally Smith Sheet 운영 — Step 3가 채우는 행 + Production/Inventory 트래픽 라이트 의미
9. LAKA Step 3 매월 cadence — Working day 4-10 (Step 2와 4-7일 병행)
10. Supply-side KPI 8개 (Production Plan Adherence·ODM Slot Utilization·Capacity Headroom·DTF Discipline 등)
11. 흔한 실패 패턴 8개
12. 출력 → Step 4 Pre-meeting (자료 패키지 7종)

**LAKA Critical Resource 인벤토리 명시 (11개)**:
- R-KK-LG/SC/SK (한국콜마 라인 3개) — Matrix
- R-CM-LG (코스맥스 립글로스, 이중 발주 시) — Matrix
- R-FN-LBL (글로벌 라벨링) — Matrix
- R-PKG-TUBE / R-PKG-BOX (자재) — Matrix
- R-WH-KR/JP/US/UK (4개국 창고) — Aligned

→ **거의 모든 ODM·자재 자원이 Matrix** = 다른 K뷰티 브랜드와 슬롯 경쟁 → Step 3의 본질은 단순 capacity 계산이 아닌 **ODM 협상 + alternative 시나리오 도출**.

**Time Fences LAKA 적용**:
- DTF 30일 = 한국콜마 Monthly PO 발행 시점
- PTF 60일 = Quarterly Confirmation 시점
- 30% demand 변동 시 단기·중기·장기 가용 elasticity 표로 시각화

**Pre-meeting 어젠다 양식**: Issue ID·Family·Resource·Gap·Root cause·Alt A/B/C·Recommendation·Decision needed 9개 필드

**index.md 업데이트**: supply_planning_odm 등재. 페이지 카운트 152 → 153.

**다음**: W5 sop_kpis — Demand-side(2.) + Supply-side(3.) KPI 통합 + Hard/Soft Benefits 측정 + [[OTD]] 확장

## [2026-05-11] 샘플 워크북 | laka_sop_template_v0.xlsx — 작동하는 Sally Smith Sheet

**신규 생성**: `wiki/industry/LAKA/concepts/sop/laka_sop_template_v0.xlsx` (16KB)

**배경**: 사용자 요청 — W3·data_gathering 본문의 Sally Smith·4-layer forecast·NPI·FVA 등이 실제 어떤 엑셀 결과물로 운영되는지 보여주는 샘플 필요.

**5 시트 구성 (수식 51개)**:
1. **README** — 사용법·가정·트래픽 라이트 의미·v0 한계 명시 (45 row)
2. **Master_Data** — Family 8개(F01~F08, 단가·Lead Time·MOQ·Safety Stock) + 환율 3 시나리오(USD/GBP/JPY) + Channel 8개
3. **F01_Sally_Smith** — 립글로스 컬러군 A 18개월 view (Nov-25~Apr-27). 3 블록(Forecast·Production·Inventory) × 4 row(Baseline·Campaign·NPI·Total Forecast) + Actual·Difference·Cum Diff. Difference 셀에 트래픽 라이트 조건부 서식 자동 적용 (±5%/±10% 임계). KRW 환산 행은 Master_Data 단가 cross-sheet 참조
4. **NPI_Tracker** — 컬러 #208 코랄 launch 양식: 채널별 launch 일자 4개·Pipeline Fill 4 채널 합계 자동·Run-in Curve base/opt/pess 3 시나리오·Cannibalization 8% (base) / 15% (worst)
5. **FVA_Tracking** — F01 × 3 month(2025-11/12, 2026-01) × 4 layer(Baseline/+Marketing/+Sales/+Consensus) = 12 row. APE·MAPE_3mo·FVA vs Baseline 수식. FVA 셀 자동 색상 (양수 녹색·음수 빨강). 예시 데이터에서 Sales layer가 일관 음수 FVA → Implement Ch4 "단기 과대예측" 패턴 진단 시연

**디자인 원칙**:
- 파란 글씨 = 수동 입력 / 검은 글씨 = 수식 / 녹색 글씨 = cross-sheet 참조 (financial model 표준 색상)
- 한국어 폰트 Malgun Gothic, 헤더 D6E5F4
- 단가 변경 시 Master_Data 1곳만 수정하면 모든 family 시트 자동 반영
- v0 한계 명시 (1 family만, 채널 분해 X, 자동화 X) → W7에서 확장

**검증**: openpyxl self-validation — 수식 51개 모두 괄호·#REF!/#NAME? 이슈 0. LibreOffice 미설치로 자동 recalc 미실시 (Excel/Numbers에서 열면 정상 작동).

**연동**:
- `demand_planning.md` §6.4에 다운로드 링크 + 5 시트 설명 추가
- `data_gathering.md` §3.6에 Master_Data 시트 다운로드 링크 추가
- `index.md`의 LAKA — S&OP 섹션에 첨부 항목으로 등재

## [2026-05-11] Step 시리즈 정비 — "1. Data Gathering" 신규 + Step-2 제목 "2. Demand Planning"

**배경**: 사용자 지적 — Wallace 5-step 중 Step 1 (Data Gathering) 별도 페이지 없음. SCI 정량 갭 1위(58% "Difficulty getting to right data")이고 LAKA Designer/Distributor 특성상 마스터 데이터 거버넌스가 W4·W7 작동의 전제 조건이므로 별도 페이지 필요. Step 시리즈 명명 규칙 정착.

**변경 1 — `demand_planning.md` 제목 변경**:
- frontmatter title: "Demand Planning — Step 2 상세 (LAKA 적용)" → **"2. Demand Planning"**
- H1: "# Demand Planning — Step 2 상세" → **"# 2. Demand Planning"**
- 본문 첫 문단에 [[data_gathering|1. Data Gathering]] 위키링크 추가

**변경 2 — `data_gathering.md` 신규 생성** (`wiki/industry/LAKA/concepts/sop/data_gathering.md`):

구성 (10개 섹션):
1. 위치·책임 매핑 — Process Owner = SCM 부문 S&OP파트, 7개 데이터 소스 책임 분담
2. Step 1의 4가지 결과물 (Sally Smith actual + Statistical baseline + 시장 인텔리전스 + Data quality report)
3. **LAKA 데이터 소스 인벤토리 7개** — ERP·ODM·세포라/Boots/Qoo10/국내 sell-through·재고·환율·시장
4. **마스터 데이터 거버넌스 6 영역** — Family Hierarchy(F01-F08 후보 8개)·SKU 매핑(글로벌 라벨 변형)·Channel 코드 표준화·UoM 환산·Lead time/MOQ/Pack·Update Cycle
5. LAKA 현행 갭 진단 — 7개 갭 중 6개가 W7 도입 전 필수 해결
6. Step 1 매월 cadence — Working day 1-3 운영표
7. 통계 baseline 도구 — Excel MVP → 12-24개월 후 ToolsGroup/o9 검토 (Hybrid)
8. Step 1 KPI 6개 (Data On-time·Completeness·Master Data Drift·Statistical FVA·ODM Latency·Channel Coverage)
9. 흔한 실패 패턴 7개
10. 출력 → Step 2 (5종)

**LAKA Family 후보 (F01~F08)** 명시: 립글로스 컬러군 A/B, 립틴트, 아이섀도, 베이스, 선케어, 스킨케어, 글로벌 전용 SKU. **확정 시점 = W7 또는 그 이전 별도 합의**.

**LAKA 도입 로드맵 (data 측면) 4 Phase**: Phase 0 마스터 데이터 정의 → Phase 1 Live Pilot manual → Phase 2 자동화 일부 → Phase 3 ETL/RPA + 통계 도구.

**index.md 업데이트**:
- 제목 prefix 정비: sop_overview/glossary는 "개요/용어집", data_gathering/demand_planning는 "**1. / 2.**" 번호 prefix
- data_gathering 등재. 페이지 카운트 151 → 152.

**Step 시리즈 명명 규칙 정착**:
- Step 1 Data Gathering → "1. Data Gathering" (이번 신규)
- Step 2 Demand Planning → "2. Demand Planning" (제목 변경)
- Step 3 Supply Planning → "3. Supply Planning (ODM)" (W4 작업)
- Step 4·5 (Pre-meeting·Exec Meeting) → W7 laka_sop_v1 통합 또는 별도 페이지 결정

**다음**: W4로 진행 → "3. Supply Planning (ODM)" — Step 3 + 한국콜마/코스맥스 슬롯 매핑 + DTF/PTF + Aligned vs Matrix Resources LAKA 적용

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
