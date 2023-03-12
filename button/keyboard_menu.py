from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = KeyboardButton('/start')
get_tags_button = KeyboardButton('/get_tags')
back_button = KeyboardButton('/back')
pomodoro_today_button = KeyboardButton('/pomodoro_today')
keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_back = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu.add(get_tags_button, pomodoro_today_button)
keyboard_back.add(back_button)
