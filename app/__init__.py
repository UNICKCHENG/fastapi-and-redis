from fastapi import FastAPI
from .redis import client as redis

app = FastAPI()

@app.get('/}')
def hi(value: str):
    return 'hi'

@app.post('/data/{value}')
def data(value: str):
    redis.set('data', value)

@app.get('/data')
def data():
    try:
        return redis.get('data')
    except:
        return None
    
@app.delete('/data')
def data():
    redis.delete('data')