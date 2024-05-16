from typing import Sequence
from aiogram import types
from database.models import Video


def words_list(videos: Sequence[Video], position, videos_qnt):
    builder = types.InlineKeyboardBuilder()

    for video in videos:
        builder.row(types.InlineKeyboardButton(
            text=video.title, callback_data=f"id_{str(video.id)}"))

    builder.row(types.InlineKeyboardButton(text='⬅️', callback_data=f'prev_{position}'), types.InlineKeyboardButton(
        text=f'{position}/{videos_qnt // 10}', callback_data='position'), types.InlineKeyboardButton(text='➡️', callback_data=f'next_{position}'), width=3)

    return builder.as_markup()
