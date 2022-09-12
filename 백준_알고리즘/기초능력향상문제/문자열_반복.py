# https://www.acmicpc.net/problem/2675

import sys
sys.stdin = open('문자열_반복.txt')

for _ in range(int(input())):
    R, S = input().split()

    result = ''
    for i in S:
        result += i * int(R)
    print(result)

        
