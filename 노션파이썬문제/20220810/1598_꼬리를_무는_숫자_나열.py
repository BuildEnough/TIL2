import sys
sys.stdin = open('1598_꼬리를_무는_숫자_나열.txt')


# for i in range(4):
#     ma = []
#     for j in range(10):
#         ma.append(0)
# print(ma)


# 처음에 좌표를 먼저 구해보자
# (0, 0)이니까 -1 해줘야하나?
A, B = map(int, input().split())

A -= 1
B -= 1

xa, ya, xb, yb = 0, 0, 0, 0

xa += A // 4
ya += A % 4

xb += B // 4
yb += B % 4

print(xa, ya, xb, yb)
print(abs(xa - xb) + abs(ya - yb))