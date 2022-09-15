# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# output : 3

# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# char이 해당하는 모음에 하나씩 대조가 안됨
# in은 멤버 연산자인데 어떤 배열이 있을때 그 배열에 값이 있으면 True를 출력해줌
# 모듬들을 or 연산자보다 리스트로 만들어 하나씩 비교 후 모음의 개수를 구함

word = "HappyHacking"

count = 0

for char in word:
    if char in ["a", "e", "i", "o", "u"]:
        count += 1
    
print(count)