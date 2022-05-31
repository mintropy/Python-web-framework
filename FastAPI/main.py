from typing import Union

from pydantic import BaseModel
from fastapi import FastAPI


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/")
def get_item():
    return {"Hello": "World"}


@app.post("/")
def create_item(item: Item, q: Union[str, None] = None):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
