name = ','.join(['홍길동', '김철수'])
print(name)

# numbers = ' '.join([10, 20, 100])
# 오류뜸
# 문자열이 아닌 숫자라서
numbers = ' '.join(map(str, [10, 20, 100]))
print(numbers)
