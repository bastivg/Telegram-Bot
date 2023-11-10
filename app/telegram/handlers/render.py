from telethon import events, Button

import app.telegram.handlers.client
import app.telegram.handlers.clases

client = app.telegram.handlers.client.client
"""
Recibe los datos del chatbot la ser llamado con '/render' y envia el evento

Utiliza el schema Render:

- **user_id**: id correspondiente a la plataforma en que fue enviado el mensaje
- **auth_token**: token de autorizacion
"""

# Define Register for user.
@client.on(events.NewMessage(pattern='/(?i)render$')) 
async def renderHandler(event):
    #sender = await event.get_sender()
    sender = event.user_id
    SENDER = sender.id
    render_user = app.telegram.handlers.clases.Render(
        user_id= sender,
        auth_token= sender.auth_token
    )
    message = 'Se esta renderizando'
    await client.send_message(SENDER, message, parse_mode="HTML")