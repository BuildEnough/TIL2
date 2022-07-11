numbers = input().split()
a = int(numbers[0])
b = int(numbers[1])
print(a)
print(b)


# 결과 동시 할당
a, b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)


# 고급 방법
a, b = map(int, input().split())
print(a, type(a))
print(b, type(b))