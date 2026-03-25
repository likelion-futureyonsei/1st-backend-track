# 🦁 멋쟁이사자처럼 대학 연세미래 1기  
## 백엔드 트랙 과제 제출 가이드

과제는 아래 순서에 맞춰 브랜치를 생성하고,  
**본인 브랜치 기준으로 Pull Request(PR)** 를 보내면 됩니다.

---

## 1. 본인 브랜치 만들기

처음 한 번만, `main` 브랜치에서 **본인의 GitHub 아이디**로 브랜치를 생성합니다.

```bash
git checkout main
git pull origin main
git switch -c {username}      # 예: git switch -c likelion26
git push origin {username}    # 예: git push origin likelion26
```

## 2. 과제용 브랜치 만들기

과제를 시작할 때는 **본인 브랜치에서 새로운 과제 브랜치**를 만들어 작업합니다.

```bash
git switch {username}                 # 본인 브랜치로 이동
git switch -c {username}/{assignment} # 예: git switch -c likelion26/basic
```

브랜치 이름은 아래 형식을 따라주세요.

```bash
{username}/{assignment}
```

예시:
- `likelion26/basic`
- `likelion26/crud`
- `likelion26/orm`

## 3. 작업 후 PR 보내기

과제를 완료했다면 GitHub에서 아래 방향으로 Pull Request를 생성합니다.

```bash
{username}/{assignment} → {username}
```

예시:
```bash
likelion26/profile → likelion26
```

> **주의:** `main` 브랜치로 직접 PR을 보내지 않도록 꼭 확인해주세요.

## 제출 흐름 한눈에 보기

```bash
main
 └─ {username}
     └─ {username}/{assignment}
```

즉,

1. `main`에서 본인 브랜치 생성  
2. 본인 브랜치에서 과제 브랜치 생성  
3. 과제 브랜치에서 작업 후 본인 브랜치로 PR 생성

이 순서로 진행하면 됩니다.

## 참고 자료

- [(무료) 매우 쉽게 알려주는 Git & GitHub](https://codingapple.com/course/git-and-github/)

---

## 과제 목록
| 과제 명 | 브랜치 명 | 강의 날짜 |
|---|---|---|
| 변수, 조건문, 반복문, 함수, 콘솔 입출력 | basic | 260326 |
