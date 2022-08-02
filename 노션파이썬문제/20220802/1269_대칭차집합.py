import sys
sys.stdin = open("1269_대칭차집합.txt")


# A = set([1, 2, 3, 4, 5])

# B = set([4, 5, 6, 7])

# print(A-B)

A, B = map(int, input().split())

# A = map(set, input().split())
# B = map(set, input().split())

A = set(input().split())
B = set(input().split())

# print(A)
# print(B)

# print(B-A)

print(len(A-B) + len(B-A))


# print(type(A)) # list
# print(B)

# A = set(A)

# print(A)


# for a in A:
#     A[int(a)] += input()
# for b in B:
#     B[int(b)] += input()


