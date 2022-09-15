T = int(input())

for i in range(1, T + 1):
    ti1, mi1, ti2, mi2 = map(int, input().split()) # 각각 시간과 분을 입력
    sum_ti = ti1 + ti2 # 시간의 합
    sum_mi = mi1 + mi2 # 분의 합

    # 분이 60이 넘어가면 1시간이 되니까 분부터 짜보기
    if sum_mi > 60:
        sum_ti += 1
        sum_mi -= 60
    if sum_ti > 12: # 이문 제 풀 때 이 줄에서 if 대신 elif를 사용해도 답이 나왔는데 오답으로 처리된게 궁금함
        sum_ti -= 12
    print(f"#{i} {sum_ti} {sum_mi}")

    