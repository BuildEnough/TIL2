# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh

import sys
sys.stdin = open('최빈수_구하기.txt')



for i in range(int(input())):
    test = int(input())
    list_ = input().split()
    score = dict()
    for i in list_:
        if i in score:
            score[i] += 1
        else:
            score[i] = 1

    max_ = max(score.values())

    for key, value in score.items():
        if value == max_:
            print(f'#{test} {key}')