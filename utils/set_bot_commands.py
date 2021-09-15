from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start Bot"),
            types.BotCommand("help", "Shows commands list"),
            types.BotCommand("random_integer", "Generate random integer"),
            types.BotCommand("random_answer", "Random Yes or No"),
            types.BotCommand("random_emoji", "Sends random emoji"),
            types.BotCommand("random_country", "Random country by the national flag"),
            types.BotCommand("random_image", "Random beautiful image"),
            types.BotCommand("random_gif", "Sends random gif"),
            types.BotCommand("random_mem", "Sends random mem gif"),
            types.BotCommand("random_color", "Random color and its hex code"),
            types.BotCommand("random_my_choice", "Random one object from the sequence you've typed"),
            types.BotCommand("random_admin", "Get random group administrator"),
        ]
    )
