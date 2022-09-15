import sys
sys.stdin = open('1453_피시방_알바.txt')

N = int(input())

c_list = list(map(int, input().split()))

c = []
# print(c_list[1])
count = 0
for i in range(N): 
    # print(c_list[i], type(c_list[i]))
    if c_list[i] in c:
        count += 1
    else:
        c.append(c_list[i])
# print(c)
print(count)


