from aiogram import Router
from bot.create_bot import start_bot


service_router = Router()

@service_router.get('/')
async def service_start() -> None:
    await start_bot()
    return "test"
    
