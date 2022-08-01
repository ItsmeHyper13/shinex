# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
from pyrogram import Client as sree, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

@sree.on_message(filters.command('ban', prefixes=['.','/']))
async def ban(sree, m: Message):
  await sree.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
  await m.reply_text(f"`Banned Successfully `\n{m.reply_to_message.from_user.mention} Unkil GoAway 😒\n")

@sree.on_message(filters.command('unban', prefixes=[".",'/']))
async def unban(devu, message: Message):
  user_id = message.reply_to_message.from_user.id
  await sree.unban_chat_member(message.chat.id, user_id)
  await message.reply_text(f"`UnBanned Successfully `\n{message.reply_to_message.from_user.mention} Can Join Again 👀\n")
