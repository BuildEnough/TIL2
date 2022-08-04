import sys
sys.stdin = open('2577.txt')

A = int(input())
B = int(input())
C = int(input())

muti = A * B * C

jari = list(str(muti))

for i in range(10):
    print(jari.count(str(i)))