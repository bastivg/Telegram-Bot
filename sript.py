import os
import asyncio
import logging
from typing import Union
from asyncio import create_task
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Telethon utility # pip install telethon
from telethon import TelegramClient, events
from telethon.tl.custom import Button
from pydantic import BaseModel

# custom modules
from routers.users import users
from discord.discord_bot import bot
from events.events import Emit

#custom modules for telegram bot
import app.telegram.handlers.client, app.telegram.handlers.help, app.telegram.handlers.game
import app.telegram.handlers.register, app.telegram.handlers.login
import app.telegram.handlers.render, app.telegram.handlers.market
import app.telegram.handlers.market, app.telegram.handlers.clases

app = FastAPI(
    title="Middleware Discord/Telegram",
    version="0.0.1",
    summary="Esta api tiene como fin conectar a un chat bot de Discord/telegram con otros microservicios"
)

app.include_router(users)

emit_events = Emit()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


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



@app.get("/")
async def root():
    return {"Hello": "World"}


@app.post(
        "/render",
        response_model=Render,
        tags=["Render"],
        summary="Envia un evento al exchange 'render' con routing key: action"
    )
def render_create(render: Render):
    """
    Recive los datos del chatbot la ser llamado con '/render' y envia el evento
    
    Utiliza el schema Render:

    - **user_id**: id correspondiente a la plataforma en que fue enviado el mensaje
    - **auth_token**: token de autorizacion
    """
    render_user = Render(
        user_id= render.user_id,
        auth_token=render.auth_token
    )
    logging.info(f"Render creado para el usuario:{render.user_id}")
    emit_events.send_render(render.user_id, "render", render_user.model_dump())

    return render_user


@app.post(
        "/marketplace",
        response_model=MarketPlace,
        tags=["MarketPlace"],
        summary="Envia un evento al exchange 'marketplace' con routing key: action.item.amount"
    )
def render_create(marketplace: MarketPlace):
    """
    Recive los datos del chatbot la ser llamado con '/(buy o sell) item amount' y envia el evento

    Utiliza el schema Marketplace:

    - **auth_token**: token de autorizacion
    - **action**: comando de accion buy o sell
    - **action_item**: item que se usara en la accion
    - **action_amount**: cantidad del item que se usara en la accion
    """

    marketplace_action = MarketPlace(
        auth_token=marketplace.auth_token,
        action= marketplace.action_item,
        action_item= marketplace.action_item,
        action_amount= marketplace.action_amount
    )
    logging.info(f"Accion realizada: Se {marketplace.action} {marketplace.action_amount} {marketplace.action_item}")
    emit_events.send_marketplace(marketplace.action, marketplace.action_item, marketplace.action_amount, marketplace_action.model_dump())

    return marketplace_action


@app.post(
        "/farm",
        response_model=Farm,
        tags=["farm"],
        summary="Envia un evento al exchange 'farm' con routing key: action.item.amount"
        )
def render_create(farm: Farm):
    """
    Recive los datos del chatbot la ser llamado con '/(harevest, plant o water) item amount' y envia el evento

    Utiliza el schema farm:
    
    - **auth_token**: token de autorizacion
    - **action**: comando de accion harvest, plant o water
    - **action_item**: item que se usara en la accion
    - **action_amount**: cantidad del item que se usara en la accion
    """

    farm_action = Farm(
        auth_token=farm.auth_token,
        action= farm.action_item,
        action_item= farm.action_item,
        action_amount= farm.action_amount
    )
    logging.info(f"Accion realizada: Se {farm.action} {farm.action_amount} {farm.action_item}")
    emit_events.send_farm(farm.action, farm.action_item, farm.action_amount, farm.model_dump())

    return farm_action

async def start_bot():
    await bot.start(os.getenv("DISCORD_TOKEN"))

create_task(start_bot())


# Telegram Bot

client = app.telegram.handlers.client.client

# Define the /start command
@client.on(events.NewMessage(pattern='/(?i)start')) 
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    text = "Welcome Farmer 🌾🐓🐷 \nAre you ready for your new adventure?"
    await client.send_message(SENDER, text, parse_mode="HTML")
    text = "If you need help just type /help to see the commands"
    await client.send_message(SENDER, text, parse_mode="HTML")

#Register
client.add_event_handler(app.telegram.handlers.register.registerHandler)
client.add_event_handler(app.telegram.handlers.register.nameHandler)
client.add_event_handler(app.telegram.handlers.register.passHandler)

#Login
client.add_event_handler(app.telegram.handlers.login.loginHandler)
client.add_event_handler(app.telegram.handlers.login.log_namehandler)

#Help
client.add_event_handler(app.telegram.handlers.help.helpHandler)
client.add_event_handler(app.telegram.handlers.help.help_granjaHandler)
client.add_event_handler(app.telegram.handlers.help.help_marketHandler)

#Game
client.add_event_handler(app.telegram.handlers.game.plantHandler)
client.add_event_handler(app.telegram.handlers.game.waterHandler)
client.add_event_handler(app.telegram.handlers.game.harvest)
client.add_event_handler(app.telegram.handlers.game.accessHandler)

#Render
client.add_event_handler(app.telegram.handlers.render.renderHandler)

#Market
client.add_event_handler(app.telegram.handlers.market.marketsellHandler)
client.add_event_handler(app.telegram.handlers.market.marketbuyHandler)

loop = asyncio.get_event_loop()
client.start()
loop.run_forever()

### MAIN
if __name__ == '__main__':
    print("Bot Started!")
    client.run_until_disconnected()