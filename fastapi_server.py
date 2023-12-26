from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
import uvicorn

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User):
    if user.username == 'kevin' and user.password == '123456':
        payload = {'sub': user.username}
        secret_key = 'kevin'
        algorithm = 'HS256'
        token = jwt.encode(payload, secret_key, algorithm)
        return {'token': token}
    else:
        raise HTTPException(status_code=401,detail='Incorrect username or password')
    
if __name__ == '__main__':
    uvicorn.run('main:app',host='127.0.0.1',port=8080,reload=True)
