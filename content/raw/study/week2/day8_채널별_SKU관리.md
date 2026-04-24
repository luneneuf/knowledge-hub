---
title: 화장품 수출 채널별 표시사항·SKU 관리
source: WebSearch "화장품 수출 채널별 표시사항 SKU 관리 세포라 영국" / https://kcia.or.kr
retrieved: 2026-04-24
day: Day 8
topic: SCM
---

# 화장품 수출 채널별 표시사항·SKU 관리

## 1. 채널별 SKU 관리 필요성

동일 제품이라도 수출 대상 국가·채널마다 요구하는 **라벨 표시사항·언어·등록 방식**이 달라 별도 SKU를 관리해야 한다.

```
[한국 내수 SKU]
   ├─ 한국어 전성분표시 필수
   └─ 식약처 기준 라벨

[미국 수출 SKU]
   ├─ 영어 전성분 (INCI명, 내림차순)
   ├─ 미국 내 Responsible Person 주소
   └─ FDA MoCRA 시설 등록번호 (해당 시)

[영국 수출 SKU]
   ├─ 영어 전성분 (INCI명)
   ├─ 영국 Responsible Person 이름·주소
   ├─ Made in Korea (Made in EU 불가)
   └─ SCPN 신고 완료

[일본 수출 SKU]
   ├─ 일본어 전성분 표기 (일본화장품공업연합회 기준 명칭)
   ├─ 일본 판매원 표기
   └─ 약사법 기준 표시사항
```

## 2. 국가별 라벨링 요건 비교

| 항목 | 한국 | 미국 | 영국 | 일본 |
|------|------|------|------|------|
| 표시 언어 | 한국어 | 영어 | 영어 | 일본어 |
| 성분 표기 | 전성분 (한국어 또는 INCI) | INCI명 (영어) | INCI명 (영어) | 전성분 (일본화장품공업연합회 명칭) |
| 책임자 표시 | 제조·판매업체명 | Responsible Person (미국 주소) | Responsible Person (영국 주소) | 일본 판매원 |
| 원산지 | 제조국 | 제조국 | 제조국 (Made in EU 불가) | 제조국 |
| 내용량 | ml/g | fl oz / oz | ml/g (UK 단위) | ml/g |
| 유통기한 | 개봉 전/후 | 해당 시 표기 | PAO (개봉 후 사용기한) | 사용기한 |
| 등록·신고 | 식약처 | FDA Cosmetics Direct | SCPN 포털 | 도도부현 신고 (일반화장품) |

## 3. 세포라 전용 SKU 요건

세포라(미국·유럽)는 일반 유통 요건 외 **추가 브랜드·패키지 기준**을 요구한다.

### 세포라 공통 요건
- 영문 라벨 완비 (성분, 용법, 경고문구)
- FDA MoCRA 기준 충족 (미국 세포라)
- SCPN 신고 완료 (영국 세포라)
- Sephora 금지 성분 리스트(Banned Ingredients List) 준수
- 패키지 품질 기준 충족 (외관, 인쇄 품질)
- GMP 인증 서류 요구 가능

### 미국 세포라 전용 추가 사항
- 미국 내 Responsible Person 지정 (주소가 라벨에 인쇄)
- FDA 시설 등록번호 (MoCRA 2023년 의무화)
- 이상사례 보고 연락처 라벨 포함
- 영문 성분 INCI명 오름차순(내림차순) 표기

## 4. SKU 관리 실무 포인트

### 채널별 SKU 코드 체계 (예시)

```
[제품코드] - [시장코드] - [채널코드] - [버전]

예: LKTINT001-US-SEPH-V1
    LKTINT001-UK-SEPH-V1
    LKTINT001-JP-DRUG-V1
    LKTINT001-KR-OLYG-V1
```

### 변경 관리 체크리스트

- [ ] 시장별 금지 성분 재확인 (포뮬러 변경 시)
- [ ] 라벨 변경 → 각국 등록/신고 업데이트 여부 확인
- [ ] 새 SKU 바코드 부여 (EAN-13 유럽, UPC-A 미국)
- [ ] 채널 바이어에게 변경 사전 공지 (일반적으로 3~6개월 전)
- [ ] 기존 재고 소진 계획 수립 (라벨 변경 전 구 재고 처리)

## 5. 영국 수출 특이사항 (Post-Brexit)

브렉시트 이후 영국은 EU CPNP와 분리된 독자 SCPN 시스템을 운영한다.

- **EU CPNP 등록 ≠ 영국 SCPN 등록**: 별도 신고 필수
- **영국 책임자(RP)**: 잉글랜드·스코틀랜드·웨일즈 소재 법인 또는 개인
- **Made in EU 원산지 표기 금지**: "Made in Korea" 등 실제 원산지 표기 필수
- **PIF (Product Information File)**: 영어 작성, 마지막 배치 출시 후 10년 보관
- **라벨 유예기간**: 2022년 12월 31일까지 기존 EU 라벨 재고 소진 허용 (이미 종료)

## 6. 일본 수출 특이사항

- 전성분 표기 명칭은 반드시 **일본화장품공업연합회(JCIA) 기준 명칭** 사용
- 미백·주름개선 등 기능성 표현 → **의약부외품** 분류 → 후생노동성 별도 승인 필요
- 산화철 등 색소: 패키지 전성분표에 하나로 통합 표기 필수
- 한국에서 허용된 성분이라도 일본에서 금지된 경우 포뮬러 변경 필요 (예: 트라넥삼산 — 일본에서는 의약품 원료로 분류)

## 참고 출처

- [2021년부터 영국 내 화장품 유통 규정 — 대한화장품협회](https://kcia.or.kr/home/industry/industry_01.php?no=13519)
- [유럽 화장품 수출 컨설팅 — cosmereg.com](https://cosmereg.com/eu-uk-cosmetics-regulations/)
- [화장품 수출 방법 — tradlinx.com](https://www.tradlinx.com/blog/guide/%EC%9A%94%EC%A6%98-%EB%A7%8E%EC%9D%B4-%ED%95%98%EB%8A%94-%ED%99%94%EC%9E%A5%ED%92%88-%EC%88%98%EC%B6%9C-%EC%88%98%EC%9E%85%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95/)
- [화장품 글로벌 규제조화 지원센터 — MFDS](https://helpcosmetic.or.kr/pc/license/license06.php)
