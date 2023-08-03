from app.api_requests import make_ask_request
from app.database import get_db

# from app.models import Ask
from app.routers.api_v1 import users
from bot.bot_state import State
from bot.features.menu.keyboards import start_kb
from bot.features.menu.texts import start_text
from aiogram import asyncio, types
from aiogram import Dispatcher
from app.database_operations import add_question, get_or_create_user


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
        chat_id = str(message.chat.id)
        last_chat = State[chat_id].get("last_chat", None)
        if not last_chat:
            return await message.answer(text=start_text, reply_markup=start_kb)

        user_id = await get_or_create_user(
            telegram_id=chat_id,
            firstname=message.chat.first_name,
            username=message.chat.username,
        )
        print("user id is", user_id)
        # user = User(name=chat_id)
        # asyncio.create_task(perform_database_operation(user))

        print(State[chat_id])
        match last_chat:
            case "ask":
                # connect it with the database that have a schema of the question and the answer
                # this would be used letter on
                # i need a function that would send reuqest to chat gpt then get the answer
                # await make_ask_request()
                # await add_question(
                #     question=message.text,
                #     answer=message.text,
                #     user_id=user_id,
                #     token_usage=1,
                # )
                response = await message.answer(text=f"getting ur answer please wait❄️")
                answer = await make_ask_request(question=message.text, user_id=user_id)
                await response.edit_text(answer)

            case "afro_chat":
                response = await message.answer(text="chat feature❄️")
                pass

            case "persona":
                pass

            case "easy formatter":
                pass
        # response = await message.answer(text="Please give me some momment while I find an answer to your request ❄️")
        # import asyncio
        # await asyncio.sleep(3)
        # return await response.edit_text(text="chat gpt response")
    except Exception:
        return await message.answer(
            text="something\
                happen please came back letter"
        )


def register_global_handler(bot: Dispatcher):
    bot.register_message_handler(handle_globale_state)
