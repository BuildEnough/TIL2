import sys
sys.stdin = open('1110.txt')

N = int(input()) # 26
NN = N 
count = 0

while True:
    a = NN // 10 # 2
    b = NN % 10 # 6
    c = (a + b) % 10 # 8
    NN = (b * 10) + c # 68
    count += 1
    if (N == NN):
        break
print(count)

#     SN = int(a + b) # 8

#     NN = str(b) + str(SN) # 68
#     count += 1
#     NN = int(NN)
#     if NN == N:
#         break
#     N = NN
# print(count)






# count = 0

# while True:
#     sum_ = int(N[0]) + int(N[-1])
#     N_ = N[-1] + str(sum_)
#     count += 1
    
#     if N_ == N:
#         break
# print(count)