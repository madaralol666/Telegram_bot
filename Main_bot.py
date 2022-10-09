import asyncio
from Config import bot_token
from aiogram import Bot, Dispatcher, executor


loop = asyncio.new_event_loop() # Начало цикла работы бота
bot = Bot(bot_token, parse_mode='HTML') 
dp = Dispatcher(bot=bot, loop=loop) # Отвечает за обновление бота 

if __name__=='__main__':
    from Handlers import dp, send
    executor.start_polling(dp, on_startup=send)