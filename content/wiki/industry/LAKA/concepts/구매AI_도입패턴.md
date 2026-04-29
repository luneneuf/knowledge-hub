---
title: 구매 AI 도입 패턴
type: concept
axis: industry
tags: [industry/LAKA, scm, ai]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# 구매 AI 도입 패턴

중견기업 구매 영역에서 AI를 도입할 때 가장 빠르게 효과를 내는 방법론. 5개 검증 사례([[FINN]], [[Kärcher]], [[The_Little_Potato_Company|TLPC]], [[CCC_Intelligent_Solutions|CCCIS]], [[Cockroach_Labs]])에서 공통으로 확인된 4가지 패턴.

## 패턴 1: 단일 부서 · 단일 task 시작

> "광역 P2P 자동화"가 아니라 **"기존에 사람이 매일 하던 1~2시간짜리 반복 task"** 에서 시작한다.

| 기업 | 첫 번째 task |
|------|------------|
| [[FINN]] | 인보이스 200개 공급업체 처리 |
| [[Kärcher]] | 공급업체 리스크 모니터링 |
| [[The_Little_Potato_Company\|TLPC]] | 안전재고 동적 조정 |
| [[CCC_Intelligent_Solutions\|CCCIS]] | 벤더 계약 검토·라우팅 |
| [[Cockroach_Labs]] | 구매 요청(티켓) 인테이크 |

효과 검증 후 인접 영역으로 확장 (NDA, tail-spend, 신규 카테고리 순).

## 패턴 2: AI는 "처리·플래깅·라우팅 엔진"

AI가 직접 결정을 내리지 않는다. **수치 기반 라우팅 룰**이 사람과 AI의 역할 분기점:

| 기업 | 임계값/라우팅 룰 |
|------|----------------|
| [[FINN]] (Rossum Aurora) | 신뢰도 0.8 이상 → 자동 처리, 미만 → 사람 검토 |
| [[Kärcher]] (Prewave) | Risk Score 임계값 기준, Critical → 사람 검토 |
| [[CCC_Intelligent_Solutions\|CCCIS]] (LinkSquares) | 표준 갱신 → one-click, 비표준 → 법무 심층 검토 |
| [[Cockroach_Labs]] (Tonkean) | 임계 금액·신규 벤더 → 반드시 사람 승인 |

## 패턴 3: Active Learning 루프

사람이 수정한 결과가 다시 학습 데이터로 피드백 → 시간이 갈수록 자동화율 상승:

- [[FINN]]: 검토팀 수정 → Rossum 재학습, 동일 패턴 다음번 자동 처리
- [[CCC_Intelligent_Solutions|CCCIS]]: Legal Operations Manager가 워크플로우·임계값 지속 튜닝

→ [[Assisted_to_Autonomous_전환패턴]]의 구매 영역 버전.

## 패턴 4: "인력 그대로, 처리량 2배"

AI 도입의 정량 목표를 "비용 절감"이 아닌 **"현재 인력으로 더 많이 처리"** 로 설정하는 것이 설득력 있다:

| 기업 | 결과 |
|------|------|
| [[FINN]] | 구독 볼륨 7배 증가에도 추가 채용 없이 처리 |
| [[CCC_Intelligent_Solutions\|CCCIS]] | 법무 인력 그대로, 계약 볼륨 2배 |
| [[Kärcher]]/Hilti | 5,000건 설문 처리 4명 → 0.5명 |

## 도입 task 선택 기준

좋은 첫 번째 AI task의 조건:
1. **매일 반복**: 일 1~2시간 이상 소요
2. **정형 입력→정형 출력**: 인보이스, 발주서, 계약서 같은 문서
3. **명확한 정답이 있음**: 수량·단가·날짜 매칭처럼 맞/틀림이 분명
4. **사람 검토가 가능한 볼륨**: 초기 Assisted mode에서 담당자가 AI 추천을 검토할 수 있는 양

## 정량 결과 종합

| 영역 | 기업 | 핵심 지표 | 개선 수치 |
|------|------|----------|---------|
| 문서 처리 | [[FINN]] | 일일 처리 시간 | 2시간 → 15분 |
| 공급업체 평가 | [[Kärcher]] | 수동 due diligence | 40배 감소 |
| 재발주·재고 | [[The_Little_Potato_Company\|TLPC]] | 주문 충족률 | 90.9% → 98% |
| 계약 검토 | [[CCC_Intelligent_Solutions\|CCCIS]] | 처리 볼륨 | 인력 유지, 2배 |
| P2P | [[Cockroach_Labs]] | 티켓 작성 | 30분 → 5분 |

## 관련 개념

- [[Assisted_to_Autonomous_전환패턴]] — SCM 영역 동일 패턴
- [[IDP_인텔리전트_문서처리]] — 문서 처리 자동화
- [[공급업체_리스크_스코어링]] — 공급업체 평가 자동화
- [[AI_계약검토_CLM]] — 계약 검토 자동화
- [[P2P_자동화_오케스트레이션]] — P2P 전구간 자동화
- [[AI_SCM_처리유형]] — SCM AI 처리유형 전체 개요
