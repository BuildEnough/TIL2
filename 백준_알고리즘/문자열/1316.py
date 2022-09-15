from ctypes.wintypes import WORD
import sys
sys.stdin = open('1316.txt')

n = int(input())
result = n
for i in range(n):
    word = input()

    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            if word[j+1] in word[:j]:
                result -= 1
                break
print(result)