# https://www.acmicpc.net/problem/2577

import sys
sys.stdin = open('숫자의_개수.txt')

A = int(input())
B = int(input())
C = int(input())

sum_result = list(str(A * B * C))

for i in range(10):
    print(sum_result.count(str(i)))





