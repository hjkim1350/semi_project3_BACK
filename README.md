# gasliMBTIng (Semi project3 - Final)

> - 주변인들의 MBTI 정보 저장하고 MBTI 별 다양한 성격사례 소개하는 MBTI 백과사전 서비스
> - 배포 주소: https://www.gaslimbting.xyz/

![image](https://user-images.githubusercontent.com/108647811/218984118-b14e2023-b638-40b6-bf58-b249a1ee6738.png)

<br>

### 🔨 프로젝트 기간

* 2022.11.23(WED) ~ 2022.12.15(THU), **총 23일**

<br>

<div>
    <h3>📚 사용한 기술 STACKS</h3>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<br>
<img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
</div>

### 📌 **BackEnd**
- DRF(Django REST Framework)를 통한 REST API 구현 및 프론트엔드 통신

###📌 **FrontEnd**
- Vue.Cli를 활용한 전반적인 디자인 및 화면 설계/구현

<br>

### 😎 프로젝트 인원 구성
- 총 5명
- 담당 역할: 회원 custom DB 설계, 회원가입, 일반/카카오 로그인, 로그아웃 등 회원 관련 BackEnd 담당


<br>

### 🕶️ DRF 개념 및 프로젝트에 적용하기 위한 방법론
- 기존 코드와 차이점이 있다면 serializer가 새로이 도입되었음. 이 serializer를 쓰는 이유는 웹에서 JSON 파일을 이용하여 다량의 데이터를 처리하기 때문에 이 데이터 양식을 맞추기 위함.
- DRF 유저/인증 방식은 JWT(JSON Web Token)을 채택함. 위에서 언급한 JSON 데이터 타입을 활용하기 위함.
- 그렇다면 왜 토큰을 이용해 이용하는가? 세션 방식도 존재하지만 토큰을 사용하는 이유는 서버에 사용자의 인증으로 인한 과부하를 막기 위한 방식이 아닐까함. 세션과 다르게 토큰 방식은 서버에서 토큰을 발급해주면 사용자의 웹브라우저에 저장하여 사용자가 웹사이트 접근 시 서버에 제시하는 '입장권' 같은 개념임.
- 이러한 상황으로 DRF에서는 djangorestframework-simplejwt 패키지를 배포하기도 함.
- 단, 프로젝트 기간이 짧다는 점과 팀원들 모두 DRF와 Vue를 처음 접한다는 환경적 제약사항으로 클론코딩을 하기로 하였고 인증 패키지는 djoser 패키지를 활용하였음.

<br>

### ⚛️ 기능 설계

- **회원관리**
  - 회원가입
    - Input: 이메일, 닉네임, 비밀번호, 비밀번호 확인, 프로필 사진, 나이, 성별, MBTI
    - 나이의 경우 selectBox 적용
    - 성별, MBTI 정보의 경우 토글키를 이용하여 입력값 받음
  - 로그인
    - 이메일/PW 로그인, 소셜로그인(KaKao)
  - 로그아웃
    - 토큰 회수, 로그아웃 페이지 리다이렉션
  - 회원정보 수정
    - 프로필 사진 업로드, MBTI 정보/나이/성별 변경
  - 마이페이지
    - 타인이 익명으로 해당 회원에게 방명록을 남길 수 있도록 구현
    - 주변인들의 MBTI 저장 페이지에 저장한 MBTI를 분석하여 친구 분포도를 그래프화
  - 회원 탈퇴
    - 토큰 폐기 및 탈퇴 안내 메시지 출력
    - 탈퇴 회원 여부 확인을 위한 DB 내 1년 간 회원 정보 보관 및 1년 후 자동 파기
- ** 주변인들의 MBTI 저장 페이지 **
  - MBTI 정보 입력
    - Input: 이름, MBTI, 그룹 태그 지정
  - MBTI 정보 출력
    - 이름과 함께 MBTI 궁합도가 저장된 DB 정보를 가져와 나의 MBTI와 궁합이 잘맞는지를 색깔로 표현
- ** 사용자 커뮤니티 페이지 **
  - CRUD 구현: 글 생성, 수정, 삭제, 이미지 업로드 가능
  - 글쓴이 프로필 출력: 글쓴이 프로필 이미지, 글 작성 시간, MBTI 정보 출력
  - 댓글, 대댓글 구현: 댓글을 글쓴이가 쓴다면 (글쓴이)로 표현
- ** MBTI 정보 페이지 **
  - MBTI 성격 유형 별 정보 제공 페이지
  - 분류 버튼으로 카테고리 분류, 원하는 MBTI 유형별 게시글 필터


<br>

### 📁 주요 source 파일 트리구조

```text
1) Back-End
┌─📁 backend (프로젝트 - setting 파일)
├─📁 accounts (회원관리 App)
├─📁 community (사용자 커뮤니티 App)
├─📁 friends (주변인들의 MBTI 저장 App)
├─📁 guestbook (방명록 App)
├─📁 mbti (MBTI 정보 App)
├─🗒️ .gitignore (env, 가상환경 파일 git ignore)
└─🗒️ requirements.txt (pip 패키지 목록)
```

<br>

### ✅ 내가 담당한 기능

> **💻 Role - Backend: 회원 custom DB 설계, 회원가입, 일반/카카오 로그인, 로그아웃 등 전반적인 회원 관련 담당**

- ** CustomDB 설계 **
  - settings.py에 인증 패키지인 djoser를 연결한 파라미터값에 커스텀한 model을 상속한 serializers를 연결해줌.
  ```python
  # 커스텀 유저모델
    AUTH_USER_MODEL = "accounts.User"

    DJOSER = {
        "SERIALIZERS": {
            "user_create": "accounts.serializers.UserSerializer",
            "user": "accounts.serializers.UserSerializer",
            "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": ['https://kauth.kakao.com/oauth/token'],
        }
    }
  ```
  - 연결만 진행한 후 models에서 ID인 이메일 주소, PW는 제외하고 커스텀으로 들어갈 성별, MBTI, 나이, 프로필 사진을 설계하고 DB를 구동하였을 때 하기와 같이 PW가 plaintext로 저장되어 로그인이 되지 않는다는 결함이 생김.
  ![image](https://user-images.githubusercontent.com/108647811/218999997-50641881-eb42-4cb0-a36f-7dfc61fc3892.png)

  - 
  - 
