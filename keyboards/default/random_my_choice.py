import numpy as np
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.random_my_choice import RandomMyChoice


@dp.message_handler(commands="random_my_choice")
async def random_my_choice(message: types.Message):
    data = message.text.split()
    if len(data) == 1:
        await message.answer("Enter a list of things you want to be randomized🔥:")
        await RandomMyChoice.list_of_choices.set()
    else:
        await message.answer(np.random.choice(data[1:]))


@dp.message_handler(state=RandomMyChoice.list_of_choices)
async def random_integer(message: types.Message, state: FSMContext):
    await message.answer(np.random.choice(message.text.split()))
    await state.finish()
