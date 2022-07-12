# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

n = 5
multiply = 1
while n > 0:
    multiply *= n
    n -= 1
print(multiply)
