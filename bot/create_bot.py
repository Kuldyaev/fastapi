from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from config import Config


bot = Bot(token=Config.TELEGRAM_BOT_TOKEN, 
    default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def start_bot():
    try:
        await bot.send_message(Config.ADMIN_ID, f'Я запущен🥳.')
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(Config.ADMIN_ID, 'Бот остановлен. За что?😔')
    except:
        pass