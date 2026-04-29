---
title: BiagiBros 3PL
type: entity
axis: industry
tags: [industry/LAKA, scm, case-study]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# BiagiBros 3PL

미국 3PL(Third Party Logistics). Docsumo IDP 도입으로 인바운드 BoL 처리시간을 건당 20~30분에서 2분 미만으로 단축(90%+). 자체 창고 입고 처리 속도가 매출 직납에 직결되는 구조의 모범 사례.

## 기본 정보

- **소재**: 미국
- **규모**: 월 1,500건+ 배송, 일 50+ 인바운드 컨테이너

## 도입 전 문제

10여 개 다른 BoL(Bill of Lading) 템플릿을 수기로 스캔해 ASN 바코드를 생성하는 데 **건당 20~30분**. HighJump WMS에 데이터 재입력 과정에서 오류 다발.

## AI 도입: Docsumo IDP

[[Docsumo]] (IDP SaaS) + Dell Boomi + HighJump WMS 통합 파이프라인. 자동 처리 95%, 수동 검토 5%의 Human-in-the-loop 구조.

## 결과

- 건당 **20~30분 → 2분 미만** (90%+ 단축)
- 건당 처리 약 40초 수준
- 매월 수백 시간 절감
- 수동 오류 대폭 감소

## LAKA/JT 시사점

한국 발송 박스 라벨·패킹 리스트 포맷이 브랜드별로 달라도 학습형 OCR이 흡수한다. **자체 창고 입고 → WMS 자동 등록 → 매장 직납 라우팅**이 분 단위로 빨라지는 효과는 도매 제거 후 소매 직거래 모델의 SLA를 결정짓는 핵심 요소.

## 관련 개념/솔루션

- [[Docsumo]] — 도입 솔루션
- [[IDP_인텔리전트_문서처리]] — AI-OCR·IDP 개념
- [[K뷰티_수입유통_SCM_AI_도입_패턴]] — 전체 도입 로드맵
