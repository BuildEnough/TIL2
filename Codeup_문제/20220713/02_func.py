def foo():
    return ''
    return '' # 여기 있는 return 값은 실행되지 않는다

def foo():
    return 1, 2
# 하나만 반환하는 것이 아닌 tuple로 반환함

result = foo()
print(result, type(result))

def no():
    a = 1

result = no()
print(result, type(result))
# 아무것도 안뜸

a = print('hi')
print(a, type(a))
# a에 print를 넣었기 때문에 아무것도 안뜸
# print 함수는 출력을 해주고, return 값은 없음 -> None

a = 'hi'
print(a)