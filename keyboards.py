from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from Config import url_translate


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='button1'),
            KeyboardButton(text='button2')
        ],
        [
            KeyboardButton(text='button3')
        ]
    ], resize_keyboard=True
)

cb = CallbackData('buy', 'id', 'name')

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Translate', callback_data='buy:22:tr')
        ],
        [
             InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]   
)

translate_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Buy', url=url_translate)
        ]
    ]
)