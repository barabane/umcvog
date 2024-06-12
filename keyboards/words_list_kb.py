from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def words_list(videos, position, videos_qnt):
    builder = InlineKeyboardBuilder()

    for video in videos:
        builder.row(types.InlineKeyboardButton(
            text=video.title, callback_data=f"id_{str(video.id)}"))

    builder.row(types.InlineKeyboardButton(text='⬅️', callback_data=f'prev_{position}'), types.InlineKeyboardButton(
        text=f'{position}/{videos_qnt // 10}', callback_data='position'), types.InlineKeyboardButton(text='➡️', callback_data=f'next_{position}'), width=3)

    return builder.as_markup()
