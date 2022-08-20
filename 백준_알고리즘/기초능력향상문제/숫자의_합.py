# https://www.acmicpc.net/problem/11720

import sys
sys.stdin = open('숫자의_합.txt')

A = int(input())
B = list(input())

sum_ = 0
for i in B:
    sum_ += int(i)
print(sum_)
