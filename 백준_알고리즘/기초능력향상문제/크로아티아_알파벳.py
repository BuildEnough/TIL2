# https://www.acmicpc.net/problem/2941

import sys
sys.stdin = open('크로아티아_알파벳.txt')

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n = input()

for i in croatia:
    n = n.replace(i, '*')
print(len(n))

    
