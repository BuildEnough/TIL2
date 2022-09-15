# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

# input = 1234
# output = 4321


import sys

sys.stdin = open("input.txt", "r")

n = int(input())

re = 0
while n > 0:
    re = n % 10
    n //= 10
    print(re, end='')



# 강사님 풀이
# 1. 
number = 123

# print(str(number)[::-1])

# 2. 
result = 0
while number:
    result *=10
    result += number % 10
    number //= 10

print(result)