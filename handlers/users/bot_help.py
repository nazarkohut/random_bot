"""
One of the crucial commands in every telegram bot - 'help'.
Whenever you add a new command, do not forget to include it in here as well.

Be consistent: include commands here in the same sequence as in ```set_bot_commands.py```,
start every description in the same capitalization as previous commands,
do not include any punctuation here if previous commands do not have it.
"""
from aiogram import types
from loader import dp


@dp.message_handler(commands="help")
async def bot_help(message: types.Message):
    text = ("Commands: ",
            "/start - start bot🌵",
            "/help - get commands list",
            "/random_integer - generate random integer🔢",
            "/random_answer - random Yes or No",
            "/random_joke - cheer🍻 yourself up",
            "/random_emoji - send random emoji😊",
            "/random_country - random country(randoms national flag 🇺🇦 )",
            "/random_image - random beautiful🌷 image",
            "/random_gif - send random gif😎",
            "/random_hobby - discover a new hobby🏓 that may become a part of you😮",
            "/random_mem - send random mem🤡",
            "/random_color - random color and its hex code",
            "/random_fact - find out an interesting fact you didn't know📚",
            "/random_my_choice - random one object👻 from the sequence you've typed",
            "/random_riddle - time🕛 to strain the brain🧠"
            "/random_admin - get random group administrator👑",
            )
    await message.answer("\n".join(text))
