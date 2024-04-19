'''imports'''
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import random
import os
from dotenv import load_dotenv, find_dotenv

from configs.config import strt_config

env=load_dotenv(find_dotenv())

#bot = Bot(token=os.getenv('bot_token'))

config=strt_config(env)
bot=Bot(token=config.tg_bot.token)

print(config.tg_bot.token,config.tg_bot.admin_ids, config.db.databasse)
print(config.db.db_password, config.db.db_host, config.db.db_host)
print(config.db.db_user)

dp = Dispatcher()

count_game = 5
user_gamer = {'in_game':False, 
              'select_number':None,
              'failure_game': None,
              'total_game':0,
              'wins_of_user_game':0}

def get_random_number()->int:
    return random.randint(1,101)

@dp.message(CommandStart())
async def ferst_start_command(message: Message):
    await message.answer('bot for testing logarifm')

@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('bot for testing logarifm and find number')

@dp.message(Command(commands=['start']))
async def starts_command(message: Message):
    await message.answer('пошла жара, пора играть')

@dp.message(F.text.lower().in_(['да', "ок", "конечно", "давай"]))
async def game_on_command(message: Message):
    await message.answer('ты попал в игру поле чудес')
    await message.answer(get_random_number)
    #user_gamer['in_game']=True
    


if __name__=='__main__':
    dp.run_polling(bot)