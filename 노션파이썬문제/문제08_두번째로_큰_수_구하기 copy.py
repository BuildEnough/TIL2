# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지
numbers = [0, 20, 100, 40]
max = 0
sec = 0
for i in numbers:
    if i > max:
        max = i
        
numbers = list(numbers)    
numbers.remove(max)
for i in numbers:
    if i > sec:
        sec = i
print(sec)

# 강사님 풀이
numbers = [0, 20, 100, 40]
max_number = numbers[0]
second_number = numbers[0]

for n in numbers:
    # 만약에, n이 최대보다 크다면
    if max_number < n:
        # 최대값이었던 것이 두 번째로 큰 수
        second_number = max_number
        max_number = n
    #elif second_number <n < max_number:
    elif second_number < n and n < max_number:
        second_number = n
print(second_number)