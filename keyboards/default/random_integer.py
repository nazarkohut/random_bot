import random

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.random_integer_limits import RandomIntegerLimits
from utils.misc.additional_functions.random_integer.is_int import is_int
from utils.misc.additional_functions.random_integer.read_and_swap import read_and_swap

WRONG_NUMBER_OF_PARAMS_MESSAGE: str = "You entered the wrong number of values🤨, please try again with 2 integers" \
                                      "(min and max values). Type /random_integer command to try again 🙈."
WRONG_VALUES_MESSAGE: str = "You entered wrong values😢, please try again with valid integers. " \
                            "Use the same /random_integer command 🙈."
SWAP_ACKNOWLEDGMENT_MESSAGE: str = "We used your second value as the minimum and your first value as the maximum. " \
                                   "Please, be more precise next time⌛."


@dp.message_handler(commands='random_integer')
async def get_limits(message: types.Message):
    data = message.text.split()
    if len(data) == 1:
        await message.reply("Type integer limits(min and max values(example: 1 10)).")
        await RandomIntegerLimits.limits.set()
    elif len(data) == 3:
        if is_int(data[1]) and is_int(data[2]):
            a, b, swapped = read_and_swap(data)
            if swapped:
                await message.answer(SWAP_ACKNOWLEDGMENT_MESSAGE)
            await message.answer(str(random.randint(a, b)))
        else:
            await message.reply(WRONG_VALUES_MESSAGE)
    else:
        await message.reply(WRONG_NUMBER_OF_PARAMS_MESSAGE)


@dp.message_handler(state=RandomIntegerLimits.limits)
async def random_integer(message: types.Message, state: FSMContext):
    data = message.text.split()
    if len(data) == 2:
        if is_int(data[0]) and is_int(data[1]):
            a, b, swapped = read_and_swap(data)
            if swapped:
                await message.answer(SWAP_ACKNOWLEDGMENT_MESSAGE)
            await message.answer(str(random.randint(a, b)))
        else:
            await message.reply(WRONG_VALUES_MESSAGE)
    else:
        await message.reply(WRONG_NUMBER_OF_PARAMS_MESSAGE)
    await state.finish()
