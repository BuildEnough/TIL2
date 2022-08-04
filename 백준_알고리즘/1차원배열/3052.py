import sys
sys.stdin = open('3052.txt')

list_ = []
count = 0

for i in range(10):
    n = int(input())
    
    na = n % 42

    list_.append(na)
# print(list_)
list_ = set(list_)
print(len(list_))    