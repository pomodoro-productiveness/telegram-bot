from creat_bot import dp, bot
from config_bot.kb import cd, kb_menu, markup, kb_back, kb_history
from aiogram import types, Dispatcher
from config_bot.tag import post_tags
from config_bot.show_tags import get_period


async def command_starts(message: types.Message):
    await bot.send_message(message.from_user.id, 'This bot working and it to be registered your time about learning. '
                                                 'If you want start learning push "/go"', reply_markup=kb_menu)
    await message.delete()


async def command_go(message: types.Message):
    await bot.send_message(message.from_user.id, 'Choose from proposed groups what you studied.', reply_markup=markup())
    await message.delete()


async def command_other(message: types.Message):
    await bot.send_message(message.from_user.id, text='Ok', reply_markup=kb_history)
    await message.delete()


async def command_history(message: types.Message):
    get_pomodoro = get_period()
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
                               reply_markup=kb_back)
        n += 1
    await bot.send_message(message.from_user.id, f'You study today.', reply_markup=kb_back)


async def command_back(message: types.Message):
    await bot.send_message(message.from_user.id, text='back', reply_markup=kb_menu)
    await message.delete()


def start_handler(dp: Dispatcher):
    dp.register_message_handler(command_starts, commands=['start'])
    dp.register_message_handler(command_back, commands=['back'])
    dp.register_message_handler(command_go, commands=['go'])
    dp.register_message_handler(command_other, commands=['other'])
    dp.register_message_handler(command_history, commands=['my_history'])


@dp.callback_query_handler(cd.filter())
async def result(callback: types.CallbackQuery, callback_data: dict) -> None:
    status_post = post_tags(int(callback_data['id']))
    await callback.answer(f'Your tags id:{int(callback_data["id"])} saved. STATUS {status_post}')
    await callback.message.answer(text=f'Your tags saved. STATUS {status_post}', reply_markup=kb_back)
