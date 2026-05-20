---
title: Rossum Aurora
type: entity
axis: industry
tags: [industry/LAKA, scm, saas, vendor]
created: 2026-04-29
updated: 2026-04-29
status: active
publish: false
---

# Rossum Aurora

체코 IDP SaaS. LLM 기반 자체 학습형 Intelligent Document Processing. 템플릿·regex 없이 변동 포맷 문서를 처리하는 가장 검증된 인보이스 자동화 솔루션 중 하나.

## 핵심 특징

- **엔진**: 자체 LLM(Aurora) 기반, 3단계 인지 흐름 (skim-reading → 필드 위치 파악 → 정밀 추출)
- **자체학습**: 담당자 수정 결과가 학습 피드백 → 동일 패턴 자동 처리율 향상
- **검증**: IBAN 포맷, 날짜 논리("6월 31일" 차단), 이중 인보이스 감지
- **통합**: SAP ERP, Spendesk, Make, Salesforce 등 webhook 통합
- **도메인 학습**: 고객별 특화 필드 추가 학습 가능 (FINN의 경우 VIN·차량번호판)

## Human-in-the-loop 설계

- **신뢰도 0.8 이상**: 무인 자동 처리
- **신뢰도 미만**: 검증 큐로 라우팅
- 신규 공급업체 등록: Retool 내부 앱에서 사람이 마스터에 추가

## 검증 사례

| 기업 | 결과 |
|------|------|
| [[FINN]] (독일, 200개 공급업체) | 문서당 처리 71% 단축, 일일 2시간→15분, 6주 내 90%+ 정확도 |

## COM-14와의 관계

[[Docsumo]] (물류 서류 특화), [[Shippio_Cargo]] (일본 포워딩 통합)와 동일 IDP 카테고리. Rossum Aurora는 **인보이스·AP(Accounts Payable) 자동화에 특화**. 물류 서류(BoL, 패킹 리스트)는 Docsumo·Shippio와 역할 분담 가능.

## 관련 개념

- [[IDP_인텔리전트_문서처리]] — IDP 기술 카테고리
- [[Docsumo]] — 물류 서류 특화 경쟁 솔루션
- [[Shippio_Cargo]] — 일본 포워딩 통합 솔루션
- [[구매AI_도입패턴]] — 단일 use case 시작 패턴
