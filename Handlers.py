
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from texts import welcome
from keyboards import keyboard_main, keyboard_second, keyboard_third
from Main_bot import bot, dp
from Config import chat_id
from texts import pods_btns, main_btns, text_xros2
from shop import Shop
from aiogram.dispatcher import FSMContext
async def send(dp):
    await bot.send_message(chat_id=chat_id, text='hello')

@dp.message_handler(Command('start'))
async def show_shop(message: Message):
    await message.answer(welcome, reply_markup=keyboard_main)


@dp.message_handler(text='Поды')
async def show_shop(message: Message):
    await message.answer('Выберите подик', reply_markup=keyboard_second)
    await message.delete()
    await Shop.step1.set()


@dp.callback_query_handler(text_contains = pods_btns[0])
async def btn1(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text_xros2, reply_markup=keyboard_third)


@dp.callback_query_handler(text_contains = pods_btns[1])
async def btn2(call: CallbackQuery):
    await call.message.answer(main_btns[0], reply_markup=keyboard_second)


@dp.callback_query_handler(text_contains = pods_btns[2])
async def btn3(call: CallbackQuery):
    await call.message.answer(main_btns[0], reply_markup=keyboard_second)


@dp.callback_query_handler(text_contains = pods_btns[3])
async def btn4(call: CallbackQuery):
    await call.message.answer(main_btns[0], reply_markup=keyboard_second)


@dp.callback_query_handler(text_contains='Назад', state=Shop.step1)
async def cancel(call: CallbackQuery, state: FSMContext):
    await state.update_data()
    await call.answer('Cancel')
    await call.message.delete()
    await call.message.edit_reply_markup(reply_markup=None)
    await state.get_data()





# @dp.message_handler(Command('start'))
# async def show_shop(message: Message):
#     await message.answer(text='Buy', reply_markup=keyboard1)

# @dp.callback_query_handler(text_contains='tr')
# async def tr(call: CallbackQuery):
#     await call.answer(cache_time=60)

#     await call.message.answer('купить', reply_markup=translate_key)
#     # await call.message.answer(reply_markup=cancel_key)

# @dp.callback_query_handler(text_contains='cancel')
# async def cancel(call: CallbackQuery):
#     await call.answer('Отмена')
#     await call.message.edit_reply_markup(reply_markup=None)