from aiogram import executor

import client
import states
from create_bot import dp


async def on_startup(_):
    print('Bot is running...')


client.register_handlers_client(dp)
states.register_handlers_states(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
