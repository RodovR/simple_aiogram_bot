# Ипморт кнопок из библиотеки aiogram.types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


# Установка клавиатуры
kbm = ReplyKeyboardMarkup(resize_keyboard=True)
help_button = KeyboardButton('/help')
description_button = KeyboardButton('/description')
picture_button = KeyboardButton('/pict')
random_button = KeyboardButton('/random')
kbm.add(help_button, description_button, picture_button, random_button)


# Установка inline-кнопок для функции like/dislike
inkb = InlineKeyboardMarkup(row_width=2)
inb1 = InlineKeyboardButton(text='Нравится',
                            callback_data='like')

inb2 = InlineKeyboardButton(text='Не нравится',
                            callback_data='dislike')

inb3 = InlineKeyboardButton(text='Следующее случайное фото',
                            callback_data='rand_ph')
inkb.add(inb1, inb2, inb3)


# Установка inline-кнопок для функции рандомайзера
rand_inkb = InlineKeyboardMarkup(row_width=2)
rand_inb1 = InlineKeyboardButton(text='Рандомный emoji',
                                 callback_data='rand_em')
rand_inb2 = InlineKeyboardButton(text='Рандомный стикер',
                                 callback_data='rand_st')
rand_inb3 = InlineKeyboardButton(text='Рандомное местоположение',
                                 callback_data='rand_pl')
rand_inkb.add(rand_inb1, rand_inb2, rand_inb3)
