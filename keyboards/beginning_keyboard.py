from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_builder = ReplyKeyboardBuilder()

button1: KeyboardButton = KeyboardButton(text="Майнить!")
button2: KeyboardButton = KeyboardButton(text="Закончить")
kb_builder.row(button1, button2, width=2)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True)
