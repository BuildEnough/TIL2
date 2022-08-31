# https://www.acmicpc.net/problem/1302

import sys
sys.stdin = open('베스트셀러.txt')

books = {}

for _ in range(int(input())):
    book = input()

    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

result = max(books.values())

list_ = []

for i in books:
    if result == books[i]:
        list_.append(i)

list_.sort()

print(list_[0])