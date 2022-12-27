from aiogram import types
from loader import dp


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(
        f"Hi, {message.from_user.full_name} 🤚 I'm a random bot, and I'll help you to make decisions and make fun😉. "
        f"Type /help command to see the list of features🤪. ")
