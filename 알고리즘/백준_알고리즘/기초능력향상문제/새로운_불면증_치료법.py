#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN

import sys
sys.stdin = open('새로운_불면증_치료법.txt')

for T in range(int(input())):
    N = int(input())

    list_ = [0]*10 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    i = 0
    while True:
        if 0 not in list_:
            break
        else:
            i += 1
            num = str(N * i)
            for j in range(len(num)):
                list_[int(num[j])] = 1
    print(f'#{T+1} {num}')
            




# t = int(input())

# for i in range(1, t + 1) :
#     n = input()
#     value = int(n)
#     data = [0] * 10
#     while True :
#         for j in range(len(n)) :
#             data[int(n[j])] += 1
#         if not data.count(0) :
#             print('#%d %d' % (i, int(n)))
#             break

#         n = str(value + int(n))