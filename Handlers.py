
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from keyboards import keyboard_main, keyboard_second, keyboard_third
from Main_bot import bot, dp
from Config import chat_id
from texts import pods_btns, main_btns, welc, txt_xros2
from shop import Shop
from aiogram.dispatcher import FSMContext

async def send(dp):
    await bot.send_message(chat_id=chat_id, text='hello')

@dp.message_handler(Command('start'))
async def show_shop(message: Message):
    name = await bot.get_me()
    await message.answer(welc(name.first_name),  reply_markup=keyboard_main)


@dp.message_handler(text='Поды')
async def show_shop(message: Message):
    await message.answer('Выберите подик', reply_markup=keyboard_second)
    await message.delete()
    await Shop.step1.set()


@dp.callback_query_handler(text=pods_btns, state=Shop.step1)
async def btn1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(txt_xros2(call.data), reply_markup=keyboard_third)


@dp.callback_query_handler(text_contains='cancel', state=Shop.step1)
async def cancel_second(call: CallbackQuery):
    await call.message.delete()
    await bot.send_message(call.from_user.id,'Выберите подик', reply_markup=keyboard_second)
