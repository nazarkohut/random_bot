from aiogram import types
from loader import dp


@dp.message_handler(commands='help')
async def bot_help(message: types.Message):
    text = ("Commands: ",
            "/start - Start Bot",
            "/help - Get commands list")
    await message.answer("\n".join(text))
