from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from service.tag_service import get_tag_groups


callback_data = CallbackData('markup', 'id')


def markup():
    markup_tag = InlineKeyboardMarkup()
    tags_dict = get_tag_groups()

    def name_tags(tags):
        list_tags = ''
        for j in tags:
            list_tags += f'#{j.name} '
        return list_tags
    for i in tags_dict.__root__:
        markup_tag.add(InlineKeyboardButton(text=f'{name_tags(i.pomodoroTags)}', callback_data=callback_data.new(i.id)))
    return markup_tag
