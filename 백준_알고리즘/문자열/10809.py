import sys
sys.stdin = open('10809.txt')

S = input()

alpha = list(range(97, 123))

for i in alpha:
    print(S.find(chr(i)), end = ' ')
        



# a: 97
# z: 122