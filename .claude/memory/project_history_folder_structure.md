---
name: history 폴더 구조
description: knowledge-hub wiki의 history/ 디렉토리 내부 구조 — uwo/는 없고 people/events/places/themes/concepts/ 직접 배치
type: project
originSessionId: 8d84ee16-5027-4991-86ba-601d71c51a58
---
`content/wiki/history/` 아래 서브폴더 구조 (2026-05-15 리팩터링):

```
history/
├── people/     인물
├── events/     사건·원정·전투
├── places/     장소·번·성곽
├── themes/     개념·유물·비교
├── concepts/   제도·시스템
├── moc.md
└── publish_log.md
```

**Why:** 원래 `history/uwo/` 중간 계층이 있었으나 UWO 전용이 아니라 역사 리서치 전반을 담는 허브였음. 계층 불필요 판단하여 제거.

**How to apply:** 새 history 페이지 생성 시 `history/[타입폴더]/파일명.md`로 직접 저장. `history/uwo/`는 더 이상 존재하지 않음.
