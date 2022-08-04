from pprint import pprint
import sys
sys.stdin = open('2669_직사각형_네개의_합집합의_면적_구하기.txt')

matrix = []

for i in range(10):
        matrix.append([0] * 10)
# print(matrix)

for z in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix

