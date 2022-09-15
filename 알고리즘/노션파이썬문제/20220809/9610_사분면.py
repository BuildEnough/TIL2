import sys
sys.stdin = open('9610_사분면.txt')

Q1 = 0 # 1사분면
Q2 = 0 # 2사분면
Q3 = 0 # 3사분면
Q4 = 0 # 4사분면
AXIS = 0 # 중심선

for _ in range(int(input())):
    n, m = map(int, input().split())

    if n > 0 and m > 0:
        Q1 += 1
    elif n < 0 and m > 0:
        Q2 += 1
    elif n < 0 and m < 0:
        Q3 += 1
    elif n > 0 and m < 0:
        Q4 += 1
    elif n == 0 or m == 0:
        AXIS += 1
        
print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {AXIS}')