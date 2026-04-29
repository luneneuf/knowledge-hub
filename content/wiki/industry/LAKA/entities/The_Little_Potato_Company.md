---
title: The Little Potato Company (TLPC)
type: entity
axis: industry
tags: [industry/LAKA, scm, case-study]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# The Little Potato Company (TLPC)

캐나다 미니 감자 재배·가공 중견 식품 기업. Netstock으로 수요예측·안전재고·재발주점을 자동화해 주문 충족률을 90.9% → 98%로 끌어올린 사례.

## 기본 정보

- **소재**: 캐나다
- **사업**: 미니 감자 재배·가공
- **규모**: 생산공장 3개, 물류센터 8개, 직원 수백 명대 중견

## 도입 전 문제

모든 수요·공급 계획을 **엑셀로 수행**. 한 고객사가 3개 물류센터에서 공급받을 때 분배 비율 산정 불가. 안전재고는 "n일치 커버리지" 정적 규칙이라 변동성 큰 SKU에 부족·작은 SKU에 과잉. **COVID-19 비정상 수요 폭증**이 미래 forecast 노이즈로 그대로 유입.

## AI 도입: Netstock

[[Netstock]] (Microsoft Dynamics Business Central 연동 AI SaaS). ERP에서 판매 이력·재고·PO·리드타임·프로모션·BOM을 자동 추출 후:
1. 시계열+ML 기반 수요예측
2. **이상치 평탄화** — COVID spike 자동 감지·제거
3. **동적 안전재고** — Z-score × σ_LT, ABC 분류 가중
4. 재발주점 = 리드타임 동안 평균 수요 + 동적 안전재고
5. 다단계 거점-공장 분배 계획

AI는 **추천까지만** 생성, 자동 발주 없음. S&OP 매니저가 검토·승인.

## 결과

- 주문 충족률(fill rate) **90.9% → 98%** (+8%p 이상)
- COVID-19 변동성에도 과재고 발생 없이 운영
- 동일 솔루션 F&B 산업 평균: **17개월 내 fill rate 99%, 과잉재고 80% 감소**

## 구매AI 시사점

K-뷰티 수요예측에서 가장 직접적으로 참고할 패턴. 특히 **COVID·프로모션 같은 이상치를 자동 평탄화**하는 기능은 K-뷰티 버즈·드라마·아이돌 효과로 인한 급등락 수요에 동일하게 적용 가능.

## 관련 개념/솔루션

- [[Netstock]] — 도입 솔루션
- [[구매AI_도입패턴]] — 단일 task 시작 패턴
- [[K뷰티_수입유통_SCM_AI_도입_패턴]] — 수요예측 3~4단계
