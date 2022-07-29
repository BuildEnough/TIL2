import sys
sys.stdin = open("5622_다이얼.txt")
# print(ord('A')) # 65


d_alpha = {
    'A': 2, 'B': 2, 'C': 2,
    'D': 3, 'E': 3, 'F': 3,
    'G': 4, 'H': 4, 'I': 4,
    'J': 5, 'K': 5, 'L': 5,
    'M': 6, 'N': 6, 'O': 6,
    'P': 7, 'Q': 7, 'R': 7, 'S': 7,
    'T': 8, 'U' : 8, 'V': 8,
    'W': 9, 'X': 9, 'Y': 9, 'Z': 9
} # 각 숫자에 1을 더할까 생각했지만 직관적으로 보이기 위해 그냥 놔둠
# print(d_alpha['Z']) # 9

sum = 0


word = input()
len_ = len(word) # len 함수 if문 안에 안 넣을려고 if문 밖에서 만들어줌
# print(len_)

if len_ >= 2 and len_ <= 15: # 2 <= 단어 <= 15
    for i in word:
        # print(i, end ='')
        # print(type(d_alpha[i])) # int
        sum += d_alpha[i] + 1 # 숫자 1을 거는데 1초니까 각 주어진 숫자에서 1을 더하고 그 값을 sum에 저장함
    print(sum)