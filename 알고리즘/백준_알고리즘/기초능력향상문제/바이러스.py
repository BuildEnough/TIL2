# https://www.acmicpc.net/problem/2606

import sys
sys.stdin = open('바이러스.txt')

computer = int(input())

pair = int(input())

arr = [[]*computer for _ in range(computer)]

for _ in range(pair):
    a, b = map(int, input().split())
    arr[a].append[b]
    arr[b].append[a]

    