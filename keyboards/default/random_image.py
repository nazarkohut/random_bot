"""
Has method that sends beautiful random images.
"""
from aiogram import types
from requests import request

from keyboards.constants import COMMON_REQUEST_TIMEOUT
from loader import dp


@dp.message_handler(commands="random_image")
async def random_image(message: types.Message):
    r = request(url="https://source.unsplash.com/random", method="GET", timeout=COMMON_REQUEST_TIMEOUT)
    await message.answer_photo(r.url)
