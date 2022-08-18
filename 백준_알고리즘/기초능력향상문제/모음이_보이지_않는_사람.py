# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcD_66pUEDFAV8

import sys
sys.stdin = open('모음이_보이지_않는_사람.txt')

memory = 'aeiou'

for T in range(int(input())):
    n = input()
    for i in memory:
        n = n.replace(i, '')
    print(f'#{T+1} {n}')