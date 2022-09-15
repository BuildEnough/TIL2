import sys
sys.stdin = open('10101_삼각형_외우기.txt')

# angles = []

# while 1:
#     try:
#         angle = input()
#         angles.append(angle)
#     except:
#         break
# print(sum(angles))


# # if sum(angles) != 180:
# #     print('ERROR')

# 어짜피 삼각형 각 3개
# 그냥 input 사용해야겠다

F = int(input())
S = int(input())
T = int(input())



if F + S + T == 180:
    if F == S == T == 60:
        print('Equilateral')
    elif F == S or F == T or S == T:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')