from telethon import events, Button

from app.telegram.handlers.client import client




async def helpHandler(client, event):
    sender = await event.get_sender()
    SENDER = sender.id
    message = 'Here is a list 📜 with basic commands that can help you🐣: \n /login to log in \n /register to register \n /help_granja To see commands of game \n /help_market To see commands of market'
    await client.send_message(SENDER, message, parse_mode="HTML")

async def help_granjaHandler(client, event):
    sender = await event.get_sender()
    SENDER = sender.id
    message = 'Do you want to see your farm? 🌄\n /plant item   ;   to plant \n /water item   ;   to watered \n /harvest   item \n /render   to   render the game \n /access item   ;   to enter somewhere'
    await client.send_message(SENDER, message, parse_mode="HTML")    


async def help_marketHandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    message = 'Do you want to buy or sell? 💸 \n\n /buy item 12 \n /sell item 12 \n\n to buy / sell 12 items'
    await client.send_message(SENDER, message, parse_mode="HTML")



'''
async def iquery(query):
    if query.text == 'help':
        result = query.builder.article('Help', text="This is inline query", buttons=[
            [ Button.inline("Upload to Tg") , Button.inline("Alive")  ],
            [ Button.inline("Upload to Tg") , Button.inline("Alive")  ],
            [ Button.inline("Upload to Tg") , Button.inline("Alive")  ],
        ])
        await query.answer([result])
'''
'''
@client.on(events.NewMessage(pattern='/help'))    
async def helpHandler(event):
    results = await client.inline_query('@granja_tegridad_bot', 'help')
    await results[0].click(event.chat_id)
'''








'''
@client.on(events.NewMessage(pattern='/(?i)help Granja')) 
async def Passhandler(event):
    sender = await event.get_sender()
    SENDER = sender.id
    mensaje = event.message.text
    if match:
        secuencia = match.group(1)
        await event.respond(f"Password save: {secuencia}")

      # You can, of course, use markdown in your messages:
    message = await client.send_message(
        '**Bienvenido granjero**.'
        'Comandos para la granja:'
        '\login para logearte'
        '\Register para registrarte'

        '\Render para renderizar el juego'
        '\plan'
        '\water'

        'This message has **bold**, `code`, __italics__ and '
        'a [nice website](https://example.com)!',
        link_preview=False
    )
'''