# 문자열 word가 주어질 때,
# 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지
# input : banana
# output : 1

word = 'apple'
count = 0

for i in word:
    count += 1
    if i == 'a':
        print(count)
        break
    elif i != 'a':
        print(-1)
        break

# 강사님 풀이
word = 'banana'

# 문자로 순회하는 것이 아니라
# 인덱스로 접근
# 원하는 숫자? 0 1 2 3 4 5
# 얻는 방법은? range(len(word)) -> range(6)
for idx in range(len(word)):
    # print(word[idx])
    # 알파벳이 a일때
    if word[idx] == 'a':
        print(idx)
        break
# for문을 다 돌았다는 뜻은
# 한번도 break에 안걸렸다
# 즉, a는 없었다
else:
    print(-1)
