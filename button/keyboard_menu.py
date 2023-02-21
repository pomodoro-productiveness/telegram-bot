from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = KeyboardButton('/start')
go_button = KeyboardButton('/go')
back_button = KeyboardButton('/back')
other_button = KeyboardButton('/other')
my_history_button = KeyboardButton('/my_history')
keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_back = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_history = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menu.add(go_button, other_button)
keyboard_back.add(back_button)
keyboard_history.add(my_history_button)
