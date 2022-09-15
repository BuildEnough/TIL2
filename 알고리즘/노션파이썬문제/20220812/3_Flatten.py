from ast import dump
import sys

sys.stdin = open("_Flatten.txt")

# 평탄화 진행 후 최대 차이 = 1
# 구하고 싶은 것: 제한된 횟수만큼 옮기는 작업을 한 후의
# 최고점과 최저점의 차이

# 제약 조건: 옮기는데 횟수제한 걸려있음
# 가로의 길이: 100 고정
# 1 <= 상자의 높이 <= 100
# 1 <= 덤프횟수 <= 1000
# 와 모르겠다 ㅋㅋ

for T in range(10) :
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        # print(max(box))
        
        box_max = box.index(max(box))
        # print(box_max)
        box[box_max] -= 1 # 최대값에서 -1

        box_min = box.index(min(box))
        box[box_min] += 1 # 최소값에서 +1

        A = max(box) - min(box)

    print(f'#{T+1} {A}')