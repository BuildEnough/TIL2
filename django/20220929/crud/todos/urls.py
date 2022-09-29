from django.urls import path
# path 추가
# 모듈 이름 기억 안나는 경우 
# 프로젝트의 urls가서 복사한 후 include만 지워주면 됨

from . import views
# views 추가

# url namespace
# url을 이름으로 분류하는 기능

app_name = "todos"
# include를 사용하는 것은 공간적인 분리
# 한 파일에 있어야 하는 것을 나눔으로써 코드의 공간을 나눔
# app_name을 지정하는 것은 만약 index를 다른 곳에서 사용하고 싶어도 사용할 수 없기 때문
# 동일한 이름은 장고 프로젝트 내에서 1개만 쓸 수 있다

urlpatterns = [
    path('', views.index, name='index'),
    # path를 추가하는데 url은 ''이고, views 함수는 index 함수로 향하게 됨
    # ''주소로 요청하면 views에 있는 index를 함수로 응답한다는 의미
    # ''urls 대신 이름을 지정하는데 변수이름 지정하듯이 name을 index로 지정한다는 뜻

    path('create/', views.create, name='create'),
    # 이름을 create로 만들고 create/로 요청할거라는 뜻
    # views는 create라는 함수를 요청한다는 의미

    path('delete/<int:todo_pk>', views.delete, name= 'delete'),
    # 이름 delete, 주소 delete/<todo_pk>, 여기서 <todo_pk>는 동적인자
    # int타입 지정안해도 되긴함
]
