from aiogram import types
from config import dp, db, bot
from asyncio import sleep

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}")


@dp.message_handler(commands=['subscribe'])
async def subscribe_user(message: types.Message):
    print(db.check_user(message.from_user.id))
    if db.check_user(message.chat.id) == False:
        db.add_user(message.chat.id)
        await message.answer("Вы успешно подписаны!")
    else:
        db.change_status(message.chat.id, True)
        await message.answer("Вы и так подписаны!")


@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe_user(message: types.Message):
    print(db.check_user(message.from_user.id))
    if db.check_user(message.chat.id) == True:
        db.change_status(message.chat.id, False)
        await message.answer("Вы успешно отписаны!")
    else:
        db.change_status(message.chat.id, False)
        await message.answer("У вас и так отключена подписка!")


@dp.message_handler(commands=['dice'])
async def dice(message: types.Message):
    dice = await bot.send_dice(message.chat.id)
    await sleep(4)
    await message.answer('Вам выпала ' + str(dice['dice']['value']))


