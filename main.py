# Telethon utility # pip install telethon
from telethon import TelegramClient, events
from telethon.tl.custom import Button
from pydantic import BaseModel
from telethon.tl import types

import random # pip install random
from random import randint
import datetime # Library that we will need to get the day and time, #pip install datetime
import asyncio
import configparser

#custom modules
import app.telegram.handlers.help, app.telegram.handlers.game
import app.telegram.handlers.register, app.telegram.handlers.login
import app.telegram.handlers.render, app.telegram.handlers.market
import app.telegram.handlers.market, app.telegram.handlers.clases

from app.telegram.handlers.client import client
from app.telegram.handlers.help import helpHandler, help_granjaHandler, help_marketHandler

# Define the /start command
@client.on(events.NewMessage(pattern='/(?i)start')) 
async def start(event):
    sender = await event.get_sender()
    SENDER = sender.id
    text = "Welcome Farmer 🌾🐓🐷 \nAre you ready for your new adventure?"
    await client.send_message(SENDER, text, parse_mode="html")    
    text = "If you need help just type /help to see the commands"
    await client.send_message(SENDER, text, parse_mode="html")    
 

@client.on(events.NewMessage(pattern='/(?i)help$'))
async def help_handler(event):
    await helpHandler(client, event)  # Llama a la función helpHandler

@client.on(events.NewMessage(pattern='/(?i)help_granja$'))
async def help_granja(event):
    await help_granjaHandler(client, event)  # Llama a la función helpHandler

@client.on(events.NewMessage(pattern='/(?i)help_market$'))
async def help_market(event):
    await help_marketHandler(client, event)  # Llama a la función helpHandler



### First command, get the time and day
@client.on(events.NewMessage(pattern='/(?i)time')) 
async def time(event):
    # Get the sender of the message
    sender = await event.get_sender()
    SENDER = sender.id
    # Define the text and send the message
    text = "Received! Day and time: " + str(datetime.datetime.now())
    await client.send_message(SENDER, text, parse_mode="html")    

  
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


### MAIN
if __name__ == '__main__':
    print("Bot Started!")
    client.run_until_disconnected()