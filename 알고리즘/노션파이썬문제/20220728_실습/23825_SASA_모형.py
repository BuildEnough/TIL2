import sys

sys.stdin = open("23825_SASA_모형.txt")

N, M = map(int, input().split())

SASA = 0

if N // 2 == M // 2: # 2로 나눠서 몫이 N과 M 같으면 둘 중 아무거나 출력
    print(N // 2)
elif N // 2 > M // 2: # N이 더 크면 N보다 작은 M을 2로 나눈 몫 출력
    print(M // 2)
else:   # M이 더 크면 N보다 작은 M을 2로 나눈 몫 출력
    print(N // 2)