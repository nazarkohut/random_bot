import random

from aiogram import types

from loader import dp
from utils.misc.decorators.is_group import is_group


@dp.message_handler(commands='random_admin')
@is_group
async def random_admin(message: types.Message):
    admins = await message.chat.get_administrators()
    await message.answer(random.choice(admins).user.mention)
