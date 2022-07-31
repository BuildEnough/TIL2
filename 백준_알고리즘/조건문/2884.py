H, M = map(int, input().split())
origin_M = M
if M >= 45:
    print(H, M - 45)
elif H == 0 and M < 45:
    H = 23
    print(H, M + 15)
else:
    print(H - 1, M + 15)