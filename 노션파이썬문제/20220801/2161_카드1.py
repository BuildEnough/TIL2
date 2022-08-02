import sys
sys.stdin = open("2161_카드1.txt")

N = int(input())

CARD = list(range(1, N+1))
# print(CARD)
trash = []

while len(CARD) > 1: # 계속 빼서 남아있는 수가 없을때까지 반복
    trash.append(CARD[0]) # 버리는 카드 trash 리스트에 저장
    CARD = CARD[2:] + [CARD[1]] # 3번째 카드 0, 2번째 카드 제일 뒤로
trash.append(CARD[0]) # while 탈출 후 맨마지막 남은 숫자 trash 리스트에 저장
        # 이거안하면 맨마지막 숫자 안나옴
for i in trash:
    print(i, end=' ')