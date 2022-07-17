> Life is short, you need Python

# Python이란
- 1991년에 발표된 [인터프리터](https://namu.wiki/w/%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0) 방식의 프로그래밍 언어
- 창시자 : Guido van Rossum(귀도 반 로섬)
- 영어와 비슷해서 읽고 쓰기 쉬운 특유의 문법과 그로 인해 개발자들로부터 만들어진 수 많은 패키지들 덕분에 사용할 수 있는 요도가 무궁무진해서 2010년대 중반부터 주류 프로그래밍 언어로 당당히 올라서게 됨
- Pyhton 별명 : Executable pseudocode(실행할 수 있는 의사코드)
- 엑셀 자동화, 파일 처리 자동화, 웹 크롤링 자동화, 3D 모델링 자동화
- 업무 시간을 단축해 주는 언어로 활용 가능
- 파이썬으로 만든 잘 알려진 프로그램 : [드롭박스](https://www.dropbox.com/ko/), 구글 앱 엔진, [유튜브](https://www.youtube.com/), [넷플릭스](https://www.netflix.com/)

# 특징
> 가장 아름다운 하나의 답이 존재한다
- 복잡하지 않으면서 의미가 명확하고, 코드의 축약보다 뚜렷하게 보이는 흐름을 중시
- 문법이 엄격한 편
- 잘 작동하는지와 별개로 가독성을 위한 스타일 가이드 존재 => 뚜렷한 권장 코드 스타일[PEP 8](https://peps.python.org/pep-0008/)
- 순수 객체 지향

# 작명 규칙
- Python에서는 변수나 클래스 이름을 어떻게 짓든 잘 작동함
- 일반적으로 [스테이크 표기법](https://ko.wikipedia.org/wiki/%EC%8A%A4%EB%84%A4%EC%9D%B4%ED%81%AC_%ED%91%9C%EA%B8%B0%EB%B2%95)을 쓰되, 특정한 종류에는 [파스칼 표기법](https://namu.wiki/w/%EC%BD%94%EB%94%A9%20%EC%8A%A4%ED%83%80%EC%9D%BC#s-3.3)을 쓴다
- 변수는 소문자 시작 : attribute_name = 0
- 내부 변수는 맨 앞에 밑줄 1개로 시작 : _protected_attribute_name = 0
- 숨은 변수는 맨 앞에 밑줄 2개로 시작 : __hidden_attribute_name = 0

|종류|규칙|예시|
|---|---|---|
|패키지|스네이크()| |
|모듈|스네이크()|import module_name|
|클래스|파스칼()|class ClassName()|
|예외|파스칼| |
|함수|스네이크()|def function_name()|
|상수|대문자 + 밑줄|MODULE_CONSTANT_NAME = 0|
|변수|스네이크|variable_name = 0|
|매개변수|스네이크|variable_name = 0|
|지역변수|스네이크|variable_name = 0|
|인스턴스 변수|스네이크|variable_name = 0|
|메쏘드|스네이크()|method_name()|

# 순수 객체 지향
- Python에는 원시 타입이 존재하지 않으며, 모든 것이 객체로 취급됨
- 클래스, 함수 역시 객체로 취급
- 상수 역시 상수가 저장된 객체라고 봄
- x = 10이라는 할당문이 있을 때
- - 이는 변수 x자체에 10이 할당된 것이 아니라 x가 10이 저장된 상수 객체를 가리키는 것을 의미함
- x = 10
- x = 20
- - x가 가리키는 대상이 10이 저장된 상수 객체에서 20이 저장된 상수 객체로 바뀐 것
- - x 자체의 값이 10에서 20으로 바뀐게 아님

