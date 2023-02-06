from aiogram.utils import executor
from config_bot import user
from creat_bot import dp

user.start_handler(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)