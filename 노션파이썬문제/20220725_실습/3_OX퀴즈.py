# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) # 테스트케이스 숫자 입력 5로 주어져 있음(다른 파일)
for testcase in range(T):
    OX = list(input())
    jumsu = 0 # 점수 변수인데 점점 커짐
    re_jumsu = 0 # X가 나왔을 때 0으로 돌리기 위한 변수
    # 그냥 for랑 if문 사용하니까 잘 안됨
    # 리스트 사용해야 되나?

    for ox in OX:
        #print(ox) # 일단 OX의 리스트가 잘 출력됨
        if ox == 'O': # ox가 O라면 
            jumsu += 1 # jumsu 변수에 1을 더함
            re_jumsu += jumsu # O이 나올수록 더해진 값을 re_jumsu 변수에 더함
        else:
            jumsu = 0 # ox가 X가 된다면 점수를 0으로 만든다
            # re_jumsu += jumsu # 필요하다고 생각했는데 절대 필요 없음, 그저 else 문에서 jumsu 변수만 초기화 하면 됨
    print(re_jumsu)

