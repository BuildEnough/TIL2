# https://www.acmicpc.net/problem/2846

import sys
sys.stdin = open('오르막길.txt')

n = int(input())

road = list(map(int, input().split()))


a = 0
list_ = []
for i in range(1, n):
    
    if road[i] > road[i-1]:
        a += road[i] - road[i-1]
        list_.append(a)
    else:
        a = 0
        list_.append(a)
print(max(list_))
