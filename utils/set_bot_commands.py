from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start Bot"),
            types.BotCommand("help", "shows commands list"),
            types.BotCommand("random_integer", "Generate random integer"),
            types.BotCommand("random_answer", 'Will random Yes or No'),
            types.BotCommand("random_emoji", 'will random emojis')
        ]
    )
