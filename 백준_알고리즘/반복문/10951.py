while True:
    A, B = map(int, input().split())
    if A <= 0 and B >= 10:
        break
    print(A + B)