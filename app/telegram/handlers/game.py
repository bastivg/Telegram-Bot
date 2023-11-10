from telethon import events, Button

import re
import app.telegram.handlers.client


client = app.telegram.handlers.client.client

# Define Register for user.
@client.on(events.NewMessage(pattern='/(?i)plant')) 
async def plantHandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mensaje = event.message.text
    match = re.search(r'/plant\s+(.+)', mensaje)
    if match:
        secuencia = match.group(1)
        await event.respond(f"You have planted {secuencia}!")

@client.on(events.NewMessage(pattern='/(?i)water')) 
async def waterHandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mensaje = event.message.text
    match = re.search(r'/water\s+(.+)', mensaje)
    if match:
        secuencia = match.group(1)
        await event.respond(f"You have watered {secuencia}!")

@client.on(events.NewMessage(pattern='/(?i)access')) 
async def accessHandler(event):
    mensaje = event.message.text
    match = re.search(r'/access\s+(.+)', mensaje)
    if match:
        secuencia = match.group(1)
        await event.respond(f"Hey!, you now have acess to: {secuencia}!")
