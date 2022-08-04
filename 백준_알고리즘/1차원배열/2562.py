import sys
sys.stdin  = open('2562.txt')

list_ = []
count = 0

for _ in range(9):
    n = int(input())
    list_.append(n)

# list_ = [input() for _ in range(9)]

print(max(list_))
print(list_.index(max(list_)) + 1)

# comprehension
# list_ = [int(input()) for _ in range(9)]