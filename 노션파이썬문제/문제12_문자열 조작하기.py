# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

word = input()
e_a_list = []
for i in word:
    if i != 'a':
        e_a_list.append(i)

a_list = ""
for j in e_a_list:
    a_list += j

print(a_list)


# 강사님 풀이

word = 'apple'
# 반복 for문 편함
for char in 'apple':
    # 만약 a 일때
    if char == 'a':
        result = result + char
        # 반복문에서 아무것도 안하고 넘어가는 것?
        # continue
        #continue
print(result)