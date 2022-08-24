# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13

from pyrogram import Client as sree, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from strings import strs as txt, handlers as hndl
from vars import SUDO_USERS as sudo, OWNER_ID as owner

@sree.on_message(filters.command(hndl.SUDO_CMD, prefixes=list("./")))
async def sudos(sree, m: Message):
    if m.from_user.id in sudo:
        await m.reply(
            (txt.sudos_01).format(sudo.remove(owner))
        )            
