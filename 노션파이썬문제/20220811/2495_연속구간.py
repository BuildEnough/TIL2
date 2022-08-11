from re import L
import sys
sys.stdin = open('2495_연속구간.txt')

# 3줄 입력
# 각 줄마다 3개의 8자리 양의 정수 입력
# 각 줄마다 연속된 값들의 가장 큰 값 출력

# num_list = []

for _ in range(3):
    num = list(input())
    a = 0
    count = 1
    for i in range(8):
        if num[i] == num[i+1]:
            count += 1
print(count)













# num_list.append(num)
  
# x = 0
# count = 1

# for j in num_list:
#     result = str(j)

#     for z in range(8):
#         print(result[:z])
        
    # for z in range(8):

        # if str(j)[z:z+1] == str(j)[z+1:z+2]:
        #     count +=1
        # print(count)