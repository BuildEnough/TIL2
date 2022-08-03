from pprint import pprint
import sys
sys.stdin = open("1236_성_지키기.txt")

# matrix = []
# for _ in range(n):
#     matrix.append([0] * m)

# matrix = [[0] * m for _ in range(n)]

# for _ in range(n):
#     C = list(input().split())
#     matrix.append(C)

# print(matrix)
# m_count = 0
# count = 0
# while m_count < n:
#     for i in matrix:
#         i = i.split()
#         # print(i, type(i))
#         m_count += 1
#         if 'X' in i:
#             count +=1
#             print(1)
#         else:
#             print(0)
#     print(count)


n, m = map(int, input().split()) # n: 행, m: 열
matrix = [input().split() for _ in range(n)]
count = 0
# print((matrix), type(matrix))
for i in matrix:
    # print(i , type(i))
    for j in i:
        # print(j, type(j))
        if 'X' not in j:
            count += 1
print(count)