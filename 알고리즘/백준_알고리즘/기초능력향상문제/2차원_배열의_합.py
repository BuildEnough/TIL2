# https://www.acmicpc.net/problem/2167

import sys
sys.stdin = open('2차원_배열의_합.txt')

n, m = map(int, input().split())

list_ = []

for _ in range(n):
    array = input().split()
    list_.append(array)

k = int(input())
