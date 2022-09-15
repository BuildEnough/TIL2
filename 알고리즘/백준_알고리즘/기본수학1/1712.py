import sys
sys.stdin = open('1712.txt')

A, B, C = map(int, input().split())

# C * n = A + B * n
# n = A / (C - B) 
# A가 아무리 커도 B > C: 손익분기점 X
# C > B: 손익분기점 O
if B - C >= 0:
    print(-1)
else:
    print(A // (C - B) + 1)
# / 이걸하면 실수로 나옴 //로 해야함
# 그리고 +1 해줘야함: 손익분기점인 때가 최초로 이익이 발생하기 때문
 