import sys
sys.stdin = open('2857_FBI.txt')

# 5줄에 첩보원 명 중 FBI 요원 찾기
# 첩보원명: 알파벳 대문자, 0~9, - 로 이루어져있고, 첩보원명 <= 10
# 첩보원명에 FBI 포함되어 있음
# 해당하는 요원이 몇 번째 입력인지를 공백으로 구분하여 출력

count = 0

for i in range(1, 6):
    name = input()
    
    if 'FBI' in name:
        print(i, end =' ')
        count += 1
    
if count == 0:
    print('HE GOT AWAY!')