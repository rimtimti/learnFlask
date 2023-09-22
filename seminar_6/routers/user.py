from fastapi import APIRouter, HTTPException
from db import users, database
from models.user import User, UserIn

router = APIRouter()


@router.post("/test_users/{count}")
async def create_test_user(count: int):
    for i in range(1, count + 1):
        query = users.insert().values(
            username=f"name_{i}", email=f"email_{i}@ya.ru", password=f"{i * 123456789}"
        )
        await database.execute(query)
    return {"message": f"{count} test users created"}


@router.post("/user", response_model=UserIn)
async def create_user(user: UserIn):
    query = users.insert().values(
        username=user.username, email=user.email, password=user.password
    )
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@router.get("/all_users/")
async def read_all_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "User deleted"}
