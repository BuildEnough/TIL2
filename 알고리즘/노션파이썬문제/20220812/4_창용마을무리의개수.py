import sys

sys.stdin = open("_창용마을무리의개수.txt")

for T in range(int(input())):
    N, M = map(int, input().split())
    # N: 마을에 사는 사람의 수
    # M: 서로를 알고 있는 사람의 관계 수(M개의 줄에 걸쳐 서로를 알고 있는 두 사람의 번호가 주어짐)
    # M은 N(N-1)/2보니까 거듭제곱?
    
    for m in range(M):
        A, B = map(int, input().split())
        print(A, B)