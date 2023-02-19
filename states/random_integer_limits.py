"""
Integer limits state. Helps with reading a user-defined range of integers.
"""
from aiogram.dispatcher.filters.state import State, StatesGroup


class RandomIntegerLimits(StatesGroup):
    limits = State()
