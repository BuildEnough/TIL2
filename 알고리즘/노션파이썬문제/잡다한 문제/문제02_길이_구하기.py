# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len() 함수를 바로 쓰기보다는 반복문을 활용하세요.

word = 'happy!'
count = 0
for i in word:
    count += 1
print(count)


# 강사님 풀이
word = 'happy!'
count = 0
for char in word:
    count = count + 1
print(count)