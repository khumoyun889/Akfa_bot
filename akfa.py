from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot=Bot(token='6184545600:AAEsUnL01mXgrNjzTOq7jWfrlkVJ4mS8HWs')

dp=Dispatcher(bot)


button1=InlineKeyboardButton(text='button1', callback_data='In_First_button')
button2=InlineKeyboardButton(text='button2', callback_data='In_Second_button')
keyboard_inline=InlineKeyboardMarkup().add(button1,button2)

@dp.message_handler(commands=['start'])
async def check(message: types.Message):
    await message.reply('hi! how are you',reply_markup=keyboard_inline)



executor.start_polling(dp)