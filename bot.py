from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram import executor
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is running...')


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'To register, click on the button below.')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
