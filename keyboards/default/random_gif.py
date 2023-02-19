"""
Has method that answers with random gif.
"""
import json
from urllib import request
from aiogram import types

from config import API_KEY
from loader import dp


@dp.message_handler(commands="random_gif")
async def random_gif(message: types.Message):
    data = json.loads(request.urlopen(f"http://api.giphy.com/v1/gifs/random?api_key={API_KEY}").read())
    await message.answer_sticker(data["data"]["images"]["downsized_large"]["url"])
