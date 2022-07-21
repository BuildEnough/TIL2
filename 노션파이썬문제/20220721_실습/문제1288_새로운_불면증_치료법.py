T = int(input()) # 테스트 케이스의 T

for test_case in range(1, T+1) : # T번 반복
    N = int(input()) # N번 양을 셈
    
    list = [0]*10 # 정수는 총 10개 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    i = 0
    while(True) :
        if 0 not in list : # 0이 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] list 안에 없을 때 멈춤
        # list안에 있는 0들이 모두 1로 바뀌면 멈춘다는 의미
            break
        else :
            i += 1 
            num = str(N*i) # i를 문자열로 바꿔주고 num에 저장
            for j in range(len(num)) :
                list[int(num[j])] = 1 # num에 i의 값이 있으므로 그 1의 값을 list에 저장한다


    print("#{} {}".format(test_case, num))

# list말고 set으로도 풀 수 있음