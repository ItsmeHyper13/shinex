# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
import time, datetime
from asyncio import sleep as rest
from pyrogram import Client as sree
from pyrogram import filters
from vars import OWNER_ID
from strings import handlers as hndl, strs as txt
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

START = hndl.START_CMD

@sree.on_message(filters.command(START))
async def start(sree, m: Message):
    user = m.from_user
    me = await sree.get_user("me")
    owner = await sree.get_user(OWNER_ID)
    e = await m.reply(
        (txt.start_01).format(
            user.mention
        )
    )
    await rest(2)
    await e.edit_text(
        (txt.start_02).format(
            me.first_name,
            owner.mention
        )
    )
    await rest(2)
    await e.edit_text(txt.start_03)        
    
