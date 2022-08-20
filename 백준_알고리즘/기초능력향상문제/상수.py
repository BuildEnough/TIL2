# https://www.acmicpc.net/problem/2908

import sys
sys.stdin = open('상수.txt')

A, B = input().split()

A = A[::-1]
B = B[::-1]

if A > B:
    print(A)
else:
    print(B)