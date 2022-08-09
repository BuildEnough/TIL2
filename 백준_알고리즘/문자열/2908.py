import sys
sys.stdin = open('2908.txt')

n, m = input().split()

n = n[::-1]
m = m[::-1]

if int(n) > int(m):
    print(n)
else:
    print(m)
