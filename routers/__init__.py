from fastapi import APIRouter
from .users import user_router
from .service import service_router
from .ssevents import ssevents_router


router = APIRouter()
router.include_router(user_router)
router.include_router(service_router)
router.include_router(ssevents_router)


