import asyncio
import logging
from aiogram.fsm.storage.redis import RedisStorage
from config import TOKEN, REDIS_URL
from handlers import router
from aiogram import Bot, Dispatcher, F

logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO, filename='logs.log')


async def main():
    """
    Главная функция для запуска бота
    """
    bot = Bot(token=TOKEN)
    storage = RedisStorage.from_url(REDIS_URL)

    dp = Dispatcher(storage=storage)
    dp.include_router(router)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    try:
        print('Start polling')
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped")
