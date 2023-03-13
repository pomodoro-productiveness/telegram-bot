from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


start_button = KeyboardButton('/start')
get_tags_button = KeyboardButton('/get_tags')
back_button = KeyboardButton('/back')
pomodoro_today_button = KeyboardButton('/pomodoro_today')
keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_back = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu.add(get_tags_button, pomodoro_today_button)
keyboard_back.add(back_button)


get_tags_inline_button = InlineKeyboardButton(text='Get_tags', callback_data='get_tags')
back_inline_button = InlineKeyboardButton(text='Back', callback_data='back')
pomodoro_today_inline_button = InlineKeyboardButton(text='Pomodoro_today', callback_data='pomodoro_today')
inline_keyboard_menu = InlineKeyboardMarkup()
inline_keyboard_back = InlineKeyboardMarkup()
inline_keyboard_menu.add(get_tags_inline_button, pomodoro_today_inline_button)
inline_keyboard_back.add(back_inline_button)
