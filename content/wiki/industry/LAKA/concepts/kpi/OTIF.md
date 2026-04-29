---
title: OTIF (On Time In Full)
type: concept
axis: industry
tags: [industry/LAKA, industry/kpi, industry/scm]
created: 2026-04-26
updated: 2026-04-26
status: active
publish: false
---

# OTIF (On Time In Full)

## 정의

On Time In Full의 약자. 약속한 날짜에 주문한 수량을 빠짐없이 납품했는지를 측정하는 공급 이행 KPI. 대형 리테일 거래에서 대표적인 준수 지표이며, 미달 시 벌과금이나 바이어 평가 악화로 이어진다.

## 계산식

$$\text{OTIF} = \frac{\text{On-time and In-full orders}}{\text{Total orders}} \times 100$$

## 정의 세부 사항

OTIF는 두 요소의 곱으로도 분해할 수 있다.

$$\text{OTIF} = \text{OT (On-Time)} \times \text{IF (In-Full)}$$

'정시'와 '전량'의 정의가 리테일러마다 다르다는 점이 실무상 핵심 주의사항이다.

| 리테일러 유형 | '정시' 기준 예시 |
|---|---|
| 세포라 등 셀렉티브 리테일 | Must Arrive By Date 기준 |
| 대형 마트·마스 채널 | 예약 입고 슬롯(Routing Guide) 준수 여부 |
| eCom 풀필먼트 센터 | FC 도착 날짜 + 시간 단위 |

## 벌과금 구조

리테일러 가이드에 명시되며, 일반적으로 총 청구금액 또는 매입원가 기준 1~5% 수준에서 부과된다. EDI/ASN 오류만으로도 실제 납품은 완료됐어도 비준수 처리될 수 있다.

## 코스메틱 브랜드 관점

OTIF는 단순 물류 KPI가 아니라 **바이어 신뢰도, 분기 발주량, 판촉 협상력에 영향을 주는 거래 점수표**다. 셀렉티브 리테일에서 OTIF 저하가 반복되면 운영 역량 자체가 낮게 평가되어 SKU 확장 기회를 잃을 수 있다.

## 선행 원인과 대응

| OTIF 저하 원인 | 대응 포인트 |
|---|---|
| ODM 생산 지연 | [[ODM_납기준수율]] 관리 강화, 리드타임 버퍼 |
| 부자재 수급 불안정 | 용기·캡 SLA 계약화, 이중 소싱 |
| EDI/ASN 오류 | ASN 발송 타이밍·데이터 정확도 체크리스트 |
| 수요 급등 미예측 | [[WMAPE]] 관리 + 긴급 생산 대응 프로토콜 |
| 창고·3PL 처리 지연 | 3PL SLA 명문화, 출고 리드타임 모니터링 |

## LAKA 적용 시사점

[[세포라]]·[[Boots_UK_운영구조]] 등 셀렉티브 리테일과의 초기 거래에서 OTIF는 바이어 재발주 의사결정의 핵심 기준이다. 6개월 리뷰 시 OTIF 이력이 도어 확장 협상에 직접 사용된다.

## 연결

- [[공급망_KPI]] — SC KPI 전체 연결 구조
- [[ODM_납기준수율]] — OTIF의 선행 지표
- [[WMAPE]] — 예측 오류 → 재고 부족 → OTIF 저하 경로
- [[세포라_운영구조]] — OTIF 기준 및 벌과금 구조
- [[Boots_UK_운영구조]] — 영국 채널 납기 요건
