import sys
sys.stdin = open('14467_소가_길을_건나간_이유1.txt')

cow = {}
count = 0

for _ in range(int(input())):
    num, road = map(int, input().split())
    if num not in cow: # 소의 번호가 cow 딕셔너리에 없으면
        cow[num] = road # 입력된 값 2개를 딕셔너리에 저장
    else: # 소의 번호가 딕셔너리에 이미 있을때
        if cow[num] != road: # road의 수가 다르면 count에 1을 더해주고
            count += 1
            cow[num] = road # road가 다른 걸 다시 저장시켜줌
print(count)