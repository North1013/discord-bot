#!/usr/local/bin/python3.6
import asyncio
import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.startswith("!aniki"):
        await client.send_message(message.channel, "ANIKI <:HandsUp:510384211346063360>")
    elif message.content.startswith("!music"):
        await client.send_message(message.channel, "qwe")
    elif message.content("!f"):
        await client.send_message(message.channel, "<:PepeHands:517047131329003530> BILLY <:PepeHands:517047131329003530> BILLY https://youtu.be/ISJlNRRvT3g")

with open("key.txt", "r") as keyfile:
    key = keyfile.read().rstrip("\n")
    client.run(key)
