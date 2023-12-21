from typing import Union

from fastapi import FastAPI, HTTPException
from schemas import UserCreate, User

app = FastAPI()

users = []

@app.get(f"/users/{user_id}")
def user_by_id():
    return {"Hello": "World"}

@app.post(f"/users/add")
def create_user(new_user: UserCreate):
    for user in users:
        if user.name == new_user.username:
            raise HTTPException(status_code=403, detail="Такий користувач існує")
    
    users.append(new_user)
    return new_user


@app.get("/users")
def get_all_users():
    return users