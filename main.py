#!/usr/local/bin/python3.6

import asyncio
import logging
import discord

from discord.ext import commands
from datetime import datetime

# from mymodules.respond import message_respond
from mymodules.crisis.crisis import crisis_information

LOGGER = logging.getLogger('discord')
LOGGER.setLevel(logging.DEBUG)
HANDLER = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
HANDLER.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
LOGGER.addHandler(HANDLER)

client = commands.Bot(command_prefix = "!")

extensions =  ["mymodules.commands", "mymodules.music"]

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
    except Exception as error:
        print("{} cannto be loaded. [{}]".format(extension, error))

@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
    except Exception as error:
        print("{} cannto be unloaded. [{}]".format(extension, error))

@client.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(client.user))

async def at_time():
    while True:
        now = datetime.now().strftime("%H")
        await asyncio.sleep(300)
        if now == "07":
            await client.send_message(client.get_channel("232917647250030592"), crisis_information())

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(extension, error))
    
    asyncio.get_event_loop().create_task(at_time())
   
    with open("key.txt", "r") as keyfile:
        key = keyfile.read().rstrip("\n")
        client.run(key)
