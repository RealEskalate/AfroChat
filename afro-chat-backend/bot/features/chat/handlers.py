from aiogram import types
from .texts import chat_text
from .keyboards import chat_keyboard
import time
from bot.bot_state import State
from bot.person_list import Persona, PersonaState


async def chat_command_handler(message: types.Message):
    try:
        chat_id = str(message.chat.id)
        persona_name = "persona:afro_chat"
        # State[chat_id].update({'last_chat':'afro_chat', 'last_request': int(time.time())})
        # return await message.answer(text=chat_text, reply_markup=chat_keyboard)

        try:
            persona: Persona = PersonaState[persona_name]
            # handle your memory code and everything here!!!
            State[chat_id].update(
                {
                    "last_chat": persona_name,
                    "last_request": int(time.time()),
                    "session_id": None,
                    "history": [],
                }
            )
            await message.answer_sticker(persona.get_initial_sticker())
            return await message.answer(
                persona.get_greeting_text(message.chat.username)
            )

        except Exception:
            await message.answer(
                "You need a premium account to have an access to this persona"
            )

    except Exception:
        return await message.answer(text="something happen please came back letter")


async def handle_chat_callback(call: types.CallbackQuery):
    try:
        # FIXME
        initial_time, current_time = int(call.message.date.timestamp()), int(
            time.time()
        )
        diff = abs(initial_time - current_time)
        diff /= 60

        message = call.message
        chat_id = str(message.chat.id)
        persona_name = "persona:afro_chat"

        try:
            persona: Persona = PersonaState[persona_name]
            # handle your memory code and everything here!!!
            State[chat_id].update(
                {
                    "last_chat": persona_name,
                    "last_request": int(time.time()),
                    "session_id": None,
                    "history": [],
                }
            )
            await message.answer_sticker(persona.get_initial_sticker())
            return await message.answer(
                persona.get_greeting_text(message.chat.username)
            )

        except Exception:
            await message.answer(
                "You need a premium account to have an access to this persona"
            )
    
        # State[chat_id].update(
        #     {"last_chat": "afro_chat", "last_request": int(time.time())}
        # )
        # print(State[chat_id])
        # return await call.message.answer(text=chat_text, reply_markup=chat_keyboard)
    except Exception:
        return await call.message.answer(
            text="something happen please came back letter"
        )
