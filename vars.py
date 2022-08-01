# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13


from os import getenv
from dotenv import load_dotenv

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", '5072650671'))
SUDOS = list(map(int, getenv("SUDO_USERS", "5072650671 5280801259 5221163629").split()))
SUDO_USERS = []
for x in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)
