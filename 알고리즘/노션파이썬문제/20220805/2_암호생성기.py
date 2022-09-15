import sys

sys.stdin = open("_암호생성기.txt")

for T in range(1, 11):
    N = int(input()) # 1 ~ 10
    num = list(map(int, input().split())) # 9550 9556 9550 9553 9558 9551 9551 9551
    # print(num)
    # print(num[0])
    X = 1
 
    while True:
        temp = num.pop(0) - X #첫 번째 숫자를 1.. n 감소한 뒤
        if temp < 0: # 숫자가 감소할 때 0보다 작아지는 경우
            temp = 0 #  0으로 유지
        num.append(temp) # 맨 뒤로 보낸다

        X += 1 # 1....n
 
        if X > 5: # 사이클
            X = 1

        if temp <= 0: # 0보다 작아저거나 0일 경우 그만
            break




    print(f'#{T} ', end= '')
    for z in num:
    
        print(z, end =' ')
    print()