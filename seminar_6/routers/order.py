import datetime
import random

from fastapi import APIRouter
from db import products, database, orders, users
from models.order import Order, OrderIn

router = APIRouter()


@router.post("/test_order/{count}")
async def create_test_order(count: int):
    for i in range(1, count + 1):
        users_query = users.select()
        users_list = await database.fetch_all(users_query)
        products_query = products.select()
        products_list = await database.fetch_all(products_query)
        query = orders.insert().values(
            user_id=random.choice([user_id[0] for user_id in users_list]),
            products_id=random.choice(
                [products_id[0] for products_id in products_list]
            ),
            order_date=datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
            status=random.choice(["new", "accepted", "at work", "completed"]),
        )
        await database.execute(query)
    return {"message": f"{count} test orders create"}


@router.post("/order/{user_id}/{products_id}", response_model=OrderIn)
async def create_order(user_id: int, products_id: int, new_order: OrderIn):
    query = orders.insert().values(
        user_id=user_id,
        products_id=products_id,
        order_date=datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
        status=new_order.status,
    )
    last_record_id = await database.execute(query)
    return {**new_order.model_dump(), "id": last_record_id}


@router.put("/order/{order_id}", response_model=OrderIn)
async def update_order(order_id, new_products: OrderIn):
    query = (
        orders.update()
        .where(orders.c.id == order_id)
        .values(
            status=new_products.status,
            order_date=datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
        )
    )
    await database.execute(query)
    return {**new_products.model_dump(), "id": order_id}


@router.get("/all_orders/")
async def read_all_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.get("/order/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@router.delete("/order/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {"message": "order deleted"}
