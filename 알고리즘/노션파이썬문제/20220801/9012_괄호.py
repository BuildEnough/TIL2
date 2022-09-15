import sys
sys.stdin = open("9012_괄호.txt")

N = int(input())

for _ in range(N):


    list_ = list(input())
    # print(list_)
    # print(len(list_))

    count = 0

    for i in range(len(list_)):
        if list_[i] == '(':
            count += 1 # '('면 +1
        else:
            count -= 1 # ')'면 -1
        if count < 0:
            break

    if count == 0: # () 짝이 맞으면 0이고 아니면 올바르지 않은 구성
        print('YES')
    else:
        print('NO')