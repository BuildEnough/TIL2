import sys

sys.stdin = open("3052_나머지.txt")

list_ = [] # 리스트 만들어줌

for i in range(10): # 10개 입력
    N = int(input())
    NA = N % 42 # 42로 나눠줌 => 나머지 값 저장
    # print(NA)
    list_.append(NA) # 나눈 값을 리스트에 저장
# print(list_)
list_ = set(list_) # set 이용하여 중복 제거
# print(type(list_))
print(len(list_)) # len으로 중복을 제거한 리스트의 값의 길이 출력