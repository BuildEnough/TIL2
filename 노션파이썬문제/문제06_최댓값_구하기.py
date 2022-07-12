# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)
        
# 강사님 풀이
numbers = [0, 20, 100, 40]
max_num = 0
for n in numbers:
    # 만약 max값이n보다 작으면 바꾼다
    if max_num < n:
        max_num = n
print(max_num)