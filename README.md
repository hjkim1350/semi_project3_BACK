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
- **주변인들의 MBTI 저장 페이지**
  - MBTI 정보 입력
    - Input: 이름, MBTI, 그룹 태그 지정
  - MBTI 정보 출력
    - 이름과 함께 MBTI 궁합도가 저장된 DB 정보를 가져와 나의 MBTI와 궁합이 잘맞는지를 색깔로 표현
- **사용자 커뮤니티 페이지**
  - CRUD 구현: 글 생성, 수정, 삭제, 이미지 업로드 가능
  - 글쓴이 프로필 출력: 글쓴이 프로필 이미지, 글 작성 시간, MBTI 정보 출력
  - 댓글, 대댓글 구현: 댓글을 글쓴이가 쓴다면 (글쓴이)로 표현
- **MBTI 정보 페이지**
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

> **💻 Role - Backend: 회원 custom DB 설계, 일반/카카오 로그인, 회원가입, 마이페이지 등 전반적인 회원 관련 담당**

- **CustomDB 설계**
  - settings.py에 인증 패키지인 djoser를 연결한 파라미터값에 커스텀한 model을 상속한 serializers를 연결해줌.
  ```python
  # backend/settings.py
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
  - 해결방법: djoser의 PW는 SHA256으로 처리한다는 것을 확인, djoser에서 제공하는 set_password 활용하여 암호화
  - 참고: https://github.com/sunscrapers/djoser/blob/master/poetry.lock
  ```python
  # accounts/serializers.py
  def create(self,validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None :
        #provide django, password will be hashing!
        instance.set_password(password)
    instance.save()
    return instance
  ```

<br>

- **일반/카카오 로그인, 회원가입**

![image](https://user-images.githubusercontent.com/108647811/219248236-5b220223-235f-4930-b8a4-b4a47f464cf4.png)

  - JWT 방식의 경우 토큰을 활용하기 때문에 회원가입할 때 사용자에게 토큰을 발급해주고, 발급해준 토큰은 총 2가지가 됨. 1) Access Token, 2) Refresh Token.
  - 로그인할 때 사용자는 Access Token을 서버에게 전달하고 서버는 Front에서 토큰을 받아들이고 Back에 넘김. Back에서는 이 토큰이 자신이 발급한 토큰인지 확인 후 응답값을 보내고 Front에서 정당한 토큰임을 확인하였으면 서비스 화면으로 리다이렉션하며, 정당하지 않은 토큰일 경우 에러 메시지를 출력하도록 하였음.
  - Refresh Token의 경우 사용자가 로그인 한 후 정당한 사용자임을 계속해서 서버에게 알리는 역할을 함. 이 Refresh Token에 대한 주기는 settings.py에서 제어가 가능함. 계속해서 서버에게 알리는 역할을 하는 이유는 HTTP의 비연결적 특성 때문임. HTTP는 필요할 때만 요청/응답을 하기 때문에 지속적으로 연결되어 있지 않음. 따라서 응답값을 보낸 서버는 사용자와 연결을 끊게 되는데 사용자 입장에서는 정당하게 로그인을 하고 들어왔지만 서비스 연결이 끊기는 불편함을 느낄 수 있으므로 주기적으로 사용자와 서버(Back) 간에 Refresh Token을 주고받음으로써 인증된 사용자임을 증빙함.
  - 카카오 로그인의 경우 사용자가 카카오 로그인 시도할 경우 카카오 로그인 페이지로 리다이렉션 되며, 사용자가 카카오 정상 로그인 후 카카오 측에서 Access Token, Refresh Token이 발급되면 이를 서버로 가져와 발급 여부만 확인하여 다시 서버에서 만든 Token을 사용자에게 발급하는 형태로 구성되었음.
  - 회원가입의 경우 앞서 CustomDB 설계한 대로 이메일, 닉네임, 비밀번호, 프로필 사진, 나이, 성별, MBTI 정보를 받아 DB에 저장하는 형태로 구성되어 있음. 서버에서 원하는 데이터셋이 아니라면 회원가입이 취소되도록 함.

<br>

- **마이페이지**

![image](https://user-images.githubusercontent.com/108647811/219250253-6fa5af8c-e506-441e-bb1f-bc850f6feb8f.png)

  - 회원가입 시 입력하였던 본인의 정보를 출력하도록 함.
  - 로그아웃 버튼의 경우 Back 단에서 로그인을 하기 위해 서버 측으로부터 보냈던 Access Token을 회수하고 더이상 Refresh Token을 보내지 않도록 함. Front 단에서 서비스 시작 페이지로 리다이렉션 되도록 함.
  - 회원탈퇴 버튼의 경우 Back 단에서 발급하였던 Access Token, Refresh Token을 모두 폐기하고 DB에 저장되었던 회원의 정보를 삭제하도록 함. Front 단에서 회원탈퇴 안내 메시지를 출력하고 서비스 시작 페이지로 리다이렉션 되도록 함.


<br>

### ⌨️ 프로젝트 후기
가장 긴 시간을 투자하게된 프로젝트이자 개인적으로 가장 성과 있었던 프로젝트였다.<br>
다만, 서비스를 사용하였을 때 Django-model 기반의 CRUD 서비스와 별반 다를게 없어보이는 듯 하였지만, BackEnd/FrontEnd 폴더를 나누고 BackEnd는 DRF, FrontEnd는 Vue.Cli를 사용하는 등 신기술을 직접 우리가 공부하고 적용할 수 있었던 가장 성과있는 프로젝트가 아니였을까 한다.<br>
교육 때 배웠던 웹 서비스는 세션 기반이다보니 RefreshToken 등의 개념을 인지하지 않아도 되었다. 하지만 DRF는 세션 기반도 제공하지만 Token 기술이 좀 더 발전되어 있기도하고 채택했던 인증 패키지인 Djoser도 Token 베이스라 Token을 깊게 들여다 볼 수 있었던 것 같다.<br>
사실 교육을 들으면서 강사님이 강조했던 "공식 문서"와 "공식 Github"의 중요성을 잘 몰랐는데, 새로운 기술을 접하면서 "왜 이 코드는 이렇게 돌아갈 수 밖에 없을까?"라는 고민이 들기 시작하면서 비로소 공식 문서와 공식 Github를 자세히 뜯어볼 수 있었다. 공식 문서를 보면서 이 함수는 어떠한 문제점으로부터 시작되서 나왔다라는 개념을 확인할 수 있었고, 공식 Github를 통해 이 함수를 구현하기 위한 소스 코드를 볼 수 있었다.<br>
결국 우리가 쓰는 함수/클래스들은 그 역사를 거슬러 올라가다보면, 프로그래밍 초급을 배울 때 썼던 if, while 등 가장 기초적인 문법으로 이루어져있고 이렇게 만들어진 함수/클래스가 다시 다른 곳에 상속되면서 또 새로운 기술이나 로직을 가진 함수/클래스로 발전한 것 같다. 그래서 이 역사와 흐름을 살피기 위해서라도 "공식 문서", "공식 Github"는 반드시 찾아보고 확인해야 할 중요 문서임을 절실히 깨달을 수 있었던 것 같다.
