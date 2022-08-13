from aiogram import types, Dispatcher

from create_bot import bot
from bot_keyboard import kb


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'To register, click on the button below.',
                           reply_markup=kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
