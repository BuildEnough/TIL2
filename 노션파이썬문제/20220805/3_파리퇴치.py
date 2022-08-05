from pprint import pprint
import sys

sys.stdin = open("_파리퇴치.txt")


for T in range(int(input())):

    N, M = map(int,(input().split()))
    matrix = []


    for _ in range(N):
        line = list(input())
        matrix.append(line)
        print(line)