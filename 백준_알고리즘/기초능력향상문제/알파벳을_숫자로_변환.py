import sys
sys.stdin = open('알파벳을_숫자로_변환.txt')

alphabet = list(input())

for i in alphabet:
    print(ord(i)-64, end=' ')