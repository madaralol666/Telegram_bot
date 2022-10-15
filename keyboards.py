from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from texts import main_btns, pods_btns


keyboard_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=main_btns[0]),
            KeyboardButton(text=main_btns[1])
        ],
        [
            KeyboardButton(text=main_btns[2]),
            KeyboardButton(text=main_btns[3])
        ],
        [
            KeyboardButton(text=main_btns[4])
        ]
    ], resize_keyboard=True
)


keyboard_second = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = pods_btns[0], callback_data = pods_btns[0]),
            InlineKeyboardButton(text = pods_btns[1], callback_data = pods_btns[1])
        ],
        [
            InlineKeyboardButton(text = pods_btns[2], callback_data = pods_btns[2]),
            InlineKeyboardButton(text = pods_btns[3], callback_data = pods_btns[3])
        ], 
        [
            InlineKeyboardButton(text='Назад', callback_data='cancel')
        ]
    ]
)

keyboard_third = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = 'Купить', callback_data = 'buy'),
            InlineKeyboardButton(text = 'Назад', callback_data = 'cancel1')
        ]
    ]
)
