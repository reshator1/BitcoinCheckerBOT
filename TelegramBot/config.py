import logging
from aiogram import Bot, Dispatcher
from db import Database

API_TOKEN = "1527686508:AAFWSAfjHBsPff0v556RekyJERx5lHLs0h0"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# подсоединение к БД
db = Database("db.db")

logging.basicConfig(level=logging.DEBUG)
