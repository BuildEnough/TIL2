# https://www.acmicpc.net/problem/7785

import sys
sys.stdin = open('회사에_있는_사람.txt')

n = int(input())

company = dict()

for _ in range(n):
    name, work = input().split()
    
    if work == 'enter':
        company[name] = 'enter'
    else:
        del company[name]


result = sorted(company.keys(), reverse=True)

for i in result:
    print(i)
    
