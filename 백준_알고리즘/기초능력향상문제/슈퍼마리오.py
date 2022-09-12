# https://www.acmicpc.net/problem/2851

import sys
sys.stdin = open('슈퍼마리오.txt')

list_ = []
sum_ = 0

for _ in range(10):
    list_.append(int(input()))
# print(list_)

for i in list_:
    sum_ += i

    if sum_ > 100:
        if sum_ - 100 > 100 - (sum_ - i):
            sum_ -= i
        break
print(sum_)





# for _ in range(10):

#     m = int(input())

#     sum_ += m

#     list_.append(sum_)


# result = []
# for i in list_:
#     a = i - 100
    
#     result.append(abs(a))

# b = min(result)

# c = result.index(b)

# print(c[1])





