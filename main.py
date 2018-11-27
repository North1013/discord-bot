import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "ANIKI":
        await client.send_message(message.channel, "ANIKI :HandsUp:")


client.run("key")
