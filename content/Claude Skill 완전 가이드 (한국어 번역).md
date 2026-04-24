# Claude Skill 완전 가이드 (한국어 번역)

> **번역 정보**
> 원문: *The Complete Guide to Building Skills for Claude* — Anthropic
> 번역 기준: 팀 내 핵심 기술 용어집(Glossary) v1.0 적용
> 대상 독자: 서비스 기획자, 개발자, 운영자
> 번역 기준일: 2026년 3월

---

## 목차

1. [핵심 기술 용어집 (Glossary)](#1-핵심-기술-용어집)
2. [소개 (Introduction)](#2-소개)
3. [Chapter 1: 기초 개념 (Fundamentals)](#chapter-1-기초-개념)
4. [Chapter 2: 기획 및 설계 (Planning and Design)](#chapter-2-기획-및-설계)
5. [Chapter 3: 테스트 및 반복 개선 (Testing and Iteration)](#chapter-3-테스트-및-반복-개선)
6. [Chapter 4: 배포 및 공유 (Distribution and Sharing)](#chapter-4-배포-및-공유)
7. [Chapter 5: 패턴 및 트러블슈팅 (Patterns and Troubleshooting)](#chapter-5-패턴-및-트러블슈팅)
8. [Chapter 6: 리소스 및 참조 자료 (Resources and References)](#chapter-6-리소스-및-참조-자료)
9. [참고 자료 A: 빠른 체크리스트](#참고-자료-a-빠른-체크리스트)
10. [참고 자료 B: YAML 프론트매터 레퍼런스](#참고-자료-b-yaml-프론트매터-레퍼런스)
11. [참고 자료 C: 완성 예제 Skill 모음](#참고-자료-c-완성-예제-skill-모음)
12. [성공적인 Claude Skill 구축을 위한 핵심 원칙 10](#성공적인-claude-skill-구축을-위한-핵심-원칙-10)

---

## 1. 핵심 기술 용어집 (Glossary)

번역 전 과정에서 아래 용어집을 기준으로 일관성 있게 표기합니다.

| 영문 원어 | 번역 / 표기 | 표기 원칙 | 비고 |
|---|---|---|---|
| Skill | Skill (스킬) | 영문 그대로 사용 | 첫 등장 시 '스킬(Skill)'로 병기 |
| SKILL.md | SKILL.md | 파일명 원문 유지 | 대소문자 정확히 지킬 것 |
| MCP | MCP | 첫 등장 시 풀네임 병기 | Model Context Protocol |
| Tool | Tool (도구) | 기술 맥락: 영문 | 일반 맥락: '도구' |
| Workflow | 워크플로우 | 음차 허용 | |
| Trigger | 트리거 | 동사형: 트리거되다 | |
| Progressive Disclosure | 점진적 공개 | 첫 등장 시 원문 병기 | |
| Composability | 조합 가능성 | 첫 등장 시 원문 병기 | |
| Portability | 이식성 | 첫 등장 시 원문 병기 | |
| kebab-case | kebab-case | 코드 규약: 원문 유지 | |
| Token | 토큰 | 음차 허용 | |
| Claude Code | Claude Code | 제품명: 원문 유지 | |
| skill-creator | skill-creator | 도구명: 원문 유지 | |
| Undertriggering | 과소 트리거 | 첫 등장 시 원문 병기 | |
| Overtriggering | 과잉 트리거 | 첫 등장 시 원문 병기 | |

> 💡 **용어 사용 원칙:**
> - 제품명·파일명·폴더명은 항상 원문 그대로 표기합니다.
> - 핵심 기술 개념은 첫 등장 시 `한국어(English)` 형식으로 병기 후 이후 선택 적용합니다.
> - 코드/명령어 블록 내부는 항상 영문을 유지합니다.

---

## 2. 소개 (Introduction)

**Skill이란 무엇인가요?** Skill은 Claude가 특정 작업이나 워크플로우를 처리하는 방법을 가르치기 위한 일련의 지침(Instructions)을 하나의 폴더로 패키징한 것입니다. Skill은 Claude를 여러분의 필요에 맞게 커스터마이징하는 **가장 강력한 방법 중 하나**입니다. 매번 대화할 때마다 선호 방식, 업무 프로세스, 전문 지식을 다시 설명하는 대신, Skill을 통해 Claude에게 **한 번만 가르치고 매번 활용**할 수 있습니다.

Skill은 반복 가능한 워크플로우가 있을 때 특히 강력합니다.

- 스펙(Spec) 문서로부터 프론트엔드 디자인 생성
- 일관된 방법론으로 리서치 수행
- 팀의 스타일 가이드를 따르는 문서 제작
- 여러 단계로 구성된 프로세스 자동화 및 조율

Skill은 코드 실행, 문서 생성 등 Claude의 내장 기능과도 함께 잘 동작합니다. MCP 연동을 개발하시는 분들께는, Skill이 원시적인 Tool 접근 권한을 신뢰성 있고 최적화된 워크플로우로 전환해 주는 강력한 추가 레이어가 됩니다.

**이 가이드에서 배울 수 있는 것:**
- Skill 구조에 대한 기술적 요구사항 및 모범 사례(Best Practices)
- 독립형 Skill과 MCP 강화 워크플로우를 위한 패턴
- 다양한 사용 사례에서 효과적인 것으로 검증된 패턴
- Skill을 테스트하고, 반복 개선하고, 배포하는 방법

**이 가이드의 대상:**
- Claude가 특정 워크플로우를 일관성 있게 따르게 하고 싶은 개발자 및 파워 유저
- 조직 전체에서 Claude의 작동 방식을 표준화하려는 팀

> 💡 **두 가지 학습 경로**
> - **독립형 Skill을 구축하시나요?** → Chapter 1 기초 개념, Chapter 2 기획 및 설계, 카테고리 1~2에 집중하세요.
> - **MCP 연동을 강화하시나요?** → 'Skills + MCP' 섹션과 카테고리 3을 참고하세요.

**이 가이드를 통해 얻게 되는 것:** 가이드를 마치면 한 번에 앉아서 작동하는 Skill을 구축할 수 있게 됩니다. `skill-creator`를 활용하면 첫 번째 Skill을 만들고 테스트하는 데 약 **15~30분**이면 충분합니다.

---

## Chapter 1: 기초 개념 (Fundamentals)

### Skill이란 무엇인가요?

Skill은 다음 항목들을 포함하는 **폴더**입니다.

| 파일/폴더 | 필수 여부 | 설명 |
|---|---|---|
| `SKILL.md` | **필수 ★** | YAML 프론트매터가 포함된 Markdown 형식의 지침 파일 |
| `scripts/` | 선택 | 실행 가능한 코드 (Python, Bash 등) |
| `references/` | 선택 | 필요에 따라 로드되는 참조 문서 |
| `assets/` | 선택 | 출력에 사용되는 템플릿, 폰트, 아이콘 등 에셋 |

---

### 핵심 설계 원칙 (Core Design Principles)

#### 1. 점진적 공개 (Progressive Disclosure)

> 💡 **비유로 이해하기:** 점진적 공개(Progressive Disclosure)는 잘 정리된 매뉴얼과 같습니다.
> - 책의 **표지** → 어떤 내용인지 한눈에 파악 (YAML 프론트매터)
> - **목차** 펼치기 → 원하는 챕터를 즉시 탐색 (SKILL.md 본문)
> - **본문** 열람 → 필요할 때만 세부 내용 확인 (연결된 참조 파일)
>
> 모든 내용을 한꺼번에 펼쳐두지 않아도 원하는 정보를 즉시 찾을 수 있는 것이 핵심입니다.

Skill은 3단계 구조를 사용합니다.

| 단계 | 로드 시점 | 역할 |
|---|---|---|
| **1단계 — YAML 프론트매터** | 항상 로드됨 | Claude의 시스템 프롬프트에 항상 포함. Skill 전체를 로드하지 않고도 어떤 상황에서 이 Skill을 써야 하는지 판단할 수 있는 최소 정보 제공. |
| **2단계 — SKILL.md 본문** | 관련성 판단 시 로드됨 | Claude가 현재 작업과 Skill이 관련 있다고 판단할 때 로드. 전체 지침과 안내 내용이 포함됨. |
| **3단계 — 연결된 파일** | 필요 시에만 탐색 | Skill 디렉토리 내 번들 파일들. Claude가 필요하다고 판단할 때만 탐색 및 발견. |

이 점진적 공개 방식은 **토큰 사용량을 최소화하면서도 전문적인 기능을 유지**하는 핵심 메커니즘입니다.

#### 2. 조합 가능성 (Composability)

Claude는 **여러 Skill을 동시에 로드**할 수 있습니다. 따라서 여러분의 Skill은 본인이 유일한 기능이라고 가정하지 말고, 다른 Skill과 함께 잘 동작하도록 설계해야 합니다.

#### 3. 이식성 (Portability)

Skill은 **Claude.ai, Claude Code, API 전반에서 동일하게 작동**합니다. 한 번 만든 Skill은 해당 Skill이 요구하는 의존성(Dependency)을 환경이 지원하는 한, 모든 환경에서 별도 수정 없이 사용 가능합니다.

---

### MCP 빌더를 위한 안내: Skills + Connectors

> 💡 MCP 없이 독립형 Skill을 구축 중이시라면? 이 섹션은 건너뛰고 Chapter 2로 이동하셔도 됩니다.

MCP 서버가 이미 잘 작동하고 있다면, 가장 어려운 부분은 이미 완료하신 겁니다. **Skill은 그 위에 쌓이는 지식 레이어**입니다.

**🍳 MCP:** 전문 주방 — 도구, 재료, 장비에 대한 접근 권한
**📖 Skill:** 레시피 — 무언가 가치 있는 것을 만들기 위한 단계별 지침

이 둘이 합쳐질 때, 사용자는 매 단계를 직접 파악할 필요 없이 복잡한 작업을 완수할 수 있습니다.

| MCP (연결성) | Skill (지식) |
|---|---|
| Claude를 서비스에 연결 (Notion, Asana, Linear 등) | Claude가 서비스를 효과적으로 사용하는 방법을 교육 |
| 실시간 데이터 접근 및 Tool 호출 기능 제공 | 워크플로우와 모범 사례를 캡처 |
| Claude가 **할 수 있는 것** | Claude가 **어떻게 해야 하는지** |

| ❌ Skill 없이 | ✅ Skill이 있으면 |
|---|---|
| MCP를 연결해도 다음에 무엇을 할지 모름 | 미리 구축된 워크플로우가 자동으로 활성화됨 |
| "이 연동으로 X를 어떻게 하나요?" 지원 티켓 폭증 | 일관되고 신뢰할 수 있는 Tool 사용 |
| 매 대화가 처음부터 시작됨 | 모든 상호작용에 모범 사례가 내재됨 |
| 사용자마다 결과 불일치 | 사용자의 연동 학습 곡선이 낮아짐 |

---

## Chapter 2: 기획 및 설계 (Planning and Design)

### 사용 사례(Use Case)부터 시작하세요

코드를 작성하기 전에, Skill이 지원해야 할 **구체적인 사용 사례 2~3개**를 먼저 정의하세요.
```yaml
Use Case: 프로젝트 스프린트 플래닝
Trigger: 사용자가 "스프린트 계획 도와줘" 또는 "스프린트 작업 만들어줘"라고 말할 때
Steps:
  1. MCP를 통해 Linear에서 현재 프로젝트 상태 가져오기
  2. 팀의 속도(velocity)와 가용 역량 분석
  3. 작업 우선순위 제안
  4. 적절한 레이블과 예상 시간으로 Linear에 작업 생성
Result: 작업이 생성된 완전한 스프린트 계획
```

Skill을 설계할 때 스스로에게 물어보세요.
- 사용자가 달성하고자 하는 것은 무엇인가?
- 이를 위해 어떤 다단계 워크플로우가 필요한가?
- 어떤 Tool이 필요한가? (내장 Tool인가, MCP Tool인가?)
- 어떤 도메인 지식이나 모범 사례를 내재화해야 하는가?

---

### 일반적인 Skill 사용 사례 카테고리

#### 카테고리 1: 문서 및 에셋 생성 (Document & Asset Creation)

| 항목 | 내용 |
|---|---|
| **사용 목적** | 문서, 프레젠테이션, 앱, 디자인, 코드 등 일관성 있고 고품질의 결과물 생성 |
| **실제 예시** | `frontend-design` Skill (`docx`, `pptx`, `xlsx` Skill도 참고) |
| **핵심 기술** | 스타일 가이드 및 브랜드 표준 내재화 / 일관된 출력을 위한 템플릿 구조 / 마무리 전 품질 체크리스트 / 외부 Tool 불필요 |

#### 카테고리 2: 워크플로우 자동화 (Workflow Automation)

| 항목 | 내용 |
|---|---|
| **사용 목적** | 일관된 방법론이 필요한 다단계 프로세스 처리. 여러 MCP 서버 간 조율 포함 |
| **실제 예시** | `skill-creator` Skill |
| **핵심 기술** | 검증 게이트(Validation Gate)가 있는 단계별 워크플로우 / 반복적 개선 루프 / 내장된 검토 및 개선 제안 |

#### 카테고리 3: MCP 강화 (MCP Enhancement)

| 항목 | 내용 |
|---|---|
| **사용 목적** | MCP 서버가 제공하는 Tool 접근 권한에 워크플로우 안내를 추가하여 강화 |
| **실제 예시** | `sentry-code-review` Skill (Sentry 제공) |
| **핵심 기술** | 여러 MCP 호출을 순서에 따라 조율 / 도메인 전문 지식 내재화 / 일반적인 MCP 오류 처리 로직 포함 |

---

### 성공 기준 정의하기

> ⚠️ 아래 기준들은 **목표치(Aspirational Target)**입니다. 정확한 임계값이 아닌 대략적인 벤치마크로 활용하세요.

**정량적 지표:**

| 지표 | 목표치 | 측정 방법 |
|---|---|---|
| 트리거 정확도 | 관련 쿼리의 90% 이상 | 관련 테스트 쿼리 10~20개 실행. 자동 로드 vs. 명시적 호출 횟수 추적 |
| 워크플로우당 Tool 호출 수 | 사전 정의한 X회 이내 | Skill 유무에 따른 동일 작업 비교. Tool 호출 수와 총 소비 토큰 집계 |
| API 호출 실패 수 | 0건 | 테스트 실행 중 MCP 서버 로그 모니터링 |

**정성적 지표:**

| 지표 | 평가 방법 |
|---|---|
| 사용자가 다음 단계를 별도로 프롬프팅하지 않아도 됨 | 테스트 중 리디렉션이나 재설명이 필요한 빈도를 기록 |
| 사용자 수정 없이 워크플로우 완료 | 동일 요청을 3~5회 실행. 구조적 일관성 및 품질 비교 |
| 세션 간 일관된 결과 | 새로운 사용자가 최소한의 안내로 첫 시도에 작업을 완수할 수 있는가? |

---

### 기술 요구사항 (Technical Requirements)

#### 파일 구조
```
your-skill-name/
├── SKILL.md            # 필수 — 메인 Skill 파일
├── scripts/            # 선택 — 실행 가능한 코드
│   ├── process_data.py # 예시
│   └── validate.sh     # 예시
├── references/         # 선택 — 참조 문서
│   ├── api-guide.md    # 예시
│   └── examples/       # 예시
└── assets/             # 선택 — 템플릿 등 에셋
    └── report-template.md  # 예시
```

#### ⚠️ 반드시 지켜야 할 규칙

> **`SKILL.md`는 정확히 이 표기를 사용해야 합니다 (대소문자 구분).** `SKILL.MD`, `skill.md` 등의 변형은 허용되지 않습니다.
```
✅ 올바른 예: notion-project-setup   (kebab-case)
❌ 잘못된 예: Notion Project Setup   (공백 포함 불가)
❌ 잘못된 예: notion_project_setup   (언더스코어 불가)
❌ 잘못된 예: NotionProjectSetup     (대문자 불가)
```

> ⚠️ Skill 폴더 내에 `README.md`를 포함하지 마세요. 모든 문서는 `SKILL.md` 또는 `references/` 폴더에 작성하세요. GitHub 배포 시 저장소 최상단에는 별도 README 작성 가능합니다.

---

### YAML 프론트매터: 가장 중요한 부분

**YAML 프론트매터는 Claude가 여러분의 Skill을 로드할지 말지를 결정하는 핵심 요소입니다.**

**최소 필수 형식:**
```yaml
---
name: your-skill-name
description: 이 Skill이 하는 일. 사용자가 [특정 문구]를 말할 때 사용.
---
```

**필드 요구사항:**

| 필드 | 필수 여부 | 설명 및 규칙 |
|---|---|---|
| `name` | **필수 ★** | kebab-case만 허용. 공백 및 대문자 금지. 폴더 이름과 일치 권장. |
| `description` | **필수 ★** | ① 무엇을 하는지 + ② 언제 사용하는지 반드시 포함. 1024자 이내. XML 태그 금지. |
| `license` | 선택 | 오픈소스 공개 시 사용. 예: MIT, Apache-2.0 |
| `compatibility` | 선택 | 1~500자. 환경 요구사항 명시 |
| `metadata` | 선택 | 임의 키-값 쌍. 권장 필드: author, version, mcp-server |
```yaml
metadata:
  author: ProjectHub        # 작성자 또는 팀 이름
  version: 1.0.0            # 현재 버전
  mcp-server: projecthub    # 연동 MCP 서버명
```

> ⚠️ **보안 제약사항:** 프론트매터에 XML 꺾쇠 괄호(`< >`)를 절대 사용하지 마세요. 이름에 `claude` 또는 `anthropic` 포함 불가 (예약어).

---

### 효과적인 Skill 작성법

#### description 필드 — 구성 구조

`[무엇을 하는지] + [언제 사용하는지] + [핵심 기능]`

**✅ 좋은 예시:**
```yaml
# 구체적이고 실행 가능한 표현
description: Figma 디자인 파일을 분석하여 개발자 핸드오프 문서를 생성합니다.
  사용자가 .fig 파일을 업로드하거나, "디자인 스펙", "컴포넌트 문서화",
  "디자인-코드 핸드오프"를 요청할 때 사용하세요.

# 트리거 표현 포함
description: Linear 프로젝트 워크플로우를 관리합니다.
  사용자가 "스프린트", "Linear 작업", "프로젝트 플래닝"을 언급할 때 사용하세요.

# 명확한 가치 제안
description: PayFlow의 종합 고객 온보딩 워크플로우.
  사용자가 "신규 고객 온보딩", "구독 설정"을 말할 때 사용하세요.
```

**❌ 나쁜 예시:**
```yaml
# 너무 모호함
description: 프로젝트를 도와줍니다.

# 트리거 조건 없음
description: 정교한 다중 페이지 문서 시스템을 생성합니다.

# 너무 기술적이고 사용자 트리거 없음
description: 계층적 관계를 가진 Project 엔티티 모델을 구현합니다.
```

#### 본문 지침 권장 구조
```markdown
---
name: your-skill
description: [여기에 description 작성]
---

# Skill 이름

## Step 1: [첫 번째 주요 단계]
해당 단계에서 발생하는 일에 대한 명확한 설명.
Expected output: [성공 시 어떤 결과가 나와야 하는지 설명]

## 예시 (Examples)
사용자 발화: "새 마케팅 캠페인 설정해줘"
수행 작업:
  1. MCP를 통해 기존 캠페인 조회
  2. 제공된 파라미터로 새 캠페인 생성
Result: 확인 링크와 함께 캠페인 생성 완료

## 문제 해결 (Troubleshooting)
오류: [일반적인 오류 메시지]
원인: [발생 이유]
해결책: [수정 방법]
```

#### 지침 작성 모범 사례

**1. 구체적이고 실행 가능하게 작성하기**
```
# ✅ 좋은 예
# 데이터 형식 검증을 위해 아래 명령을 실행하세요.
# python scripts/validate.py --input {filename}
# 검증 실패 시 일반적인 원인:
#   - 필수 필드 누락 (CSV에 해당 필드 추가 필요)
#   - 잘못된 날짜 형식 (YYYY-MM-DD 형식 사용)

# ❌ 나쁜 예
# 진행하기 전에 데이터를 검증하세요.
```

**2. 오류 처리 포함하기**
```
## MCP 연결 실패
"Connection refused" 오류가 발생하면:
  1. MCP 서버 실행 상태 확인: 설정 > 확장 프로그램
  2. API 키 유효성 확인
  3. 재연결 시도: 설정 > 확장 프로그램 > [서비스명] > 재연결
```

**3. 점진적 공개(Progressive Disclosure) 활용하기**
SKILL.md는 핵심 지침에만 집중하고, **상세 문서는 `references/` 폴더로 분리한 뒤 링크로 연결**하세요.

---

## Chapter 3: 테스트 및 반복 개선 (Testing and Iteration)

Skill은 목적과 노출 범위에 따라 다양한 수준의 엄밀성으로 테스트할 수 있습니다.

| 테스트 방식 | 방법 | 특징 |
|---|---|---|
| **수동 테스트** | Claude.ai에서 직접 쿼리 실행 및 동작 관찰 | 빠른 반복, 별도 설정 불필요 |
| **스크립트 테스트** | Claude Code에서 자동화된 테스트 케이스 실행 | 변경 사항에 대해 반복 검증 가능 |
| **프로그래밍 방식 테스트** | Skills API를 통해 평가 모음(Evaluation Suite) 구축 | 정의된 테스트 세트를 체계적으로 실행 |

> 💡 **프로 팁: 단일 작업부터 반복 개선 후 확장하세요**
> 가장 효과적인 Skill 제작자들은 까다로운 단일 작업에서 Claude가 성공할 때까지 반복 개선한 뒤, 그 성공 방식을 Skill로 추출합니다. 이 방식은 Claude의 인컨텍스트 학습(In-context Learning)을 활용하며, 광범위한 테스트보다 빠른 신호를 제공합니다. 작동하는 기반을 확보한 후, 다양한 테스트 케이스로 커버리지를 확장하세요.

---

### 권장 테스트 접근법

#### 1단계: 트리거 테스트 (Triggering Tests)

**목표:** Skill이 적절한 시점에 로드되는지 확인합니다.

- ✅ 명확한 작업에서 트리거됨
- ✅ 다르게 표현된 요청에서도 트리거됨
- ❌ 관련 없는 주제에서는 트리거되지 않음

**테스트 스위트(Test Suite) 예시:**
```
# 트리거되어야 하는 케이스
- "ProjectHub에 새 워크스페이스 설정해줘"
- "ProjectHub에서 프로젝트를 만들어야 해"
- "Q4 플래닝을 위해 ProjectHub 프로젝트 초기화해줘"

# 트리거되지 않아야 하는 케이스
- "샌프란시스코 날씨가 어때?"
- "Python 코드 작성 도와줘"
- "스프레드시트 만들어줘"
```

#### 2단계: 기능 테스트 (Functional Tests)

**목표:** Skill이 올바른 결과를 생성하는지 검증합니다.
```
테스트: 5개 작업이 있는 프로젝트 생성
Given: 프로젝트명 "Q4 Planning", 작업 설명 5개
When: Skill이 워크플로우를 실행할 때
Then:
  - ProjectHub에 프로젝트가 생성됨
  - 올바른 속성으로 작업 5개가 생성됨
  - 모든 작업이 프로젝트에 연결됨
  - API 오류 없음
```

#### 3단계: 성능 비교 테스트 (Performance Comparison)

| 측정 항목 | Skill 없이 | Skill 적용 시 |
|---|---|---|
| 사용자 지침 제공 방식 | 매번 직접 설명 필요 | 자동 워크플로우 실행 |
| 메시지 왕복 횟수 | 15회 | 2회 (명확화 질문만) |
| API 호출 실패 | 3건 (재시도 필요) | 0건 |
| 소비 토큰 수 | 12,000 토큰 | 6,000 토큰 |

---

### skill-creator Skill 활용하기

`skill-creator` Skill은 Claude.ai 플러그인 디렉토리 또는 Claude Code용 다운로드를 통해 사용할 수 있으며, Skill 구축과 반복 개선을 도와줍니다.

**Skill 생성:**
- 자연어 설명으로 Skill 생성
- 올바른 형식의 YAML 프론트매터가 포함된 `SKILL.md` 자동 생성
- 트리거 표현 및 구조 제안

**Skill 검토:**
- 모호한 description, 누락된 트리거, 구조적 문제 등 일반적인 이슈 감지
- 과소/과잉 트리거(Under/Overtriggering) 위험 식별
- Skill의 명시된 목적에 기반한 테스트 케이스 제안

**반복 개선:**
- Skill 사용 후 엣지 케이스나 실패 사례를 발견하면 skill-creator로 가져오세요.
- 예시: *"이 대화에서 발견된 이슈와 해결책을 바탕으로, [특정 엣지 케이스]를 처리하는 방식을 개선해 줘"*
```
사용 방법:
"skill-creator Skill을 사용하여 [사용 사례]에 맞는 Skill 구축을 도와줘"
```

> ⚠️ `skill-creator`는 Skill 설계 및 개선을 돕지만, 자동화된 테스트 스위트를 실행하거나 정량적 평가 결과를 산출하지는 않습니다.

---

### 피드백 기반 반복 개선 (Iteration based on Feedback)

Skill은 살아있는 문서입니다. 다음 신호를 기반으로 지속적으로 개선하세요.

#### 과소 트리거(Undertriggering) 신호

**증상:**
- Skill이 로드되어야 할 때 로드되지 않음
- 사용자가 수동으로 활성화하고 있음
- "언제 이 Skill을 사용하나요?"라는 지원 문의 발생

**해결책:** `description` 필드에 더 많은 세부 사항과 뉘앙스를 추가하세요. 특히 기술 용어에 대한 키워드를 보강하세요.

#### 과잉 트리거(Overtriggering) 신호

**증상:**
- 관련 없는 쿼리에서 Skill이 로드됨
- 사용자가 Skill을 비활성화하고 있음
- Skill의 목적에 대한 혼란 발생

**해결책:** 부정 트리거(Negative Trigger)를 추가하고, description을 더 구체적으로 작성하세요.

#### 실행 이슈(Execution Issues) 신호

**증상:**
- 일관성 없는 결과
- API 호출 실패
- 사용자의 수정이 필요한 상황

**해결책:** 지침을 개선하고 오류 처리 로직을 추가하세요.

---

## Chapter 4: 배포 및 공유 (Distribution and Sharing)

Skill은 MCP 연동을 더욱 완성도 있게 만들어 줍니다. Skill이 포함된 연동은 더 빠른 가치 제공 경로를 제시하며 MCP 단독 대안보다 경쟁 우위를 가집니다.

---

### 현재 배포 모델 (2026년 1월 기준)

**개인 사용자가 Skill을 설치하는 방법:**

1. Skill 폴더 다운로드
2. 폴더를 압축 파일(.zip)로 묶기 (필요 시)
3. Claude.ai의 설정 > 기능(Capabilities) > Skills에서 업로드
4. 또는 Claude Code의 Skills 디렉토리에 배치

**조직 수준의 Skill 배포:**
- **관리자가 워크스페이스 전체에 Skill을 배포**할 수 있습니다. (2025년 12월 18일 출시)
- 자동 업데이트
- 중앙 집중식 관리

---

### 오픈 표준 (An Open Standard)

Anthropic은 Agent Skills를 오픈 표준으로 공개했습니다. MCP와 마찬가지로, Skill은 도구와 플랫폼 간에 이식 가능해야 한다고 생각합니다. 동일한 Skill이 Claude나 다른 AI 플랫폼 어디서든 동작해야 합니다.

---

### API를 통한 Skill 활용

**주요 기능:**
- `/v1/skills` 엔드포인트를 통한 Skill 목록 조회 및 관리
- Messages API 요청에 `container.skills` 파라미터를 통해 Skill 추가
- Claude Console을 통한 버전 관리
- 커스텀 에이전트(Agent) 구축을 위한 Claude Agent SDK 연동

**API vs. Claude.ai 사용 기준:**

| 사용 사례 | 권장 환경 |
|---|---|
| 사용자가 Skill과 직접 상호작용 | Claude.ai / Claude Code |
| 개발 중 수동 테스트 및 반복 개선 | Claude.ai / Claude Code |
| 개인적·임시적 워크플로우 | Claude.ai / Claude Code |
| 프로그래밍 방식으로 Skill을 활용하는 애플리케이션 | API |
| 대규모 프로덕션 배포 | API |
| 자동화 파이프라인 및 에이전트 시스템 | API |

> ⚠️ API에서 Skill을 사용하려면 Code Execution Tool 베타 기능이 필요합니다.

---

### 권장 배포 방법 (Step by Step)

#### Step 1: GitHub에 호스팅하기
- 오픈소스 Skill을 위한 공개(Public) 저장소 생성
- 설치 방법이 포함된 명확한 README 작성 (저장소 최상단 레벨, Skill 폴더 안 아님)
- 사용 예시 및 스크린샷 포함

#### Step 2: MCP 저장소에 문서화하기
- MCP 문서에서 Skill로 링크 연결
- Skill과 MCP를 함께 사용할 때의 가치 설명
- 빠른 시작 가이드 제공

#### Step 3: 설치 가이드 작성하기
```markdown
# [서비스명] Skill 설치 방법

## 1. Skill 다운로드
- 저장소 클론: git clone https://github.com/yourcompany/skills
- 또는 Releases에서 ZIP 파일 다운로드

## 2. Claude에 설치
- Claude.ai > 설정 > Skills 열기
- "Skill 업로드" 클릭
- Skill 폴더 선택 (압축 파일 형태)

## 3. Skill 활성화
- [서비스명] Skill 토글 ON
- MCP 서버가 연결되어 있는지 확인

## 4. 테스트
- Claude에게 다음과 같이 말해보세요:
  "[서비스명]에 새 프로젝트 설정해줘"
```

---

### Skill 포지셔닝 전략

**결과 중심으로 표현하기:**
```
✅ 좋은 예:
"ProjectHub Skill을 사용하면 팀이 수동 설정에 30분을 쏟는 대신,
페이지, 데이터베이스, 템플릿이 포함된 완전한 프로젝트 워크스페이스를
단 몇 초 만에 구성할 수 있습니다."

❌ 나쁜 예:
"ProjectHub Skill은 YAML 프론트매터와 Markdown 지침이 포함된 폴더로,
우리 MCP 서버 Tool을 호출합니다."
```

**MCP + Skill 스토리 강조하기:**
```
"우리의 MCP 서버는 Claude에게 Linear 프로젝트 접근 권한을 줍니다.
우리의 Skill은 팀의 스프린트 플래닝 워크플로우를 Claude에게 가르칩니다.
이 둘이 합쳐지면 AI 기반 프로젝트 관리가 실현됩니다."
```

---

## Chapter 5: 패턴 및 트러블슈팅 (Patterns and Troubleshooting)

이 챕터의 패턴들은 얼리 어답터(Early Adopter)와 내부 팀이 구축한 Skill에서 도출되었습니다. **규범적인 템플릿이 아니라, 효과적인 것으로 검증된 공통 접근법**입니다.

---

### 접근 방식 선택: 문제 중심 vs. 도구 중심

> 💡 **홈디포(Home Depot) 비유:** 홈디포에 들어서는 방식은 두 가지입니다. "부엌 캐비닛을 고쳐야 해"라는 문제를 갖고 들어와 직원의 안내로 올바른 도구를 찾을 수도 있고, 새 드릴을 들고 와서 특정 작업에 어떻게 쓸지를 물어볼 수도 있죠. Skill도 마찬가지입니다.

| 접근 방식 | 설명 | 사용자 관점 |
|---|---|---|
| **문제 중심 (Problem-first)** | "프로젝트 워크스페이스를 설정해야 해" → Skill이 올바른 순서로 MCP 호출을 조율 | 결과를 설명하면, Skill이 도구를 알아서 처리 |
| **도구 중심 (Tool-first)** | "Notion MCP가 연결됐어" → Skill이 최적의 워크플로우와 모범 사례를 교육 | 접근 권한이 있고, Skill이 전문성을 제공 |

---

### 5가지 핵심 설계 패턴

#### 패턴 1: 순차적 워크플로우 조율 (Sequential Workflow Orchestration)

**사용 시점:** 사용자가 특정 순서로 진행해야 하는 다단계 프로세스가 필요할 때
```markdown
# 워크플로우: 신규 고객 온보딩

## Step 1: 계정 생성
MCP Tool 호출: `create_customer`
파라미터: name, email, company

## Step 2: 결제 수단 설정
MCP Tool 호출: `setup_payment_method`
대기 조건: 결제 수단 검증 완료

## Step 3: 구독 생성
MCP Tool 호출: `create_subscription`
파라미터: plan_id, customer_id (Step 1 결과값)

## Step 4: 환영 이메일 발송
MCP Tool 호출: `send_email`
템플릿: welcome_email_template
```

**핵심 기술:** 명시적 단계 순서 / 단계 간 의존성 / 각 단계 검증 / 실패 시 롤백(Rollback) 지침

---

#### 패턴 2: 다중 MCP 조율 (Multi-MCP Coordination)

**사용 시점:** 워크플로우가 여러 서비스에 걸쳐 있을 때
```markdown
# Phase 1: 디자인 익스포트 (Figma MCP)
1. Figma에서 디자인 에셋 익스포트
2. 디자인 스펙 문서 생성

# Phase 2: 에셋 보관 (Drive MCP)
1. Drive에 프로젝트 폴더 생성
2. 모든 에셋 업로드

# Phase 3: 작업 생성 (Linear MCP)
1. 개발 작업 생성
2. 에셋 링크 첨부

# Phase 4: 알림 발송 (Slack MCP)
1. #engineering 채널에 핸드오프 요약 게시
```

**핵심 기술:** 명확한 Phase 분리 / MCP 간 데이터 전달 / Phase 이전 검증 / 중앙 집중식 오류 처리

---

#### 패턴 3: 반복적 개선 (Iterative Refinement)

**사용 시점:** 반복을 통해 출력 품질이 향상되는 작업일 때
```markdown
# 반복적 보고서 생성

## 초안 작성
1. MCP를 통해 데이터 수집
2. 첫 번째 초안 보고서 생성

## 품질 검사
1. 검증 스크립트 실행: `scripts/check_report.py`
2. 이슈 식별: 누락된 섹션 / 포맷 오류 / 데이터 오류

## 개선 루프
1. 각 이슈 해결
2. 영향받은 섹션 재생성
3. 재검증 → 품질 기준 충족 시까지 반복

## 최종화
1. 최종 포맷 적용
2. 최종 버전 저장
```

**핵심 기술:** 명시적 품질 기준 / 검증 스크립트 / 반복 종료 조건 명확화

---

#### 패턴 4: 컨텍스트 인식 Tool 선택 (Context-aware Tool Selection)

**사용 시점:** 동일한 결과를 달성하는 방법이 컨텍스트에 따라 달라질 때
```markdown
# 스마트 파일 저장

## 결정 트리
1. 파일 유형과 크기 확인
2. 최적 저장 위치 결정:
   - 대용량 파일 (10MB 초과): 클라우드 스토리지 MCP
   - 협업 문서: Notion/Docs MCP
   - 코드 파일: GitHub MCP
   - 임시 파일: 로컬 저장

## 저장 실행
- 적절한 MCP Tool 호출
- 서비스별 메타데이터 적용
- 접근 링크 생성

## 사용자에게 컨텍스트 제공
해당 저장 방식을 선택한 이유를 설명
```

**핵심 기술:** 명확한 결정 기준 / 폴백(Fallback) 옵션 / 선택 이유 투명하게 공개

---

#### 패턴 5: 도메인 특화 지식 내재화 (Domain-specific Intelligence)

**사용 시점:** Skill이 단순 Tool 접근을 넘어 전문적 지식을 추가해야 할 때
```markdown
# 컴플라이언스가 적용된 결제 처리

## 처리 전 (컴플라이언스 확인)
1. MCP를 통해 거래 상세 정보 조회
2. 컴플라이언스 규칙 적용:
   - 제재 목록 확인
   - 관할권 허용 여부 검증
   - 리스크 수준 평가
3. 컴플라이언스 결정 문서화

## 처리
컴플라이언스 통과 시: 결제 처리 MCP Tool 호출
컴플라이언스 실패 시: 검토 플래그 지정 및 컴플라이언스 케이스 생성

## 감사 로그 (Audit Trail)
- 모든 컴플라이언스 확인 기록
- 처리 결정 기록
- 감사 보고서 생성
```

**핵심 기술:** 도메인 전문성을 로직에 내재화 / 행동 전 컴플라이언스 확인 / 포괄적 문서화 / 명확한 거버넌스(Governance)

---

### 트러블슈팅 가이드 (Troubleshooting Guide)

#### 🔴 Skill 업로드 오류

| 현상 | 원인 | 해결책 |
|---|---|---|
| `"Could not find SKILL.md in uploaded folder"` | 파일명이 정확히 `SKILL.md`가 아님 | 파일명을 `SKILL.md`로 변경 (대소문자 구분). `ls -la`로 확인 |
| `"Invalid frontmatter"` | YAML 포맷 오류 | 아래 공통 실수 패턴 참고 |
| `"Invalid skill name"` | 이름에 공백 또는 대문자 포함 | kebab-case로 변경 (예: `my-cool-skill`) |

**YAML 포맷 공통 실수:**
```yaml
# ❌ 잘못된 예 — 구분자(Delimiter) 없음
name: my-skill
description: 뭔가를 합니다

# ❌ 잘못된 예 — 따옴표 미닫힘
name: my-skill
description: "뭔가를 합니다

# ✅ 올바른 예
---
name: my-skill
description: 뭔가를 합니다
---
```

---

#### 🟡 Skill이 트리거되지 않음

| 현상 | 원인 | 해결책 |
|---|---|---|
| Skill이 자동으로 로드되지 않음 | `description`이 너무 모호하거나 트리거 표현 부족 | description을 구체적으로 개선 |

**빠른 체크리스트:**
- `description`이 너무 일반적이지 않은가? ("프로젝트를 도와줍니다"는 동작하지 않음)
- 사용자가 실제로 말할 법한 트리거 표현이 포함되어 있는가?
- 관련 파일 형식이 있다면 명시되어 있는가?

> **디버깅 방법:** Claude에게 *"[Skill 이름] Skill을 언제 사용하시겠어요?"* 라고 물어보세요. Claude가 description을 그대로 인용합니다. 부족한 부분을 파악하고 수정하세요.

---

#### 🟡 Skill이 너무 자주 트리거됨

| 현상 | 해결책 |
|---|---|
| 관련 없는 쿼리에서도 Skill이 로드됨 | 부정 트리거(Negative Trigger) 추가 |
| 사용자가 Skill을 비활성화하고 있음 | description을 더 구체적으로 작성 |
| Skill 목적에 대한 혼란 | 적용 범위(Scope) 명확화 |

**부정 트리거 추가 예시:**
```yaml
description: 고급 데이터 분석 (CSV 파일 대상). 통계 모델링, 회귀분석,
  클러스터링에 사용하세요. 단순 데이터 탐색에는 사용하지 마세요
  (data-viz Skill을 사용하세요).
```

---

#### 🔴 MCP 연결 이슈

| 현상 | 확인 항목 | 해결책 |
|---|---|---|
| Skill은 로드되나 MCP 호출 실패 | MCP 서버 연결 상태 | 설정 > 확장 프로그램 > "Connected" 상태 확인 |
| | 인증(Authentication) 오류 | API 키 유효성 및 만료 여부 확인, OAuth 토큰 갱신 |
| | Tool 이름 불일치 | Skill에서 참조하는 MCP Tool 이름 확인 (대소문자 구분) |

> **MCP 독립 테스트:** Skill 없이 MCP를 직접 호출해 보세요. *"[서비스] MCP를 사용해서 내 프로젝트를 가져와줘"* — 이것도 실패한다면, 문제는 Skill이 아닌 MCP 자체에 있습니다.

---

#### 🟡 지침이 따라지지 않음

| 현상 | 원인 | 해결책 |
|---|---|---|
| Skill은 로드되나 지침을 무시함 | 지침이 너무 장황함 | 간결하게 유지. 상세 참조 자료는 별도 파일로 분리 |
| | 중요 지침이 묻혀 있음 | 핵심 지침을 상단에 배치. `## 중요` 헤더 사용 |
| | 모호한 표현 | 명확하고 단호한 언어 사용 (아래 예시 참고) |

**모호한 표현 개선 예시:**
```markdown
# ❌ 나쁜 예
진행하기 전에 항목들을 올바르게 검증하세요.

# ✅ 좋은 예
필수: create_project를 호출하기 전에 반드시 확인하세요:
- 프로젝트 이름이 비어 있지 않을 것
- 팀원이 최소 1명 이상 지정될 것
- 시작 날짜가 과거가 아닐 것
```

**모델 독려 문구:**
```markdown
# 성능 참고사항
- 이 작업을 충분한 시간을 들여 철저히 수행하세요
- 속도보다 품질이 중요합니다
- 검증 단계를 건너뛰지 마세요
```

> ⚠️ **고급 기법:** 핵심 검증 작업의 경우, 언어 지침에 의존하는 대신 검사를 프로그래밍 방식으로 수행하는 스크립트를 번들로 포함하는 것을 고려하세요. 코드는 결정론적(Deterministic)이지만, 언어 해석은 그렇지 않습니다.

---

#### 🟡 대규모 컨텍스트 이슈

| 현상 | 원인 | 해결책 |
|---|---|---|
| Skill이 느리거나 응답 품질 저하 | SKILL.md 파일이 너무 큼 | 상세 문서를 `references/`로 이동. SKILL.md를 5,000단어 이내로 유지 |
| | 너무 많은 Skill이 동시에 활성화됨 | 20~50개 이상 동시 활성화 여부 검토. 관련 기능별 Skill "팩(Pack)" 구성 고려 |
| | 모든 컨텍스트가 한꺼번에 로드됨 | 점진적 공개(Progressive Disclosure) 구조 활용 |

---

## Chapter 6: 리소스 및 참조 자료 (Resources and References)

> 💡 처음 Skill을 구축하신다면, **모범 사례 가이드(Best Practices Guide)** 부터 시작한 후 필요에 따라 API 문서를 참고하세요.

---

### 공식 문서 (Official Documentation)

**Anthropic 공식 리소스:**

| 리소스 | 용도 |
|---|---|
| **Best Practices Guide** | Skill 구축 모범 사례 총람. 처음 시작할 때 필독 |
| **Skills Documentation** | Skill 공식 기술 문서. 구조·규격 레퍼런스 |
| **API Reference** | API 엔드포인트 및 파라미터 상세. 프로그래밍 방식 활용 시 참고 |
| **MCP Documentation** | MCP 서버 연동 기술 가이드. MCP 기반 Skill 구축 시 필수 |

**블로그 포스트:**

| 포스트 | 내용 요약 |
|---|---|
| **Introducing Agent Skills** | Agent Skills 공개 발표 및 개요 |
| **Engineering Blog: Equipping Agents for the Real World** | Anthropic 엔지니어링팀의 Skill 설계 철학 |
| **Skills Explained** | Skill 개념과 구조에 대한 심층 설명 |
| **How to Create Skills for Claude** | Skill 제작 단계별 실전 가이드 |
| **Building Skills for Claude Code** | Claude Code 환경에서의 Skill 구축법 |
| **Improving Frontend Design through Skills** | 프론트엔드 디자인 Skill 적용 사례 |

---

### 예제 Skill (Example Skills)

| 저장소 | 내용 | 활용법 |
|---|---|---|
| **GitHub: anthropics/skills** | Anthropic이 직접 제작한 공식 Skill 모음 | 커스터마이징하거나 템플릿으로 활용 |
| **Document Skills** | PDF, DOCX, PPTX, XLSX 생성 Skill | 문서 작업 자동화의 출발점 |
| **Example Skills** | 다양한 워크플로우 패턴 예제 | 패턴별 실제 구현 참고 |
| **Partner Skills Directory** | Asana, Atlassian, Canva, Figma, Sentry, Zapier 등 | 실제 서비스 연동 Skill 참고 |

---

### 도구 및 유틸리티 (Tools and Utilities)

| 항목 | 내용 |
|---|---|
| **접근 방법** | Claude.ai 내장 또는 Claude Code용 다운로드 |
| **주요 기능** | 설명으로부터 Skill 생성, 검토 및 개선 권장사항 제공 |
| **사용 방법** | `"skill-creator를 사용해서 Skill 만드는 것을 도와줘"` |
| **검토 요청** | `"이 Skill을 검토하고 개선 사항을 제안해줘"` |

---

### 지원 채널 (Getting Support)

| 용도 | 채널 |
|---|---|
| **기술적 질문** | Claude Developers Discord 커뮤니티 포럼 |
| **버그 리포트** | GitHub Issues: `anthropics/skills/issues` |

**버그 리포트 시 포함할 정보:** Skill 이름 / 오류 메시지 전문 / 재현 단계(Steps to Reproduce)

---

## 참고 자료 A: 빠른 체크리스트 (Quick Checklist)

### 시작 전
- [ ] 구체적인 사용 사례 2~3개 정의 완료
- [ ] 필요한 Tool 식별 (내장 또는 MCP)
- [ ] 이 가이드 및 예제 Skill 검토 완료
- [ ] 폴더 구조 계획 수립

### 개발 중
- [ ] 폴더명이 kebab-case로 작성됨
- [ ] `SKILL.md` 파일이 존재함 (정확한 철자)
- [ ] YAML 프론트매터에 `---` 구분자 포함
- [ ] `name` 필드: kebab-case, 공백 없음, 대문자 없음
- [ ] `description`에 WHAT과 WHEN 모두 포함
- [ ] XML 태그 (`< >`) 미포함
- [ ] 지침이 명확하고 실행 가능함
- [ ] 오류 처리 포함
- [ ] 예시 제공
- [ ] 참조 파일이 명확히 링크됨

### 업로드 전
- [ ] 명확한 작업에서 트리거 테스트 완료
- [ ] 다르게 표현된 요청에서도 트리거 테스트 완료
- [ ] 관련 없는 주제에서 트리거되지 않음 확인
- [ ] 기능 테스트 통과
- [ ] Tool 연동 동작 확인 (해당 시)
- [ ] `.zip` 파일로 압축 완료

### 업로드 후
- [ ] 실제 대화에서 테스트
- [ ] 과소/과잉 트리거 모니터링
- [ ] 사용자 피드백 수집
- [ ] description 및 지침 반복 개선
- [ ] 메타데이터의 버전 업데이트

---

## 참고 자료 B: YAML 프론트매터 레퍼런스

### 최소 필수 형식
```yaml
---
name: skill-name-in-kebab-case
description: 무엇을 하는지, 언제 사용하는지. 구체적인 트리거 표현 포함.
---
```

### 모든 선택 필드 포함 형식
```yaml
name: skill-name
description: [필수 description]
license: MIT                              # 선택: 오픈소스 라이선스
allowed-tools: "Bash(python:*) Bash(npm:*) WebFetch"  # 선택: Tool 접근 제한
metadata:                                 # 선택: 커스텀 필드
  author: Company Name                    # 작성자 또는 팀 이름
  version: 1.0.0                          # 현재 버전
  mcp-server: server-name                 # 연동 MCP 서버명
  category: productivity                  # 카테고리 분류
  tags: [project-management, automation]  # 검색용 태그
  documentation: https://example.com/docs # 문서 링크
  support: support@example.com            # 지원 이메일
```

### 보안 규칙 요약

| 허용 | 금지 |
|---|---|
| 모든 표준 YAML 타입 (문자열, 숫자, 불리언, 리스트, 객체) | XML 꺾쇠 괄호 (`< >`) |
| 커스텀 메타데이터 필드 | YAML 내 코드 실행 |
| 최대 1,024자 description | `claude` 또는 `anthropic` 접두사 이름 |

---

## 참고 자료 C: 완성 예제 Skill 모음

| 저장소 | 포함 내용 |
|---|---|
| **Document Skills** | PDF, DOCX, PPTX, XLSX 생성 Skill |
| **Example Skills** | 다양한 워크플로우 패턴 예제 |
| **Partner Skills Directory** | Asana, Atlassian, Canva, Figma, Sentry, Zapier 등 파트너 Skill |

> 💡 저장소를 클론하거나, 여러분의 사용 사례에 맞게 수정하여 템플릿으로 활용하세요. 이 저장소들은 지속적으로 업데이트되며 가이드에 수록된 것보다 더 많은 예제가 포함되어 있습니다.

---

## 성공적인 Claude Skill 구축을 위한 핵심 원칙 10

### 원칙 1. 사용 사례를 먼저, 코드는 나중에
코드를 작성하기 전에 Skill이 해결해야 할 **구체적인 사용 사례 2~3개를 먼저 정의**하세요. "무엇을 만들 것인가"보다 "누가, 어떤 상황에서 무엇을 원하는가"를 먼저 답하는 Skill이 언제나 더 효과적입니다.

### 원칙 2. description은 Skill의 얼굴이다
`description` 필드는 단순한 설명이 아니라 **Claude가 Skill을 사용할지 결정하는 판단 근거**입니다. 무엇을 하는지(WHAT)와 언제 쓰는지(WHEN)를 반드시 포함하고, 사용자가 실제로 말할 법한 트리거 표현을 구체적으로 넣으세요.

### 원칙 3. 점진적 공개로 토큰을 절약하라
**모든 정보를 SKILL.md에 몰아넣지 마세요.** 핵심 지침은 SKILL.md에, 상세 문서는 `references/` 폴더로 분리하고 링크로 연결하세요. SKILL.md는 5,000단어 이내가 이상적입니다.

### 원칙 4. 구체적이고 실행 가능하게 작성하라
"잘 검증하세요"가 아니라 **"검증 스크립트를 실행하고, 실패 시 이 세 가지를 확인하세요"** 처럼 작성하세요. Claude는 모호한 지침보다 명확하고 단계적인 지침을 훨씬 잘 따릅니다.

### 원칙 5. 오류 처리를 처음부터 설계하라
행복 경로(Happy Path)만 설계하지 마세요. **MCP 연결 실패, API 오류, 엣지 케이스에 대한 처리 로직**을 처음부터 Skill에 포함하세요. 실무에서 오류는 예외가 아니라 일상입니다.

### 원칙 6. 단일 작업에서 먼저 성공하라
처음부터 모든 경우를 커버하려 하지 마세요. **가장 까다로운 단일 작업에서 Claude가 성공할 때까지 반복 개선**한 후, 그 방식을 Skill로 추출하고 범위를 확장하세요.

### 원칙 7. MCP와 Skill은 분리된 역할이다
MCP는 "무엇을 할 수 있는가(접근 권한)", Skill은 "어떻게 해야 하는가(워크플로우)"입니다. **좋은 MCP가 있어도 Skill 없이는 사용자가 매번 처음부터 시작**합니다. 이 두 레이어를 명확히 구분하고 함께 설계하세요.

### 원칙 8. 트리거를 지속적으로 모니터링하라
Skill은 출시 후에도 살아있는 문서입니다. **과소 트리거와 과잉 트리거** 신호를 지속적으로 모니터링하고, description을 반복 개선하세요.

### 원칙 9. 결과로 말하고 기능을 설명하지 마라
사용자에게 Skill을 소개할 때, "YAML 프론트매터와 Markdown 지침이 포함된 폴더"라고 설명하지 마세요. **"30분 걸리던 워크스페이스 설정을 30초에 완료"** 처럼 구체적인 결과로 가치를 전달하세요.

### 원칙 10. 이식성을 전제로 설계하라
Claude.ai, Claude Code, API 어디서든 동일하게 작동하도록 설계하세요. 특정 환경에 의존하는 요소가 있다면 `compatibility` 필드에 명시하세요. **한 번 만든 Skill은 모든 환경에서 동작**하는 것이 이상적인 목표입니다.

---

*번역 기준일: 2026년 3월 | 용어집 v1.0 기준 | 원문: Anthropic, "The Complete Guide to Building Skills for Claude"*