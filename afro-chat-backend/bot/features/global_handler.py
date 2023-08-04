import random
from app.api_requests import make_ask_request, make_chat_request
from app.database import get_db

# from app.models import Ask
from app.routers.api_v1 import users
from bot.bot_state import State
from bot.person_list import PersonaState, Persona
from bot.features.menu.keyboards import start_kb
from bot.features.menu.texts import start_text
from aiogram import asyncio, types
from aiogram import Dispatcher
from app.database_operations import add_question, get_or_create_user
from typing import List


# async def perform_database_operation(user: User, message: str = "") -> None:
#     print("continue working the task", flush=True)

#     async for session in get_db():
#         await user.save(session)
#         await asyncio.sleep(3)
#         user2 = User(name="abella")
#         await user2.save(session)
#         print(user.id, user.telegram_id, flush=True)


async def handle_globale_state(message: types.Message):
    try:
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

        print("*" * 100)
        print("users last_chat", last_chat)
        print("USER", State[chat_id])
        match last_chat:
            case "ask":
                response = await message.reply(
                    text=f"Getting your answer please wait...❄️"
                )
                answer = await make_ask_request(question=message.text, user_id=user_id)
                await response.edit_text(answer)

            case "afro_chat":
                response = await message.answer(text="chat feature❄️")
                pass

            case last_chat if last_chat.startswith("persona"):
                persona: Persona = PersonaState[last_chat]
                history: List[dict] = State[chat_id].get("history")
                session_id: int = State[chat_id].get("session_id")

                print("---"*100)
                history = history[-6:]

                sticker_response = await message.answer_sticker(
                    persona.get_intermediate_sticker()
                )
                text_response = await message.reply(persona.get_intermediate_answers())
                history = await make_chat_request(
                    history=history,
                    system_prompt=persona.system_prompt,
                    question=message.text,
                    session_id=session_id,
                )
                answer = history[-1]["content"]

                await sticker_response.delete()
                await text_response.edit_text(answer)
                State[chat_id].update({"history": history})
                # send a request by passing the history, session_id, system_prompt
                # # handle your memory code and everything here!!!
                # history = State[chat_id].get("")
    except Exception as e:
        return await message.answer(
            text="something\
                happen please came back letter"
        )


def register_global_handler(bot: Dispatcher):
    bot.register_message_handler(handle_globale_state)
