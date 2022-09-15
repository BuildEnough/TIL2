import sys
sys.stdin = open('10769_행복한지_슬픈지.txt')



# emotion = {
#     ':-)': 0,
#     ':-(': 0
# }


# if emotion in line:
#     print('A')

line = input()

happy = line.count(':-)')
sad = line.count(':-(')

if happy == 0 and sad == 0:
    print('none')
else:
    if happy == sad:
        print('unsure')
    elif happy > sad:
        print('happy')
    else:
        print('sad')
