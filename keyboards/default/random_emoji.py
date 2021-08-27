import random
from aiogram import types

from loader import dp, db


# generator for db data can be used in situation where we have a lot of data
@dp.message_handler(commands='random_emoji')
async def random_emoji(message: types.Message):
    emojis = db.get_emojis_list()
    await message.answer(random.choice(emojis))
