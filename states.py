from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types


class FSM(StatesGroup):
    login = State()
    password = State()


async def reg_start(message: types.Message):
    await FSM.login.set()
    await message.reply('Enter login:')


async def get_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text
    await FSM.next()
    await message.reply("Enter password:")


async def get_password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text

    async with state.proxy() as data:
        await message.reply(str(data))

    await state.finish()


def register_handlers_states(dp: Dispatcher):
    dp.register_message_handler(reg_start, commands='register', state=None)
    dp.register_message_handler(get_login, content_types=['text'], state=FSM.login)
    dp.register_message_handler(get_password, content_types=['text'], state=FSM.password)
