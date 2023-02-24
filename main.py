from aiogram.utils import executor

from creat_bot import dispatcher
from interaction import user

user.start_handler(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)