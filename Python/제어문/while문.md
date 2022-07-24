# while문 기본 구조
- 반복해서 문장을 수행해야 할 경우 while문 사용
```python
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
```
- while문은 조건문이 True인 동안에 while문 아래의 문장이 반복해서 수행됨

## while문 만들기
### 1. 여러 줄의 문자열을 입력
```python
>>> prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """
>>>
```
### 2. 변수에 숫자 대입
- 변수를 먼저 설정하지 않으면 다음에 나올 while문에서 변수가 존재하지 않는다는 오류 발생함
```python
>>> number = 0
>>> while number != 4:
...     print(prompt)
...     number = int(input())
...

1. Add
2. Del
3. List
4. Quit

Enter number:
```
- 여기서 4를 입력하게되면 조건문이 `False`가 되어 while문을 빠져나가게 된다

## break 문
- 강제로 while문을 빠져나가고 싶을때 `break`문 사용
```python
>>> coffee = 10
>>> money = 300
>>> while money:
...     print("돈을 받았으니 커피를 줍니다.")
...     coffee = coffee -1
...     print("남은 커피의 양은 %d개입니다." % coffee)
...     if coffee == 0:
...         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
...         break
...
```
- money가 300으로 고정되어 있기 때문에 무한히 반복되는 무한 루프를 돌게 된다
- 하지만 coffee가 while 문을 수행할 때마다 1개씩 줄어들게 되고
- coffee가 0이 된다면 break 문에 의해 while 문을 빠져나가게 된다
#
## continue 문
- while 문을 빠져나가지 않고 while문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우가 생긴다
```python
>>> a = 0
>>> while a < 10:
...     a = a + 1
...     if a % 2 == 0: continue
...     print(a)
...
1
3
5
7
9
```
- a가 짝수일 경우 continue 문장을 수행하고
- while 문의 맨 처음으로 돌아가게 된다
#
## 무한 루프
- 무한 루프란 무한히 반복한다는 의미이고
- 일반 프로그램 중에서 무한 루프 개념을 사용하지 않는 프로그램은 거의 없다
- 즉, 자주 사용한다는 의미이다
```python
while True: 
    수행할 문장1 
    수행할 문장2
    ...
```
- while 문의 조건문이 True이므로 항상 참이된다
- 따라서 while 문 안에 있는 문장들은 무한하게 수행될 것이다
```python
>>> while True:
...     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
...
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
....
```
- 무한 루프의 예로 윈도우 유저라면
- Ctrl + c를 눌러 while 문을 빠져나갈 수 있다