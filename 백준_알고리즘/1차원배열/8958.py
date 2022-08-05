import sys
sys.stdin = open('8958.txt')

count = 0
result = 0

for _ in range(int(input())):
    quiz = list(input())
    for i in quiz:
        if i == 'O':
            count += 1
            result += count
        elif i == 'X':
            count = 0
    print(result)
    result = 0
    count = 0