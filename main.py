# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
import time
import asyncio
from pyrogram import Client, idle
from vars import (API_ID, API_HASH, BOT_TOKEN)

sree = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="shinex")
)
tim = time.time()
async def main():
    async with sree:
        try:
            await sree.send_message(-1001491370204, "ʙᴏᴛ sᴛᴀʀᴛᴇᴅ 🥀")
        except Exception as e:
            print(e)
            pass
print("""╭┈┈┈┈┈┈┈┈┈┈┈┈𑁍ࠬ┈┈┈╮
❝ʙᴏᴛ ɪs ᴀʟɪᴠᴇ🎗⚡❞
❝sᴛᴀᴛᴜs » sᴛᴀʀᴛᴇᴅ 🥀❞
❝ᴅᴇᴠ » ɪᴛ's ʜʏᴘᴇʀ🇮🇳❞
❝ᴊᴏɪɴ @SILENT_DEVS❞
╰┈┈┈𑁍ࠬ┈┈┈┈┈┈┈┈┈┈┈┈╯""")

sree.start()
idle()
