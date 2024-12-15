from aiogram.types import Message

class BotRepository:
  
     async def greet_user(message: Message) -> None:
               await message.answer(
                    f"Добро пожаловать! Присоединяйтесь к нашему проекту!\n"
               )
