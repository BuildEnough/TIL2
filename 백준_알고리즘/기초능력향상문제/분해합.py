# https://www.acmicpc.net/problem/2231
import sys
sys.stdin = open('분해합.txt')


N = int(input())

for i in range(1, N):
    A = sum(map(int, str(i)))

    result = i + A

    if result == N:
        print(i)
        break
else:
    print(0)
    