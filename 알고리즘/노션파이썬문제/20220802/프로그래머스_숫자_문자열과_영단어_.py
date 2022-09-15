import sys
sys.stdin = open("프로그래머스_숫자_문자열과_영단어.txt")

word = input()

dic = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
answer = word

for i in dic.items():
    # print(i[0])
    answer = answer.replace(i[0], str(i[1]))
answer = answer.replace("'", "")    
print(answer)