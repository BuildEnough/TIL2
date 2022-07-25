# https://www.acmicpc.net/problem/2908
from audioop import reverse
import sys

sys.stdin = open("1_상수.txt")

A, B = list(input().split()) # A와 B를 입력 -> split을 사용하여 띄어쓰기 입력하게 하고, map을 사용하여 int로 형변환 해준다
# reserve는 리스트에만 적용되는거 같다
# 그리면 입력한 값들을 리스트로 바꿔서 reverse 함수를 사용하면 될 듯 싶다
# 근데 [::-1] 사용하면 뒤로 읽는 것 아닌가?
# print(A[::-1]) # 뒤로 읽는거 맞음
# 그럼 굳이 리스트로 안바꾸고 뒤로 읽은 것을 숫자형으로 바꿔서 큰 것 나오게 하면됨
A = A[::-1]
B = B[::-1]

A = int(A)
B = int(B)

# print(type(A)) # 여기까지 반대로 나오게 하고 숫자형으로 바꿈
# 그럼 두 수 중 큰 것을 출력시키면 됨
if A > B:
    print(A) # A가 B보다 크면 A출력
else:
    print(B) # B가 A보다 같거나 큰 경우인데 0은 포함되어 있지 않음