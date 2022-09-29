from django.shortcuts import render, redirect
from .models import Todo
# models의 Todo 함수를 import함
# redirect는 입력했을시 create에서 안보기 때문에 사용
# redirect하면 todos:index를 요청했기 때문에 root로 돌아옴(index가 현재 root페이지임)
# root 페이지에서 입력하면 다시 root 페이지로 돌아온다는 의미

def index(request):
    _todos = Todo.objects.all()
    # 만들어 놓은 데이터를 불러오는 ORM 코드
    # 불러온 데이터를 todos라는 변수에 할당
    context = {
        "todos" : _todos,
    }
    # templates 변수에서 _todos를 출력해야 하기 때문에 context라는 딕셔너리 변수 만들고 _todos를 넘겨줌
    # 만든 context를 render 함수의 인자로 넘겨줌 return render(request, 'todos/index.html',context)
    return render(request, 'todos/index.html', context)
    # index 페이지를 만든다
    # todos/index.html: 이건 앱 안의 templates안의 todos 안의 index.html

def create(request):
    content = request.GET.get("content_")
    # templates에서 데이터를 get해야됨
    # input name에 있는 content_로 데이터를 받아옴
    # request.GET.get를 이용해서 값을 가져옴
    
    Todo.objects.create(content=content)
    # DB에 저장
    # Todo에 objects에 create메소드 사용
    # create메소드 안에 content 필드를 넣음

    return redirect('todos:index')
    # 원래 return render(request, 'todos/index.html') 지만 render 대신 redirect사용
    # redirect하면 todos:index를 요청했기 때문에 root로 돌아옴(index가 현재 root페이지임)


def delete(request, todo_pk):
    # todo_pk라는 인자를 받음
    todo = Todo.objects.get(pk = todo_pk)
    # 삭제 해야될 값을 불러와야하고 삭제할 값을 todo에 저장함
    # 불러오는 방법은 Todo.objects.get(pk = todo_pk)
    todo.delete()
    # todo save를 여기서 하게되면 안됨: save를 하게되면 동일한 데이터가 또 생성됨
    return redirect('todos:index')
    # return을 root페이지로 redirect함