from flask import Flask, request
import random
import requests
from utils import send_message

app = Flask('hi')

@app.route('/', methods=['POST'])                     # route 란 길을 뚫어주는 역할을 하는것
def home():
    # 서버로서 우리가 받은 요청  -->  server
    data = request.json  # 요청을 받는것
    input_message = data['message']['text']
    sender_id = data['message']['from']['id']

    if input_message == '안녕':
        send_message('안녕하세요', sender_id)
    elif input_message == '로또':
        lotto = random.sample(range(1,46), 6)
        send_message(lotto, sender_id)

    return 'Hello Server'
if __name__ == '__main__':
    app.run(port=80, debug=True)


