import sys
sys.stdin = open("1292_쉽게푸는문제.txt")

F, S = map(int, input().split()) # F: First, S: Second

N = 1

# 리스트를 만들어서 for문 사용하는게 좋지 않을까?
list_ = []

for i in range(S+1): # 뒤에 입력되는 값이 무조건 큼
# print(list_) # [1, 2, 3, 4, 5, 6, 7] 만듬
    for j in range(N):
        list_.append(N)
print(list_,len(list_))

# 못풀었음 ㅠ

while len(list_) < S:
    for _ in range(N):
        list_.append(N)
print(list_)