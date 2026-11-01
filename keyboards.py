from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from service import *

users_key = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌍 Places")],
        [KeyboardButton(text="❓ Help"), KeyboardButton(text="❌ Cancel")]
    ],
    resize_keyboard=True
)
