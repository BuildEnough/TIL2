# 아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# output : 두 번째 리스트의 최댓값이 더 큽니다.

# number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# max()는 함수명이기 때문에 number_list2에서 max함수를 사용하는 것이 아닌
# 윗 줄에서 사용하던 max(number_list)의 값이 할당된 max를 불러오기 때문에
# max를 다른 이름으로 바꿔줘야한다
# 나같은 경우 max1

number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")


    # 강사님 해설