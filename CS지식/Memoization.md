# 궁금하게 된 계기
- 백준에서 문제 풀다가 2차원 배열에서 막혔음
- Memoization이라는 개념을 알아야 문제를 풀 수 있을거 같아서 작성해봄

# Memoization 메모이제이션
- DP 동적 계획법 알고리즘에서 핵심이 되는 기술
- 중복 계산을 제거함으로써 프로그램의 전체적인 실행 속도를 빠르게, 성능을 향상할 수 있는 기법
- 이전에 계산한 값을 메모리에 저장하여 중복적인 계산을 제거하여 전체적인 실행 속도를 빠르게 해주는 기법

</br>

## 피보나치 수열로 알아보는 재귀(recursion)와 memoization
- 피보나치 수열은 첫째 및 둘째 항이 1이고 그 뒤의 모든 항은 바로 앞의 두 항의 합인 수열
- 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
- [피보나치 수열 유튜브](https://www.youtube.com/watch?v=V9d7wrMPzHE)
- 피보나치 수를 구하는 재귀 함수 알고리즘의 문제점은 엄청난 중복 호출이 발생함
- 이때 피보나치의 단점을 보완할 수 있는 프로그래밍 기법인 **momoization**

</br>

### 재귀 함수를 사용한 피보나치 수열 
```python
def fibo(n):
    if n < 2 :
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

</br>

### 메모이제이션 기법을 사용한 피보나치 수열
- 메모이제이션 리스트에 값이 저장되어 있으면 다시 계산하지 않는 알고리즘
- fibo_memo(n)의 결과 값이 momo[n]에 저장됨
```python
def fibo_memo(n):
    global memo
    if n >= len(memo):
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
```