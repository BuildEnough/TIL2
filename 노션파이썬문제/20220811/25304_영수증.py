import sys
sys.stdin = open('25304_영수증.txt')

# X: 총 금액
# N: 구매한 물건의 종류의 수
# a: 물건의 가격
# b: 물건의 개수

X = int(input())
N = int(input())

price = 0

for _ in range(N):
    a, b = map(int, input().split())

    price += (a * b)

if price == X:
    print('Yes')
else:
    print('No')