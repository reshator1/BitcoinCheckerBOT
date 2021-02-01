from aiogram import executor
from config import dp, db, bot
from asyncio import sleep, get_event_loop
import handlers

async def scheduled(wait_for):
    while True:
        await sleep(wait_for)
        subscriptions = db.active_users()
        try:
            for s in subscriptions:
                for i in s:
                    await bot.send_message(i, "Привет Захар Егоров")
        except:
            pass


if __name__ == '__main__':
    loop = get_event_loop()
    #loop.create_task(scheduled(5))
    executor.start_polling(dp, skip_updates=True)

    
    

    
