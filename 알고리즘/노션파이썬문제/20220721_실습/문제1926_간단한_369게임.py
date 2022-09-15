T = int(input())

for i in range(1, T + 1):
    N = int(input()) # N 입력
    for i in range(1, N+1):
        if str(i) == 3:
            i = '-'
            print(i, end=' ')
    
# 아직 다 못품