import requests

def get_token():
    url = 'http://127.0.0.1:8080/login'
    info = {'username': 'kevin',
            'password': '123456'}
    res = session.post(url=url,json=info)
    token = res.json()['token']
    print(token)
    return token

def verify_token(token):
    url = 'http://127.0.0.1:8080/verify'
    headers = {'Authorization': f'Bearer {token}'}
    res = session.get(url=url,headers=headers)
    print(res.json())
    print(res.status_code)

if __name__ == '__main__':
    session = requests.session()
    token = get_token()
    verify_token(token)
