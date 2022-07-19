# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

# input = 123
# output = 6

from contextlib import AbstractAsyncContextManager
from math import remainder
from re import A
import sys

sys.stdin = open("input.txt", "r")

number = int(input())

number = str(number)

sum_n = 0

for i in number:
    i = int(i)
    sum_n += i
print(sum_n)


# 강사님 풀이
number = 123

# number가 0일 때 Stop!
# => int는 0일 때 False가 되기 때문
result = 0
while number:
    # 몫은 다음 number 됨
    # 나머지는 더해나가면 됨

    # 1. 
    # result += number % 10
    # number //= 10

# print(result)

    # 2.
    # divmod(x, y)는 x를 y로 나누고,
    # 결과를 tuple로 반환
    # (몫, 나머지)
    number, remainder = divmod(number, 10)
    result += remainder

print(result)

