
### 📓 프로젝트 개요
- 설명 : 숏츠를 활용한 영화 추천 서비스
- 기간 : 2024.11.18(월) ~ 2023.11.26(화)

### 🦝 서비스 특징

- 숏츠 형태로 영화 예고편을 제시하여 유저가 영화를 추천받음
- DQN을 활용하여 최적의 영화를 짧은 시간안에 추천받을 수 있음
 
### ⚙ 주요 기능

- 영화 정보
- 해당 영화의 예고편
- DQN을 활용한 영화 추천

### 🦾 팀 소개 
| 이상화 | 윤수한 |
| ------ | ------ |
| 팀장, Backend | 팀원, Frontend |

## 🛒 기술 스택

### Backend
![Django](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=django&logoColor=white)&nbsp;
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)&nbsp;
![sqlite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=nodedotjs&logoColor=white)&nbsp;

### Frontend
![Vue.js](https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)&nbsp;
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)&nbsp;
![sass](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)&nbsp;
![Vuetify](https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=white)&nbsp;

### Tools
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)&nbsp;
![VS code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)&nbsp;
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)&nbsp;

<br />

## 🔧 개발 환경

**Backend**
- django 4.2.4

**Frontend**
- vue.js 3.3.4

<br/>

## 💿 프로젝트 폴더 구조

- Backend - Django
```
django_project
├─accounts
├─articles
├─ml
├─movies
└─my_django_project
```

- Frontend - Vue.js
```
vue_project
├─.vscode
├─node_modules
├─public
└─src
    ├─assets
    ├─components
    ├─router
    ├─stores
    └─views
        ├─ShortsPage.vue
        ├─signupPage.vue
        ├─communityPage.vue
        ├─LoginPage.vue
        └─etc..
```

<br/>

### 🖱 코드 컨벤션

<details>
<summary><b>명명법</b></summary> 

- 프론트엔드
    - 변수명, 메서드명
        - `camelCase`
    - HTML 템플릿
        - `kebab-case`
    - CSS 클래스
        - 고유한 클래스명 부여하여 부모 컴포넌트 내의 속성 상속을 방지
    - 의미없는 변수명 사용 지양

- 백엔드
    - 클래스명
        - `PascalCase`
    - 함수명
        - `snake_case`
    - 의미없는 변수명 사용 지양
</details>

<br/>

## 🔈 기능 상세 설명
### 메인페이지
- 숏츠를 통해 유저 직관적으로 영화를 추천
- 왼쪽에 네비게이션 바를 통해 다른 페이지 이동가능

<br />
   
### 마이 페이지

- 유저가 각 숏츠를 얼마나 시청했는지 확인할 수 있음
- 유저가 자신이 작성한 커뮤니티 내용을 확인할 수 있음
- 유저가 숏츠에 남긴 댓글을 영화 포스터와 함께 남길 수 있음

<br />

### 커뮤니티 게시판
- 무비클립 유저들 간의 영화 지식 공유가 가능한 공간
- 댓글 기능을 통해 의견을 나눌 수 있음
- 로그인한 사용자만 조회와 게시가 가능하여 exclusive한 경험 제공
  
<br />

### 회원 페이지

- 회원 가입을 통해 닉네임을 설정하고 커뮤니티 게시판 사용이 가능
- 회원정보 조회 및 수정, 비밀번호 변경, 로그아웃 기능 포함

<br />

## API 입력 위치
```
django_project/.env
TMDB_API_KEY= ""
YOUTUBE_API_KEY= ""
```
