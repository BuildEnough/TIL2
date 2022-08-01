import sys
sys.stdin = open("14720_우유_축제.txt")

store = int(input()) # 가게 수

milk = list(map(int, input().split())) # milk라는 변수 안에 순서를 만들 수 있는 리스트 생성

count = 0

for i in range(store):
    if milk[i] == count % 3:
        count = count + 1

print(count)