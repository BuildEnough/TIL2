# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QGNvKAtEDFAUq

for T in range(1, int(input())+1):
    a, b = map(int, input().split())
    print(f'#{T} {a//b} {a%b}')
