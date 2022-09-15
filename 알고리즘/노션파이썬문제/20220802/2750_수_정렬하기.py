import sys
sys.stdin = open("2750_수_정렬하기.txt")

# N = int(input())

list_ = []

for i in range(int(input())):
    X = int(input())
    list_.append(X)
# print(list_)
list_.sort()
# print(list_)
for j in list_:
    print(j)