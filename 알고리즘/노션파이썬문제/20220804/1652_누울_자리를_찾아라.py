from pprint import pprint
import sys
sys.stdin = open('1652_누울_자리를_찾아라.txt')

r_count = 0
c_count = 0
r_result = 0
c_result = 0
# print(result[0], type(result[0]))

room = []
N = int(input())
for i in range(N):
    room.append(list(input()))
# pprint(room)

for i in range(N):
    for j in range(N):
        # print(room[i][j], end = ' ')   
    # print()
        if room[i][j] == '.':
            r_count += 1
        elif room[i][j] == 'X':
            r_count = 0
        if r_count == 2:
            r_result += 1
    r_count = 0

for i in range(N):
    for j in range(N):
        # print(room[j][i], end = ' ')   
    # print()
        if room[j][i] == '.':
            c_count += 1
        elif room[j][i] == 'X':
            c_count = 0
        if c_count == 2:
            c_result += 1
    c_count = 0 # 디버깅 해보니까 다음 열로 넘어가는 구간에서 초기화를 안해주니까
    # 다음꺼랑 같이 카운트돼서 더 많이 나올 수도 있었음


print(r_result, c_result)


# room = []

# for i in range(N):
#     for j in range(N):
#         room.append(lay * N)
# pprint(room)