# https://www.acmicpc.net/problem/2669

import sys
sys.stdin = open('직사각형_네개의_합집합의_면적_구하기.txt')


square = []
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    square.append((x1, y1, x2, y2))

print(square)