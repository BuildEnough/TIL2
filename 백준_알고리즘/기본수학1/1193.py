import sys
sys.stdin = open('1193.txt')

# 1/1: 1 => 2
# 1/2: 2 => 3
# 2/1: 3 => 3
# 3/1: 4 => 4
# 2/2: 5 => 4
# 1/3: 6 => 4
# 1/4: 7

# 분자와 분모의 합이 1씩 커질때 마다, 분자 <-> 분모

x = int(input())
num_list = []

num = 0
num_count = 0

while num_count < x:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = x - num_count
    j = num - i + 1
else:
    i = num - (x - num_count) + 1
    j = x - num_count

print(f"{i}/{j}")