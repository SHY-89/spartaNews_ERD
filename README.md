# SpartaNews_ERD

## 프로젝트 소개

### [GOOD NEWS]
스파르타 코딩 클럽 부트캠프를 통해 진행된 팀 프로젝트인 '굿 뉴스'는 최신 뉴스와 정보를 제공하는 플랫폼입니다.
본 프로젝트에서는 Django REST Framework(DRF), Serializer, APIView 등을 활용하여 백엔드 기능을 구현하였습니다.

프론트엔드는 개발하지 않고 백엔드에 집중하여, 사용자들이 뉴스 기사를 효율적으로 조회하고 관리할 수 있는 API를 구축하였으며, API 문서를 생성하여 개발자들이 API의 사용법을 쉽게 이해할 수 있도록 하였습니다.
      

## 프로젝트 기능
    - 회원
        - 회원 가입
            - 아이디(username)
            - 비밀번호(password)
            - 비밀번호 확인(password_ok)
        - 로그인
            - 아이디
            - 비밀번호
        - 로그아웃
        - 회원 정보 수정
            - 아이디 노출
            - 가입일 노출
            - Karam(point) 노출
            - 소개 노출 & 수정 가능
            - 비밀번호 재설정
                - 패스워드 검증 없이 수정 가능
            - 이메일 노출 & 수정가능 & 인증

    - 게시판
        - 전체 목록 조회
            - 제목 + 링크
            - 상세내용
            - 투표 수
            - 작성자
            - 시간(1일전...)
            - 댓글 수
            - 뉴스 투표 하기
        -
        - 뉴스 등록
            - 제목
            - 링크
            - 카테고리
            - 내용

        - 뉴스 상세 조회
            - 제목, 링크
            - 투표 수, 작성자
            - 즐겨찾기
            - 댓글 수
            - 상세내용
            - 뉴스 즐겨찾기
            - 댓글 목록
        - 뉴스 수정
            - 제목
            - 링크
            - 카테고리
            - 내용
        - 뉴스 삭제
        - 댓글
            - 댓글 조회
                - 내용
                - 작성자
                - 시간
            - 댓글 등록
                - 내용
            - 댓글 삭제
            - 댓글 즐겨찾기
            - 댓글 투표하기
            - 대댓글 등록

## ERD
![ERD](doc/images/News.drawio.png)

## 개발 기간  예정기한
> **Dead Line**   
2024-09-11 ~ 2024-09-20

> **Sprint**   
2024-09-11 ~ 2024-09-16

## 개발 환경 및 사용 기술
    IDE : VSCODE
    Windows 10, 11  ,   MacOS
    Python 3.10.14
    Django 4.2
    django-seed 0.3.1 
    djangorestframework 3.15.2 
    djangorestframework-simplejwt 5.3.1
    requests==2.32.3
    bs4==0.0.2
    beautifulsoup4==4.12.3
    
## API Reference

### 회원

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **응답**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| POST       | /api/accounts/signup   | 회원 가입                       | `username`, `password`, `password_ok`  | JSON        |
| POST       | /api/accounts/login      | 로그인                           | `username`, `password`                 | JSON        |
| POST       | /api/accounts/logout     | 로그아웃                         | 없음                                   | JSON        |
| GET        | /api/accounts/profile/<str:username>/     | 회원 정보 조회      | 없음                | JSON        |
| PATCH        | /api/accounts/profile/<str:username>/     | 회원 정보 수정    | `introduction`, `email`, `password` , `password_ok`                 | JSON        |
| POST        | /api/accounts/send-email/     | 메일전송    | 없음                | JSON        |
| GET        | /activate/<str:uid64>/<str:token>/     | 이메일 인증    | 없음                | JSON        |

### 게시판

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **응답**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| GET        | /api/news/            | 전체 목록 조회                   | 없음                                   | JSON        |
| POST       | /api/news/            | 뉴스 등록                        | `title`, `link`, `category`, `content` | JSON        |
| GET        | /api/news/<int:news_id>/       | 뉴스 상세 조회                   | 없음                                   | JSON        |
| PUT        | /api/news/<int:news_id>/       | 뉴스 수정                        | `title`, `link`, `category`, `content` | JSON        |
| DELETE     | /api/news/<int:news_id>/       | 뉴스 삭제                        | 없음                                   | JSON        |
| POST       | /api/news/<int:news_id>/vote | 뉴스 추천하기               | 없음                                   | JSON        |
| POST       | /api/news/<int:news_id>/favorite | 뉴스 즐겨찾기하기               | 없음                                   | JSON        |

### 댓글

| **메소드** | **엔드포인트**            | **설명**                          | **요청 본문**                           | **응답**     |
|------------|--------------------------|----------------------------------|----------------------------------------|-------------|
| GET        | /api/news/<int:news_id>/comment/ | 댓글 조회                      | 없음                                   | JSON        |
| POST       | /api/news/<int:news_id>/comment/ | 댓글 등록                      | `content`                              | JSON        |
| DELETE     | /api/news/comments/<int:coment_id>/    | 댓글 삭제                        | 없음                                   | JSON        |
| POST     | /api/news/comments/<int:coment_id>/    | 대댓글 등록                        | `content`                                   | JSON        |
| POST       | /api/news/comment/<int:comment_id>/favorite/ | 댓글 즐겨찾기               | 없음                                   | JSON        |
| POST       | /api/news/comment/<int:comment_id>/vote/ | 댓글 투표하기                  | 없음                                   | JSON        |

### API 문서
- https://www.notion.so/teamsparta/66da1b2b732a436e8eff3841a0c77b74?v=aff2525f9dda4af6828b9f99577b71c4
