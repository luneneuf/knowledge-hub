# CLAUDE.md — 지식 허브 스키마

## 역할
너는 이 vault의 유일한 편집자다.
나는 소스를 가져오고 질문을 던진다. 너는 위키를 쓰고 유지한다.

---

## Vault 구조

```
obsidian-vaults/wiki/
├── raw/                  # 원본 소스 (읽기 전용, 절대 수정 금지)
│   └── assets/           # 이미지 등 첨부 파일
├── wiki/                 # LLM 생성 위키 (네가 소유)
│   ├── history/          # 축 1: 역사 공부
│   ├── work/             # 축 2: 회사 업무
│   └── industry/         # 축 3: 다른 산업 공부
│       └── [회사명]/     # 현재 공부 중인 산업/회사 단위
├── index.md              # 전체 위키 카탈로그 (인제스트마다 업데이트)
├── log.md                # 작업 이력 (append-only)
└── CLAUDE.md             # 이 파일
```

---

## 페이지 frontmatter 표준

모든 wiki/ 페이지는 아래 frontmatter를 포함해야 한다.

```yaml
---
title: 페이지 제목
type: summary | entity | concept | comparison | log
axis: history | work | industry
tags: [축/세부, ...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft | active | archived
publish: true | false   # true = 웹에 공개, false(기본값) = 로컬 전용
---
```

태그 체계:
- history 축: `#history/uwo`, `#history/[주제]`
- work 축: `#work/[프로젝트명]`
- industry 축: `#industry/[회사명]`

---

## 운영 워크플로

### 인제스트 (새 소스 추가)
1. raw/에 소스 파일 저장
2. 내가 "이거 인제스트해줘" 라고 지시
3. 네가 수행:
   - 소스 읽기 + 핵심 내용 요약
   - wiki/에 summary 페이지 작성
   - 관련 entity/concept 페이지 업데이트 또는 신규 작성
   - index.md 업데이트
   - log.md에 항목 추가: `## [YYYY-MM-DD] ingest | [소스 제목]`

### 질의
- 내가 질문하면 index.md → 관련 페이지 순서로 검색 후 답변
- 좋은 답변은 wiki/에 새 페이지로 저장 (내 요청 시)

### 린트 (월 1회 또는 요청 시)
- 고아 페이지 탐지 (인바운드 링크 없음)
- 내용 충돌 감지
- 빠진 [[링크]] 추가
- stale 페이지 status → archived 처리 제안

---

## index.md 구조

```markdown
# Index
> 마지막 업데이트: YYYY-MM-DD | 총 N페이지

## 역사 (history/)
| 페이지 | 타입 | 한 줄 설명 |
|--------|------|------------|

## 업무 (work/)
| 페이지 | 타입 | 한 줄 설명 |
|--------|------|------------|

## 산업 (industry/)
| 페이지 | 타입 | 한 줄 설명 |
|--------|------|------------|
```

---

## 금지 사항

- raw/ 파일 수정 또는 삭제 금지
- frontmatter 없는 페이지 생성 금지
- 내 확인 없이 페이지 삭제 금지
- 위키링크 없는 고립 페이지 생성 금지 (최소 1개 이상 링크 포함)
