## if문의 기본 구조
```python
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
```
- 조건문을 테스트해서 True면 if문 바로 다음 문장들을 수행하고
- 조건문이 False면 else문 다음 문장들을 수행하게 된다
- else문은 if문 없이 독립적으로 사용할 수 없다

## 들여쓰기
- 오류 문장
```python
if 조건문:
    수행할 문장1
수행할 문장2
    수행할 문장3
```
- 들여쓰기를 하지 않아 오류가 발생
***
```python
if 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
```
- 정상적인 문장

## 공백(Spacebar)과 탭(Tab)
- 공백과 탭 사이에서 어떤 것을 사용할지에 대한 논쟁은 계속 진행 중이지만
- 2가지(공백, 탭)를 혼용해서 쓰지 않으면 된다
- 공백으로 할거면 항상 공백, 탭으로 할거면 항상 탭으로 통일해서 사용하면 된다
- 탭이나 공백은 프로그램 소스에서 눈으로 보이는 것이 아니기 때문에 혼용해서 쓰면 오류의 원인이 됨
- 보통 공백 4개를 사용하는 것을 권장
- **본인은 탭 사용하는 것이 편해 탭을 사용함**

## 콜론(:)
- if 조건문 뒤에 반드시 `:`이 붙는다
- 어떤 특별한 의미보다 파이썬의 문법 구조이다

## elif
- if와 else만으로 다양한 조건을 판단하기 어렵기 때문에 elif를 사용함
- elif는 이전 조건문이 거짓일 때 수행됨
- elif는 개수 제한 없이 사용 가능
```python
>>> pocket = ['paper', 'handphone']
>>> card = True
>>> if 'money' in pocket:
...     print("택시를 타고가라")
... else:
...     if card:
...         print("택시를 타고가라")
...     else:
...         print("걸어가라")
...
택시를 타고가라
>>>
```
- 이해하기 어렵고 산만한 느낌이 듬
- elif 문을 사용하면
```python
>>> pocket = ['paper', 'cellphone']
>>> card = True
>>> if 'money' in pocket:
...      print("택시를 타고가라")
... elif card: 
...      print("택시를 타고가라")
... else:
...      print("걸어가라")
...
택시를 타고가라
```
- 이해하기 쉽기 표현 가능하다

## if문 한 줄 작성
```python
>>> if 'money' in pocket:
...     pass 
... else:
...     print("카드를 꺼내라")
...
```
- 위에 표현된 문장을 밑에 표현된 문장으로 표현 가능하다
```python
>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money' in pocket: pass
... else: print("카드를 꺼내라")
...
```
- if문 다음 수행할 문장을 `:` 뒤에 바로 적어 주었다

## 조건부 표현식
```python
조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
```

```python
if score >= 60:
    message = "success"
else:
    message = "failure"
```
```python
message = "success" if score >= 60 else "failure"
```
- 조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다