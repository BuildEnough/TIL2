# h의 처음 값과 마지막 값을
# if 문을 사용하여 하나씩 비교할 순 없을까

T = int(input())

for i in range(1, T + 1): # T번 반복

    h = input() # 일단 문장을 입력 받는다
    word = list(h) # h에 입력되는 데이터를 리스트로 만들어 word에 할당시킨다
    # print(word)
    rev = word[::-1] # rev에 word의 데이터 리스트를 역순환 시킨다
    # print(rev)
    if word == rev:
        print(f"#{i} {1}")
    else:
        print(f"#{i} {0}")