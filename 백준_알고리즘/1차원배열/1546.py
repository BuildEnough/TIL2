import sys
sys.stdin = open('1546.txt')

list_ = []

N = int(input())
scores = list(map(int, input().split()))
max_ = max(scores)

for i in scores:
    list_.append(i / max_ * 100)

avg_ = sum(list_) / N
print(avg_)
