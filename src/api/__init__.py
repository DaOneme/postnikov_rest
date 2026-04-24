from src.api.users import router as users_router
from fastapi import APIRouter


#добавить prefix= для более широкого ветвления
router = APIRouter(tags=['MASTER'])
router.include_router(users_router)
