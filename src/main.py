from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {"root": "root"}


@app.get('/hello')
def hello():
    return {"hello": "hello fastapi"}