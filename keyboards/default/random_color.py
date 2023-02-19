"""
Has method that shows random color in hex and shows how this color looks like.
"""
from requests import request
from aiogram import types

from keyboards.constants import COMMON_REQUEST_TIMEOUT
from loader import dp
from utils.misc.additional_functions.random_color.random_hex_code import random_hex_code


@dp.message_handler(commands="random_color")
async def random_color(message: types.Message):
    code = random_hex_code()
    r = request(url=f"https://singlecolorimage.com/get/{code}/400x100", method="GET", timeout=COMMON_REQUEST_TIMEOUT)
    await message.answer_photo(r.url)
    await message.reply(f"#{code} - Hex code for this color")

