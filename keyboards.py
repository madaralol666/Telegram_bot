from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from texts import main_btns, pods_btns, cancel_btn, buy_btn


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

cb_pods = CallbackData('buy', 'name')


keyboard_second = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = pods_btns[0], callback_data = f'buy:{pods_btns[0]}'),
            InlineKeyboardButton(text = pods_btns[1], callback_data = f'buy:{pods_btns[1]}')
        ],
        [
            InlineKeyboardButton(text = pods_btns[2], callback_data = f'buy:{pods_btns[2]}'),
            InlineKeyboardButton(text = pods_btns[3], callback_data = f'buy:{pods_btns[3]}')
        ], 
        [
            InlineKeyboardButton(text=cancel_btn, callback_data='cancel')
        ]
    ]
)

keyboard_third = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = buy_btn, callback_data = f'buy:{buy_btn}'),
            InlineKeyboardButton(text = cancel_btn, callback_data = f'buy:{cancel_btn}')
        ]
    ]
)
