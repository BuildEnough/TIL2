A = int(input())
B = input()
B = B[::-1]
for i in B:
    print(int(i) * A)
B = B[::-1]
print(int(A) * int(B))