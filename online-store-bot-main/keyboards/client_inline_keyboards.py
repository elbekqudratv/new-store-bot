from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import DB_NAME
from utils.database import Database


db = Database(DB_NAME)


# Function for make inline keyboards from category names
def get_category_list() -> InlineKeyboardMarkup:
    categories = db.get_categories()
    rows = []
    for category in categories:
        rows.append([
            InlineKeyboardButton(
                text=category[1],
                callback_data=str(category[0])
            )
        ])
    kb_categories = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb_categories


# Function for make inline keyboards from product names
def left_right_k():
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton(text="⬅️", callback_data="left"),
        InlineKeyboardButton(text="➡️", callback_data="right")
    )
    return keyboard

