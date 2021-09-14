from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start Bot"),
            types.BotCommand("help", "Shows commands list"),
            types.BotCommand("random_integer", "Generate random integer"),
            types.BotCommand("random_answer", 'Will random Yes or No'),
            types.BotCommand("random_emoji", 'Will random emojis'),
            types.BotCommand("random_country", "Will random country by the national flag"),
            types.BotCommand("random_image", "Will random image"),
            types.BotCommand("random_gif", "Will random gif"),
            types.BotCommand("random_mem", "Will random mem"),
            types.BotCommand("random_color", "Will random color with it's hex code"),
            types.BotCommand("random_my_choice", "Will random one object from the sequence you've typed")
        ]
    )
