import random

from aiogram import types
from loader import dp


@dp.message_handler(commands='random_answer')
async def random_answer(message: types.Message):
    await message.answer(random.choice(["Yes", "No"]))
