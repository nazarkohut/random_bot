"""
Has method that says 'Yes' or 'No' whenever the command is executed.
"""
import numpy as np

from aiogram import types
from loader import dp


@dp.message_handler(commands="random_answer")
async def random_answer(message: types.Message):
    await message.answer(np.random.choice(["Yes", "No"]))
