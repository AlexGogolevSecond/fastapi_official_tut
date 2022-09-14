from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items5/")
async def read_items(q: str | None = Query(default=..., min_length=3)):
    """странная конструкция, тут допускается None, но обязательно передать какое-то значение не None - такая вот непонятность"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



@app.get("/items4/")
async def read_items(q: str = Query(default=..., min_length=3)):
    """
    тут q является обязательным query-параметром и тоже не может быть None
    default=... - альтернативный способ указать, что значение требуется
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items3/")
async def read_items(q: str = Query(min_length=3)):
    """тут q является обязательным query-параметром и не может быть None"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items2/")
async def read_items(q: str | None = Query(default=None, max_length=5)):
    """Query-параметр q необязательный, но если его завели, то по нему есть ограничение в количестве символов"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: str | None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results