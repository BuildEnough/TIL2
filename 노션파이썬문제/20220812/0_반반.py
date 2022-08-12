import sys

sys.stdin = open("_반반.txt")


# for _ in range(int(input())):
#     S = list(input())
#     # print(S)
#     S_list.append(S)

# print(S_list)

for T in range(int(input())):
    S = list(input())
    S.sort()

    if (S[0] == S[1]) and (S[2] == S[3]) and (S[0] != S[2]) and (S[0] != S[3]):
        print(f'#{T + 1} Yes')
    else:
        print(f'#{T + 1} No')
