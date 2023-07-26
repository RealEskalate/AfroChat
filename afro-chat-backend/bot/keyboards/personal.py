from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


help_kb = InlineKeyboardMarkup(row_width=2)
help_kb.insert(InlineKeyboardButton(text='A', callback_data='help_main'))
help_kb.insert(InlineKeyboardButton(text='B', callback_data='help_games'))
help_kb.insert(InlineKeyboardButton(text='C', callback_data='help_work'))
help_kb.insert(InlineKeyboardButton(text='D', callback_data='help_imush'))

back_kb = InlineKeyboardMarkup(row_width=1)
back_kb.add(InlineKeyboardButton(text='🔙 Back', callback_data='start'))
