import sys
sys.stdin = open('10818.txt')
n = input()
integer = list(map(int, (input().split())))

print(min(integer), max(integer))