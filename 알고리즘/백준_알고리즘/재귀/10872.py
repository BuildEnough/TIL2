import sys
sys.stdin = open('10872.txt')

N = int(input())

result = 1

for i in range(1, N+1):
    result *= i
print(result)