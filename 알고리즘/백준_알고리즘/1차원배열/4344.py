import sys
sys.stdin = open('4344.txt')

for _ in range(int(input())):
    N = list(map(int, input().split()))
    avg_ = sum(N[1:]) / N[0]
    c = 0
    for z in N[1:]:
        if z > avg_:
            c += 1
    result = c / N[0] * 100
    print(f'{result:.3f}%')

n = int(input())

# >=인지 >인지 주의 여기서 못찾아서 1시간 더 걸림