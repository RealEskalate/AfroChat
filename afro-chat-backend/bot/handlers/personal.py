from aiogram.types import Message,CallbackQuery
from ..keyboards.personal import back_kb,help_kb
from ..data.personal import action_text,actions_help
from ..handlers.start import handle_start_callback,start_handler

async def handle_list_personal(call: CallbackQuery):
    
    print(call.data.split('_'))
    action = call.data.split('_')[1]
    if action == '':
        return await handle_start_callback(call)
    text = actions_help[action]
    try:
        return await call.message.edit_text(text=text, reply_markup=back_kb if action != 'start' else help_kb)
    except:
        return await call.answer('😎')


async def handle_single_personal(message: Message):
    await message.answer(action_text)
