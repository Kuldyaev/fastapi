
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import Config

def app_keyboard(user_id: int, is_new_user: bool) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    if is_new_user:
         url_add_application = f"{Config.BASE_URL}index.html?user_id={user_id}"
         kb.button(text="Участвовать", callback_data="participate")
    else:
         url_add_application = f"{Config.BASE_URL}index.html?user_id={user_id}"
         kb.button(text="Приложение", web_app=WebAppInfo(url=url_add_application))
        
    

    kb.adjust(1)
    return kb.as_markup()