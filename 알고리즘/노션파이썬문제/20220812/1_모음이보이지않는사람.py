
import sys

sys.stdin = open("_모음이보이지않는사람.txt")

word_list = ['a', 'e', 'i', 'o', 'u']

for T in range(int(input())):
    word = input()

    for i in word_list:
        word = word.replace(i, '')
    print(f'#{T+1} {word}')