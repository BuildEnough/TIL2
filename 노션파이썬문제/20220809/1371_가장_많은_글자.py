import sys
sys.stdin = open('1371_가장_많은_글자.txt')

# print(ord('a')) # 97
# print(ord('z')) # 122
# print(122- 97) # 25인데 +1해서 알파벳 총 26개

sen = ''
while True:
    try:
        sen += input()
# print(sen)
    except:
        break

# print(sen.count('a'))
# 비교
sen_list = ['a', sen.count('a')]
for i in range(98, 123): # b ~ z
    z = sen.count(chr(i))

    if z > sen_list[1]: 
        sen_list[0] = chr(i) # z보다 많으면 해당 알파벳을 0번째로 해줌
        sen_list[1] = z

    elif z == sen_list[1]: # 여러 개일 경우 0번째에 더해줌
        sen_list[0] += chr(i)

print(sen_list[0])