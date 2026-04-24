from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated

from src.database import users as db
from src.models.users import UserAdd


router = APIRouter(prefix='/users', tags=['Работа с User'])


@router.get("/")
def get_all_users():
    users = db.select_all()

    if users:
        return users
    raise HTTPException(status_code=404, detail="User not found")
    
@router.get("/{id}")
def get_user_by_id(id: int):
    user = db.select_by_id(id)
    
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")



@router.post("/")
def post_user(user: Annotated[UserAdd, Depends()]):
    user_id = db.insert(user)

    if user_id:
        return user_id
    raise HTTPException(status_code=404, detail="User_id not found, smth wrong")



@router.delete("/{user_id}")
def delete_user(user_id: int):
    status = db.delete(user_id)

    if status:
        return {"msg": "user deleted"}
    raise HTTPException(status_code=404, detail="User_id not found")
        
    
@router.put("/{user_id}")
def update_store(user_id: int, user: Annotated[UserAdd, Depends()]):
    status = db.update(user_id, user)

    if status:
        return {"msg": "User updated"}
    raise HTTPException(status_code=404, detail="User not found")
        
