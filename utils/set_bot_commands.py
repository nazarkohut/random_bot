"""
Add new command using ```types.BotCommand(<command_name: str>, <command_description: str>)```
inside list of commands
"""
from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start Bot"),
            types.BotCommand("help", "Shows commands list"),
            types.BotCommand("random_integer", "Generate random integer1️⃣"),
            types.BotCommand("random_answer", "Random Yes or No"),
            types.BotCommand("random_joke", "Сheer🍻 yourself up"),
            types.BotCommand("random_emoji", "Sends random emoji🍊"),
            types.BotCommand("random_country", "Random country 🇺🇦 by the national flag"),
            types.BotCommand("random_image", "Random beautiful🌸 image"),
            types.BotCommand("random_gif", "Sends random gif"),
            types.BotCommand("random_hobby", "Discover a new hobby🏓 that may become a part of you😮‍"),
            types.BotCommand("random_mem", "Sends📨 random mem gif"),
            types.BotCommand("random_color", "Random color🟥 and its hex code"),
            types.BotCommand("random_fact", "Find out an interesting fact you didn't know📚"),
            types.BotCommand("random_my_choice", "Random one object from the sequence you've typed"),
            types.BotCommand("random_riddle", "Time🕛 to strain the brain🧠"),
            types.BotCommand("random_youtube_video", "Random video from youtube"),
            types.BotCommand("random_admin", "Get random group administrator"),
        ]
    )
