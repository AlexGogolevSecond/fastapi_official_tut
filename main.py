from fastapi import FastAPI, Body
import uvicorn
from enum import Enum
from pydantic import BaseModel


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items2/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body(), q: str | None = None):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({'q': q})
    return results


@app.post("/items2/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    #result = {"item_id": item_id, **item.dict()}
    result = {"item_id": item_id, "item": item}
    if q:
        result.update({"q": q})
    return result


@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


class ModelName(str, Enum):
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"
    
    
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
    

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str, needy: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "needy": needy}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(item_id: str, user_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


if __name__ == '__main__':
    uvicorn.run('main:app')

