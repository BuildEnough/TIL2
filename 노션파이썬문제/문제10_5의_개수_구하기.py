# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
five_count = 0
for num in numbers:
    if num == 5:
        five_count += 1
print(five_count)