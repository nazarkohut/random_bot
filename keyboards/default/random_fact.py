"""
Has method that makes the world smarter with random facts.
"""
import requests
from aiogram import types

from keyboards.constants import ERROR_ON_OUR_SIDE, NINJAS_API_HEADER, COMMON_REQUEST_TIMEOUT
from loader import dp
from utils.schemas.fact import fact_validator


@dp.message_handler(commands="random_fact")
async def random_fact(message: types.Message):
    limit = 1
    api_url = f"https://api.api-ninjas.com/v1/facts?limit={limit}"

    response = requests.get(api_url, headers=NINJAS_API_HEADER, timeout=COMMON_REQUEST_TIMEOUT)
    if response.status_code != requests.codes.ok:
        return await message.answer(ERROR_ON_OUR_SIDE)

    response = response.json()
    if not isinstance(response, list) or len(response) == 0:
        return await message.answer(ERROR_ON_OUR_SIDE)

    data = response[0]
    if not fact_validator.validate(data):
        return await message.answer(ERROR_ON_OUR_SIDE)

    fact = data.get("fact", "")
    await message.answer(f"💡{fact}")
