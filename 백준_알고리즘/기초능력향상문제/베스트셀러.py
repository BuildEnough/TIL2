# https://www.acmicpc.net/problem/1302

import sys
sys.stdin = open('베스트셀러.txt')

n = int(input())
books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] +=1

max_freq = max(books.values())

best_seller=[]

for book, number in books.items():
    if number ==max_freq:
        best_seller.append(book)

print(sorted(best_seller)[0])