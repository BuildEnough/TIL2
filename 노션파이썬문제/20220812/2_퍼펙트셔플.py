import sys

sys.stdin = open("_퍼펙트셔플.txt")


for T in range(int(input())):
    N = int(input())
    card = input().split()
    # print(card, type(card))
    # print(len(card))

    if len(card) % 2 == 0:
        F = card[:N//2]
        S = card[N//2:]
    else:
        F = card[:N//2 + 1]
        S = card[N//2 + 1:]
    # print(S)

    # count = 0
    result = ''

    for i in range(len(card)//2):
        if len(card) % 2 == 0:
            a = F[i] + ' ' + S[i] + ' '
            result += a
            # print(result)
        else:
            if i == len(card)//2 - 1:
                a = F[i] + ' ' + S[i] + ' ' + F[-1]
                result += a
            else:
                a = F[i] + ' ' + S[i] + ' '
                result += a

    print(f'#{T+1} {result}')

    
#1 A D B E C F
#1 A D B E C F 
#2 JACK KING QUEEN ACE
#2 JACK KING QUEEN ACE 
#3 ALAKIR LORD-JARAXXUS ALEXSTRASZA AVIANA DR-BOOM
#3 ALAKIR LORD-JARAXXUS ALEXSTRASZA ALEXSTRASZA AVIANA DR-BOOM

