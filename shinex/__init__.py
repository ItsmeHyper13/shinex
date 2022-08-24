

import logging
from importlib import import_module
from os import environ, getenv, listdir, path
from dotenv import load_dotenv

from telethon import TelegramClient
import vars
from pyrogram import Client

loop = asyncio.get_event_loop()
load_dotenv()
boot = time.time()






logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = getenv("BOT_TOKEN")
API_KEY = getenv("API_KEY")
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID", 0))
SUDO_USERS = getenv("SUDO_USERS") 

for key in ["API_KEY", "API_HASH", "BOT_TOKEN", "OWNER_ID", "SUDO_USERS"]:
    if not getenv(key):
        print(f"Please setup {str(key)}")
        try:
            value = input(f"{str(key)}: ")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            exit(1)
        environ[str(key)] = value
    if not path.exists(".env"):
        with open(".env", "w") as f:
            for key in ["API_KEY", "API_HASH", "BOT_TOKEN", "OWNER_ID", "SUDO_USERS"]:
                if key in environ:
                    f.write(f"{str(key)}={environ[str(key)]}\n")

bot = TelegramClient(None, api_id=API_KEY, api_hash=API_HASH)

sree = Client(
    ":shinex:",
    config.API_KEY,
    config.API_HASH,
    bot_token=vars.BOT_TOKEN,
)

client = TelegramClient("client", API_KEY, API_HASH).start(bot_token=TOKEN)
telethn = TelegramClient("Hyper", API_KEY, API_HASH)

async def rani_boot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await sree.start()
    getme = await sree.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name 


                 
loop.run_until_complete(rani_boot())
sree.start(bot_token=vars.BOT_TOKEN) 
