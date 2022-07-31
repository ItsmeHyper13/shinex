# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13

from pyrogram import Client
import time
from pyrogram import idle
from vars import (API_ID, API_HASH, BOT_TOKEN)

sree = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="shinex")
)
tim = time.time()


print("Try To Logging.....🌚")
print("Bot Logging Successfully✅")


sree.start()
idle()
