"""
Has a method that makes a riddle with the spoiled solution to it.
"""
import requests
from aiogram import types

from keyboards.constants import ERROR_ON_OUR_SIDE, NINJAS_API_HEADER, COMMON_REQUEST_TIMEOUT
from loader import dp
from utils.schemas.riddle import riddle_validator


@dp.message_handler(commands="random_riddle")
async def random_riddle(message: types.Message):
    api_url = "https://api.api-ninjas.com/v1/riddles"

    response = requests.get(api_url, headers=NINJAS_API_HEADER, timeout=COMMON_REQUEST_TIMEOUT)
    if response.status_code != requests.codes.ok:
        return await message.answer(ERROR_ON_OUR_SIDE)

    response = response.json()
    if not isinstance(response, list) or len(response) == 0:
        return await message.answer(ERROR_ON_OUR_SIDE)

    data = response[0]
    if not riddle_validator.validate(data):
        return await message.answer(ERROR_ON_OUR_SIDE)

    question = data.get("question", "").capitalize()
    answer = data.get("answer", "").capitalize()
    await message.reply(f"<b> {question} </b> \n\n Solution: <tg-spoiler> {answer} </tg-spoiler>")
