# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh

import sys
sys.stdin = open('최빈수_구하기.txt')


dic = {}
for i in range(int(input())):
    test = int(input())
    list_ = input().split()
    for i in list_:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    dic_list = list(dic.values())
    dic_list.sort()
    
    max_num = dic_list[-1]

    for j in dic:
        if str(dic[j]) in str(max_num):
            print(j)




T = int(input())
for i in range(T):
    idx = int(input())
    arr = list(map(int, input().split()))
    score = dict()
    for s in arr:
        if s in score:
            score[s] += 1
        else:
            score[s] = 1
    _max = max(score.values())

    print('#', end='')
    print(idx, next(key for key, value in score.items() if value == _max))