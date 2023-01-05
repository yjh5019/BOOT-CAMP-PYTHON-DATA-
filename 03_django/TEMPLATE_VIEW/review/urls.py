# review/urls.py

from django.urls  import path  # 4.app 에 urls.py 파일 만들고 임포트 ㄱㄱ
from . import views

# url 구성 맨앞에 review/는 이미 끝났어 master에서
# 변수명 반드시 app_name
app_name = 'review'
urlpatterns=[


    # 패턴 (review/index)가 요청이 들어온다면, (우리가원하는)함수를 실행!!!!
    # 
    path('', views.index, name='index'),
    # review/hello/
    path('hello/', views.hello, name='hello'),

]



# review/hello => view hello 함수실행 => hello.html을 응답(랜더)


