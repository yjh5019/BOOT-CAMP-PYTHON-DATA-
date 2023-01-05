# data/urls.py

from django.urls  import path  # 4.app 에 urls.py 파일 만들고 임포트 ㄱㄱ
from . import views

app_name = 'data'

# urlpatterns  는 무적권 urls.py 에 있어야함
urlpatterns = [
    # data/
    path('', views.index, name='index'),

    # data/hello/<name>/ => variable    Routing
    # data/hello
    path('hello/<str:name>/', views.hello, name='hello'),
    # data/input
    path('user_input/', views.user_input, name='user_input'),
    path('user_output/', views.user_output, name='user_output'),
    
]
