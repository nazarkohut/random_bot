"""
Has method that sends random hobby with a link of the detailed description of it.
"""
import requests
from aiogram import types

from keyboards.constants import ERROR_ON_OUR_SIDE, NINJAS_API_HEADER, COMMON_REQUEST_TIMEOUT
from loader import dp
from utils.schemas.hobby import hobby_validator


@dp.message_handler(commands="random_hobby")
async def random_hobby(message: types.Message):
    api_url = "https://api.api-ninjas.com/v1/hobbies"

    response = requests.get(api_url, headers=NINJAS_API_HEADER, timeout=COMMON_REQUEST_TIMEOUT)
    if response.status_code != requests.codes.ok:
        return await message.answer(ERROR_ON_OUR_SIDE)

    data = response.json()
    if not hobby_validator.validate(data):
        return await message.answer(ERROR_ON_OUR_SIDE)

    hobby = data.get("hobby", "")
    wiki_link = data.get("link", "")
    await message.answer(f"{hobby}. More info here: {wiki_link}")
