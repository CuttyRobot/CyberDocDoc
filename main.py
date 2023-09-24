import fastapi
import telebot
from fastapi import FastAPI
from telebot import async_telebot
import uvicorn
import aiohttp
app = FastAPI()

token = "token"
bot = async_telebot.AsyncTeleBot(token)


@bot.message_handlers(commands=["start"])
async def start(message):
    await bot.send_message(message.chat.id, f"Hello, {message.chat.id}")


@app.get("/")
async def root():
    return "ok"

@app.post("/message")
async def root(request: fastapi.requests):
    print('Message')
    return {"text": request}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    bot.set_webhook()
    uvicorn.run(app, host='localhost', port=8000)