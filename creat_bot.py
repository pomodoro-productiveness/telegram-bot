from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)
