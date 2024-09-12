# SpartaNews_ERD

## 프로젝트 소개
    -

## 프로젝트 기능
    - 게시판 (누구나 이용가능)
        - 제목 + 링크
        - 상세내용
        - 투표 수
        - 작성자
        - 시간(1일전...)
        - 댓글 수

    - 게시판 상세(누구나 이용가능)
        - 제목, 링크
        - 투표 수, 작성자
        - 즐겨찾기
        - 댓글 수
        - 상세내용
        - 댓글 목록

    - 댓글(로그인한 사람)
        - 작성자
        - 시간

    - 로그인, 로그아웃
        - 회원가입
            -> 이용 가이드 노출

    - 회원 정보 수정
        - 아이디 노출
        - 가입일 노출
        - Karma 노출
        - 소개 수정
        - 비밀번호 재설정
        - 이메일, 인증
        - 작성한 글
        - 작성한 댓글
        - 즐겨찾기한 글

## ERD
![ERD](doc/images/News.drawio.png)

## 개발 기간
    2024-09-11 ~ 2024-09-

## 개발 환경 및 사용 기술
    IDE : VSCODE
    Windows 10, 11  ,   MacOS
    Python 3.10.14
    Django 4.2
    django-seed 0.3.1 
    djangorestframework 3.15.2 
    djangorestframework-simplejwt 5.3.1
    
## API Reference

### 회원

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **응답**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| POST       | /api/accounts/signup   | 회원 가입                       | `username`, `password`, `password_ok`  | JSON        |
| POST       | /api/accounts/login      | 로그인                           | `username`, `password`                 | JSON        |
| POST       | /api/accounts/logout     | 로그아웃                         | 없음                                   | JSON        |
| GET        | /api/accounts/profile/{username}/     | 회원 정보 조회      | 없음                | JSON        |
| PATCH        | /api/accounts/profile/{username}/     | 회원 정보 수정    | `introduction`, `email`, `password` , `password_ok`                 | JSON        |

### 게시판

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **응답**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| GET        | /api/news            | 전체 목록 조회                   | 없음                                   | JSON        |
| POST       | /api/news            | 뉴스 등록                        | `title`, `link`, `category`, `content` | JSON        |
| GET        | /api/news/{id}       | 뉴스 상세 조회                   | 없음                                   | JSON        |
| PUT        | /api/news/{id}       | 뉴스 수정                        | `title`, `link`, `category`, `content` | JSON        |
| DELETE     | /api/news/{id}       | 뉴스 삭제                        | 없음                                   | JSON        |
| POST       | /api/news/{id}/vote | 뉴스 투표하기               | 없음                                   | JSON        |

### 댓글

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **응답**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| GET        | /api/news/comments/{news_id} | 댓글 조회                      | 없음                                   | JSON        |
| POST       | /api/news/comments/{news_id} | 댓글 등록                      | `content`                              | JSON        |
| DELETE     | /api/news/comments/{id}    | 댓글 삭제                        | 없음                                   | JSON        |
| POST       | /api/news/comments/{id}/favorite | 댓글 즐겨찾기               | 없음                                   | JSON        |
| POST       | /api/news/comments/{id}/vote | 댓글 투표하기                  | 없음                                   | JSON        |