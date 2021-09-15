from functools import wraps

from aiogram import types


def is_group(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        message: types.Message = args[0]
        if message.chat.type == "group" or message.chat.type == "supergroup":
            return await func(*args, **kwargs)
        else:
            await message.answer("Sorry, but this command created for groups, not for {} chat".format(message.chat.type))
    return wrapper
