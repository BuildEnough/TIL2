numbers = ['1', '2', '3']

# 숫자로 바꿔서 쓰고 싶다?
# 리스트를 숫자로 형 변환은 불가능
# 다만,ㅣ 숫자 형태의 문자를 변환할 수 있음
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
new_numbers = [a, b, c]

# 반복분
numbers = ['1', '2', '3']
print(numbers)
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# map
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2)
print(list(new_numbers_2))
# 리스트로 형변환해서보면 바뀌어있다
# 보기 위해서 바꾼 것일 뿐, 반드시 list로 바꿔야하는 것은 아님