from telethon import TelegramClient
import configparser

#### Access credentials
config = configparser.ConfigParser() # Define the method to read the configuration file
config.read('config.ini') # read config.ini file


api_id = config.get('default','api_id') # get the api id
api_hash = config.get('default','api_hash') # get the api hash
BOT_TOKEN = config.get('default','BOT_TOKEN') # get the bot token



# Create the client and the session called session_master. We start the session as the Bot (using bot_token)
client = TelegramClient('sessions/session_master', api_id, api_hash).start(bot_token=BOT_TOKEN)
