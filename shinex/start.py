# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
import time, datetime
from asyncio import sleep as rst
from pyrogram import client as sree
from pyrogram import filters
from string import handlers as hndl
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@sree.on_message(filters.command(hndl.START_CMD))
async def start(sree, m: Message):
    await m.reply("Hey i am alive!")
