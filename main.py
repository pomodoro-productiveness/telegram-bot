from aiogram.utils import executor
from interaction import user
from creat_bot import dispatcher

user.start_handler(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)