"""
Method that can chose random receipt from spoonacular service.
"""
from aiogram import types

from keyboards.constants import COMMON_REQUEST_TIMEOUT
from loader import dp
from config import SPOONACULAR_API_KEY
import requests

base_url = "https://api.spoonacular.com/recipes/random"


@dp.message_handler(commands="random_recipe")
async def get_random_recipe(message: types.Message):

    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "number": 1
    }

    response = requests.get(base_url, params=params, timeout=COMMON_REQUEST_TIMEOUT)

    recipe_data = response.json()["recipes"][0]
    recipe_str = f"Random recipe: {recipe_data['title']}\nIngredients:\n"
    for ingredient in recipe_data["extendedIngredients"]:
        recipe_str += f"- {ingredient['original']}\n"
    recipe_str += "Instructions:\n"
    for step in recipe_data["analyzedInstructions"][0]["steps"]:
        recipe_str += f"{step['number']}. {step['step']}\n"
    await message.answer(recipe_str)


