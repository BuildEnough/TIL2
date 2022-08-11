import sys
sys.stdin = open('17388_와글와글_숭고한.txt')

# 참여도 합 >= 100: 일처리 잘됨
# 참여도 합 < 100: c참여도가 낮은 곳에 압박 넣음

# S: 숭실대
# K: 고려대
# H: 한양대

S, K, H = map(int, input().split())

min_= min(S, K, H)


if S + K + H >= 100:
    print('OK')
else:
    if min_ == S:
        print('Soongsil')
    elif min_ == K:
        print('Korea')
    else:
        print('Hanyang')