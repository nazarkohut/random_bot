"""
Contains decorator that sends message to the user
in case group command was called not in group or supergroup.
"""
from functools import wraps

from aiogram import types


def is_group(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        message: types.Message = args[0]
        if message.chat.type in {"supergroup", "group"}:
            return await func(*args, **kwargs)
        else:
            await message.answer(
                f"Sorry, but this command created for groups, not for {message.chat.type} chat")

    return wrapper
