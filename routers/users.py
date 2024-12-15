from fastapi import APIRouter

user_router = APIRouter(
   prefix="/users",
   tags=["Users"],
)

@user_router.post("")
async def add_user():
   return {"user_id": 1, "tel_id":77857857}

@user_router.get("")
async def get_users():
   return "users"

@user_router.get("/me")
async def get_user(telegram_id: int ):
   return telegram_id

