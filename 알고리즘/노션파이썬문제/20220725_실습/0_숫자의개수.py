# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

# 자연수 3개를 입력받는다
A = int(input())
B = int(input())
C = int(input())

multi = A * B * C # 자연수 곱한 값을 multi 변수에 저장함
# print(multi) # 17037300

# 각 자리수에서 구하는 거니까 리스트를 사용하는 것이 더 좋을거 같음
jarisu = list(str(multi))  # multi에 저장되어 있는 수를 문자열로 바꾸고 이를 리스트로 바꿈
# print(jarisu) # ['1', '7', '0', '3', '7', '3', '0', '0']

for i in range(10): # 0~9의 숫자라 차례대로 나와야 하므로 range에 10을 넣음
    # print(i) # 확인차 출력
    # count 함수 사용하면 몇개 있는지 알 수 있음
    # i에 multi의 각 숫자들이 순회함
    # print(type(i)) # 문자열로 안바꿔주면 multi는 이미 문자열로 바껴서 카운트가 안됨
    # 따라서 str을 사용하여 같은 문자열로 바꿔줘야함
    print(jarisu.count(str(i)))
