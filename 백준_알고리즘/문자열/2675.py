import sys
sys.stdin = open('2675.txt')

for _ in range(int(input())):
    R, P = input().split()
    
    result = ''

    for i in P:
        result += (i * int(R))
    print(result)
