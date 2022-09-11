# https://www.acmicpc.net/problem/7785

import sys
sys.stdin = open('회사에_있는_사람.txt')

n = int(input())

company = dict()

for i in range(n):
    name, work = input().split()
    
    if work == 'enter':
        company[name] = 'enter'

    else:
        company[name] = 'lever'
        