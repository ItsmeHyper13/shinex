# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
from pyrogram import Client as sree, filters
from vars import SUDO_USERS as sudo, OWNER_ID as owner
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup     
from strings import handlers as hndl, strs as txt

@sree.on_message(filters.command(hndl.BAN_CMD, prefixes=list("./")) & filters.group)
async def banthisgay(sree, m: Message):
    sender = m.from_user
    if sender.id in sudo:
        await app.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        await app.send_message(
            m.chat.id,
            (txt.ban_01).format(
                
