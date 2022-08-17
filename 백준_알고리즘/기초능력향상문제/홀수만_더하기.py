# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq

import sys
sys.stdin = open('홀수만_더하기.txt')



for T in range(int(input())):
    sum_ = 0
    n = list(map(int, input().split()))
    for i in n:
        if i % 2 == 1:
            sum_ += i
    print(f'#{T+1} {sum_}')