import sys

sys.stdin = open("_민석이의과제체크하기.txt")

# list_ = []

for T in range(1, int(input()) + 1):
    N, K = map(int, (input().split())) 
    num = list(map(int, (input().split()))) # list로 출력해야됨
    # N: 수강생 수, K: 과제 제출한 사람 수, num: 과제를 제출한 사람의 번호K개
    # print(N)
    # print(K)
    # print(num)
    list_ = []
    for i in range(1, N + 1): # 5번 돌려주고
        if i not in num: # 제출한 학생 번호에 없으면, != 안됨
            list_.append(i) # list_에 없는 번호 추가
    # print(list_, type(list_))
    # [1, 4]
    # [1, 2, 3, 5, 7]
    # for z in list_:
    #     print(f"#{T} {z, end =' '}")
    # print()
    print(f'#{T} ', end= '')
    for z in list_:
    
        print(z, end =' ')
    print()