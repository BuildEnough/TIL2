#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq

import sys
sys.stdin = open('초심자의_회문_검사.txt')

for T in range(int(input())):
    word = input().strip()

    drow = word[::-1]
    # print(word, type(word))
    # print(drow, type(drow))
    if word == drow:
        print(f'#{T+1} 1')
    else:
        print(f'#{T+1} 0')