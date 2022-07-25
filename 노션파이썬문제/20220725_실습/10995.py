star = int(input())
for i in range(1, star + 1):
    if i % 2 != 0:
        print('* ' * star)
    else:
        print(' ' + '* ' * star)