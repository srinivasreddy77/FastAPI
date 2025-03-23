from typing import Optional
from fastapi import FastAPI

app = FastAPI()

inventory={
    1:{
        "name": "Apple",
        "price": 1.00,
        "quantity": 100
    }
}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/get-item/{item_id}")
def get_item(item_id:int):
    return inventory[item_id]


@app.get("/users/{user_id}")
def get_user(user_id:int,details:Optional[bool]=None):
    return {
        "user_id": user_id,
        "details": details
    }
