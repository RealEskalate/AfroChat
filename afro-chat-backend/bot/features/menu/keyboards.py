from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_kb = InlineKeyboardMarkup(row_width=2)
start_kb.insert(InlineKeyboardButton(text='🗣 AskMe', callback_data='ask'))
start_kb.insert(InlineKeyboardButton(text='🗯 Chat', callback_data='chat'))
start_kb.insert(InlineKeyboardButton(text='🧑‍🎄 Personals 👥', callback_data='personals_main'))
start_kb.insert(InlineKeyboardButton(text='👨‍🏫 Task 👥', callback_data='personals_main'))
start_kb.insert(InlineKeyboardButton(text='⚙️ Settings', callback_data='setting'))
start_kb.insert(InlineKeyboardButton(text='🪄 About us', callback_data='about'))
