"""
My choice state. Helps with reading a user-defined choices.
"""
from aiogram.dispatcher.filters.state import State, StatesGroup


class RandomMyChoice(StatesGroup):
    list_of_choices = State()
