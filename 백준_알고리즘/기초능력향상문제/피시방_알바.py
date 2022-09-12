# https://www.acmicpc.net/problem/1453

import sys
sys.stdin = open('피씨방_알바.txt')

n = int(input())

sit = list(map(int, input().split()))


list_ = []


count = 0
for i in range(n):
    if sit[i] in list_:
        count += 1
    else:
        list_.append(sit[i])

print(count)