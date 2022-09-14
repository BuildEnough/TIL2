# https://www.acmicpc.net/problem/2511

import sys
sys.stdin = open('카드놀이.txt')

A = list(map(int, (input().split())))
B = list(map(int, (input().split())))

A_score = 0
B_score = 0

score = []

for i in range(10):
    if A[i] > B[i]:
        score.append('A')
    elif A[i] < B[i]:
        score.append('B')
    else:
        score.append('D')
    
for i in score:
    if i == 'A':
        A_score += 3
    elif i == 'D':
        A_score += 1
        B_score += 1
    else:
        B_score += 3


remove_set = {'D'}

if A == B:
    print(A_score, B_score)
    print('D')
elif A_score > B_score:
    print(A_score, B_score)
    print('A')
elif A_score < B_score:
    print(A_score, B_score)
    print('B')
else:
    score = [i for i in score if i not in remove_set]
    print(A_score, B_score)
    print(score[-1])

