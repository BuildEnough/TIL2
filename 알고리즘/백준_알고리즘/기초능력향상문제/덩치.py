# https://www.acmicpc.net/problem/7568

import sys
sys.stdin = open('덩치.txt')


body = []
for i in range(int(input())):
    w, h = map(int, input().split())
    body.append((w, h))

for i in body:
    a = 1
    for j in body:
        if i[0] < j[0] and i[1] < j[1]:
            a += 1
    print(a, end = ' ')
