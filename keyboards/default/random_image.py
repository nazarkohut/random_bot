from aiogram import types
from requests import request

from loader import dp


@dp.message_handler(commands="random_image")
async def random_image(message: types.Message):
    r = request(url="https://source.unsplash.com/random", method="GET")
    await message.answer_photo(r.url)
