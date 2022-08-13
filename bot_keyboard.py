from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/register')
b2 = KeyboardButton('/help')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(b1, b2)
