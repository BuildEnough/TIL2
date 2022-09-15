# 약수 : 정수로 떨어지는 수

# 공약수 : 두 숫자 사이의 공통으로 존재하는 약수
# 최대공약수 : 공약수 중에서 가장 큰 숫자

# 공배수 : 두 수의 공통적인 배수
# 최소공배수 : 공배수 중 제일 작은 공배수

# 약수부터 출력해볼까 싶음
# while True:
#     A = int(input())
#     if A == 0:
#         break
#     for i in range(1, A+1):
#         if A % i == 0:
#             print(i)

# 최대공약수 구하기
A, B = map(int, input().split())
# if A == 0 or B == 0: # 이거 왜 안됨?
#     break             # 이거 왜 안됨?

for i in range(1, max(A, B)): # A와 B 중 제일 큰 값까지 1에서 순회반복
    if A % i == 0 and B % i == 0:
        # print(i) # 공약수들
        max_ = i # i를 max_변수에 할당시켜줌, i에 약수들에서 제일 마지막 수 -> 가장 큰 값이 옴
print(max_) # 즉, 공약수의 맨 마지막 값이 제일 크고, 이것이 공약수 중에 가장 크기 때문에 최대 공약수이다


for i in range(max(A, B), A*B + 1): # A와 B의 공통된 숫자부터니까 A, B 중 큰 수부터 A와 B 곱한 값까지 순회반복
    if (i % A == 0) and (i % B == 0): # 입력된 값들이 나눠 각각 0이되는 첫 숫자가 최소공배수
        print(i)
        break