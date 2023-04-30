import asyncio
from pyrogram import Client, compose,idle
import os
from telethon import TelegramClient
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from plugins.cb_data import app as Client2


TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")

tbot = TelegramClient("test-Telethon", api_id=API_ID, api_hash=API_HASH)



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()


    
else:
    bot.run()

tbot.start(bot_token=BOT_TOKEN)

print("tbot started")

tbot.run_until_disconnected()
