# X = 110

# X_list = []
# for i in range(1, X+1):
#     X_list.append(i)

# X_count = 0
# for j in X_list:
#     if j < 100:
#         X_count += 1
#         print(str(j)[2])    
# #     elif j[2] - j[1] == j[1] - j[0]:
# #         X_count += 1
# # print(X_count)
n = int(input())
X_count = 0
for i in range(1, n+1):
    X_list = list(map(int, str(i)))
    if i < 100:
        X_count += 1
    elif X_list[2] - X_list[1] == X_list[1] - X_list[0]:
        X_count += 1
print(X_count)