import fastapi
from fastapi import FastAPI
from telebot import async_telebot
import telebot
from telebot import types
import uvicorn
import aiohttp
import requests
import json
import httpx
import grpc

app = FastAPI()


project_url = "t.me/CyberDoctorBot"
personal_url = "test2.wwestern-gate.online/message"
token = "6496231521:AAEoxoPKL2PctD2NEfF2GDtBoKubQWvFKcE"
url = f'https://api.telegram.org/bot{token}/setWebhook'
bot = async_telebot.AsyncTeleBot(token)


@app.post("/message")
async def rocker(request: fastapi.Request):
    alpha = await request.body()

    # Decode string to from bytes format
    input_string_decoded = alpha.decode('utf-8')

    # Loading decoded string to json format
    json_data = json.loads(input_string_decoded)
    message = json_data

    # Message first level keys
    first_level_keys = message.keys()

    if "message" in first_level_keys:
        line = int(message["message"]['chat']["id"])
        # Message second level keys
        second_level_keys = message["message"].keys()
        if "video" in second_level_keys:
            # Message with video file
            print('Type: message with video')
            # Not handling
            await bot.send_message(line, "Sorry, but we are not handeling video files")

        elif "audio" in second_level_keys:
            # Message with audio file
            print('Type: message with audio')
            # Not handling
            await bot.send_message(line, "Sorry, but we are not handeling Audio files")

        elif "document" in second_level_keys:
            # Message with document file
            print('Type: message with document')
            # Not handling
            await bot.send_message(line, "Sorry, but we are not handeling Documents")

        elif "photo" in second_level_keys:
            # Message with image file
            print('Type: message with photo')
            # Handling
            await bot.send_message(line, "Photo can be processed")

        elif "entities" in second_level_keys:
            # Text message (can include command)
            print('Type: command message')
            # Handling
            await bot.send_message(line, "Command messages can be processed")

        else:
            print('Type: common message')
            await bot.send_message(line, str(message['message']['text']))
            print(line)
            # Handling

    elif "callback_query" in first_level_keys:
        print('Type: callback')
        print('Callback data:', message['callback_query']['data'])
        # Handling


@app.get("/check/{name}")
async def say_hello(name: str):
    return {"message": f"Checking system, {name}"}


def set_webhook():
    url = f'https://api.telegram.org/bot{token}/setWebhook'
    webhook_url = 'https://test2.western-gate.online/message'
    response = requests.post(url, json={'url': webhook_url})
    print(response.text)


if __name__ == "__main__":
    bot.set_webhook()
    uvicorn.run(app, host='127.0.0.1', port=13412)