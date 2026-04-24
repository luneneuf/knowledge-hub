# 작업 지시서 — UWO-3
**대상 팀**: 개발팀 (Claude Code)  
**관련 이슈**: UWO-3  
**작업 유형**: 신규 블로그 글 3편 추가

---

## 작업 내용

아래 3개 파일을 `src/content/blog/` 디렉토리에 생성한다.

### 파일 1

**경로**: `src/content/blog/이사벨라-데스테-완전-정리.md`  
**내용**: 첨부된 `post1-이사벨라-데스테-완전-정리.md` 파일 전체

### 파일 2

**경로**: `src/content/blog/이사벨라-데스테-패션-유산.md`  
**내용**: 첨부된 `post2-이사벨라-데스테-패션-유산.md` 파일 전체

### 파일 3

**경로**: `src/content/blog/이사벨라-데스테-다빈치-소묘.md`  
**내용**: 첨부된 `post3-이사벨라-데스테-다빈치-소묘.md` 파일 전체

---

## 확인 사항

- frontmatter의 `draft: false` 확인 (세 파일 모두)
- 내부 링크 슬러그 확인:
  - 2편·3편 → 1편 링크: `/blog/이사벨라-데스테-완전-정리`
  - 외부 링크: `https://isabella-deste.vercel.app` (변경 없음)
- Astro content collection 스키마(`src/content.config.ts`)가 `pubDate` 필드를 Date 타입으로 받는지 확인. 현재 스키마와 충돌 시 `pubDate: "2026-04-13"` 문자열로 수정

---

## 커밋 및 배포

```bash
git add src/content/blog/이사벨라-데스테-완전-정리.md \
        src/content/blog/이사벨라-데스테-패션-유산.md \
        src/content/blog/이사벨라-데스테-다빈치-소묘.md
git commit -m "feat: 이사벨라 데스테 블로그 시리즈 3편 추가 (UWO-3)"
git push
```

Vercel 자동 배포 후 아래 URL에서 확인:
- https://chunsblog.vercel.app/blog/이사벨라-데스테-완전-정리
- https://chunsblog.vercel.app/blog/이사벨라-데스테-패션-유산
- https://chunsblog.vercel.app/blog/이사벨라-데스테-다빈치-소묘
