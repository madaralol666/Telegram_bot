import asyncio
from email import message
from Config import bot_token
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


loop = asyncio.new_event_loop() # Начало цикла работы бота
bot = Bot(bot_token, parse_mode='HTML')
storage = MemoryStorage() 
dp = Dispatcher(bot=bot, loop=loop, storage=storage) # Отвечает за обновление бота 

async def shutdown(dp):
    await storage.close()
    await bot.close()
    
if __name__=='__main__':
    from Handlers import dp, send
    executor.start_polling(dp, on_startup=send, on_shutdown=shutdown)