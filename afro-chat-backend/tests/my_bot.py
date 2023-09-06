from aiogram import Bot, Dispatcher, types, executor

# Please, keep your bot tokens on environments, this code only example
bot = Bot('6589107359:AAFU8PAdEOr-u1wX11AF-u3JwEr9O-YA-YI')
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
