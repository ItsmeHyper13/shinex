

import logging
from importlib import import_module
from os import environ, getenv, listdir, path
from dotenv import load_dotenv
from telethon import TelegramClient


def __load_modules():
    for module in listdir("shinex/modules"):
        if module.endswith(".py") and not module.startswith("_"):
            import_name = f"shinex.modules.{module[:-3]}"
            import_module(import_name, module)
            print(f"Loaded {import_name}")
