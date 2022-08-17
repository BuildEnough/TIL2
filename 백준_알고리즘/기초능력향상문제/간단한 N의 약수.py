# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PhcWaAKIDFAUq

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end = ' ')