from service.tag_service import show_tags_with_today
from creat_bot import bot
from button.keyboard_menu import keyboard_back
from aiogram import types


async def show_pomodoro_period(message: types.Message):
    get_pomodoro = show_tags_with_today()

    def name_tags(tags):
        str_tags = ""
        for j in tags:
            str_tags += f'#{j.name} '
        return str_tags
    n = 1
    for i in get_pomodoro.__root__:
        await bot.send_message(message.from_user.id, f'{n}){i.startTime.strftime(" %H:%M:%S")}-'
                                                     f'{i.endTime.strftime("%H:%M:%S")}∥ '
                                                     f'{(i.endTime - i.startTime)} min∥ '
                                                     f'{name_tags(i.tags)}',
                               reply_markup=keyboard_back)
        n += 1
