from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message): # message-параметр, types-пакет, Message-класс. Аннотация создана для подсказки
    # от среды разработки 
    await message.answer('Привет, я виртуальный помощник') #await-оператор


@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('вот меню')


