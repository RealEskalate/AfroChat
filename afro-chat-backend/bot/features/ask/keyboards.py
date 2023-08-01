from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ask_keyboard = InlineKeyboardMarkup(row_width=2)
ask_keyboard.row(InlineKeyboardButton(
    text='🔙 Go Back to Main Menu', callback_data='start'))
