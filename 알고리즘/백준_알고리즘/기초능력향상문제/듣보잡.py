# https://www.acmicpc.net/problem/1764

import sys
sys.stdin = open('듣보잡.txt')

n, m = map(int, input().split())

listen = set()

for i in range(n):
    listen.add(input())


look = set()
for j in range(m):
    look.add(input())

listen_look = listen & look

listen_look = list(listen_look)

listen_look.sort()

print(len(listen_look))

for i in listen_look:
    print(i)
