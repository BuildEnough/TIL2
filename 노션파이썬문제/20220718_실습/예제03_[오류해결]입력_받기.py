# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# input : 10 20
# output : 30

# numbers = input().split()
# print(sum(numbers))

# 현재는 numbers가 문자열이기 때문에 map을 사용하여 int로 바꿔줌

numbers = map(int, input().split())
print(sum(numbers))