"""
Has method that sends jokes.
"""
import requests
from aiogram import types

from keyboards.constants import ERROR_ON_OUR_SIDE, NINJAS_API_HEADER, COMMON_REQUEST_TIMEOUT
from loader import dp
from utils.schemas.joke import joke_validator


@dp.message_handler(commands="random_joke")
async def random_joke(message: types.Message):
    limit = 1
    api_url = f"https://api.api-ninjas.com/v1/dadjokes?limit={limit}"

    response = requests.get(api_url, headers=NINJAS_API_HEADER, timeout=COMMON_REQUEST_TIMEOUT)
    if response.status_code != requests.codes.ok:
        return await message.answer(ERROR_ON_OUR_SIDE)

    response = response.json()
    if not isinstance(response, list) or len(response) == 0:
        return await message.answer(ERROR_ON_OUR_SIDE)

    data = response[0]
    if not joke_validator.validate(data):
        return await message.answer(ERROR_ON_OUR_SIDE)

    joke = data.get("joke", "").capitalize()
    await message.answer(f"{joke}")
