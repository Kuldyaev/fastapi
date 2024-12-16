from fastapi import APIRouter
from bot.create_bot import start_bot


service_router = APIRouter(
   prefix="/service",
   tags=["Service"],
)

@service_router.get('/start')
async def service_start() -> None:
    await start_bot()
    return "test"
    
