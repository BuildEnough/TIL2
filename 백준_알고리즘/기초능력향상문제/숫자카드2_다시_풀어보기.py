# https://www.acmicpc.net/problem/10816

import sys
sys.stdin = open('숫자카드2.txt')

N = int(input())
num_list = list(map(int, input().split()))
nums = {}
for num in num_list:
    if num not in nums:
        nums[num] = 1
    else:
        nums[num] += 1

M = int(input())
num_list = list(map(int, input().split()))
for num in num_list:
    if num in nums:
        print(nums[num], end = ' ')
    else:
        print(0, end = ' ')




# N = int(input())
# N_card = list(input().split())

# M = int(input())
# M_card = list(input().split())

# count = 0

# list_ = []

# for i in M_card:
#     a = N_card.count(i)
#     print(a, end = '')