from fastapi import APIRouter, Request
from bot.create_bot import start_bot, stop_bot, feed_update_bot
from database import create_tables, delete_tables

service_router = APIRouter(
   prefix="/service",
   tags=["Service"],
)

@service_router.get('/start')
async def service_start() -> None:
   await create_tables()
   await start_bot()
   return "start"

@service_router.get('/finish')
async def service_start() -> None:
   await delete_tables()
   await stop_bot()
   return "stop"
    
@service_router.post("/webhook")
async def webhook(request: Request) -> None:
   await feed_update_bot(request)
    
