from aiogram import types
from .texts import chat_text
from .keyboards import chat_keyboard 
import time
from bot.bot_state import State



async def chat_command_handler(message: types.Message):
    try:
        chat_id = str(message.chat.id)
        State[chat_id].update({'last_chat':'afro_chat', 'last_request': int(time.time())})
        return await message.answer(text=chat_text, reply_markup=chat_keyboard)

    except Exception:
        return await message.answer(text="something happen please came back letter")

async def handle_chat_callback(call: types.CallbackQuery):
    try:
        # FIXME 
        initial_time, current_time = int(call.message.date.timestamp()), int(time.time())
        diff = abs(initial_time - current_time)
        diff /=  60

        chat_id = str(call.message.chat.id)
        State[chat_id].update({'last_chat':'afro_chat', 'last_request': int(time.time())})
        print(State[chat_id])
        return await call.message.answer(text=chat_text, reply_markup=chat_keyboard)
    except Exception:
        return await call.message.answer(text="something happen please came back letter")
