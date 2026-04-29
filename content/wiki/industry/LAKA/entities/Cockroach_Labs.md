---
title: Cockroach Labs
type: entity
axis: industry
tags: [industry/LAKA, scm, case-study]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# Cockroach Labs

미국 뉴욕 분산 SQL DB 기업. Tonkean ProcurementGPT 도입으로 티켓 작성 30분→5분(83% 단축), P2P 인테이크 100% 자동화·오케스트레이션 달성. P2P AI 도입 사례 중 가장 완성도 높은 구현.

## 기본 정보

- **소재**: 미국 뉴욕
- **사업**: 분산 SQL 데이터베이스 기업 (CockroachDB)
- **규모**: 직원 약 300~500명 미드마켓

## 도입 전 문제

기존 Coupa S2P가 비구매 부서에 너무 복잡. Finance·Legal·IT·Procurement가 사일로로 움직여 법무팀이 **마지막 단계에서 컴플라이언스 리스크를 발견해 처음부터 재시작**하는 일이 빈번. 티켓 1건 작성에 평균 **30분** 소요 → maverick spend 유발.

## AI 도입: Tonkean ProcurementGPT

[[Tonkean]] (P2P 오케스트레이션 플랫폼). Slack·Teams·이메일·포털에서 자연어로 "I need to buy …" 입력 → AI Front Door가 처리:
1. NLP 카테고리 자동 분류 (SaaS/하드웨어/컨설팅)
2. 컨텍스트 인식 동적 폼 (카테고리·금액별 필요 필드만 표시)
3. 벤더 웹사이트 자동 분석, 대안 제시
4. tail-spend는 "3 Bids and a Buy" AI 자동 실행 + RFx 초안 생성
5. **순차 승인 → 병렬 승인** 전환 (Finance·Legal·Compliance·Procurement 동시 호출)
6. Coupa에 PO 자동 생성, 인보이스 자동 추출·PO 매칭

## 결과

| 지표 | 수치 |
|------|------|
| 티켓 작성 시간 | **30분 → 5분** (83% 단축) |
| 인테이크 자동화 | **100%** |
| 도입 기간 | **2~3개월** (no-code) |
| 동일 솔루션 평균 | PR-to-PO 13일→7일 (46% 단축), Spend under management +40% |

## 구매AI 시사점

**구매 요청 → 승인 → PO 전 과정의 자동화 조율**이 핵심. 임계 금액·신규 벤더·고위험 카테고리는 반드시 사람이 승인하는 구조는 유지. K-뷰티 수입 유통에서 발주·정산 프로세스 자동화의 종착지 모델.

## 관련 개념/솔루션

- [[Tonkean]] — 도입 솔루션
- [[P2P_자동화_오케스트레이션]] — P2P 자동화 개념
- [[구매AI_도입패턴]] — 단일 task 시작 패턴
