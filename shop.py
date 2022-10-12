from aiogram.dispatcher.filters.state import StatesGroup, State

class Shop(StatesGroup):
    step1 = State()
    step2 = State()