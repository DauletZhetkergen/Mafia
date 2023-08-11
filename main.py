import os
import shutil
import sqlite3
import configparser
from datetime import datetime
import time

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove, InputMedia, ParseMode, InputFile
from aiogram.utils import executor, callback_data
import keyboard

conn = sqlite3.Connection('database.db',check_same_thread=False)
cursor = conn.cursor()

config = configparser.ConfigParser()
config.read("settings.ini")

TOKEN = config["Basic"]["TOKEN"]

bot = Bot(TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())


message_dict = {
    "gameStart":"Game started!",

}


@dp.message_handler(commands=["start", "menu"], state='*')
async def start(message: types.Message,state:FSMContext):
    await message.answer("Бот активирован!")




@dp.message_handler(commands=["create"], state='*')
async def create(message: types.Message,state:FSMContext):
    await message.answer(message_dict["gameStart"],reply_markup= await keyboard.joinToGame())








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



