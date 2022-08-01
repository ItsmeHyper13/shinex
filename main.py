# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13

import time
from pyrogram import Client, idle
from vars import (API_ID, API_HASH, BOT_TOKEN)

tim = time.time()

sree = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="shinex")
)
print("Bot Started")
sree.start()
idle()
