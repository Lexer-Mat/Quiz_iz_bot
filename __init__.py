import aiosqlite
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F
from data import quiz_data

# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = '7729704723:AAFdyR1F8_JFXIPdpiAyF4s-b0ujCfIw-e8'

# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()

DB_NAME = 'quiz_bot.db'

from defs import generate_options_keyboard, create_table, update_quiz_index, get_quiz_index
from defs import new_quiz, get_question
from handlers import cmd_start, cmd_quiz, right_answer, wrong_answer