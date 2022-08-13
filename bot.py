from aiogram import types
from aiogram import executor
from bot_keyboard import kb
from create_bot import dp, bot
import states


async def on_startup(_):
    print('Bot is running...')


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'To register, click on the button below.',
                           reply_markup=kb)

states.register_handlers_states(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
