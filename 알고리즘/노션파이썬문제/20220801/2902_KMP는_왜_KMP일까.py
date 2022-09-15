import sys
sys.stdin = open("2902_KMP는_왜_KMP일까_.txt")

name = list(input().split('-'))
for i in name:
    # print(i)
    print(i[0], end = '')