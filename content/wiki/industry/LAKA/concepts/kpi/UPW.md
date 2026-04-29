---
title: UPW (Units Per Week / Units Per Door Per Week)
type: concept
axis: industry
tags: [industry/LAKA, industry/kpi, industry/scm]
created: 2026-04-26
updated: 2026-04-26
status: active
publish: false
---

# UPW (Units Per Week / Units Per Door Per Week)

## 정의

Units Per Week 또는 Units Per Door Per Week의 약자. 오프라인 리테일에서 매장(door) 하나당 일주일에 해당 SKU가 몇 개 팔리는지를 나타내는 판매 속도(velocity) 지표. 매출 총량보다 **매장당 생산성**을 보기 때문에 신규 입점 테스트·전국 확대·저성과 SKU 정리 판단에 직접 사용된다.

## 계산식

$$\text{UPW} = \frac{\text{Total Units Sold}}{\text{Number of Doors} \times \text{Weeks}}$$

## 활용 맥락

| 상황 | UPW 활용법 |
|---|---|
| 파일럿 입점 평가 | 소수 매장에서 UPW 임계치 충족 여부로 전국 확대 결정 |
| SKU 컬러 관리 | 낮은 UPW 컬러는 페이싱 축소 또는 퇴점 대상 |
| 계절성 분석 | 시즌별 UPW 변화로 보충 주기 조정 |
| 매장 등급별 비교 | 플래그십 vs 일반 매장 간 UPW 편차로 SKU 배정 최적화 |

## 코스메틱 색상 SKU에서의 중요성

같은 립 라인 안에서도 핵심 컬러는 높은 UPW를 보이지만 비주류 컬러는 낮은 회전으로 매장 공간만 점유한다. 바이어는 총매출보다 "매장당 주당 몇 개가 꾸준히 팔리는지"를 보고 컬러 추가, 페이싱 확대, 퇴점 여부를 검토한다.

## 해석 주의사항

- UPW는 **매출액이 아니라 단위 수량 중심의 velocity metric**이다.
- 채널별 기준선은 리테일러·카테고리·런칭 단계에 따라 다르다. 세포라 기준 "성공"과 부츠 기준 "성공"은 수치가 다를 수 있다.
- 결품 기간이 포함된 경우 UPW가 실제보다 낮게 계산된다 — [[Channel_Stockout_Rate]]와 함께 봐야 정확한 수요를 파악할 수 있다.

## LAKA 적용 시사점

세포라 파일럿 단계에서 UPW가 바이어의 도어 확장 결정의 핵심 트리거다. 결품 없이 지속적인 UPW를 유지하는 것이 [[STR]] 목표 달성과 동시에 달성해야 할 지표다.

## 연결

- [[공급망_KPI]] — SC KPI 전체 연결 구조
- [[Channel_Stockout_Rate]] — 결품 기간은 UPW를 낮게 왜곡
- [[STR]] — STR과 UPW는 같은 판매 성과의 다른 표현
- [[세포라_운영구조]] — 도어 확장 3단계와 UPW 임계치
- [[히어로_SKU_프랜차이즈화]] — 히어로 컬러의 UPW 유지 전략
