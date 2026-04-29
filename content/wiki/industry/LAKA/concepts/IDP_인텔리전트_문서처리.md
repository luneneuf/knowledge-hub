---
title: IDP (Intelligent Document Processing)
type: concept
axis: industry
tags: [industry/LAKA, scm, ai]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# IDP (Intelligent Document Processing)

AI-OCR + 자동 분류 + 데이터 추출 + 검증을 결합해 비정형 문서를 정형 데이터로 변환하는 기술 카테고리. 인보이스·B/L·패킹 리스트·BoL 등 수입 서류 처리의 핵심 자동화 레이어.

## 작동 원리

```
입력 (PDF/이메일 첨부)
  ↓
AI-OCR + 분류 (문서 유형 판별)
  ↓
필드 추출 (단가, 수량, 품번, 날짜 등)
  ↓
검증 (포맷, 수식, 이중 청구 감지)
  ↓
신뢰도 판별 → [임계값 이상] 자동 통과 / [미만] 사람 검토 큐
  ↓
ERP·WMS·자체 DB로 자동 푸시
```

핵심은 **포맷이 달라도 학습으로 흡수**한다는 점이다. 템플릿이나 정규식(regex) 없이 LLM 기반 인지 흐름으로 변동 포맷을 처리.

## 주요 솔루션 비교

| 솔루션 | 제조사 | 특징 | 검증 사례 |
|--------|--------|------|----------|
| [[Rossum_Aurora]] | Rossum (체코) | LLM 기반 IDP, 자체학습, SAP·Spendesk·Make 연계 | [[FINN]] — 71% 처리 시간 단축 |
| [[Docsumo]] | Docsumo | 물류 서류 특화, Dell Boomi·WMS 연계 | [[BiagiBros]] — 90%+ 처리 시간 단축 |
| [[Shippio_Cargo]] | Shippio (일본) | 일본 포워딩 통합, NACCS 연계, 97%+ 정확도 | [[Gong_Cha_Japan]] — 인보이스 대조 80% 단축 |

## K-뷰티 수입 서류 적용

수입 유통사에서 IDP가 처리하는 주요 문서:

| 문서 | 브랜드별 포맷 차이 | IDP 처리 포인트 |
|------|-----------------|---------------|
| 인보이스 (Invoice) | 브랜드사마다 단가·수량·합계 표기 위치 다름 | 필드 자동 추출, PO와 3-Way Matching |
| 패킹 리스트 (Packing List) | 박스별 SKU 구성 다름 | 입고 데이터로 변환, WMS 자동 등록 |
| B/L (Bill of Lading) | 선사마다 템플릿 다름 | ETA 자동 추출, 화물 트래킹 연계 |
| BoL (Bill of Lading, 미국형) | 3PL 파트너마다 다름 | ASN 바코드 자동 생성 |

**일본 K-뷰티 수입 컨텍스트**: 7-8개 브랜드의 인보이스 포맷을 모두 다르게 처리해야 하는 문제를 IDP가 단일 레이어에서 해결한다. [[Shippio_Cargo]]는 일본 NACCS 연계를 포함해 일본 수입 전 구간을 커버하는 점이 강점.

## Human-in-the-loop 설계

IDP도 [[Assisted_to_Autonomous_전환패턴]]과 동일한 원칙 적용:
- **신뢰도 0.8+ (Rossum 기준)**: 자동 처리
- **신뢰도 미만**: 검토 큐로 라우팅
- 담당자 수정 결과 → 재학습 피드백 → 자동화율 점진적 상승

## 도입 효과 (벤더 공식 케이스 기준)

| 지표 | 사례 | 개선 수치 |
|------|------|---------|
| 일일 처리 시간 | [[FINN]] | 2시간 → 15분 |
| 건당 처리 시간 | [[BiagiBros]] | 20~30분 → 2분 미만 |
| 인보이스 대조 공수 | [[Gong_Cha_Japan]] | 약 80% 삭감 |
| 추출 정확도 달성 기간 | [[FINN]] | 6주 내 90%+ |

## 관련 개념

- [[AI_SCM_처리유형]] — SCM AI 4대 처리유형 중 "비정형→정형 변환"
- [[Assisted_to_Autonomous_전환패턴]] — 도입 시퀀스
- [[K뷰티_수입유통_SCM_AI_도입_패턴]] — 1단계 수입 서류 자동화
- [[구매AI_도입패턴]] — 구매 영역 동일 원칙
