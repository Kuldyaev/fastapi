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

from fastapi.templating import Jinja2Templates


app = FastAPI()

app.add_middleware(
   CORSMiddleware, 
   allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"], 
)

templates = Jinja2Templates(directory='templates')

app.include_router(api_router)

@app.post("/webhook")
async def webhook(request: Request) -> None:
   update = Update.model_validate(await request.json(), context={"bot": bot})
   await dp.feed_update(bot, update)
    
@app.get("/")
async def home_page(request: Request):
   return templates.TemplateResponse(name='home.html', context={'request': request})

application = ASGIMiddleware(app)

if __name__ == "__main__":    
   uvicorn.run(application, host='0.0.0.0', log_level='info')