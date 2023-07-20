from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot=Bot(token='6184545600:AAEsUnL01mXgrNjzTOq7jWfrlkVJ4mS8HWs')

dp=Dispatcher(bot)


button_uz=InlineKeyboardButton(text='🇺🇿 Узбекский', callback_data='uz_lang')
button_ru=InlineKeyboardButton(text='🇷🇺 Русский', callback_data='ru_lang')
lang_inline=InlineKeyboardMarkup().add(button_uz,button_ru)

@dp.message_handler(commands=['start'])
async def check(message: types.Message):
    await message.reply(text='Выбор язык',reply_markup=lang_inline)
    print(message.from_user.username)


executor.start_polling(dp)