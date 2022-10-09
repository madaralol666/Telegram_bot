from email import message
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from keyboards import keyboard, keyboard1, translate_key
from Main_bot import bot, dp
from Config import chat_id

async def send(dp):
    await bot.send_message(chat_id=chat_id, text='hello')

# @dp.message_handler(Command('start'))
# async def show_shop(message: Message):
#     await message.answer('shop', reply_markup=keyboard)


# @dp.message_handler(Text(equals=['button1', 'button2', 'button3']))
# async def get_goods(message: Message):
#     await message.answer(message.text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Command('start'))
async def show_shop(message: Message):
    await message.answer(text='Buy', reply_markup=keyboard1)

@dp.callback_query_handler(text_contains='tr')
async def tr(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('купить', reply_markup=translate_key)