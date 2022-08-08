import sys
sys.stdin = open('9325_얼마.txt')

for _ in range(int(input())):
    S = int(input())

    n = int(input())
    option_ = 0
    if n == 0:
        print(S)
    else:
        for _ in range(n):
            q1, p1 = map(int, input().split())
            option_ += q1 * p1
        print(S + option_)