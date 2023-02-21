from creat_bot import dispatcher, bot
from button.keyboard_grup_tags import callback_data, markup
from button.keyboard_menu import keyboard_menu, keyboard_history, keyboard_back
from aiogram import types, Dispatcher
from service.pomodoro_service import save_pomodoro_automatically
from service.pomodoro_period import show_pomodoro_period


async def command_starts(message: types.Message):
    await bot.send_message(message.from_user.id, 'This bot working and it to be registered your time about learning. '
                                                 'If you want start learning push "/go"', reply_markup=keyboard_menu)
    await message.delete()


async def command_go(message: types.Message):
    await bot.send_message(message.from_user.id, 'Choose from proposed groups what you studied.', reply_markup=markup())
    await message.delete()


async def command_other(message: types.Message):
    await bot.send_message(message.from_user.id, text='Ok', reply_markup=keyboard_history)
    await message.delete()


async def command_history(message: types.Message):
    await show_pomodoro_period(message)
    await bot.send_message(message.from_user.id, f'You study today.', reply_markup=keyboard_back)


async def command_back(message: types.Message):
    await bot.send_message(message.from_user.id, text='back', reply_markup=keyboard_menu)
    await message.delete()


def start_handler(dp: Dispatcher):
    dp.register_message_handler(command_starts, commands=['start'])
    dp.register_message_handler(command_back, commands=['back'])
    dp.register_message_handler(command_go, commands=['go'])
    dp.register_message_handler(command_other, commands=['other'])
    dp.register_message_handler(command_history, commands=['my_history'])


@dispatcher.callback_query_handler(callback_data.filter())
async def result(callback: types.CallbackQuery, callback_data: dict) -> None:
    status_post = save_pomodoro_automatically(int(callback_data['id']))
    await callback.answer(f'Your tags id:{int(callback_data["id"])} saved. STATUS {status_post}')
    await callback.message.answer(text=f'Your tags saved. STATUS {status_post}', reply_markup=keyboard_back)
