# https://www.acmicpc.net/problem/10871

A, X = map(int, input().split())

N = list(map(int, input().split()))

for i in N:
    if i < X:
        print(i, end = ' ')
