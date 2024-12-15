from fastapi import APIRouter
from .users import user_router

router = APIRouter()
router.include_router(user_router)

