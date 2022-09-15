# https://www.acmicpc.net/problem/2920



u = list(map(int, input().split()))



if u == sorted(u):
    print('ascending')
elif u == sorted(u, reverse=True):
    print('descending')
else:
    print('mixed')

