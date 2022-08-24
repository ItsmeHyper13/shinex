


from shinex import sree, BOT_TOKEN as TOKEN 
from shinex.modules import ALL_MODULES


sree.start(bot_token=TOKEN)
    
        
async def xxx_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("shinex.modules." + all_module)
    print("────────────BOT START────────────")
    await idle()
    print("GoodBye! Stopping Bot")


if __name__ == "__main__":
    loop.run_until_complete(xxx_boot())



     
    




