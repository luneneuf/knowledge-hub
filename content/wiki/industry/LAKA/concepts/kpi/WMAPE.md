---
title: WMAPE
type: concept
axis: industry
tags: [industry/LAKA, industry/kpi, industry/scm]
created: 2026-04-26
updated: 2026-04-26
status: active
publish: false
---

# WMAPE

## 정의

Weighted Mean Absolute Percentage Error의 약자. 실제 판매량 대비 예측 오차를 절대값 기준으로 합산하고, 실제 판매량의 합으로 나눈 수요예측 정확도 지표. 값이 낮을수록 예측 정확도가 높다.

## 계산식

$$\text{WMAPE} = \frac{\sum |\text{Actual} - \text{Forecast}|}{\sum \text{Actual}} \times 100$$

## 일반 MAPE와의 차이

일반 MAPE는 SKU별 오차 비율을 단순 평균하기 때문에, 소량 판매 SKU 하나가 이상값을 만들면 전체 수치가 크게 왜곡된다. WMAPE는 실제 판매량(매출 비중)으로 가중치를 줘 고판매 SKU의 예측 정확도가 지표에 더 크게 반영된다. S&OP에서 더 현실적인 기준이다.

## 코스메틱 업계 해석

- **SKU 분리 관리 필수** — 코어 SKU와 신제품·시즌 컬러를 같은 기준으로 관리하면 왜곡이 생긴다. 컬러 트렌드·바이럴·프로모션 영향으로 립·아이·시즌 컬렉션의 예측 난도는 베이스 메이크업보다 훨씬 높다.
- **허용치는 카테고리·수명주기·채널 프로모션 여부에 따라 다르다** — 코어 기초 SKU는 20~25% 이하 목표가 합리적이지만, 신제품 첫 시즌은 40~50%도 불가피하다.
- **S&OP의 출발점** — WMAPE가 악화되면 재고 부족 또는 과잉 → WoC·Channel Stockout Rate 악화 → OTIF 저하의 연쇄가 시작된다.

## LAKA 적용 시사점

색조 위주 포트폴리오는 컬러별 수요 편차가 크다. 베스트셀러 컬러와 신규 컬러를 동일 모델로 예측하면 안전재고 설계가 틀어진다. 세포라·부츠 등 리테일러 납품 직전 프로모션 기간에는 별도 예외 처리가 필요하다.

## 연결

- [[공급망_KPI]] — SC KPI 전체 연결 구조
- [[WoC]] — WMAPE 오류가 직접 영향을 주는 재고 지표
- [[서비스_레벨]] — 예측 정확도와 안전재고 수준의 관계
- [[ODM_발주_프로세스]] — MOQ·배치 크기 결정에 예측 정확도가 기초 자료로 쓰인다
