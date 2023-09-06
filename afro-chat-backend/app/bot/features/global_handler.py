import random
from app.api_requests import make_ask_request, make_chat_request
from app.database import get_db
from app.models import Conversation

# from app.models import Ask
from app.routers.api_v1 import users
from app.bot.bot_state import State
from app.bot.person_list import PersonaState, Persona
from app.bot.features.menu.keyboards import start_kb
from app.bot.features.menu.texts import start_text
from aiogram import asyncio, types
from aiogram import Dispatcher
from app.database_operations import add_question, get_conversation, get_or_create_user
from typing import List


async def handle_globale_state(message: types.Message):
    try:
        if message.chat.id <= 0:
            return
        chat_id: str = str(message.chat.id)
        last_chat: str = State[chat_id].get("last_chat", None)

        if not last_chat:
            return await message.answer(text=start_text, reply_markup=start_kb)

        # store the USER_ID localy on dictionary to avoid further requests
        user_id: int = State[chat_id].get("user_id", None)
        if not user_id:
            user_id = await get_or_create_user(
                telegram_id=chat_id,
                firstname=message.chat.first_name,
                username=message.chat.username,
            )
            State[chat_id].update({"user_id": user_id})

        match last_chat:
            case "ask":
                response = await message.reply(
                    text="Getting your answer please wait...❄️"
                )
                answer = await make_ask_request(question=message.text, user_id=user_id)
                return await response.edit_text(answer)

            case "afro_chat":
                response = await message.answer(text="chat feature❄️")
                pass

            case last_chat if last_chat.startswith("persona") or last_chat.startswith(
                "tool"
            ):
                persona: Persona = PersonaState[last_chat]
                history: List[dict] = State[chat_id].get("history")
                session_id: int = State[chat_id].get("session_id")

                history = history[-6:]

                sticker_response = await message.answer_sticker(
                    persona.get_intermediate_sticker()
                )
                text_response = await message.reply(persona.get_intermediate_answers())

                response, session_id = await make_chat_request(
                    history=history,
                    system_prompt=persona.system_prompt,
                    question=message.text,
                    session_id=session_id,
                    user_id=user_id,
                    persona=last_chat,
                )

                answer = response["content"]
                history.append(response)

                await sticker_response.delete()
                await text_response.edit_text(answer)
                State[chat_id].update({"history": history, "session_id": session_id})
                # send a request by passing the history, session_id, system_prompt
                # # handle your memory code and everything here!!!
                # history = State[chat_id].get("")
    except Exception as e:
        print(e)
        return await message.answer(
            text="something\
                happen please came back letter"
        )


def register_global_handler(bot: Dispatcher):
    bot.register_message_handler(handle_globale_state)
