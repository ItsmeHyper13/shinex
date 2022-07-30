# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
import time, datetime
from asyncio import sleep as rst
from pyrogram import client as sree
from pyrogram import filters
from strings import handlers as hndl
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

START = hndl.START_CMD

@sree.on_message(filters.command(START))
async def start(sree, m: Message):
    await m.reply("Hey i am alive!")
