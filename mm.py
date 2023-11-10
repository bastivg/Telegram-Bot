# Telethon utility # pip install telethon
from telethon import TelegramClient, events
from telethon.tl.custom import Button
from pydantic import BaseModel
from telethon.tl import types

import configparser # Library for reading from a configuration file, # pip install configparser
import random # pip install random
from random import randint
import datetime # Library that we will need to get the day and time, #pip install datetime
import requests # Library used to make requests to external services (the weather forecast one) # pip install requests



import asyncio

#custom modules
import app.telegram.handlers.client, app.telegram.handlers.help, app.telegram.handlers.game
import app.telegram.handlers.register, app.telegram.handlers.login
import app.telegram.handlers.render, app.telegram.handlers.market
import app.telegram.handlers.market, app.telegram.handlers.clases

client = app.telegram.handlers.client.client
 
## Function that waits user event [press button]
def press_event(user_id):
    return events.CallbackQuery(func=lambda e: e.sender_id == user_id)


### Quiz command
@client.on(events.NewMessage(pattern='/(?i)quiz')) 
async def quiz(event):
    # get the sender
    sender = await event.get_sender()
    SENDER = sender.id

    # Start a conversation
    async with client.conversation(await event.get_chat(), exclusive=True) as conv:
        # get two random numbers between 1 and 10
        rand1 = randint(1,10)
        rand2 = randint(1,10)
        # make the sum
        sum = rand1+rand2
        # make another sum based on two different random numbers. This will be used for the wrong option
        sum_not_true = randint(1,10) + randint(1,10)

        # To make the position of the button random, let's define two keyboard that activates with 50% probability
        if(bool(random.getrandbits(1))):
            keyboard = [[Button.inline("{}".format(sum), sum)], [Button.inline("{}".format(sum_not_true), sum_not_true)]]
        else:
            keyboard = [[Button.inline("{}".format(sum_not_true), sum_not_true)],[Button.inline("{}".format(sum), sum)]]

        text = "<b>Quiz time</b> 🤖\n{} + {} = ?\n".format(str(rand1), str(rand2))
        await conv.send_message(text, buttons=keyboard, parse_mode='html')
        press = await conv.wait_event(press_event(SENDER))
        choice = str(press.data.decode("utf-8"))

        if(choice == str(sum)):
            await conv.send_message("Correct Answer!", parse_mode='html')
        else:
            await conv.send_message("Nope, i won!", parse_mode='html')

        await conv.cancel_all()
        return 




@client.on(events.NewMessage(outgoing=True, pattern='/(?i)start')) 
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    text = "Welcome Farmer 🌾🐓🐷 \nAre you ready for your new adventure?"
    await client.send_message(SENDER, text, parse_mode="html")
    text = "If you need help just type /help to see the commands"
    await client.send_message(SENDER, text, parse_mode="html")


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
#client.add_event_handler(telegram.handlers.game.harvest)
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