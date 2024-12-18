from fastapi import APIRouter, Request
from bot.create_bot import  bot, dp, start_bot
from aiogram.types import Update

from config import config


service_router = APIRouter(
   prefix="/service",
   tags=["Service"],
)

@service_router.get('/start')
async def service_start() -> None:
   await start_bot()
   webhook_url = config.get_webhook_url()
   await bot.set_webhook(url=webhook_url,
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
   return "test"
    
@service_router.post("/webhook")
async def webhook(request: Request) -> None:
   update = Update.model_validate(await request.json(), context={"bot": bot})
   await dp.feed_update(bot, update)
    
