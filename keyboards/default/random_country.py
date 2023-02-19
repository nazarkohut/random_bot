"""
Has method that shows flag of random country.
"""
import numpy as np

from aiogram import types

from loader import dp, db


@dp.message_handler(commands="random_country")
async def random_country(message: types.Message):
    await message.answer(np.random.choice(db.get_flags_list()))
