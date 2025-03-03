from fastapi import FastAPI, Body, Path, Query
from pydantic import BaseModel
from typing import Annotated

class UserWallet(BaseModel):
    wallet_age: int = 0
    dollar_value: float | None = None
    ruble_value: float | None = None
    tokens_number: int = 0
    tokens: dict = {}

class Update(BaseModel):
    token: str
    buy: float | None = 0
    sell: float | None = 0


app = FastAPI()


data_base = {}

@app.post(/users/{user_id})
def add_user(user_id: int, wallet_info: Annotated[UserWallet, Body()):
    if user_id not in data_base:
      data_base[user_id] = wallet_info
      return "Wallet has been updated."

    return "User does not exist"

@app.put(/users/{user_id})
def update_wallet(user_id: int, change: Update):
    if change.token in data_base[user_id]:
      data_base[user_id].tokens[token] += change.buy - change.sell
    else:
      data_base[user_id].tokens[token] = change.buy - change.sell
    return "New tokens has been added"

@app.get(/users/{user_id})
def show_wallet(user_id: int) -> UserWallet:
    return data_base[user_id]
