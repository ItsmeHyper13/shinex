# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
import re, time
from sys import argv
from datetime import datetime
from asyncio import sleep as rest
from pyrogram import Client as sree
from pyrogram import filters, __version__ as pyro
from vars import OWNER_ID as owner, SUDO_USERS as sudo
from strings import handlers as hndl, strs as txt
from main import tim
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@sree.on_message(filters.command(hndl.PING_CMD, prefixes=list("./")) & filters.group)
async def ping(sree, m: Message):
    start_time = time.time()
    sender = m.from_user
    up = get_readable_time((time.time() - tim))
    end_time = time.time()
    ping1 = str(round((end_time - start_time) * 1000, 3)) + " ms"
    if m.from_user.id in sudo or m.from_user.id == owner:
        e = await m.reply('⚡')
        await rest(3)
        await e.edit_text(txt.ping_01)
        await rest(1)
        await e.edit_text(
            (txt.ping_03).format(
                ping1,
                up,
            )
        )
    if (m.from_user.id not in sudo) or (m.from_user.id != owner):
        await m.reply((txt.ping_02).format(sender.id))
