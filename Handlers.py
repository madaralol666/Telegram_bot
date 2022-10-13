
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from texts import welcome
from keyboards import keyboard_main, keyboard_second, keyboard_third
from Main_bot import bot, dp
from Config import chat_id
from texts import pods_btns, main_btns, text_xros2, name_pod
from shop import Shop
from aiogram.dispatcher import FSMContext
async def send(dp):
    await bot.send_message(chat_id=chat_id, text='hello')

@dp.message_handler(Command('start'))
async def show_shop(message: Message):
    await message.answer(f'Добро пожаловать, в бота {message.from_user.username}, здесь вы сможете' +
    f'приобрести товары различных категорий.', reply_markup=keyboard_main)


@dp.message_handler(text='Поды')
async def show_shop(message: Message):
    await message.answer('Выберите подик', reply_markup=keyboard_second)
    await message.delete()


@dp.callback_query_handler(text=pods_btns)
async def btn1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖" + f"\nТовар: {call.data}"
     + f"\nВ наличии: ⭕ or ✅" + "\n➖➖➖➖➖➖➖➖➖➖➖➖",
      reply_markup=keyboard_third)


@dp.callback_query_handler(text_contains='Назад')
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await bot.send_message(call.from_user.id,'Выберите подик', reply_markup=keyboard_second)





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