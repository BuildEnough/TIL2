import sys
sys.stdin = open('1526_가장_큰_금민수.txt')

num = int(input())


while True:
    count = 0 # 0으로 계속 초기화시켜야됨
    for i in str(num):
        if i != '4' and i !='7': # 100 -> 99 -> 98
            num -= 1
            count = 1
    if count == 0: 
        print(num)
        break
        # else:
        #     result = num # 계속 77나옴
        # if i == '4' and i =='7':
            
