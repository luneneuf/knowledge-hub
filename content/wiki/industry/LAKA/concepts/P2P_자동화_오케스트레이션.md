---
title: P2P 자동화 오케스트레이션
type: concept
axis: industry
tags: [industry/LAKA, scm, ai]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# P2P 자동화 오케스트레이션

Purchase-to-Pay(구매 요청 → 승인 → 발주 → 수령 → 정산)의 전 구간을 AI가 조율·자동화하는 방법론. 기존 S2P 시스템(Coupa, Ariba) 위에 AI 레이어를 얹어 사용자 경험과 내부 효율을 동시에 개선.

## 전통적 P2P의 병목

| 단계 | 문제 |
|------|------|
| 구매 요청 | 비구매 부서에 복잡한 ERP UI, 30분/건 소요 |
| 승인 | 순차 승인으로 1~2주 소요, 사일로 문제 |
| 계약 | 이메일에 분산, 상태 추적 불가 |
| 인보이스 | 수기 대조, PO 미매칭 오류 |
| 가시성 | Spend under management 낮음, maverick spend 발생 |

## AI가 각 단계에서 하는 일

```
자연어 요청 (Slack/이메일)
  ↓
카테고리 자동 분류 + 동적 폼 (필요 필드만 표시)
  ↓
벤더 분석 + 대안 제시 (tail-spend: 3 Bids and a Buy 자동 실행)
  ↓
순차 승인 → 병렬 승인 (Finance·Legal·Compliance 동시 호출)
  ↓
PO 자동 생성 (기존 S2P 연동)
  ↓
인보이스 AI 추출 + PO 자동 매칭
  ↓
NDA·계약 AI 초안 + 라우팅
```

## 사람 개입 지점

- 임계 금액 초과·신규 벤더·고위험 카테고리: **반드시 사람 승인**
- AI는 라우팅·컨텍스트 제공·요약만 수행
- 신규 공급업체 온보딩: 구매팀이 AI 추천 리스트를 검토·확정

## 효과 (벤더 공식 케이스 기준)

| 기업/지표 | 수치 |
|----------|------|
| [[Cockroach_Labs]] 티켓 작성 | 30분 → 5분 |
| 미드마켓 평균 PR-to-PO | 13일 → 7일 |
| Spend under management | +40% |
| Semrush PR-to-PO | 19일 → 10일 |

## 관련 솔루션·개념

- [[Tonkean]] — P2P 오케스트레이션 대표 솔루션
- [[AI_계약검토_CLM]] — 계약 검토 자동화 연계
- [[IDP_인텔리전트_문서처리]] — 인보이스 처리 연계
- [[구매AI_도입패턴]] — 구매 AI 도입 원칙
