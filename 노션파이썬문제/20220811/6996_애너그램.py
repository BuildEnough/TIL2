import sys
sys.stdin = open('6996_애너그램.txt')

for _ in range(int(input())):
    A, B = map(str, input().split())
    
    a = list(A)
    b = list(B)

    a.sort()
    b.sort()
    
    if a == b:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')