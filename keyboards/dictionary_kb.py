from aiogram import types


def dictionary_kb() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Словарь")]], resize_keyboard=True)
