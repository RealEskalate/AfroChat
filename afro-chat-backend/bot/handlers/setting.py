
from aiogram.types import CallbackQuery
from ..keyboards.setting import setting_kb
from ..data.setting import setting_text

async def handler_setting_callback(call:CallbackQuery):
    return await call.message.edit_text(text=setting_text,reply_markup=setting_kb)