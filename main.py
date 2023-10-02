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
    # Message chat id
    first_level_keys = message.keys()
    if "message" in first_level_keys:
        second_level_keys = message["message"].keys()
        if "video" in second_level_keys:
            # Message with video file
            print('Type: message with video')
        elif "audio" in second_level_keys:
            # Message with audio file
            print('Type: message with audio')
        elif "document" in second_level_keys:
            # Message with document file
            print('Type: message with document')
        elif "photo" in second_level_keys:
            # Message with image file
            print('Type: message with photo')
        elif "entities" in second_level_keys:
            # Text message (can include command)
            print('Type: command message')
        else:
            print('Type: common message')


    elif "callback_query" in first_level_keys:
        print('Type: callback')

    # line = 0
    # try:
    #     if message["message"] is not None:
    #         # For messages
    #         print("Update_id:", message["update_id"])
    #         print("Message_id:", message["message"]["message_id"])
    #         print("Chat_id:", message["message"]["chat"]["id"])
    #         print("Date:", message["message"]["date"])
    #         print("Text:", message["message"]["text"])
    #         print("is_bot:", message["message"]["from"]["is_bot"])
    #         line = int(message["message"]['chat']["id"])
    #         print(line)
    #         print('---------------------------------')
    # except:
    #     print('Error')
    #
    # try:
    #     if message["callback_query"] is not None:
    #         # For callbacks
    #         print("Update_id:", message["update_id"])
    #         print("Callback_query:", message["callback_query"]['message']["message_id"])
    #         print("From:", message["callback_query"]['from']["id"])
    #         print("Callback_data:", message["callback_query"]["data"])
    #         print("Date:", message["callback_query"]['from']["date"])
    #         print("Text of the callback Initiating message:", message["callback_query"]['from']["text"])
    #         print("is_bot:", message["message"]["from"]["is_bot"])
    #         line = int(message["callback_query"]['from']["id"])
    #         print(line)
    #         print('---------------------------------')
    # except:
    #     print('Error')
    #
    # if line == 0:
    #     breakpoint()
    #
    # # Language choice
    # markup = telebot.types.InlineKeyboardMarkup()
    # button_1 = types.InlineKeyboardButton("Fuck You!", callback_data="1")
    # button_2 = types.InlineKeyboardButton("No, Fuck You", callback_data="2")
    #
    # markup.add(button_1, button_2)
    # await bot.send_message(line, "Welcome to HealthC bot. Choose system language: ",
    #                        reply_markup=markup)
    # return "ok"


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
    uvicorn.run(app, host='localhost', port=9012)