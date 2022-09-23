# https://www.acmicpc.net/problem/1543

import sys
sys.stdin = open('문서_검색.txt')

document = input()
word = input()

result = 0
index = 0

for i in range(len(document)):
    if index > i:
        continue
    if word == document[i: i + len(word)]:
        result += 1
        index = i + len(word)

print(result)
        