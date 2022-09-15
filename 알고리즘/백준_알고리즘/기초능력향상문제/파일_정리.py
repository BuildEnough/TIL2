# https://www.acmicpc.net/problem/20291

import sys
sys.stdin = open('파일_정리.txt')

# for i in range(int(input())):
#     file_ = input()
#     for i in file_:
#         if i == '.':
#             print(file_.index('.'))


file_dic = {}
for i in range(int(input())):
    file_name = input()
    file_name = file_name.split('.')[1]
    if file_name in file_dic:
        file_dic[file_name] += 1
    else:
        file_dic[file_name] = 1

file_name = list(file_dic.keys())

file_name.sort()

for j in file_name:
    print(j, file_dic[j])









# N = int(input())
# ext = {}
# for i in range(N):
#     f_n = input().strip()
#     file_name = f_n.split('.')[1]
#     if file_name not in ext:
#         ext[file_name] = 1
#     else:
#         ext[file_name] += 1

# file_name = list(ext.keys())

# file_name.sort()
# for z in file_name:
#     print(z, ext[z])