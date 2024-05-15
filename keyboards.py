from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

class Markups():
    async def github():
        button = InlineKeyboardButton(text="Get mbutsk's reminder to yourself", url="https://github.com/mbutskpy/mbutsks-reminder")
        markup = InlineKeyboardBuilder().add(button).as_markup()
        return markup