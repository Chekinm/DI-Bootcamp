from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API, HELP_COMMAND, DESCRIPTION
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# coonect both with my tocken

bot = Bot(TOKEN_API)
# connet it with dispather
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True
                         )    # default = False
  

b1 = KeyboardButton('/help')
b2 = KeyboardButton('/vote')

kb.add(b1).add(b2)

ib1 = InlineKeyboardButton(text = '❤️',
                           callback_data='like')
ib2 = InlineKeyboardButton(text = ' 👎' ,
                            callback_data='dislike')
ikb = InlineKeyboardMarkup(row_width=2)
ikb.add(ib1, ib2)


print(str(kb))
async def on_startup(_):
    print ('started up')

@dp.message_handler(commands=['start'])
async def help_command(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcom to DI hacaton bot',
                         reply_markup=kb)
    await message.delete()



@dp.message_handler(commands=['vote'])
async def help_command(message:types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                        photo='https://www.treehugger.com/thmb/IAlZGVzhRLGZL_E0zSv7qbzyGRA=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-1273584292-cbcd5f85f4c646d58f7a7fa158dcaaeb.jpg',
                        caption='Do you like the photo',
                        reply_markup=ikb)
    

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='you like it')
    await callback.answer(text='you dont like it')

@dp.message_handler(commands=['help'])
async def start_command(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                          text=HELP_COMMAND,
                          parse_mode='HTML',
                          reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message:types.Message):
    await message.answer(text=DESCRIPTION)
    await message.delete()


@dp.message_handler(commands=['give'])
async def give_command(message:types.Message):
    await bot.send_sticker(chat_id=message.chat.id, sticker ='CAACAgIAAxkBAAEIzr1kT75xEKWOz7fMBr8VJH34z4Od_wACDwMAAm2wQgMOtExku51dRi8E')

@dp.message_handler()
async def hear_in_message(message:types.Message):
    if '❤️' in message.text:
        await message.answer(text='💙')





if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)