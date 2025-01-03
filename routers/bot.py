from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from repos.bot import BotRepository
from bot.create_bot import bot 

bot_router = Router()

@bot_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    print(message)
    await bot.send_message(Config.ADMIN_ID, f'Я запущен🥳.')
    
