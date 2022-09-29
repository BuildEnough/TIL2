from django.db import models

# Create your models here.
# django에서 DB에서 data는 models를 의미함
# 템플릿: 화면
# 뷰: 데이터 가공하여 템플릿으로 전달, 요청과 응답을 처리
# 모델: 데이터베이스의 데이터

class Todo(models.Model):
    # django에서 pk(id)는 자동으로 만들어줌
    # models에 Model을 상속받아야함

    content = models.CharField(max_length = 80)
    # models에 CharField 필드, 최대 80자까지 작성가능

    completed = models.BooleanField(default=False)
    # default는 데이터를 생성할 때 값을 넣지 않으면 자동으로 값을 채워서 데이터를 생성해줌
    # 메모앱을 기준으로 메모를 할때 미완료인 상태로 메모를 만들기 때문에 default값을 거짓으로 생성함
    




    # 데이터 추가하면 다시 마이그레이트 해줘야 함