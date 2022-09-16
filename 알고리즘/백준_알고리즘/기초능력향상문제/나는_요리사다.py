# https://www.acmicpc.net/problem/2953

import sys
sys.stdin = open('나는_요리사다.txt')

score = [sum(map(int, input().split())) for _ in range(5)]


print(score.index(max(score))+1, max(score))