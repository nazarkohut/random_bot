import random

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.random_integer_limits import RandomIntegerLimits
from utils.misc.additional_functions.is_int import is_int


@dp.message_handler(commands='random_integer')
async def get_limits(message: types.Message):
    await RandomIntegerLimits.limits.set()
    if len(message.text.split()) == 1:
        await message.reply("Type integer limits(min and max values)")


@dp.message_handler(state=RandomIntegerLimits.limits)
async def random_integer(message: types.Message, state: FSMContext):
    if "/random_integer" in message.text:
        if len(message.text.split()) != 3:
            await message.reply("You entered the wrong number of values, please try again with 2 integers(min and max "
                                "values)")
        else:
            if is_int(message.text.split()[1]) and is_int(message.text.split()[2]):
                a, b = map(int, message.text.split()[1:])
                await message.answer(str(random.randint(a, b)))
            else:
                await message.reply("You entered wrong values, please try again with valid integers")
    elif len(message.text.split()) == 2:
        if is_int(message.text.split()[0]) and is_int(message.text.split()[1]):
            a, b = map(int, message.text.split())
            await message.answer(str(random.randint(a, b)))
        else:
            await message.reply("You entered wrong values, please try again with valid integers")
    else:
        await message.reply("You entered the wrong number of values, please try again with 2 integers(min and max "
                            "values)")
    await state.finish()
