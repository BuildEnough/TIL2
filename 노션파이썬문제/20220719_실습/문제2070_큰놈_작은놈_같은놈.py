# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.


t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    if a > b:
        print('#' + str(i), '>')
    elif a < b:
        print('#' + str(i), '<')
    else:
        print('#' + str(i), '=')
