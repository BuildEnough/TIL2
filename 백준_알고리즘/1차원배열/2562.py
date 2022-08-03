import sys
sys.stdin  = open('2562.txt')

list_ = []
count = 0

for _ in range(9):
    n = input()
    list_.append(n)

print(max(list_))
print(list_.index(max(list_)) + 1)

# comprehension