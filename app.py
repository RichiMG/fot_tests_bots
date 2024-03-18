'''imports'''
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from random import randint


bot = Bot(token=bot_token)
dp = Dispatcher()

count_game = 5
user_gamer = {'in_game':False, 
              'select_number':None,
              'failure_game': None,
              'total_game':0,
              'wins_of_user_gamer':0}

def get_random_number()->int:
    return randit(1,101)

@dp.message(CommandStart())
async def ferst_start_command(message: Message):
    await message.answer('bot for testing logarifm')

@dp.message(Command(commands=['help']))
async def starts_command(message: Message):
    await message.answer('helps')

if __name__=='__main__':
    dp.run_polling(bot)