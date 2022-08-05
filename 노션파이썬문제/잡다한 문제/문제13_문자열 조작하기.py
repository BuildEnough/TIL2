# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

word = input()

reverse_word = ''
len = len(word) - 1
while len >= 0:
    reverse_word += word[len]
    len -= 1
print(reverse_word)

# 강사님 풀이
word = 'apple'
result= ''
for char in word:
    result = char + result

print(result)
print(word[::-1])
print(''.join(reverser(word)))


# 3. index 조작
# index에 익술해질수록 알고리즘 코드 풀기 쉽다
word = 'apple'

for i in range(len(word)):
    #print(i)
    print(word[len(word)-i-1], end='')


# sep (' '): 여러 개를 동시에 출력할 때 사이에 구분값
# end ('\n') = 개행 : print(출력이 된 이후 뒤에 뭐를 붙일 때)
print(1, end='수업끝~')
print(2, end='끝~')
print(3)