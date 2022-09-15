# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

# ord 표 봐야함

a = ord(input())
m = ord('a')

while a >= m:
    print(chr(m), end=' ')
    m += 1