import json
from urllib import request
from aiogram import types

from config import API_KEY
from loader import dp


@dp.message_handler(commands='random_mem')
async def random_mem(message: types.Message):
    data = json.loads(request.urlopen(f"http://api.giphy.com/v1/gifs/random?api_key={API_KEY}&tag=mem&rating=pg-13").read())
    await message.answer_sticker(data['data']['images']['downsized_large']['url'])
