# https://www.acmicpc.net/problem/3052

import sys
sys.stdin = open('나머지.txt')

na = []

for _ in range(10):
    i = int(input())
    na.append(i % 42)

na = set(na)

count = 0
for j in na:
    count += 1

print(count)