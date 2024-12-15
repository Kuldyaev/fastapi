from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from a2wsgi import ASGIMiddleware
from fastapi.middleware.cors import CORSMiddleware
from aiogram.types import Update
from database import create_tables, delete_tables
from bot.create_bot import bot, dp, stop_bot, start_bot
from routers.bot import bot_router
from routers import router as api_router
import uvicorn
from config import config


app = FastAPI()

app.add_middleware(
   CORSMiddleware, 
   allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
 
)

app.include_router(api_router)



@app.get("/test")
async def test_route():
   await start_bot()
   return "test"

@app.post("/webhook")
async def webhook(request: Request) -> None:
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)

application = ASGIMiddleware(app)

if __name__ == "__main__":    
    uvicorn.run(application, host='0.0.0.0', log_level='info')