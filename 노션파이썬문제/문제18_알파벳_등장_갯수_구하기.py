# 문자열 word가 주어질 때,
# Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
# input : banana

word = 'banana'
dic = {}

alpha_list = list(word)
# print(alpha_list)
# print(dic.get('b'))

for i in alpha_list:
    if dic.get(i) == None: # dic에 각 알파벳이 올 때 없으면 내용을 생성해줌
        dic[i] = 1
    else:
        dic[i] += 1 # dic에 이미 생성이 되었을 경우 중복이라서 생성된 값에 1을 더해줌

# print(dic)
for i in dic:
    print(i, dic[i])

