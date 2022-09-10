# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh

import sys
sys.stdin = open('최빈수_구하기.txt')



T = int(input())
for i in range(T):
    idx = int(input())
    arr = list(map(int, input().split()))
    score = dict()
    for s in arr:
        if s in score:
            score[s] += 1
        else:
            score[s] = 1
    _max = max(score.values())

    print('#', end='')
    print(idx, next(key for key, value in score.items() if value == _max))