from typing import Sequence
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
from database.models import Video


def get_dictionary_kb(videos: Sequence[Video], position, videos_qnty):
    builder = InlineKeyboardBuilder()

    for video in videos:
        builder.row(InlineKeyboardButton(
            text=video.title, callback_data=f"id_{str(video.id)}"))

    builder.row(InlineKeyboardButton(text='⬅️', callback_data=f'prev_{position}'), InlineKeyboardButton(
        text=f'{position}/{videos_qnty // 10}', callback_data='position'), InlineKeyboardButton(text='➡️', callback_data=f'next_{position}'), width=3)

    return builder.as_markup()
