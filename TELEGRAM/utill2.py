import requests   # 브라우저에다 요청을 했다면 이거는 리퀘스트로 요청해야함
import random

tocken = '5929925771:AAFUNOFPm6SjNphVGpy0JkDC1ZT9606BHC4'  # 봇 아이디
me = 5815766823

# 우리 챗봇이 받은 메세지를 확인 하려면?----> requests.get() 을 해야된다
# update_url = f'https://api.telegram.org/bot{tocken}/getUpdates'
# response = requests.get(update_url).json()  # 변수에 저장해야함 안그러면 의미가 없어짐
# print(response)
# input_message = response['result'][-1]['message']['text']
# chat_id = response['result'][-1]['message']['from']['id']             # 보낸 사람의 최신 메세지의 발신자 id 출력


if input_message == '로또':
    output_message = random.sample(range(1,40), 6)
# hi라고 들어오면
# output_message = 'hello'
# 서버에 요청(url)을 보낸다
elif input_message == '안녕':
    output_message = '안녕하세요'

else:
    output_message = '처리할 수 없습니다'



send_url = f'https://api.telegram.org/bot{tocken}/sendMessage?chat_id={chat_id}&text={output_message}' # 
requests.get(send_url)

server_url = 'https://dac2-211-33-180-73.jp.ngrok.io'
print(f'https://api.telegram.org/bot{tocken}/setWebhook?url={server_url}')         

# hi 라고 들어오면 'hello' 로 답을 하고
# 안녕이라고 들어오면 '안녕하세요'로 답을 한다
    

# url = f'https://api.telegram.org/bot{tocken}/sendMessage?chat_id={me}&text={message}' #  requesets 모듈에 이 url을 보낼것임

# requests.get(url)

'''
https://api.telegram.org/bot5929925771:AAFUNOFPm6SjNphVGpy0JkDC1ZT9606BHC4/getMe

https://api.telegram.org/bot5929925771:AAFUNOFPm6SjNphVGpy0JkDC1ZT9606BHC4/getUpdates
https://api.telegram.org/bot5929925771:AAFUNOFPm6SjNphVGpy0JkDC1ZT9606BHC4/sendMessage?chat_id=5815766823&text=hi

'''

# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

