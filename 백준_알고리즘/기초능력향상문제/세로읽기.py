# https://www.acmicpc.net/problem/10798

import sys
sys.stdin = open('세로읽기.txt')


# word_list = []
# length_list = []

# for _ in range(5):
#     word = input()
#     word_list.append(word)
#     length_list.append(len(word))

# result = ''

# for i in range(max(length_list)):
#     for j in range(5):
#         if i < length_list[j]:
#             result += word_list[j][i]
        
# print(result)

words = [input() for i in range(5)]

for i in range(5):
    for j in range(15):
        if j < len(words[i]):
            print(f'{words[j][i]}')
        print()

