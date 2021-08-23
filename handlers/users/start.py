from aiogram import types
from loader import dp


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}!")
