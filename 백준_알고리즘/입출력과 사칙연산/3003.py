import sys
sys.stdin = open('3003.txt')

board = [1, 1, 2, 2, 2, 8]

c = list(map(int, input().split()))

for i in range(6):
    print(board[i] - c[i], end= ' ')