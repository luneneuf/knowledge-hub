---
title: Tonkean / ProcurementGPT
type: entity
axis: industry
tags: [industry/LAKA, scm, saas, vendor]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# Tonkean / ProcurementGPT

미국 P2P 오케스트레이션 플랫폼. Slack·Teams·이메일·포털에서 자연어로 구매 요청 → 자동 분류 → 병렬 승인 → PO 생성까지 전 구간을 no-code로 자동화.

## 핵심 기능

| 기능 | 내용 |
|------|------|
| AI Front Door | 자연어 구매 요청 접수, 채널 무관 |
| 카테고리 분류 | NLP로 SaaS/하드웨어/컨설팅 등 자동 분류 |
| 동적 폼 | 카테고리·금액별 필요 필드만 표시 |
| ProcurementGPT | OpenAI LLM 연결, 벤더 분석·대안 제시 |
| 병렬 승인 | 순차 승인 → Finance·Legal·Compliance·Procurement 동시 호출 |
| PO 자동 생성 | Coupa, Ariba 등 기존 S2P에 PO 자동 생성 |
| 인보이스 매칭 | AI Invoice Processing Agent, PO 자동 대조 |

## 검증 사례

| 기업 | 결과 |
|------|------|
| [[Cockroach_Labs]] | 티켓 30분→5분, 인테이크 100% 자동화, 도입 2~3개월 |
| Semrush (동일 솔루션) | PR-to-PO 19일→10일 |
| 미드마켓 평균 | PR-to-PO 13일→7일, Spend under management +40% |

## 특징

- **no-code**: 도입 2~3개월, IT 개발 불필요
- **기존 S2P 위에 얹는 레이어**: Coupa·Ariba 교체 불필요
- 임계 금액·신규 벤더·고위험 카테고리는 반드시 사람이 최종 승인

## 관련 개념

- [[P2P_자동화_오케스트레이션]] — P2P 자동화 개념
- [[구매AI_도입패턴]] — 구매 AI 도입 패턴
