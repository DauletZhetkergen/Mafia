import sqlite3

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard_dict = {
    "joinToGame":"Join to Game!"
}

async def joinToGame():
    mark = InlineKeyboardMarkup()
    mark.add(InlineKeyboardButton(keyboard_dict["joinToGame"]))
    return mark
