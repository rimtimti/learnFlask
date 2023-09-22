from fastapi import APIRouter

from db import products, database
from models.products import Product, ProductIn

router = APIRouter()


@router.post("/test_products/{count}")
async def create_test_products(count: int):
    for i in range(1, count + 1):
        query = products.insert().values(
            name=f"name_{i}", description=f"description_{i}", price=i * 1000
        )
        await database.execute(query)
    return {"message": f"{count} test products created"}


@router.post("/products", response_model=ProductIn)
async def create_product(new_products: ProductIn):
    query = products.insert().values(
        name=new_products.name,
        description=new_products.description,
        price=new_products.price,
    )
    last_record_id = await database.execute(query)
    return {**new_products.model_dump(), "id": last_record_id}


@router.put("/products/{products_id}", response_model=Product)
async def update_product(products_id: int, new_products: ProductIn):
    query = (
        products.update()
        .where(products.c.id == products_id)
        .values(**new_products.model_dump())
    )
    await database.execute(query)
    return {**new_products.model_dump(), "id": products_id}


@router.get("/all_products/")
async def read_all_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{products_id}", response_model=Product)
async def read_product(products_id: int):
    query = products.select().where(products.c.id == products_id)
    return await database.fetch_one(query)


@router.delete("/products/{products_id}")
async def delete_product(products_id: int):
    query = products.delete().where(products.c.id == products_id)
    await database.execute(query)
    return {"message": "products deleted"}
