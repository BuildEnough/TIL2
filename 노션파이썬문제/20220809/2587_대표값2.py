import sys
sys.stdin = open('2587_대표값2.txt')

sum_ = 0
num_list = []
count = 0

while True:
    try:
        num = int(input())
        sum_ += num
        num_list.append(num)
        count += 1
    except:
        break

print(int(sum_ / count))


num_list.sort()

n = len(num_list)

if n % 2 == 1:
    m = ((n + 1) / 2)
    # print(type(m)) # list
    print(num_list[int(m-1)]) # 1번째 부터 세기 때문에 -1
else:
    m = ((n/2) * ((n /2) + 1))
    print(num_list[int(m-1)])