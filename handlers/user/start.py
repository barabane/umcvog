import os
from dotenv import load_dotenv
from aiogram import types
from aiogram.fsm.context import FSMContext
from states import UserState
from database import db

load_dotenv()


async def start_handler(msg: types.Message, state: FSMContext):
    if user := db.get_user(msg.from_user.id):
        if user.role == "admin":
            await msg.answer("У вас есть права администратора. Для того, чтобы перейти в панель администратора, введите команду /admin")
        await state.set_state(UserState.search)
        return await msg.answer("Введите слово для поиска:", reply_markup=types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Словарь",)]], resize_keyboard=True))
    await state.set_state(UserState.password)
    await msg.answer("Введите пароль для входа:")


async def get_pass(msg: types.Message, state: FSMContext):
    if msg.text != os.getenv('PASS'):
        return await msg.answer("Неправильный пароль")
    await msg.answer("Добро пожаловать!")
    db.reg_user(msg.from_user, "user")
    await state.set_state(UserState.search)
    await msg.answer("Введите слово для поиска:", reply_markup=types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="Словарь")]], resize_keyboard=True))
