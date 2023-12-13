from typing import Annotated
from fastapi import FastAPI, Query
from views import items_routers, calc_router

app = FastAPI()
app.include_router(items_routers)
app.include_router(calc_router)

@app.get("/")
def hello():
    return {"message": "Hello world!"}

@app.get("/hello/")    # параметр в Query в основном не обязателен
def hello_user(name: Annotated[str, Query(min_length=2)]):
    return {"message": f"Hello {name}!"}

@app.get("/hello/{name}/")    # параметр в пути в основном обязателен
def hello_user_path(name: str):
    return {"message": f"Hello {name}!!!!"}


def power_num(
        power: Annotated[int, Query(default=2)],
        num: int,
):
    return {"pow": num ** power}