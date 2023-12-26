import jwt
import uvicorn
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Request
from datetime import datetime, timedelta

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User):
    if user.username == 'kevin' and user.password == '123456':
        expiration_time = datetime.utcnow() + timedelta(minutes=10)
        payload = {'sub': user.username, 'exp': expiration_time}
        secret_key = 'kevin'
        algorithm = 'HS256'
        token = jwt.encode(payload, secret_key, algorithm)
        return {'token': token}
    else:
        raise HTTPException(status_code=401,detail='Incorrect username or password')

def verify_token(token: Optional[str] = None):
    if token is None:
        raise HTTPException(status_code=401, detail='Token is None')
    try:
        payload = jwt.decode(token, key='kevin', algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')

@app.get('/verify')
def verify(request: Request):
    # Get token
    authorization: Optional[str] = request.headers.get('Authorization')
    print(authorization)
    if not authorization or not authorization.startswith('Bearer '):
        raise HTTPException(status_code=401, detail='Invalid Authorization header')
    token = authorization.split()[1]
    payload = verify_token(token)
    print(payload)
    return {'success': 200}

if __name__ == '__main__':
    uvicorn.run('main:app',host='127.0.0.1',port=8080,reload=True)
