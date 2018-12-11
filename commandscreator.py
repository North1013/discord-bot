#!/usr/local/bin/python3.6

def create_commands():
    PATH = "/root/discord-bot/"
    JSON = "data/commands.json"
    NEWFILE = "cogs/commands.py"

    START = """import discord
from discord.ext import commands

class Commands:
    def __init__(self, bot):
        self.bot = bot
"""
    END = """
def setup(bot):
    bot.add_cog(Commands(bot))
"""
    COMMAND = """
    @commands.command()
    async def {}(self, ctx):
        await ctx.send("{}")
"""
    with open(JSON, "r") as f:
        j = json.load(f)

    with open(NEWFILE, "w+") as f:
        f.write(START)

    for qwe in j["Command"]:
        command = qwe["command"]
        content = qwe["content"]
        with open(NEWFILE, "a") as f:
            f.write(COMMAND.format(command, content))

    with open(NEWFILE, "a") as f:
        f.write(END)
import json
