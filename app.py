"""
Run this file to start the bot.
"""
# Do not remove these imports, because bot won't work!
import keyboards  # pylint: disable=unused-import
import handlers  # pylint: disable=unused-import
import middlewares  # pylint: disable=unused-import

from aiogram import executor
from loader import dp
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
