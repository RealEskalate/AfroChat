
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

setting_kb = InlineKeyboardMarkup(row_width=2)
# setting_kb.insert(InlineKeyboardButton(text='🗣 Personal Mode', callback_data='mode'))
setting_kb.insert(InlineKeyboardButton(text='📜 Chat History', callback_data='history'))
setting_kb.insert(InlineKeyboardButton(text='🌐 Lanaguage', callback_data='lanaguage'))
setting_kb.row(InlineKeyboardButton(text='🅰️ About', callback_data='about'))
setting_kb.row(InlineKeyboardButton(text='🔙 BACK', callback_data='start'))
