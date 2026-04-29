---
title: "K-뷰티 ODM 의존 립 브랜드 QA 실패 8유형"
type: summary
axis: industry
tags: [cosmetics, analysis, regulation, odm, qa, market/us, market/uk]
created: 2026-04-26
updated: 2026-04-26
status: active
publish: false
---

# K-뷰티 ODM 의존 립 브랜드 QA 실패 8유형

**핵심 주장**: LAKA가 직면한 가장 큰 단일 리스크는 미생물 오염(Type 1)이 아니라 색소·라벨 위반(Type 3·6)과 OTC drug 오분류(Type 4)다.

JAAD 2024 분석(Venkatesh et al., 2011~2023년 FDA 리콜 334건)에 따르면 미생물이 사유의 76.8%를 차지하지만, 한국 ODM이 미국에서 실제로 적발되는 패턴은 다르다. K-뷰티 브랜드의 직접 노출은 **FDA Import Alert 53-06(색소)·66-40(GMP) 등재**와 **ChemLinked 2025년 월간 통계에서 한국이 미국 화장품 수입거부 1~2위(2025-02 40%+, 2025-07 29%+)**로 반복되는 misclassification 트랩에서 더 빈발한다.

[[AMUSE]]가 중국 ODM 경유로 IA 53-06 Red List에 등재된 사례(2022-01-10)는 K-뷰티 브랜드의 직접 선례로, "한국 MFDS 통과 = 글로벌 통과"라는 가정이 깨지는 지점을 정확히 보여준다.

---

## 8유형 분류표

| Type | 유형명 | LAKA 해당 가능성 | 대표 사례 |
|------|--------|----------------|----------|
| 1 | 미생물 오염 | **중** | Juice Beauty/Gemdo(2015), Kleancolor(2016), L'Oréal Mizani(2023) |
| 2 | 중금속 초과 | **중상** | 화성코스메틱 안티몬 13개 SKU(2018), FDA 립스틱 Pb 조사(2010~2016) |
| 3 | 색소 위반 | **상** | **AMUSE(2022)**, Lime Crime(2015), Dongyang Fresh(2026) |
| 4 | Drug claim 오분류 | **상** | StriVectin(2015), Skin Beauty Solutions(2024), Cosmecca/Hanbul(2018) |
| 5 | 처방 변경 미통보 | **중** | Jaclyn Hill/Beautydom(2019, 색소 swap 정황) |
| 6 | 패키징·라벨 오류 | **상** | Lip Smacker 땅콩 알레르겐(2024), **AMUSE CI 단독표기(2022)**, MoCRA RP 미기재 |
| 7 | ODM 시설 GMP 위반 | **상** | **Kolmar Korea(2018)**, **Seoul Cosmetics(2023)**, **Mirfeel Korea(2022)** |
| 8 | 안정성 시험 미비 | **중상** | **It's Hanbul(2018, 6주 가속만)**, rom&nd 틴트 cheilitis(2025) |

> **확인된 K-뷰티 브랜드 직접 미국 enforcement**: [[AMUSE]] (IA 53-06, 2022) 1건이 명확. 한국 ODM 시설 단위: Kolmar Korea·Seoul Cosmetics·Mirfeel Korea·It's Hanbul·Cosmecca 모두 OTC drug 라인 Warning Letter.

---

## 대표 케이스 상세

### Type 3 — AMUSE Liquid Eyeliner Waterproof (2022): K-뷰티 직접 선례

[[AMUSE]]의 Liquid Eyeliner Waterproof가 **2022년 1월 10일 FDA Import Alert 53-06 Red List 등재**. 제조는 중국 동관 Dongguan Hui Ming Plastic & Metal. 라벨에 "CI 77499, CI 77266"(Iron Oxide Black, Carbon Black)만 표기하고 FDA 명칭(D&C Black No. 2 등)을 병기하지 않아 **21 CFR 70.25 위반**(undeclared color additive). 결과: **Detention Without Physical Examination(DWPE)**.

**핵심 실수**: 한국·EU 관행대로 CI 번호 단독 표기를 미국향에 그대로 사용. 브랜드 라벨 검수 미흡 + ODM 미국 가이드 미준수 공동 책임.

출처: FDA Import Alert 53-06 (accessdata.fda.gov/cms_ia/importalert_130.html), China section, "DONGGUAN HUI MING PLASTIC & METAL".

---

### Type 3 — Lime Crime Velvetines "Red Velvet" (2015): 외용 색소를 립에 사용

**2015년 7월 29일 FDA Warning Letter**. Velvetines Red Velvet 립스틱에 **ferric ferrocyanide(CI 77510)·ultramarines(CI 77007)**가 표기됐는데 두 색소 모두 미국에서 **외용 전용으로만 허가** — 점막인 입술에 불가. Lime Crime은 "라벨 오인쇄, 실제 처방에는 미함유"로 해명해 라벨 시정 종결.

**LAKA 적용**: 한국·EU에서는 두 색소가 립 처방에 합법. 한국 ODM이 한국 처방을 그대로 미국 수출용 INCI에 옮기면 자동 위반. manganese violet, chromium oxides 등 외용 한정 색소가 립 처방에 포함 시 미국향에서 제외 필요.

---

### Type 7 — Kolmar Korea Warning Letter 542511 (2018-05-18): 한국 ODM 거대기업 적발

세종 Jeonui 공장 FDA 사찰(2017-09-25~28)에서 **OOS 결과를 정당화 없이 retest로 무효화** + **batch production records·CoA가 quality unit 승인 없이 폐기** 적발. 21 CFR Parts 210·211(OTC drug cGMP) 위반.

**시사점**: 단순 ISO 22716 인증서 보유 ≠ 실제 준수. 브랜드는 quality agreement에서 OOS 처리 SOP·document retention(7년+)·QA approval flow를 명시적으로 통제해야 한다.

---

### Type 7 — Juice Beauty / Gemdo Cosmetics (2015): "외주해도 책임은 외주 못한다"

Juice Beauty의 아이섀도 3색에서 **Bacillus cereus** 검출 → 2014년 Class II 자발적 리콜. FDA 핵심 인용:

> **"Although your firm may contract out certain cosmetic manufacturing operations, it cannot contract out its ultimate responsibility to ensure that the cosmetics it places into commerce are not adulterated."**

외주 제조해도 adulteration에 대한 최종 책임은 브랜드에 있다는 법리적 근거.

---

### Type 2 — 화성코스메틱 안티몬 사건 (2018): 단일 ODM → 8개 브랜드 동시 회수

**2018년 3월 19일 MFDS 회수 명령**: Etude House·Aritaum·3CE·Skinfood·Makeheal 등 **8개 브랜드 13개 색조 품목**에서 안티몬 10.1~14.3 ppm(한국 한도 10 ppm) 검출. 경기도 김포 소재 **화성코스메틱** 단일 ODM의 컬러 마스터배치가 원인. 270개 이상 매장 영향.

**시사점**: 단일 ODM의 한 원료 lot 문제가 다수 브랜드 cross-contamination 리스크로 확대. 색소 raw COA에 As/Sb/Pb/Cd/Hg 5종 ICP-MS 동시 검사 의무화 필요.

---

### Type 2 — FDA 립스틱 납 조사 vs. Sephora Clean RSL 갭

2010년 FDA 시험: Maybelline "125 Pink Petal" 7.19 ppm Pb, L'Oréal "410 Volcanic" 7.00 ppm Pb. **FDA 권고 한도(10 ppm) 미만이지만 Sephora Clean RSL(립 Pb 0.5 ppm)·Prop 65에서는 위반**. 한국 MFDS 한도(20 ppm)를 통과한 처방이라도 Sephora US 입점 시 즉각적인 매대 위험.

---

### Type 4 — StriVectin (2015): "복원·재생" claim의 unapproved new drug 분류

Basic Research의 StriVectin이 "restore the elastin fiber architecture", "provide noticeable lift" 등 structure/function claim으로 Warning Letter. FD&C Act §201(g)(1)(C) 위반.

**LAKA 직접 적용**: "재생·복원·치료·주름 제거·barrier·soothing·regenerate·restore·heal·treat chapped lips" 키워드는 즉시 unapproved new drug 트리거. **FDA는 "chapped lips"를 disease로 간주**(skin protectant OTC monograph)하므로 립밤의 "treats chapped lips" 표기가 OTC drug 재분류로 이어진다.

---

### Type 6 — Lip Smacker 땅콩 알레르겐 회수 (2024)

14개 향에서 미공개 **peanut** 함유 발견 → 2024년 1월 voluntary recall. 알레르겐 함유 향료 라인 미분리 + cross-contamination 정황.

**시사점**: MoCRA fragrance allergen disclosure NPRM(2026년 5월 예정) 전에 EU 2023/1545의 80+ 알레르겐 기준으로 선제 대응. K-뷰티 립 틴트의 limonene·linalool·citronellol·geraniol 빈도 높음.

---

### Type 8 — It's Hanbul Cosmetics (2018): 6주 가속 시험만으로 expiry 표기

충북 음성 소재 한국 ODM. **FDA 인용**: "Your firm has only conducted six-week accelerated stability studies to support your labeled expiry periods. You have not conducted long term stability studies." 21 CFR 211.166 위반 → Import Alert 66-40 자동 등재.

**rom&nd 연결**: 2025년 5월 Juicy Lasting Tint cheilitis 컴플레인 300배 spike. rom&nd "Project ZERO"로 setting solvent 제거 신처방 358명 3차 테스트, 자극 보고 90% 감소. 단, 공식 결함 미인정·영수증 제출자만 환불.

**안정성 프로토콜 표준**: ICH-style 6개월 가속(40°C/75% RH) + 24개월 long-term + 50°C 4주 미국 여름 운송 stress + freeze-thaw.

---

## K-뷰티 ODM 특화 패턴

### "한국 MFDS 통과 ≒ 글로벌 통과" 가정이 깨지는 4개 시점

1. **개발 단계**: 색소 시스템 차이 — 한국 Negative list vs. 미국 21 CFR 74·82 Positive list + batch certification
2. **생산 단계**: OTC 트랩 — 한국 "기능성 화장품"이 미국에서 OTC drug으로 재분류
3. **유통 단계**: 안정성·라벨 — 미국 여름 운송·freeze-thaw를 반영하지 않은 6주 가속 시험
4. **리테일러 입점 단계**: Sephora Clean RSL·EU 2023/1545 80+ 알레르겐이 동시 적용

### OTC 트랩

한국 공개 Warning Letter 전체가 OTC drug 라인 발생: **Kolmar Korea(2018)·Cosmecca Korea(2018)·It's Hanbul(2018)·Mirfeel Korea(2022)·Seoul Cosmetics(2023)**. 색조 립 단독 라인의 직접 위험은 낮지만, **같은 ODM이 다른 브랜드의 OTC 라인으로 IA 66-40 등재 시 시설 단위 전체 shipment refusal — 무관한 립 SKU도 자동 통관 거부**.

### 한국 수입거부 반복 등장 (ChemLinked)

- 2024년 9월: 4위
- 2025년 1월: 2위 (makeup 35.96%로 1위 사유)
- 2025년 2월: **1위 (40%+)**
- 2025년 7월: **1위 (29%+)**

사유 1위: "unapproved new drug" — K-뷰티 효능형 마케팅 언어("진정·트러블케어·재생·회복·수분 폭발")의 영문 직역이 핵심 트리거.

### 색소 시스템 갭

| 항목 | 한국 | 미국 |
|------|------|------|
| 방식 | Negative list (타르·순색소·레이크) | 21 CFR 74·82 Positive list + batch certification |
| 립 제한 | 별도 없음 | mucous membrane 전용만 허용 (externally applied 불가) |
| 표기 기준 | CI 번호 허용 | D&C/FD&C 명칭 + lot 번호 추적 필수 |
| Carmine | 처방 가능 | 21 CFR 73.100 — "carmine" 또는 "cochineal extract" 라벨 명시 필수 (2009~) |

---

## LAKA 적용 시사점

### 가장 가능성 높은 Type 순위: 3 → 6 → 4

**Type 3** (색소 위반): [[AMUSE]] 직접 선례 + Lime Crime 패턴이 LAKA의 빨강·체리 계열 립 틴트(Fruity Glam Tint, Bonding Glow)에 직접 적용. D&C Red No. 6/7/21/27/30/33 batch certification lot 번호 추적 + CI 단독 표기 → D&C/FD&C 명칭 전환 필수.

**Type 6** (라벨 오류): MoCRA RP·FPLA net contents·Sephora 24 allergen·Carmine 명시가 동시 적용되는 다층 위험.

**Type 4** (drug claim): 영문 카피 ban list — "lip serum·lip treatment·barrier·soothing·regenerate·restore·heal·treat chapped lips".

### rom&nd 2025 cheilitis 사건의 함의

동일 카테고리(글로시 워터 틴트)에서 소비자 인식·리테일러 모니터링·SNS QA 압박이 이미 고조된 시장 환경. LAKA 출시 후 90일/180일 시점 SKU별 review sentiment 분석 + MoCRA serious adverse event 15일 보고 시스템이 첫 6개월 내 반드시 작동해야 한다.

### ODM QA 계약 필수 추가 조항 (7개)

1. **OOS·deviation 24시간 내 브랜드 통보** (Kolmar Korea OOS 무효화 대응)
2. **batch records·CoA·라벨 인쇄 데이터 7년+ 보존 + 분기별 사본 제출**
3. **MoCRA 120일 이내 reformulation update 자동 알림** — ODM 원료 swap 시 RP product listing 갱신
4. **색소 raw CoA에 As/Sb/Pb/Cd/Hg 5종 ICP-MS + batch certification lot 번호 의무 첨부**
5. **안정성 프로토콜**: 6개월 가속(40°C/75% RH) + 24개월 long-term + 50°C 4주 stress + freeze-thaw (It's Hanbul 6주 가속 직접 대응)
6. **환경 모니터링 보고서 분기별 제출** (dry-fill 라인 Bacillus·Pseudomonas·Burkholderia trend)
7. **알레르겐 함유 향료 라인 분리 + cross-contamination SOP** (Lip Smacker 땅콩 대응)

### 4주 플랜 Week 2 감사 체크리스트 추가 5항목

1. ODM FDA facility registration·MoCRA product listing 정합성 + U.S. Agent 지정 여부
2. 같은 ODM 라인 공유 브랜드 리스트 (화성코스메틱 cross-contamination 사례 대응)
3. 최근 2년 ODM Form 483·Warning Letter·Import Alert 이력 조회 (IA 66-40·53-06·53-17)
4. OOS·deviation 처리 SOP 실물 확인 + 최근 12개월 OOS 로그 샘플링
5. PET(USP \<51\>) 데이터 + dry room 환경 sampling 12개월 trend 확보

---

## 한계 및 확인/추측 구분

**확인된 사실**: JAAD 2024 통계(DOI 10.1016/j.jaad.2024.09.040), Kolmar Korea·Seoul Cosmetics·Mirfeel Korea·It's Hanbul·Cosmecca Warning Letter, [[AMUSE]] IA 53-06 등재, 화성코스메틱 안티몬 13개 SKU 회수, FDA 립스틱 Pb 시험, EU 2023/1545, FDA Import Refusal 월간 한국 비중, rom&nd Project ZERO, [[LAKA]] Sephora 2026-02-20 데뷔.

**미확인/추측**: LAKA 자체 공개 FDA 액션·리콜·매대 철수 없음 (2026-04-26 기준). ODM 파트너 (Cosmax 색조 라인, G&I Cosmetic 가능성) — **검증되지 않은 추측**. Type 5(처방 변경 미통보) 공개 enforcement 0건, 2026년 이후 활성화 예측은 법률 전문가 추정.

---

## 관련 페이지

- [[AMUSE]] — K-뷰티 FDA IA 53-06 직접 선례 브랜드
- [[LAKA]] — 분석 대상 브랜드
- [[ODM]] — ODM 구조 및 한국 ODM 역할
- [[ODM_발주_프로세스]] — 10단계 발주 플로우, 안정성 시험
- [[한국콜마]] — Kolmar Korea Warning Letter 542511 해당 기업
- [[코스맥스]] — 글로벌 화장품 ODM 1위, MoCRA 전담팀 보유
- [[미국_MoCRA]] — MoCRA cGMP 시행 일정, SAE 15일 보고
- [[Clean_at_Sephora]] — Sephora Clean RSL 기준 (립 Pb 0.5 ppm 등)
- [[K뷰티_립_CS_벤치마크]] — rom&nd Project ZERO 상세
