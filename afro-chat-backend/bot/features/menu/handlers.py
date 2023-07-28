from aiogram import types
import time
from bot.features.menu.keyboards import start_kb
from bot.features.menu.texts import start_text

async def start_handler(message: types.Message):
    return await message.answer(text=start_text, reply_markup=start_kb)
    


async def handle_start_callback(call:types.CallbackQuery):
    # FIXME  should i edit the messages
    initial_time, current_time = int(call.message.date.timestamp()), int(time.time())
    diff = abs(initial_time - current_time)
    diff /=  60

    return await call.message.answer(text=start_text, reply_markup=start_kb)

    # return await call.message.edit_text(text=start_text, reply_markup=start_kb)

