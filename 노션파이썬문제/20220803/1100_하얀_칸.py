import sys
from pprint import pprint
sys.stdin = open("1100_하얀_칸.txt")

matrix = []

for _ in range(8):
    matrix.append(list(input()))

count = 0

# pprint(matrix)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if matrix[i][j] == 'F':
                count += 1
print(count)
