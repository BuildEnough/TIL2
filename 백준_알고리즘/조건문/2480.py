F, S, T = map(int, input().split())

if F == S == T:
    print(10000 + F * 1000)
elif F == S:
    print(1000 + F * 100)
elif F == T:
    print(1000 + F * 100)
elif S == T:
    print(1000 + S * 100)
else:
    print(max(F, S, T) * 100)