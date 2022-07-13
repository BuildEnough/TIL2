# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())

a1 = bool(a)
b1 = bool(b)

print((a1 and (not b1)) or ((not a1) and b1))

# a1과 b1에 다른 type를 입력하면 오류가 나는데 codeup에서는 정답이라고 뜨는게 이상함