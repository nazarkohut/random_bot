from aiogram import types
from loader import dp


@dp.message_handler(commands='help')
async def bot_help(message: types.Message):
    text = ("Commands: ",
            "/start - start bot🌵",
            "/help - get commands list",
            "/random_integer - generate random integer🔢",
            "/random_answer - random Yes or No",
            "/random_emoji - sends random emoji😊",
            "/random_country - random country by the national flag 🇺🇦",
            "/random_image - random beautiful🌷 image",
            "/random_gif - sends random gif😎",
            "/random_mem - sends random mem🤡",
            "/random_color - random color and its hex code",
            "/random_my_choice - random one object👻 from the sequence you've typed",
            "/random_admin - get random group administrator👑",
            )
    await message.answer("\n".join(text))
