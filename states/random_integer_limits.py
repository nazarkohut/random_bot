from aiogram.dispatcher.filters.state import State, StatesGroup


class RandomIntegerLimits(StatesGroup):
    limits = State()
