from bot.bot_state import State
from bot.features.menu.keyboards import start_kb
from bot.features.menu.texts import start_text
from aiogram import types
from aiogram import Dispatcher



async def handle_globale_state(message: types.Message):
    try:
        
        chat_id = str(message.chat.id)
        last_chat = State[chat_id].get('last_chat', None)
        if not last_chat:
            return await message.answer(text=start_text, reply_markup=start_kb)

            # pass = last_chat
        print(State[chat_id])
        
        match last_chat:
            case 'ask':
                # connect it with the database that have a schema of the question and the answer
                # this would be used letter on
                response = await message.answer(text="ask feature❄️")
                pass

            case 'afro_chat':
                response = await message.answer(text="chat feature❄️")
                pass

            case 'persona':
                pass

            case 'easy formatter':
                pass

        # response = await message.answer(text="Please give me some momment while I find an answer to your request ❄️")
        # import asyncio
        # await asyncio.sleep(3)
        # return await response.edit_text(text="chat gpt response")
    except Exception:
        return await message.answer(text="something happen please came back letter")



def register_global_handler(bot : Dispatcher):
    bot.register_message_handler(handle_globale_state)

