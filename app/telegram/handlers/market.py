import re
from telethon import events, Button




# custom modules

import app.telegram.handlers.clases
import app.telegram.handlers.client
client = app.telegram.handlers.client.client

"""
Recibe los datos del chatbot la ser llamado con '/(buy o sell) item amount' y envia el evento

Utiliza el schema Marketplace:

- **auth_token**: token de autorizacion
- **action**: comando de accion buy o sell
- **action_item**: item que se usara en la accion
- **action_amount**: cantidad del item que se usara en la accion
"""
@client.on(events.NewMessage(pattern='/(?i)buy')) 
async def marketbuyHandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mensaje = event.message.text
    match = re.search(r'/buy\s+(.+)', mensaje)
    if match:
        items,  amount = match.group(1).split(None, 1)[0], match.group(1).split(None, 1)[1]
        await event.respond(f"Buy.")
        # Obtener la cadena después de "/buy"
        await event.respond(f"item {items}")
        #amount = match.group(2)
        await event.respond(f"amount {amount}")


@client.on(events.NewMessage(pattern='/(?i)sell'))
async def marketsellHandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mensaje = event.message.text
    match = re.search(r'/sell\s+(.+)', mensaje)
    if match:
        items,  amount = match.group(1).split(None, 1)[0], match.group(1).split(None, 1)[1]
        await event.respond(f"Sell.")
        # Obtener la cadena después de "/buy"
        await event.respond(f"item {items}")
        #amount = match.group(2)
        await event.respond(f"amount {amount}")



'''

def render_create(marketplace: handlers.clases.MarketPlace):


    marketplace_action = handlers.clases.MarketPlace(
        auth_token=marketplace.auth_token,
        action= marketplace.action_item,
        action_item= marketplace.action_item,
        action_amount= marketplace.action_amount
    )
    logging.info(f"Accion realizada: Se {marketplace.action} {marketplace.action_amount} {marketplace.action_item}")
    emit_events.send_marketplace(marketplace.action, marketplace.action_item, marketplace.action_amount, marketplace_action.model_dump())

    return marketplace_action

'''