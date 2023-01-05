from django.shortcuts import render

# Create your views here.


def index(request):
    # response => html render  렌더링을 해줄꺼야~
    # render(1. request, 2, html 이름 3. 넘길 데이터)의 형식으로 ㄱㄱ
    return render(request, 'data/index.html') 
def hello(request, name):
    context = {'name': name, }  # 딕셔너리
    return render(request, 'data/hello.html', context) 
def user_input(request):
    
    return render(request, 'data/user_input.html')

def user_output(request):
    c = int(request.POST['cel'])                # request 안에서 섭씨데이터 꺼내기
    f = c * 1.8 + 32
    
    context = {
        'f' : f,
        'username' : request.POST['username'],
        'password' : request.POST['password'],
    }

    return render(request, 'data/user_output.html', context)
