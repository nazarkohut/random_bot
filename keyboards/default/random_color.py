from requests import request
from aiogram import types

from loader import dp
from utils.misc.additional_functions.random_color.random_hex_code import random_hex_code


@dp.message_handler(commands="random_color")
async def random_color(message: types.Message):
    code = random_hex_code()
    r = request(url=f"https://singlecolorimage.com/get/{code}/400x100", method="GET")
    await message.answer_photo(r.url)
    await message.reply(f"#{code} - Hex code for this color")

