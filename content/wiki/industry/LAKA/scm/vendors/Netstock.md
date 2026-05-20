---
title: Netstock
type: entity
axis: industry
tags: [industry/LAKA, scm, saas, vendor]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# Netstock

수요예측·재고최적화·재발주점 자동화 SaaS. Microsoft Dynamics Business Central 등 주요 ERP와 사전 통합. 이상치 평탄화 기능으로 COVID·프로모션 등 비정상 수요를 자동 제거하는 것이 강점.

## 핵심 기능

1. **수요예측**: 시계열+ML 기반, top-down/bottom-up/middle-out 지원
2. **이상치 평탄화**: COVID·프로모션 spike 자동 감지·제거
3. **동적 안전재고**: Z-score × σ_LT 기반, ABC 분류 가중
4. **재발주점 자동계산**: 리드타임 평균 수요 + 동적 안전재고
5. **다단계 분배**: 거점-공장 간 분배 계획

**AI는 추천까지만** — 자동 발주 없음, S&OP 매니저 검토·승인.

## 통합

- Microsoft Dynamics Business Central (사전 커넥터)
- 기타 ERP 연동 지원

## 검증 사례

| 기업 | 결과 |
|------|------|
| [[The_Little_Potato_Company\|TLPC]] | fill rate 90.9%→98%, COVID 변동성 흡수 |
| F&B 산업 평균 | 17개월 내 fill rate 99%, 과잉재고 80% 감소 |

## 관련 개념

- [[K뷰티_수입유통_SCM_AI_도입_패턴]] — 3~4단계 수요예측
- [[구매AI_도입패턴]] — 추천 생성 + 사람 승인 패턴
