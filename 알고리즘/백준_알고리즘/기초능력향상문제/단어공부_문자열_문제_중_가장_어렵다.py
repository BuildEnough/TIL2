# https://www.acmicpc.net/problem/1157

import sys
sys.stdin = open('단어공부.txt')

word = input().lower()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)
    
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))].upper())


