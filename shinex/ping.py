# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
import time
from asyncio import sleep as rest
from pyrogram import Client as sree
from pyrogram import filters
from vars import OWNER_ID
from strings import handlers as hndl, strs as txt
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@sree.on_message(filters.command(hndl.PING_CMD) & filters.group)
async def ping(sree, m: Message):
    start_time = time.time()
    await m.reply(txt.ping_01)
