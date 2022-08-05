# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

n = int(input())
sum_n = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_n += i
print(sum_n)