# https://www.acmicpc.net/problem/1822

import sys
sys.stdin = open('차집합.txt')

n_a, n_b = map(int, (input().split()))



a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = a-b

result = sorted(result)


if len(result) != 0:
    print(len(result))
    print(*(result))
else:
    print(0)
