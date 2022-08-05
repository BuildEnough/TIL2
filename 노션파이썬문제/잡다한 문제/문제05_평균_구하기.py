# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

numbers = [3, 10, 20]

avg = (numbers[0] + numbers[1] + numbers[2])/3
avg = int(avg)
print(avg)

# 강사님 해설
numbers = [3, 10, 20]
result = 0
count = 0

for numbers in numbers:
    result += numbers
    count = count + 1

print(result/count)