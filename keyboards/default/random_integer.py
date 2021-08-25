import random

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.random_integer_limits import RandomIntegerLimits
from utils.misc.additional_functions.random_integer.is_int import is_int
from utils.misc.additional_functions.random_integer.read_and_swap import read_and_swap


@dp.message_handler(commands='random_integer')
async def get_limits(message: types.Message):
    data = message.text.split()
    if len(data) == 1:
        await message.reply("Type integer limits(min and max values)")
        await RandomIntegerLimits.limits.set()
    elif len(data) == 3:
        if is_int(data[1]) and is_int(data[2]):
            a, b = read_and_swap(data)
            await message.answer(str(random.randint(a, b)))
        else:
            await message.reply("You entered wrong values, please try again with valid integers")
    else:
        await message.reply("You entered the wrong number of values, please try again with 2 integers(min and max "
                            "values)")


@dp.message_handler(state=RandomIntegerLimits.limits)
async def random_integer(message: types.Message, state: FSMContext):
    data = message.text.split()
    if len(data) == 2:
        if is_int(data[0]) and is_int(data[1]):
            a, b = read_and_swap(data)
            await message.answer(str(random.randint(a, b)))
        else:
            await message.reply("You entered wrong values, please try again with valid integers")
    else:
        await message.reply("You entered the wrong number of values, please try again with 2 integers(min and max "
                            "values)")
    await state.finish()
