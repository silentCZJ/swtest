import requests

url = 'http://127.0.0.1:8080/login'
session = requests.session()
info = {'username': 'kevin',
        'password': '123456'}
res = session.post(url=url,json=info)
print(res.text)
print(res.status_code)
