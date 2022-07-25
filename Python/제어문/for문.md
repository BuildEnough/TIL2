## for문 기본구조
```python
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
```
- 리스트나 튜플, 문자열의 1번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 `수행할 문장1`, `수행할 문장2` 등이 실행됨

```python
>>> test_list = ['one', 'two', 'three'] 
>>> for i in test_list: 
...     print(i)
... 
one 
two 
three
```
#
## 다양한 for문 사용
```python
>>> a = [(1,2), (3,4), (5,6)]
>>> for (first, last) in a:
...     print(first + last)
...
3
7
11
```
- a 리스트의 요소값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last 변수에 대입됨)
  
#
## for문과 continue
- for문 안의 문장을 수행하는 도중 continue문을 만나면 for문의 처음으로 돌아감
```python
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)
```
- 60점 이상인 사람에게 축하 메시지 보내고 나머지 사람에게 아무 메시지도 전하지 않는 코드

#
## for문과 range
- for문은 숫자 리스트를 자동으로 만들어주는 range 함수와 함께 사용하는 경우가 많다
```python
>>> a = range(10)
>>> a
range(0, 10)
```
- `range(10)`은 0부터 10미만의 숫자를 포함하는 range 객체를 만들어 준다

#
## 리스트 내포 사용
- 리스트 안에 for문을 포함하는 리스트 내포(List comprehension)를 사용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있다
```python
[표현식 for 항목 in 반복가능객체 if 조건문]
```
```python
>>> a = [1, 2, 3, 4]
>>> result = []
>>> for num in a:
...     result.append(num*3)
...
>>> print(result)
[3, 6, 9, 12]
```
- 를 리스트 내포를 사용하면
```python
>>> a = [1, 2, 3, 4]
>>> result = [num * 3 for num in a]
>>> print(result)
[3, 6, 9, 12]
```
- 만약 [1, 2, 3, 4] 중에서 짝수에만 3을 곱하여 담고 싶다면 if조건을 사용할 수 있다
```python
>>> a = [1,2,3,4]
>>> result = [num * 3 for num in a if num % 2 == 0]
>>> print(result)
[6, 12]
```
- 리스트 내포에서 for문을 2개 이상 사용하는 것도 가능함
```python
[표현식 for 항목1 in 반복가능객체1 if 조건문1
        for 항목2 in 반복가능객체2 if 조건문2
        ...
        for 항목n in 반복가능객체n if 조건문n]
```