from tracemalloc import start
from aiogram import types
from aiogram import Dispatcher
from ..keyboards.start import start_kb
from ..data.start import start_text

async def start_handler(message: types.Message):
    return await message.answer(text=start_text, reply_markup=start_kb)
    



async def handle_start_callback(call:types.CallbackQuery):
    
    return await call.message.edit_text(text=start_text, reply_markup=start_kb)
