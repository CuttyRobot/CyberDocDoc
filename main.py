import fastapi
import telebot
from fastapi import FastAPI
from telebot import async_telebot
import uvicorn
import aiohttp


app = FastAPI()

token = "token"
bot = async_telebot.AsyncTeleBot(token)

@app.post("/")
async def rocker():
    return "ok"


@app.post("/message/{text}")
async def root(text: str):
    print('Message')
    return {"text": text}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
    
