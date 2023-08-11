from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_kb = InlineKeyboardMarkup(row_width=2)
start_kb.insert(InlineKeyboardButton(text='🗣 AskMe', callback_data='ask'))
start_kb.insert(InlineKeyboardButton(text='🗯 Chat', callback_data='chat'))
start_kb.insert(InlineKeyboardButton(text='🧑‍🎄 Personas 👥', callback_data='personas'))
start_kb.insert(InlineKeyboardButton(text='✍️  Tools ', callback_data='tools'))
# start_kb.insert(InlineKeyboardButton(text='⚙️ Settings', callback_data='setting'))
# start_kb.insert(InlineKeyboardButton(text='🪄 About us', callback_data='about'))
