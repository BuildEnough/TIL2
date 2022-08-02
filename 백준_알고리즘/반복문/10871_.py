A, X = map(int, input().split())

N = list(map(int, input().split()))

for i in range(A):
    if X > N[i]:
        print(N[i], end=' ')



