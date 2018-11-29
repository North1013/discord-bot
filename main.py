#!/usr/local/bin/python3.6

import asyncio
import logging
import discord

from datetime import datetime

from mymodules.respond import message_respond
from mymodules.crisis.crisis import crisis_information

LOGGER = logging.getLogger('discord')
LOGGER.setLevel(logging.DEBUG)
HANDLER = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
HANDLER.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
LOGGER.addHandler(HANDLER)

client = discord.Client()

async def at_time():
    while True:
        now = datetime.now().strftime("%H")
        await asyncio.sleep(300)
        if now == "07":
            await client.send_message(client.get_channel("517044016697704448"), crisis_information())

@client.event
async def on_ready():
    print(f"Bot is has started and you have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        response = message_respond(message.author.id, message.content)
        print(response)
        if response:
            await client.send_message(message.channel, response)

asyncio.get_event_loop().create_task(at_time())

with open("key.txt", "r") as keyfile:
    KEY = keyfile.read().rstrip("\n")
    client.run(KEY)
