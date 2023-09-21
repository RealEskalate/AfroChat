import unittest

from my_bot import echo

from aiogram_unittest import Requester
from aiogram_unittest.handler import MessageHandler
from aiogram_unittest.types.dataset import MESSAGE


class TestBot(unittest.IsolatedAsyncioTestCase):
    async def test_echo(self):
        request = Requester(request_handler=MessageHandler(echo))
        calls = await request.query(message=MESSAGE.as_object(text="Hello, Bot!"))
        answer_message = calls.send_messsage.fetchone()
        self.assertEqual(answer_message.text, 'Hello, Bot!')
