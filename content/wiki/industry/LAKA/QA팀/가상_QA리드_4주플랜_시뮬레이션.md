---
title: "가상 QA 리드 4주 플랜 (시뮬레이션, v2 / 2026-04-26)"
type: summary
axis: industry
tags: [cosmetics, analysis, simulation, qa, regulation, onboarding, market/us, market/uk]
created: 2026-05-18
updated: 2026-05-18
status: active
publish: false
source: src_LAKA_QA리드_가상_4주플랜_v2_20260426
---

# 가상 QA 리드 4주 플랜 — 시뮬레이션

> ⚠️ **시뮬레이션 — 가상 인물 기준 사고 실험**
>
> 이 페이지는 사용자가 Claude Web과의 문답으로 작성한 가상 시뮬레이션이다. 실제 채용·실행 계획이 아니다.
>
> - **전제 가상 인물**: 삼성전자 QA 조직장 출신 → [[LAKA]] 품질·운영 시니어 리드로 이직한다고 가정
> - **시뮬레이션 작성일**: 2026-04-26 (Claude Web 문답, v1 → v2)
> - **원본**: [[LAKA_QA리드_가상_4주플랜_v2_20260426]]
>
> 비교: [[laka_sop_v1]] (LAKA S&OP v1)도 동일하게 시뮬레이션 성격으로 작성됨.

---

## 시뮬레이션의 가치

가상 플랜이지만 진단 프레임은 실제 LAKA의 규제 리스크 구조를 정밀하게 반영한다.

이 4주 플랜은 [[K뷰티_ODM_QA_실패_8유형]] (2026-04-26 작성, 같은 날짜)이 정의한 **8가지 실패 유형 중 Type 3(색소)·Type 4(Drug Claim)·Type 6(라벨)** 을 "첫 4주에 어떻게 손에 잡히게 처리할 것인가"로 실행 시퀀스화한 것이다.

즉 두 페이지의 관계:
- **8유형 분류표** → 진단 프레임 (위험의 종류와 사례)
- **4주 플랜** → 실행 시퀀스 (Week 1~4 가설적 진행)

---

## 4주 플랜 핵심 구조

### v1 → v2 핵심 변경

| 항목 | v1 | v2 |
|------|----|----|
| SKU 수 | 4,000+ | **400개** (정정) — 합리화 긴급 → 중기 과제 |
| 즉시 위험 1순위 | ICP-MS 재시험 | **색소 FDA batch certification** |
| UK 즉시 리스크 | 컴플라이언스 갭 확인 | **SI 2024/1334 + SI 2024/455 off-shelf 시한 이미 경과** |
| ODM 분석 | 파트너 품질 파악 | **QA 부속서 분리 + MoCRA 조항 확인** |
| RP 인프라 | [[구다이글로벌]] 공유 가능성 | **결별 확정 — 외부 대행사 즉시 선정** |

### 전제 재설정

v1 프레임("시스템을 이식하기 전에 기계를 해독하라")은 유효하나, v2에서는 두 가지가 추가됐다.

1. 한국 OEM 공급 색소가 FDA batch cert 받지 않은 lot이면 [[세포라]] 80개 매장 진열 SKU가 미국 법상 adulterated cosmetic. 입점 이전 통관 통과와 무관, 재주문 시마다 import detention 리스크.
2. [[부츠|Boots UK]] 91개 매장의 경우 SI 2024/1334(64종 CMR 금지)·SI 2024/455(BHT 강화)의 off-shelf 시한이 이미 경과. 해당 성분 포함 SKU 진열 중이라면 현재 OPSS 제재 대상.

→ 이 4주 = "진단 → 보고"가 아니라 **"진단 + 긴급 처리 병행"**.

---

## Week별 요약

### Week 1 — 해독 + 긴급 신호 탐지

**이해관계자 미팅 5명** (Day 1~5)
- [[이지철]] 대표: RP 지정 현황, 컴플라이언스 담당 지정 여부, 브랜드 정체성 절대선
- 임지현 CD: 마케팅 카피 영문화 검토 프로세스
- 손여진 본부장 (글로벌사업): [[세포라]] Vendor Compliance 연락 이력, ODM 파트너 확인
- 생산·SCM: 색소 FDA batch cert 번호 확보 여부

**Day 1~3 즉시 확인 4건** (미팅 전 SCM 통해 병렬 진행):
1. 색소 FDA Batch Cert 현황 — CI 15850(D&C Red No. 7), CI 15510(립 사용 불가), 식물성 색소
2. UK SI 2024/1334 + SI 2024/455 위반 여부 — Boots 진열 SKU 처방 확인
3. 세포라닷컴 + 라벨 Drug Claim 스캔 — regenerate/restore/heal/treat/anti-aging/repair
4. ODM QA 계약 형태 — Quality Agreement 부속서 분리 여부 ([[한국콜마]])

### Week 2 — 4개 시장 × SKU 규제 매트릭스

**핵심 산출물**: SKU × (KR MFDS / JP 약기법 / US MoCRA·Clean@Sephora / UK UKCR SI) 매트릭스. 우선순위는 세포라 입점 SKU(3종) → Boots 입점 SKU → 나머지.

**시장별 체크포인트**:
- **미국**: Pb(세포라 1ppm), 색소 Batch Cert, Mineral Oil 금지([[Clean_at_Sephora]]), Drug Claim, MoCRA FEI+리스팅, RP 라벨, Carmine 표기 → [[미국_MoCRA]]
- **영국**: SI 2024/1334 CMR 64종, SI 2024/455 BHT 0.001%, Formaldehyde-releaser(2026.07.15~), BVL Pb 2ppm, CPSR Part B Safety Assessor 자격, SCPN 등록 → [[영국_화장품규제]]
- **일본**: [[株式会社JT]] 경유 PMDA 1차 대응 → JT 계약상 SLA·CS 데이터 공유 확인 → [[K뷰티_일본시장]]

**ODM QA 운영 현실적 3가지** ([[K뷰티_ODM_QA_실패_8유형]]과 직결):
1. TPT(Third Party Testing) 연간 계획 — 신제품 출시 전 1회 ICP-MS + 색소 CI→D&C 매핑
2. ODM 배치 기록 분기별 요청 루틴화 — 색소 공급사·cert 번호·처방 변경·IPC 결과
3. 영문 마케팅 카피 Ban List 운영 — 5개 한국 원문 키워드(재생/복원/주름개선/트러블진정/회복) → 대체 표현

### Week 3 — 갭 분석 + Quick Win 3개 확정

리스크 매트릭스(긴급도 × 중요도 2×2):
- **즉시 처리**: 색소 batch cert 미확보 SKU / SI 2024/1334 UK 위반 SKU / Drug claim 카피
- **계획적 개선**: ICP-MS 재시험, MoCRA FEI+리스팅, UK RP 대행사 계약, Formaldehyde 라벨
- **구조 설계**: ODM QA 부속서 분리, 4개 시장 SKU 매트릭스 상시 관리, Shade range 확장

**Quick Win 3개** (4주 내 완료, 8월 세포라 6개월 리뷰 직접 영향):
1. **Drug Claim 카피 정화** — 세포라닷컴 + 패키지 영문 카피 수정. 비용 거의 없음, FDA misbranding 즉시 제거
2. **색소 Batch Cert 현황 문서화** — CI 15510 함유 SKU 격리, FDA-compliant 색소 현황표 작성
3. **UK SI 위반 SKU 정리** — Boots 채널 분리, 재고 처리 방향 결정

**삼성 QA 배경의 활용**: "삼성처럼 해야 한다"가 아니라 **"세포라와 Boots가 요구하는 것을 갖춘다"** 라는 언어로 프레임 변환. batch records, 변경관리 사전승인, supplier qualification, 색소 공급망 추적 → 세포라 리뷰 통과 요건으로 번역.

### Week 4 — 경영진 보고서 5슬라이드 + 실행 착수

**슬라이드 구조**:
1. 판단 테이블 (1페이지 요약): 7개 영역 × 위험도 🔴🟡🟢 × 즉시 조치
2. Quick Win 3건 7월 전 완료 데드라인
3. 세포라 8월 리뷰 시나리오: Fruity Glam Tint 카테고리 Top 10~20 진입 + BA 무상 증정 + BI 리뷰 500~1,000개·4.3+ + TikTok/KOL 7월 피크
4. **Olive Young × Sephora 이중 트랙** (2026.01 파트너십, 가을 미국·캐나다·동남아·홍콩 K-뷰티 존, 8월 세포라 리뷰 타이밍과 정확히 겹침)
5. 90일 로드맵 (5~8월)

**90일 로드맵**:
| 월 | 핵심 과제 |
|----|-----------|
| 5월 | 색소 Batch Cert 취합 / Drug Claim 정화 / UK 위반 SKU 정리 / RP 대행사 계약 |
| 6월 | ICP-MS 재시험 / ODM QA 부속서 협의 / MoCRA FEI+리스팅 / Formaldehyde 라벨 |
| 7월 | 세포라 컴플라이언스 패키지 완비 / BA 교육 / Clean@Sephora Negative Declaration |
| 8월 | 세포라 6개월 바이어 리뷰 / [[올리브영]] 큐레이션 존 합류 타진 |

---

## 시뮬레이션의 함의 — 사용자(현 위키 소유자) 관점

이 플랜은 가상 인물(삼성 QA 출신)이 주체지만, **사용자가 LAKA 글로벌/해외사업 + 경영지원 직무로 이직했을 경우 인접 부서 리더로서 받을 영향**을 짚어준다.

- 사용자 현직: LINE GAMES 라이브본부장 → 관심 직무: LAKA 글로벌/해외사업 + 경영지원 ([[overview]])
- 가상 QA 리드가 첫 4주에 발견할 "불난 곳" 3건(색소·UK SI·Drug Claim)은 글로벌사업 부문(손여진)과 직결 — 세포라 입점 SKU 격리·Boots 채널 분리는 영업·재고 충격을 동반
- 4주 보고서 슬라이드 4(Olive Young × Sephora 이중 트랙)는 글로벌사업의 8월 전략 결정 이슈

[[LAKA_조직도_2026-05]] 기준 LAKA에는 **품질전략 부문(천승범, 차승호·김건 포함 총 3명)** 이 존재하지만, 이 시뮬레이션 가상 인물은 그 위의 시니어 리드급(부문장급 또는 부문장 직속)에 해당한다. 현재 조직도상 직접 매칭되는 빈 자리는 없음 — 어디까지나 가상 시나리오.

---

## 관련 위키

### 진단 프레임
- [[K뷰티_ODM_QA_실패_8유형]] — 같은 날짜 작성, 위험 분류 백본
- [[미국_MoCRA]] — RP, FEI, 색소 batch cert
- [[영국_화장품규제]] — SI, CPSR, SCPN

### LAKA 컨텍스트
- [[LAKA]] — 회사 entity
- [[이지철]] — 현 대표 (가상 미팅 대상)
- [[LAKA_채용공고_현황분석]] — 채용 동결, 이지철 체제 조직 재편
- [[LAKA_조직도_2026-05]] — 품질전략 부문 현 인력 구성
- [[한국콜마]] — ODM 파트너, QA 계약 협의 대상

### 채널·시장
- [[세포라]], [[세포라_운영구조]], [[Clean_at_Sephora]]
- [[부츠]]
- [[Qoo10_일본]]

### 출처
- [[LAKA_QA리드_가상_4주플랜_v2_20260426]] — raw/cosmetics/ 원본
