# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# output : 5.5

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# count += 1문이 for문 안에 들어가야 number_list가 for문에서
# 돌때마다 증가됨
# //는 몫을 구하는 연산자라서 5.5가 나오기 위해 / 연산자를 이용해야함

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)

# 강사님 해설