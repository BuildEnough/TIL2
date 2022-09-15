# https://www.acmicpc.net/problem/1357

import sys
sys.stdin = open('뒤집한_덧셈.txt')

X, Y = input().split()

def Rev(integer):
    integer = int(integer[::-1])
    return integer

print(Rev(str(Rev(X) + Rev(Y))))