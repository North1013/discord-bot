#!/usr/local/bin/python3.6

import asyncio
import logging
import discord
import os
import yaml
import commandscreator

from discord.ext import commands
from datetime import datetime

# from cogs.crisis.crisis import crisis_information

# Create commands from data/commands.json
try:
    commandscreator.create_commands()
except:
    print("Couldn't create the commands")

PATH = "/root/discord-bot/"
SETTINGS = PATH + "data/settings.yaml"
DATA = yaml.safe_load(open(SETTINGS))

DISCORD_LOG = PATH + "data/discord.log"
MESSAGE_LOG = PATH + "data/message.log"

LOGGER = logging.getLogger('discord')
LOGGER.setLevel(logging.WARNING)
HANDLER = logging.FileHandler(filename=DISCORD_LOG, encoding='utf-8', mode='w')
HANDLER.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
LOGGER.addHandler(HANDLER)

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

extensions =  [
        "cogs.advanced_commands",
        "cogs.commands",
        "cogs.crisis",
        "cogs.cryptoprice.cryptoprice",
        "cogs.quiz",
        "cogs.music",
        "cogs.duckduckgo",
        "cogs.wikipedia",
        "cogs.wolframalpha",
        "cogs.help"
        ]

# @bot.command()
# async def load(extension):
#     try:
#         bot.load_extension(extension)
#     except Exception as error:
#         print("{} cannot be loaded. [{}]".format(extension, error))
# 
# @bot.command()
# async def unload(extension):
#     try:
#         bot.unload_extension(extension)
#     except Exception as error:
#         print("{} cannot be unloaded. [{}]".format(extension, error))

# @bot.event
# async def on_message(message):
#     with open(MESSAGE_LOG, "a+") as f:
#         f.write("Message from {0.author} at {0.created_at}: {0.content}\n".format(message))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    print('Discord.py version: ' + discord.__version__)
    await bot.change_presence(activity=discord.Game(name=DATA["game"]))

# async def at_time():
#     while True:
#         now = datetime.now().strftime("%H")
#         await asyncio.sleep(300)
#         if now == "07":
#             await bot.send_message(bot.get_channel(232917647250030592), crisis_information())

def check_folder():
    if not os.path.exists(PATH):
        os.mkdir(PATH)

if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(extension, error))
    
#    asyncio.get_event_loop().create_task(at_time())
    
    check_folder() 
    bot.run(DATA['key'], bot=True, reconnect=True)
