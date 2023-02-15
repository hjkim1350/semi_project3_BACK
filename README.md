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

