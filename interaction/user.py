from creat_bot import dispatcher, bot
from button.keyboard_group_tags import callback_data, markup
from button.keyboard_menu import keyboard_menu, keyboard_back, inline_keyboard_menu, inline_keyboard_back
from aiogram import types, Dispatcher
from service.pomodoro_service import save_pomodoro_automatically
from service.pomodoro_period import show_pomodoro_period


async def command_starts(message: types.Message):
    await bot.send_message(message.from_user.id, 'Bot started', reply_markup=keyboard_menu)
    await message.answer(text='Bot started', reply_markup=inline_keyboard_menu)
    await message.delete()


async def command_get_tags(message: types.Message):
    await bot.send_message(message.from_user.id, 'Choose from proposed groups what you studied.',
                           reply_markup=markup())
    await message.delete()


@dispatcher.callback_query_handler(text='get_tags')
async def get_tags(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='Choose from proposed groups what you studied.',
                           reply_markup=markup())


async def command_pomodoro_today(message: types.Message):
    await show_pomodoro_period(message)
    await bot.send_message(message.from_user.id, f'You study today.', reply_markup=keyboard_back)
    await message.delete()


@dispatcher.callback_query_handler(text='pomodoro_today')
async def pomodoro_today(callback_query: types.CallbackQuery):
    await show_pomodoro_period(callback_query)
    await bot.send_message(callback_query.from_user.id, text='You study today.', reply_markup=inline_keyboard_back)


@dispatcher.callback_query_handler(text='back')
async def back(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text='wtf', reply_markup=inline_keyboard_menu)


def start_handler(dp: Dispatcher):
    dp.register_message_handler(command_starts, commands=['start'])
    dp.register_message_handler(command_starts, commands=['back'])
    dp.register_message_handler(command_get_tags, commands=['get_tags'])
    dp.register_message_handler(command_pomodoro_today, commands=['pomodoro_today'])


@dispatcher.callback_query_handler(callback_data.filter())
async def result(callback: types.CallbackQuery, callback_data: dict) -> None:
    status_post = save_pomodoro_automatically(int(callback_data['id']))
    await callback.answer(f'Your tags id:{int(callback_data["id"])} saved. STATUS {status_post}')
    await callback.message.edit_reply_markup()
    await callback.message.answer(text=f'Your tags saved. STATUS {status_post}', reply_markup=inline_keyboard_back)
