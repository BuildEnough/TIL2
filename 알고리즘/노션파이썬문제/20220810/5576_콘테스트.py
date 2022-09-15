import sys
sys.stdin = open('5576_콘테스트.txt')

s_list = []

for i in range(20):
    score = int(input())
    s_list.append(score)

A = s_list[:10]
B = s_list[10:]

A.sort(reverse=1)
B.sort(reverse=1)

A = A[:3]
B = B[:3]

print(sum(A), sum(B))
