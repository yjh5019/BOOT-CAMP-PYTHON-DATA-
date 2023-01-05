# review/views.py

from django.shortcuts import render

# Create your views here.
# 이제 여기서 함수 실행할걸 옮겨넣는거지

def index(request):
    
    # response => html render  렌더링을 해줄꺼야~
    # render(1. request, 2, html 이름 3. 넘길 데이터)의 형식으로 ㄱㄱ
    return render(request, 'review/index.html')              # html을 내보내야하는것이 render
                   
                                                    # html은 templates => index.html을 만들어서 ㄱㄱ
def hello(request):
    return render(request, 'review/hello.html')
