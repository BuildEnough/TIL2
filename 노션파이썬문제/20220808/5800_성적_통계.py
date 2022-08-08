from re import L
import sys
sys.stdin = open('5800_성적_통계.txt')

K = int(input())


for k in range(K):
    score = list(map(int, input().split()))
    score = score[1:]
    max_ = max(score)
    min_ = min(score)

    score.sort()
    # print(score)

    gap_list = []
    for i in range(len(score)-1):
        gap_list.append(score[i+1]- score[i])
    gap_ = max(gap_list)

    print(f'Class {k+1}')
    print(f'Max {max_}, Min {min_}, Largest gap {gap_}')