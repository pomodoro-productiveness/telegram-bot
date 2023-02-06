from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config_bot.get_tags import get_tags
from aiogram.utils.callback_data import CallbackData

cd = CallbackData('markup', 'id')
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/go')
b3 = KeyboardButton('/back')
b4 = KeyboardButton('/other')
b5 = KeyboardButton('/my_history')
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
kb_history = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.add(b2, b4)
kb_back.add(b3)
kb_history.add(b5)


def markup():
    markup_tag = InlineKeyboardMarkup()
    tags_dict = get_tags()
    def name_tags(tags):
        list_tags = ''
        for j in tags:
            list_tags += f'#{j.name} '
        return list_tags
    for i in tags_dict.__root__:
        markup_tag.add(InlineKeyboardButton(text= f'{name_tags(i.pomodoroTags)}', callback_data=cd.new(i.id)))
    return markup_tag