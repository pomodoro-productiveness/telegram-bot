from creat_bot import dispatcher, bot
from button.keyboard_group_tags import callback_data, markup
from button.keyboard_menu import keyboard_menu, keyboard_back
from aiogram import types, Dispatcher
from service.pomodoro_service import save_pomodoro_automatically
from service.pomodoro_period import show_pomodoro_period


async def command_starts(message: types.Message):
    await bot.send_message(message.from_user.id, 'This bot working and it to be registered your time about learning. '
                                                 'If you want start learning push "/get_tags"', reply_markup=keyboard_menu)
    await message.delete()


async def command_get_tags(message: types.Message):
    await bot.send_message(message.from_user.id, 'Choose from proposed groups what you studied.', reply_markup=markup())
    await message.delete()


async def command_pomodoro_today(message: types.Message):
    await show_pomodoro_period(message)
    await bot.send_message(message.from_user.id, f'You study today.', reply_markup=keyboard_back)
    await message.delete()


def start_handler(dp: Dispatcher):
    dp.register_message_handler(command_starts, commands=['start'])
    dp.register_message_handler(command_starts, commands=['back'])
    dp.register_message_handler(command_get_tags, commands=['get_tags'])
    dp.register_message_handler(command_pomodoro_today, commands=['pomodoro_today'])


@dispatcher.callback_query_handler(callback_data.filter())
async def result(callback: types.CallbackQuery, callback_data: dict) -> None:
    status_post = save_pomodoro_automatically(int(callback_data['id']))
    await callback.answer(f'Your tags id:{int(callback_data["id"])} saved. STATUS {status_post}')
    await callback.message.answer(text=f'Your tags saved. STATUS {status_post}', reply_markup=keyboard_back)
