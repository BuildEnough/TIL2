# https://www.acmicpc.net/problem/8958

import sys
sys.stdin = open('OX퀴즈.txt')

t = int(input())



for _ in range(t):
    quiz = list(input())

    result = 0
    count = 0
    for i in quiz:
        if i == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)
