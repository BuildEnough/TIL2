# 불(bool)
- True와 False를 나타내는 자료형
- 불 자료형은 True, Flase 2가지 값만 가질 수 있다
```python
>>> a = True
>>> b = False

>>> type(a)
<class 'bool'>

>>> type(b)
<class 'bool'>
```

## 불 예시
```python
>>> 1 == 1
True

>>> 2 > 1
True

>>> 2 < 1
False
```

## 자료형의 참과 거짓

| 값	|참 or 거짓 |
| ------------ | ------------- |
| "python"|	참 |
| ""|	거짓 |
| [1, 2, 3] |	참 |
| []|	거짓 |
| ()|	거짓 |
| {}|	거짓 |
| 1| 참 |
| 0| 거짓 |
| None| 거짓 |
- 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 거짓
- 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있지 않으면 참
```python
>>> a = [1, 2, 3, 4]
>>> while a:
...     print(a.pop())
...
4
3
2
1
```
- `pop` 함수를 사용해 a안에 있는 요소들을 while문을 통해 끄집어 내면 a가 빈 리스트(`[]`)가 되어 거짓이 됨
- 따라서 `while`문에서 조건이 `거짓`이 되어 중지됨

```python
>>> if []:
...     print("참")
... else:
...     print("거짓")
...
거짓
```
- if문에서 리스트에 요소 값이 없으므로 `거짓`이 출력됨

```python
>>> if [1, 2, 3]:
...     print("참")
... else:
...     print("거짓")
... 
참
```
- if 문에서 [1, 2, 3]은 요소값이 있는 리스트이기 때문에 `참`

```python
>>> bool('python')
True
```
- 'python'은 문자열이 아니므로 bool 연산의 결과로 `True`를 돌려줌

```python
>>> bool([1,2,3])
True
>>> bool([])
False
>>> bool(0)
False
>>> bool(3)
True
```
- bool 예시