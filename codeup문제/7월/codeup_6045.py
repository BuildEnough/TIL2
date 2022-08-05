# 정수 3개를 입력받아 합과 평균을 출력해보자.
a, b, c = map(int, input().split())

list1 = [a, b ,c]

count = 0
for i in list1:
    count += 1

sum = a + b + c
avg = sum/count
print(sum, format(avg, '.2f'))