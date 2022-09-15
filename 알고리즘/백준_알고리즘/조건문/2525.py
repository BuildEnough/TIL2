H, M  = map(int, input().split())
input_time = int(input())

H += input_time // 60
M += input_time % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(H, M)

