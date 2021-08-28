import random

from aiogram import types

from loader import dp, db


@dp.message_handler(commands='random_country')
async def random_country(message: types.Message):
    await message.answer(random.choice(db.get_flags_list()))
