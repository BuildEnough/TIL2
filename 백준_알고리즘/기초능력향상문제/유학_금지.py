# https://www.acmicpc.net/problem/2789

n = input()

colleage = 'CAMBRIDGE'

for i in colleage:
    n = n.replace(i, '')
print(n)