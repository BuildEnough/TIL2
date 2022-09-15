N = int(input())

# 방법1
sum_ = 0 # 더해진 값 그냥 사용하면 오류나서 초기값 설정해줬음
for i in range(1, N +1):
    A = list(map(int, str(i))) # N까지 입력된 수를 문자열로 바꾸고 리스트로 바꿈
    # print(A) # 1부터 N까지 리스트로 출력됨
    # print(sum(A)) # 각 자리수의 합이 더해짐
    # 그러면 i는 N까지 순회하니까 더해진 값이랑 더하면 생성자가 나올거 같음
    # print(i + sum(A)) # 잘 나옴
    sum_ = i + sum(A) # sum_ 변수에 더한값 할당시킴
    if sum_ == N:
        print(i)
        break # 가장 작은 생성자가 나와야 하기때문에 break문 넣어줌
    elif i == N: # 생성자가 없는 경우는 i와 N이 같을 때, 입력한 값과 같으면 생성자가 없는 것임
        print(0)

# 방법2
# print(str(N)) # N(str)
# print(len(str(N))) # 216 -> 3(int)
# 가장 큰 생성자는 9, 99, 999와 같이 생성자의 숫자가 9일때 가장 큼
# N의 수에 9를 곱한 것을 N에 -해줌
# 9를 곱한 값보다 N이 작으면 음수됨
A = N - 9*len(str(N)) # len 함수 사용하려면 str로 바꿔줘야 함

if A > 1: # N에서 뺀 값이 1보다 크면 그대로 A
    A 
else: # N에서 뺀 값이 1보다 작으면 A는 1
    A = 1

for i in range(A, N+1): # A부터 N까지 for문 실행
    # print(A)
    # print(str(i))
    BI = i + sum(map(int, str(i)))
    # print(BI)
    if N == BI: # BI가 입력한 값 N과 같으면 i 출력
        print(i)
        break

    if i == N: # 생성자가 없는 경우는 i와 N이 같을 때, 입력한 값과 같으면 생성자가 없는 것임
        print(0)