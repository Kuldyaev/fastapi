from fastapi import Request
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.types import Message, Update
from config import Config, config


bot_router = Router()

@bot_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    print(message)
    await bot.send_message(Config.ADMIN_ID, f'Test Start🥳.')

@bot_router.message()
async def message_handler(message: Message):
   print(message)
   await message.answer('Hello from my router!')
    
bot = Bot(token=Config.TELEGRAM_BOT_TOKEN, 
    default=DefaultBotProperties(parse_mode=ParseMode.HTML))    

dp = Dispatcher(storage=MemoryStorage())  


async def start_bot():
    dp.include_router(bot_router)
    webhook_url = config.get_webhook_url()
    await bot.set_webhook(url=webhook_url,
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
    try:
        await bot.send_message(Config.ADMIN_ID, f'Я запущен🥳.')
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(Config.ADMIN_ID, 'Бот остановлен. За что?😔')
    except:
        pass
    
async def feed_update_bot(request: Request) -> None:
    try:
        update = Update.model_validate(await request.json(), context={"bot": bot})
        await dp.feed_update(bot, update)
    except:
        pass