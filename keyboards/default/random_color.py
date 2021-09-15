import numpy as np
from requests import request
from aiogram import types

from loader import dp


@dp.message_handler(commands="random_color")
async def random_color(message: types.Message):
    color = lambda: np.random.randint(0, 255)
    code = '%02X%02X%02X' % (color(), color(), color())
    r = request(url=f"https://singlecolorimage.com/get/{code}/400x100", method="GET")
    await message.answer_photo(r.url)
    await message.reply(f"#{code} - Hex code for this color")

