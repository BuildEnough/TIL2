# https://www.acmicpc.net/problem/10807

import sys
sys.stdin = open('개수세기.txt')

N = int(input())

n = list(input().split())

v = input()

count = 0
for i in n:
    if v == i: # if v in i:로 했는데 오류남 처음엔 개빡쳤는데 하다보니까 이유를 암
                # in을 사용하면 있다는 것만 알고 i값이 2개라고 해도 되는데?
                # 반복문 이니까 돌아가면서 v가 있기만 하면 되잖아
                # 근데 왜 in은 답으로 안쳐주는지 개빡치네,,
        count += 1
print(count)
