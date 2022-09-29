"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
    # 프로젝트 전체의 urls 파일에서 todos의 urls을 include 해야함
    # todos에 있는 urls 파일을 가지고 오라는 의미(include)
    # 이렇게 하면 앱의 urls가 분리가 된 것임
    # path('')에서 ''에 들어가는 것이 url 주소 입력했을때
    # localhost:8000/ 다음에 들어감
]
