from pydantic import BaseModel

import app.telegram.handlers.client, app.telegram.handlers.help
import app.telegram.handlers.register, app.telegram.handlers.login
import app.telegram.handlers.render, app.telegram.handlers.market, app.telegram.handlers.market

client = app.telegram.handlers.client.client

class Render(BaseModel):
    user_id: str
    auth_token: str

class MarketPlace(BaseModel):
    auth_token: str
    action: str
    action_item: str
    action_amount: str

class Farm(BaseModel):
    auth_token: str
    action: str
    action_item: str
    action_amount: str