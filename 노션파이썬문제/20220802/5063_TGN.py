import sys
sys.stdin = open("5063_TGN.txt")

# N = int(input())

for i in range(int(input())):
    r, e, c = map(int, input().split())
    if r < e-c:
        print("advertise")
    elif r == e-c:
        print("does not matter")
    else:
        print("do not advertise")