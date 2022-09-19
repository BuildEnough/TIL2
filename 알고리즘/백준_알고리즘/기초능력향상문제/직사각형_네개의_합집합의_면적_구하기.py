# https://www.acmicpc.net/problem/2669

import sys
sys.stdin = open('직사각형_네개의_합집합의_면적_구하기.txt')


square = [[0] * 101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            square[i][j] = 1

result = 0
for z in square:
    result += sum(z)
print(result)