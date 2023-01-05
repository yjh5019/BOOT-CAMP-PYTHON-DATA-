# master URL

from django.contrib import admin
from django.urls import path, include # 2. include 추가해야 넘기기용 함수임

urlpatterns = [
    path('admin/', admin.site.urls),
    #  1. url pattern이 'review/'로 시작하면 => review/urls.py에게 일을 다 넘기 겠다~~~
    path('review/', include('review.urls')), # 3. review app 안에 urls.py 에다가 작업할수있게 인클루드 해줌
    
    path('data/', include('data.urls')),  #  지금부터~~ data로 되어 있는 앱은 data안에 있는 urls폴더로 넘기겠다
]

# review/abcd 여기서는 앞에 review만 확인하는 용도고
# 나머지  abcd는 review/urls 에 가서 확인하는것
# 그럼 urls.py review에 가서 abcd를 확인해야하는데....