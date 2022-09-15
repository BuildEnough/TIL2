import sys
sys.stdin = open('11170_0의_개수.txt')

for _ in range(int(input())):
    N, M = map(int, input().split())
    count = 0

    for i in range(N, M+1):
        i = list(str(i))
        for j in i:
            if '0' in j:
                count += 1
    print(count)
