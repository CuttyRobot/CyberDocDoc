import fastapi
from fastapi import FastAPI
from telebot import async_telebot
import uvicorn
import aiohttp
import requests
import json


app = FastAPI()


project_url = "t.me/CyberDoctorBot"
personal_url = "test2.wwestern-gate.online/message"
token = "6496231521:AAEoxoPKL2PctD2NEfF2GDtBoKubQWvFKcE"
url = f'https://api.telegram.org/bot{token}/setWebhook'
bot = async_telebot.AsyncTeleBot(token)


@app.post("/message")
async def rocker(request: fastapi.Request):
    alpha = await request.body()
    print('text' + str(alpha))
    return "ok"



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


def set_webhook():
    url = f'https://api.telegram.org/bot{token}/setWebhook'
    webhook_url = 'https://test2.western-gate.online/message'

    response = requests.post(url, json={'url': webhook_url})

    print(response.text)


if __name__ == "__main__":
    bot.set_webhook()
    uvicorn.run(app, host='localhost', port=9012)