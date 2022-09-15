from re import A
import sys
sys.stdin = open('2292.txt')

# 1 -> 7 -> 19 -> 37
# 6 -- 12 -- 18

num = int(input())

bee_house = 1
a = 0
count = 1


while num > bee_house:
    a += 6
    bee_house += a
    count +=1
print(count)