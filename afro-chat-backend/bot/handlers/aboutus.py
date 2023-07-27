
from aiogram.types import Message, CallbackQuery
from ..data.aboutus import about_text
from ..keyboards.mainmenu import mainmenu_kb

async def handle_aboutus(message:Message):
    return await message.answer(about_text,reply_markup=mainmenu_kb)

async def handle_aboutus_callback(call: CallbackQuery):
    return await call.message.edit_text(about_text,reply_markup=mainmenu_kb)