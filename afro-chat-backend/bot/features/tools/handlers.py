from aiogram import types


async def handle_tools_command(message: types.Message):
    try:
        pass
        return await message.answer("Tools Will be Added in the near future")
    except Exception:
        return await message.answer(text="something happen please came back letter")


async def handle_tools_callback(call: types.CallbackQuery):
    try:
        pass
        return await call.message.answer("Tools Will be Added in the near future")
    except Exception:
        return await call.message.answer(text="something happen please came back letter")
