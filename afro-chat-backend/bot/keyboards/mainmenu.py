


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message



mainmenu_kb = InlineKeyboardMarkup(row_width=1)
mainmenu_kb.insert(InlineKeyboardButton(text='🏘 Main Menu', callback_data='start'))

