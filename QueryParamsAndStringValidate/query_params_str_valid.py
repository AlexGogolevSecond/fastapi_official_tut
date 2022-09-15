from fastapi import FastAPI, Query
from pydantic import Required
import uvicorn


app = FastAPI()


@app.get("/items13/")
async def read_items(
    q: str
    | None = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items12/")
async def read_items(q: str | None = Query(default=None, title="Query string", min_length=3)):
    """added title"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items11/")
async def read_items(q: list = Query(default=[])):
    query_items = {"q": q}
    return query_items


@app.get("/items10/")
async def read_items(q: list[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items


@app.get("/items9/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items8/")
async def read_items(q: list[str] | None = Query(default=None)):
    """тут показано, что можно передать список query-параметров с одним именем; в q будет список
    в этом случае обязательно использовать Query
    """
    query_items = {"q": q}
    return query_items


@app.get("/items7/")
async def read_items(q: str = Query(min_length=3)):
    """если некомфортно использовать ... - можно использовать Required - НО по большому счёту можно тупо не использовать default"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items6/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    """если некомфортно использовать ... - можно использовать Required - НО по большому счёту можно тупо не использовать default"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


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


if __name__ == '__main__':
    uvicorn.run('query_params_str_valid:app')
