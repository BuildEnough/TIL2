sum = 5
print(sum([1, 2, 3]))

# Traceback (most recent call last):
#   File "D:\바탕화면\PYTHON\20220713\05_LEGB.py", line 2, in <module>
#     print(sum([1, 2, 3]))
# TypeError: 'int' object is not callable

# sum이 지금은 5가 되어버림..
# Built-in scope에 sum 함수가 있었음
# Global scope에 sum이름의 변수를 만듬
# 제가 찾으니까 L->E->G->B