import numpy as np
from aiogram import types

from loader import dp, db


@dp.message_handler(commands='random_emoji')
async def random_emoji(message: types.Message):
    emojis = db.get_emojis_list()
    await message.answer(np.random.choice(emojis))
