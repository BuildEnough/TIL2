import sys
sys.stdin = open('1264_모음의_개수.txt')


while True:
    try:
        word = input()
        cnt = 0
        for c in word:
            if c in 'aAeEiIoOuU':
                cnt += 1
   
        if word == '#':
           break
        
        print(cnt)         
    except:
        if len(word) >= 255:
            break
    