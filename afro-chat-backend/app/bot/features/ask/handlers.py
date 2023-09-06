from aiogram import types
from .texts import chat_text
from .keyboards import ask_keyboard
import time
from app.bot.bot_state import State


async def ask_command_handler(message: types.Message):
    try:
        chat_id = str(message.chat.id)
        State[chat_id].update({"last_chat": "ask",
                               "last_request": int(time.time())})
        return await message.answer(text=chat_text, reply_markup=ask_keyboard)

    except Exception:
        return await message.answer(
            text="something happen please came back letter"
        )


async def handle_ask_callback(call: types.CallbackQuery):
    try:
        # FIXME
        initial_time, current_time = int(call.message.date.timestamp()), int(
            time.time()
        )
        diff = abs(initial_time - current_time)
        diff /= 60

        chat_id = str(call.message.chat.id)
        State[chat_id].update({"last_chat": "ask",
                               "last_request": int(time.time())})
        return await call.message.answer(text=chat_text,
                                         reply_markup=ask_keyboard)
    except Exception:
        return await call.message.answer(
            text="something happen please came back letter"
        )
