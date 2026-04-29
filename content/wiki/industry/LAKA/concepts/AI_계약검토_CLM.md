---
title: AI 계약 검토 (CLM)
type: concept
axis: industry
tags: [industry/LAKA, scm, ai]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# AI 계약 검토 (CLM)

AI가 계약서에서 조항을 자동 추출하고, 표준 Clause Library와 대조해 deviation을 탐지한 뒤, 리스크 수준에 따라 검토 루트를 자동으로 결정하는 계약 라이프사이클 관리 방법론.

## 핵심 처리 흐름

```
계약서 입력 (PDF/Word)
  ↓
OCR + 조항 추출 (120종+ 표준 조항, 날짜, 금액)
  ↓
Clause Library 대조 → Deviation 탐지
  ↓
Risk Scoring
  ↓
라우팅 분기:
  - 단순 갱신·표준 언어 → One-click 승인 (구매팀)
  - 신규 벤더·비표준·AI 기술 포함 → 법무 심층 검토
  ↓
AI Redline — 비표준 조항에 표준 대안 제시 (Word 애드인)
```

## 인간 개입 지점

**AI가 결정하는 것**: 검토 우선순위와 심도
**사람이 결정하는 것**: 최종 승인, 리스크 수용 여부, 비표준 조항 협상

## 효과 (벤더 공식 케이스 기준)

| 기업/사례 | 결과 |
|----------|------|
| [[CCC_Intelligent_Solutions\|CCCIS]] | 법무 인력 유지, 계약 볼륨 2배 |
| OutSystems | 계약 완료 시간 30%+ 단축 |
| Commvault | 서명까지 50% 단축 |
| NDA 검토 (업계 평균) | 60분 → 15분 (75% 단축) |

## K-뷰티 수입 유통 적용

K-뷰티 수입 유통사가 관리하는 계약 유형:
- 브랜드사 독점 대리점 계약 (Territory, 최소발주, 가격정책)
- 일본 리테일러 입점 계약 (세포라·PARCO·NEWoMan, 반품조건, STR 기준)
- ODM 계약 (리드타임, QC 기준, 폐번 처리)
- 물류 계약 (3PL, 포워더, 통관 에이전트)

브랜드 수가 늘어날수록 계약 볼륨이 비선형으로 증가하므로, AI 검토·라우팅 자동화의 ROI가 커진다.

## 관련 솔루션·개념

- [[LinkSquares]] — CLM SaaS 대표 솔루션
- [[Tonkean]] — P2P 오케스트레이션에서 NDA 자동 초안·라우팅 포함
- [[구매AI_도입패턴]] — 단일 task 시작 패턴
