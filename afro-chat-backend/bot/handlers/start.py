from tracemalloc import start
from aiogram import types
from aiogram import Dispatcher
from ..keyboards.start import start_kb
from ..data.start import start_text
import time

async def start_handler(message: types.Message):
    return await message.answer(text=start_text, reply_markup=start_kb)
    



async def handle_start_callback(call:types.CallbackQuery):
    initial_time, current_time = int(call.message.date.timestamp()), int(time.time())
    diff = abs(initial_time - current_time)
    diff /=  60

    if diff >= 5:
        return await call.message.answer(text=start_text, reply_markup=start_kb)

    return await call.message.edit_text(text=start_text, reply_markup=start_kb)
