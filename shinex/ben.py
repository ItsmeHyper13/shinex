# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
from pyrogram import Client as sree, filters
from vars import SUDO_USERS as sudo, OWNER_ID as owner
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup     
from strings import handlers as hndl, strs as txt

@sree.on_message(filters.command(hndl.BAN_CMD, prefixes=list("./")) & filters.group)
async def banthisgay(sree, m: Message):
    chut = await sree.get_chat(m.chat.id)
    sender = m.from_user
    if sender.id in sudo:
        if len(m.command) == 1:
            usr = await sree.get_users(m.reply_to_message.from_user.id)
            try:
                await sree.ban_chat_member(m.chat.id, usr.id)
                await sree.send_message(
                    m.chat.id,
                    (txt.ban_01).format(
                        chut.title,
                        usr.mention,
                        usr.id,
                        sender.first_name
                    )
                )
            except Exception as e:
                print(e)
        if len(m.command) == 2:
            s = m.text.split(None, 1)[1].strip()
            usrr = (await sree.get_users(s))
            try:
                await sree.ban_chat_member(m.chat.id, usrr.id)
                await sree.send_message(
                    m.chat.id,
                    (txt.ban_01).format(
                        chut.title,
                        usrr.mention,
                        usrr.id,
                        sender.first_name
                    )   
                )   
            except:
                await message.reply(txt.ban_02)

