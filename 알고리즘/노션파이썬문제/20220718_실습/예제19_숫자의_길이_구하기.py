# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

# input : 123
# ouput : 3

number = 123

output = 0

while number > 0:
    number = number // 10
    output += 1
print(output)


# 강사님 해설
number = 0

# 1. 123
cnt = 0
# 몫이 0이 되면 종료해야하니까
# int : 0이 아닌 다른 수이면 무조건 True!
# while number:
while number != 0:
    # number = number // 10
    number //= 10
    number += 1

print(cnt)


# 2. 문자열로 형변환
# print(len(str(number)))

# 3. log
import math
number = 123456
print(int(math.log(number, 10)) + 1)