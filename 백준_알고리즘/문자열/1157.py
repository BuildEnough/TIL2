import sys
sys.stdin = open('1157.txt')

word = input().upper()

word_list = list(set(word))


list_ = []

for i in word_list:
    count = word.count
    list_.append(count(i))
    print(list_)
