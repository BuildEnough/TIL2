# https://www.acmicpc.net/problem/2167

import sys
sys.stdin = open('2차원_배열의_합.txt')

N, M = map(int, input().split())

arr = [] # 정수가 저장되어 있는 2차원 리스트
for _ in range(N):
    arr.append(list(map(int, input().split())))

# memoization을 이용하여 memo변수에 2차원 리스트 선언
memo = [[0] * M for _ in range(N)]

# memo에 (0, 0)부터 (a, b)까지의 합을 저장
# memo[][] - arr: (0, 0)부터 (a, b)까지의 합을 저장해둔 2차원 리스트
for m in range(N):
    for n in range(M):
        memo[m][n] = memo[m][n-1] + memo[m-1][n] - memo[m-1][n-1] + arr[m-1][n-1]

        print(memo)

# memo 값을 이용하여 (i, j)부터 (x, y)까지의 합을 구함