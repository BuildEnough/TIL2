import sys
sys.stdin = open("1357_뒤집힌덧셈.txt")

X, Y = input().split()

# [::-1] 사용하면 되지 않을까?


def Rev(word):
    word = int(word[::-1])
    return word
# print(Rev(X)) X역수 잘나옴

sum = str(Rev(X)+Rev(Y)) # X와 Y의 역수를 더하고 문자열로 바꿔줘야 함수 안에서 역수로 바꿀수 있음

# print(type(sum))
print(Rev(sum))