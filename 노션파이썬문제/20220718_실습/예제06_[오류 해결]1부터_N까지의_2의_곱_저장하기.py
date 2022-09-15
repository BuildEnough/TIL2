# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# output : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# () tuple는 이미 생성된 원소를 제거하거나 변경할 수 없음
# 그래서 [] 리스트로 바꿔줌

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# 강사님 해설