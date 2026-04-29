---
title: Channel Stockout Rate (채널 결품률)
type: concept
axis: industry
tags: [industry/LAKA, industry/kpi, industry/scm]
created: 2026-04-26
updated: 2026-04-26
status: active
publish: false
---

# Channel Stockout Rate (채널 결품률)

## 정의

특정 채널에서 SKU가 판매 가능 상태를 잃고 결품이 발생한 비중을 측정하는 지표. 서비스 레벨의 채널 현장판(역지표)이다. 값이 낮을수록 좋다.

## 계산식

$$\text{Channel Stockout Rate} = \frac{\text{Stockout SKU-days}}{\text{Total SKU-days}} \times 100$$

SKU-day: SKU 1개가 하루 동안 특정 채널에 존재해야 하는 이론적 단위. 분자는 그중 결품 상태였던 일수.

## 코스메틱 업계에서 결품의 비용

결품의 비용은 단순 매출 손실보다 크다.

| 상황 | 추가 비용 |
|---|---|
| 립·마스카라 등 대체 전환 쉬운 카테고리 | 경쟁 브랜드로 즉시 수요 이동 |
| 신제품 런칭 초기 결품 | SNS 화제성이 끊어짐 — 바이럴 모멘텀 상실 |
| 셀렉티브 리테일(세포라·부츠) 결품 반복 | 브랜드 운영 역량 자체가 낮게 평가, 재입점 리스크 |
| eCom 채널 결품 | 리뷰 수 축적 기회 상실 + 알고리즘 노출 저하 |

## 채널별 결품 임계치

채널마다 허용 임계치가 다르다. 셀렉티브 리테일은 매대 공간이 제한적이어서 결품 반복 시 해당 SKU의 공간 회수 가능성이 높다. eCom은 실시간 재고 정보가 소비자에게 노출되므로 즉각적인 전환 손실이 발생한다.

## LAKA 적용 시사점

세포라·부츠 입점 초기에 히어로 SKU의 Channel Stockout Rate를 최우선으로 관리해야 한다. 첫 6개월 바이어 리뷰 전에 결품 이력이 누적되면 [[STR]] 수치 자체가 실제보다 낮게 계산되어 도어 확장 협상에서 불리하게 작용한다.

## 연결

- [[공급망_KPI]] — SC KPI 전체 연결 구조
- [[서비스_레벨]] — 결품률의 역지표 관계
- [[WoC]] — 재고 건전성과 결품률의 연결
- [[OTIF]] — 납품 실패가 채널 결품으로 이어지는 경로
- [[세포라_운영구조]] — 셀렉티브 리테일 결품 대응 구조
- [[OSA]] — 진열 가용성(On-Shelf Availability) — 결품률의 오프라인 측면
