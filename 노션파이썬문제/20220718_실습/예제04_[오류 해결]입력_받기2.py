# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# input : I'm Tuotor 6
# output : ["I'm", 'Tutor', '6']

# words = list(map(int, input().split()))
# print(words)


# map을 사용해서 정수형으로 바꿔줄 필요와 list로 리스트 형으로 만들어 줄
# 필요가 없음 그저 input().split()을 하면 리스트로 나누어짐

words = (input().split())
print(words)

# 강사님 해설