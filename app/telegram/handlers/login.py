from telethon import events, Button

import app.telegram.handlers.client
import re

client = app.telegram.handlers.client.client

# Define Register for user.
@client.on(events.NewMessage(pattern='/(?i)login$')) 
async def loginHandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    message = 'To enter your farm please type: \n /name farmer \n /pass 123 \n with farmer, 123 your name and password'
    await client.send_message(SENDER, message, parse_mode="HTML")



#Obtencion de nombre
@client.on(events.NewMessage(pattern='/(?i)login')) 
async def log_namehandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mensaje = event.message.text
    match = re.search(r'/name\s+(.+)', mensaje)
    if match:
        secuencia = match.group(1)
        await event.respond(f"you have been logged in with name: {secuencia}")

#Obtencion de password.
@client.on(events.NewMessage(pattern='/(?i)pass')) 
async def Passhandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mensaje = event.message.text
    match = re.search(r'/pass\s+(.+)', mensaje)
    if match:
        secuencia = match.group(1)
        await event.respond(f"you have been logged in with password: {secuencia}")