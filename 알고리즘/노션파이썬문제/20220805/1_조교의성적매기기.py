from pprint import pprint
import sys
sys.stdin = open("_조교의성적매기기.txt")

scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    list_ = []
    for i in range(N):
        M, F, R = map(int, input().split())
        total = (M * 0.35) + (F * 0.45) + (R * 0.2)
        list_.append(total)
    
    score = list_[K]
    print(score)
    
        
        
    
        
    #     list_.append(M)
    #     list_.append(F)
    #     list_.append(R)
    # print(list_)





#1 A-
#2 C-
#3 C0
#4 A-
#5 C0
#6 A-
#7 C+
#8 C+
#9 B0
#10 A0


