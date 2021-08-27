import random

from aiogram import types

from loader import dp


@dp.message_handler(commands='random_admin')
async def random_admin(message: types.Message):
    admins = await message.chat.get_administrators()
    await message.answer(random.choice(admins).user.mention)
