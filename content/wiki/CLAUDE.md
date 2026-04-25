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

## 파일 저장 경로 규칙

**wiki/ 루트에 직접 파일 생성 금지.** 모든 신규 페이지는 아래 경로에 저장한다.

| 타입 | 저장 경로 |
|------|---------|
| entity | `wiki/industry/[산업폴더]/entities/[이름].md` |
| concept | `wiki/industry/[산업폴더]/concepts/[이름].md` |
| comparison | `wiki/industry/[산업폴더]/comparisons/[이름].md` |
| history | `wiki/history/[주제폴더]/[이름].md` |
| work | `wiki/work/[프로젝트폴더]/[이름].md` |

파일명 규칙:
- `wiki_entity_`, `wiki_concept_` 등 **접두사 없이** 이름만 사용. (예: `시코르.md`, `K-뷰티_글로벌_리테일_지형.md`)
- wiki/ 루트에는 `index.md`, `log.md`, `wiki_index.md`, `wiki_log.md`, `CLAUDE.md`만 존재.

신규 파일 생성 전 반드시 해당 `industry/[산업폴더]/` 하위 폴더를 ls로 확인해 기존 파일과 중복되지 않도록 한다.

---

## 이미지 정책

**로컬 저장 없이 외부 URL 직접 참조.** `wiki/assets/`나 `static/images/` 폴더는 사용하지 않는다.

```markdown
![설명](https://brand.com/image.jpg)
*캡션*
```

소스 우선순위:
1. 브랜드 공식 사이트 / CDN
2. 위키미디어 Commons (라이선스 명확)
3. 공식 SNS / 뉴스룸
4. 아마존·이커머스 제품 이미지

`publish: false` 페이지는 로컬 전용이므로 외부 URL 참조 허용. `publish: true` 페이지는 위키미디어 Commons 또는 공식 press kit 이미지 우선.

---

## 운영 워크플로

### 인제스트 (새 소스 추가)
1. raw/에 소스 파일 저장
2. 내가 "이거 인제스트해줘" 라고 지시
3. 네가 수행:
   - 소스 읽기 + 핵심 내용 파악
   - **기존 페이지 탐색**: 해당 `industry/[산업폴더]/` 하위 폴더(entities/, concepts/, comparisons/ 등)를 직접 ls로 확인. index.md만 보지 말고 실제 파일 목록을 확인한다.
   - **기존 페이지 업데이트 우선**: 관련 페이지가 이미 있으면 새 정보를 통합한다. 새 페이지를 만드는 것이 아니라 기존 페이지를 보강한다.
     - 새로운 사실 추가
     - 기존 서술과 충돌하는 내용 발견 시 명시적으로 표기
     - 관련 [[위키링크]] 추가로 크로스레퍼런스 강화
   - **신규 페이지는 필요할 때만**: 기존 페이지에 통합할 수 없는 새로운 entity나 concept이 등장할 때만 생성. 저장 경로는 반드시 위 "파일 저장 경로 규칙"을 따른다.
   - **소스 요약 페이지(src_*)**: raw/ 원본의 출처·범위·핵심 주장을 기록하는 용도로만 작성. 이것이 지식의 최종 형태가 아니다 — 지식은 wiki/ 내 entity/concept/summary 페이지에 통합된 상태가 최종 형태다.
   - index.md 업데이트
   - log.md에 항목 추가: `## [YYYY-MM-DD] ingest | [소스 제목]`
     - 업데이트한 기존 페이지 목록 포함
     - 신규 생성한 페이지 목록 포함

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

## Linear 이슈 관리

### 워크스페이스
- 워크스페이스: luneneuf
- Linear MCP: Claude Web(HQ)에서 `https://mcp.linear.app/mcp`로 직접 관리

### 팀 및 프로젝트
| 팀 | 팀 ID | prefix | 용도 |
|----|-------|--------|------|
| UWO | 749500f4-9a95-44a6-bb24-a4ba6c3946c0 | UWO- | 콘텐츠 워크플로 |
| COM | 4b6f8295-b64c-499f-b31d-58cee2964651 | COM- | 회사 업무 |

이슈 번호는 Linear가 팀별로 자동 부여한다 (UWO-1, UWO-2, COM-1, COM-2, ...).
각 팀 안에서 프로젝트를 만들어 세부 분류한다.

### UWO 팀 이슈 상태값
| 상태 | ID |
|------|----|
| Backlog | 4146fd0c-ca61-4cd5-95b3-4f378a30c533 |
| Todo | 4c8200ef-0542-4b49-973d-288087170bd4 |
| In Progress | a22cf158-2a66-474d-9857-da52d48d36be |
| In Review | 78aa4e5a-ff22-42a2-946d-0e0785540263 |
| Done | 6c164906-f8f1-440e-9e28-3aba7cc0133d |
| Canceled | 364b2a09-c3e7-4d9b-9607-c8e8e239edf1 |
| Duplicate | 514bb3df-c301-46e3-a6bf-516ae4d4e6f9 |

### COM 팀 이슈 상태값
| 상태 | ID |
|------|----|
| Backlog | 024c5e8d-14b4-46a7-9ed1-763e35a04f69 |
| Todo | 6956b346-ebf5-40b7-9967-2b7d16c15503 |
| In Progress | 5225db17-b14c-4741-a8f8-7eb22d8a5fbd |
| In Review | 125f58dd-fdd5-400f-8149-2ee62e24b627 |
| Done | e39e07d8-2984-4e59-b246-48e1a0ea759f |
| Canceled | 8065d1ea-f977-4093-91dd-d70dbb6aa110 |

### 작업 지시서 규칙
- 작업 지시서 작성 시 대응하는 Linear 이슈 번호(UWO-N 또는 COM-N) 명시
- 새 작업은 해당 팀의 프로젝트에 이슈 생성 후 진행
- 이슈 상태 관리는 Claude Web(HQ)에서 Linear MCP로 직접 처리

---

## 금지 사항

- raw/ 파일 수정 또는 삭제 금지
- frontmatter 없는 페이지 생성 금지
- 내 확인 없이 페이지 삭제 금지
- 위키링크 없는 고립 페이지 생성 금지 (최소 1개 이상 링크 포함)
