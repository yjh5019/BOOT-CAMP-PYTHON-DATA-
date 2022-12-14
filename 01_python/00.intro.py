import webbrowser


#ctrl + / --->드레그 한곳 모두 # 첨삭으로 뜨는 꿀팁~!!!!
webbrowser.open_new('google.com')
webbrowser.open('https://finance.naver.com/item/main.naver?code=005930')
webbrowser.open('https://finance.naver.com/item/main.naver?code=096770')
webbrowser.open('https://finance.naver.com/item/main.naver?code=126720')
# 이렇게 반복적인 코드는 죄악임
# 컴퓨터 자체가 반복적인 일을 시키려고 하는건데 반복을 하는 사람이 반복을 한다...???죄악 ㅠㅠ
# 개선할 수 있을까???????pyho

for code in['005930','096770','126720']:
    webbrowser.open('https://finance.naver.com/item/main.naver?code={code}')
