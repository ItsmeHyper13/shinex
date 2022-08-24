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
from shinex import sree

START = hndl.START_CMD

@sree.on_message(filters.command(START, prefixes=list("./")))
async def start(sree, m: Message):
    user = m.from_user
    me = await sree.get_users("me")
    owner = await sree.get_users(OWNER_ID)
    if m.chat.id == user.id:
        e = await m.reply(
            (txt.start_01).format(
                user.mention
            )
        )
        await rest(2)
        await e.edit_text(
            (txt.start_02).format(
                me.first_name,
                owner.username
            )
        )
        await rest(2)
        await e.edit_text(txt.start_03)
        await rest(1.5)
        await e.delete()
        await m.reply_sticker(txt.start_04)
        await m.reply(
            (txt.start_05).format(
                user.mention,
                me.mention
            )
        )
    if m.chat.id != user.id:
        await m.reply(404)
