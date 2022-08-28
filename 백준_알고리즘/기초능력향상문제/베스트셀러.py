import sys
sys.stdin = open('베스트셀러txt')

books = {}

for _ in range(int(input())):
    book = input()

    books