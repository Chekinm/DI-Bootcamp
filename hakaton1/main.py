from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API, HELP_COMMAND, DESCRIPTION
from random import choice
from string import ascii_letters

bot = Bot(TOKEN_API)  
dp = Dispatcher(bot)

async def on_startup(_):
    print ('started up')

@dp.message_handler(commands=['help'])
async def help_command(message:types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.answer(text="welcom to DI_hakaton_bot")
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message:types.Message):
    await message.answer(text=DESCRIPTION)
    await message.delete()

count_counter = 0

@dp.message_handler(commands=['count'])
async def count_command(message:types.Message):
    global count_counter 
    await message.answer(text='You run count command ' + str(count_counter) + ' times.')
    count_counter += 1


@dp.message_handler(commands=['give'])
async def give_command(message:types.Message):
    await bot.send_sticker(message.from_user.id, sticker ='CAACAgIAAxkBAAEIzr1kT75xEKWOz7fMBr8VJH34z4Od_wACDwMAAm2wQgMOtExku51dRi8E')




@dp.message_handler()
async def plain_replay(message:types.Message):
    answ = 'YES' if '0' in message.text else 'NO'
    print(answ)
    await message.reply(text=answ)
    




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)



