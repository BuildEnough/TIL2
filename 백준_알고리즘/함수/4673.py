def d(n): # d(n): self_numbers
    n += sum(map(int, str(n)))
# for i in list(str(n)):
#     number += int(i)
# print(number)
    return n

# print(d(33))

self_numbers = []

for i in range(1, 10001):
    self_numbers.append(d(i))

for j in range(1, 10001):
    if j in self_numbers:
        pass
    else:
        print(j)