import sys
sys.stdin = open('4344.txt')

for _ in range(int(input())):
    N = list(map(int, input().split()))

    list_ = []
    for i in range(1, len(N)):
        print(N(i))
    