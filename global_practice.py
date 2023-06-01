# Импорты из библиотеки aiogram
from aiogram import Bot, Dispatcher, executor, types
from config import HELP_MESSAGE, PHOTO_LIST, RANDOM_STICKER, RANDOM_EMOJI
from token import TOKEN_API

# Импорт нативной библиотеки
from random import randrange as rr

# Импорт из внешнего модуля с кнопками
from global_bot_buttons import kbm, inkb, rand_inkb


# Создание бота
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('I`ve been loaded...')


# Стартовая команда
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Бот запущен...',
                           reply_markup=kbm)


# Раздел помощи
@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    for k, v in HELP_MESSAGE.items():
        await bot.send_message(chat_id=message.chat.id,
                               text=f'/<b>{k}</b> - <em>{v}</em>',
                               parse_mode='HTML')


# Раздел с описанием
@dp.message_handler(commands='description')
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Этот бот пока что умеет ничего.')


# Реализация отправки рандомной картинки из config.PHOTO_LIST
@dp.message_handler(commands='pict')
async def send_photo_command(message: types.Message):
    ran = [i for i in PHOTO_LIST.items()]
    pic = ran[rr(0, len(ran))]
    await bot.send_photo(chat_id=message.chat.id,
                         photo=str(pic[0]),
                         caption=pic[1],
                         reply_markup=inkb)


# Открывает меню с выбором рандомного стикера/emoji/местоположения
@dp.message_handler(commands='random')
async def send_random_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Выберите опцию',
                           reply_markup=rand_inkb)


# Реализация рандомайзера
@dp.callback_query_handler()
async def get_rand_obj(callback: types.CallbackQuery):

    if callback.data == 'rand_em':
        rand_em = str(RANDOM_EMOJI[rr(0, len(RANDOM_EMOJI))])
        await callback.message.answer(text=rand_em)
        await callback.answer(text=rand_em)

    elif callback.data == 'rand_st':
        rand_st = RANDOM_STICKER[rr(0, len(RANDOM_STICKER))]
        await callback.answer(text=rand_st)
        await callback.bot.send_sticker(chat_id=callback.from_user.id,
                                        sticker=rand_st)
    elif callback.data == 'rand_pl':
        rand_pl_long = rr(0, 100)
        rand_pl_lat = rr(0, 100)
        await callback.answer(text=f'{rand_pl_long} - {rand_pl_lat}')
        await callback.bot.send_location(longitude=rand_pl_long, latitude=rand_pl_lat,
                                         chat_id=callback.from_user.id)


# Имитация функции like/dislike на фото
@dp.callback_query_handler()
async def callback_command(callback: types.CallbackQuery):
    global COUNT

    if callback.data == 'like' and COUNT >= 1:
        COUNT -= 1
        await callback.answer(f'Вы уже нажимали эту кнопку! -{COUNT+1}')
    elif callback.data == 'like':
        COUNT += 1
        await callback.answer(f'Вам понравилось! +{COUNT}')
    elif callback.data == 'rand_ph':
        pass

    await callback.answer('Вам не понравилось...')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
